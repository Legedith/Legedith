#!/usr/bin/env python3
"""Collect a daily, source-linked radar for robot psychology and AI behaviour."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "data" / "sources.json"
OUTPUT_PATH = ROOT / "data" / "daily_feed.json"
DIGEST_PATH = ROOT / "DAILY_DIGEST.md"
USER_AGENT = "Legedith-Robot-Psychology-Radar/1.0 (+https://github.com/Legedith/Legedith)"
MAX_AGE_DAYS = 30
MAX_ITEMS = 80
DIGEST_ITEMS = 24
PER_SOURCE_LIMIT = 6

CATEGORY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "robotics": (
        "robot", "robotics", "embodied", "humanoid", "manipulation", "navigation",
        "locomotion", "dexter", "grasp", "drone", "autonomous vehicle", "spatial intelligence",
    ),
    "machine behaviour": (
        "behavior", "behaviour", "psychology", "trust", "anthropomorph", "emotion", "affect",
        "personality", "values", "culture", "language", "sycophancy", "deception", "persuasion",
        "social intelligence", "human-ai", "human robot", "hri",
    ),
    "agents": (
        "agent", "agentic", "tool use", "tool-use", "mcp", "memory", "planning", "workflow",
        "computer use", "browser use", "multi-agent", "autonomy", "long-running",
    ),
    "evaluation": (
        "eval", "evaluation", "benchmark", "reliability", "robustness", "hallucination",
        "calibration", "judge", "leaderboard", "measurement", "replication", "audit",
    ),
    "safety": (
        "safety", "alignment", "prompt injection", "jailbreak", "red team", "misuse", "security",
        "control", "oversight", "monitoring", "privacy", "interpretability", "reward hacking",
    ),
    "multilingual": (
        "multilingual", "cross-lingual", "low-resource language", "translation", "language model",
        "cultural", "localization", "localisation",
    ),
    "multimodal": (
        "multimodal", "vision-language", "vision language", "audio", "speech", "video", "world model",
        "visual reasoning", "image understanding",
    ),
    "systems": (
        "inference", "training", "fine-tuning", "finetuning", "post-training", "retrieval", "rag",
        "quantization", "distillation", "model architecture", "scaling", "dataset", "open weights",
    ),
}

HIGH_SIGNAL = (
    "robot psychology", "machine behavior", "machine behaviour", "human-robot", "human robot",
    "agent evaluation", "agent safety", "social robot", "embodied ai", "multilingual llm",
    "prompt injection", "anthropomorphism", "trust", "sycophancy", "calibration",
)

BLOCKED_TITLE_PATTERNS = (
    r"\bwebinar\b", r"\bsale\b", r"\bhiring\b", r"\bjob opening\b", r"\bsponsored\b",
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


def clean_html(value: str) -> str:
    parser = TextExtractor()
    try:
        parser.feed(value or "")
        text = " ".join(parser.parts)
    except Exception:
        text = re.sub(r"<[^>]+>", " ", value or "")
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def truncate(value: str, limit: int) -> str:
    value = re.sub(r"\s+", " ", value).strip()
    if len(value) <= limit:
        return value
    cut = value[: limit - 1].rsplit(" ", 1)[0]
    return f"{cut}…"


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    raw = value.strip()
    try:
        parsed = parsedate_to_datetime(raw)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        pass
    try:
        parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed.astimezone(timezone.utc)
    except ValueError:
        return None


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def child_text(node: ET.Element, names: Iterable[str]) -> str:
    wanted = {name.lower() for name in names}
    for child in list(node):
        if local_name(child.tag) in wanted:
            return "".join(child.itertext()).strip()
    return ""


def atom_link(entry: ET.Element) -> str:
    fallback = ""
    for child in list(entry):
        if local_name(child.tag) != "link":
            continue
        href = child.attrib.get("href", "").strip()
        rel = child.attrib.get("rel", "alternate")
        if href and rel == "alternate":
            return href
        if href and not fallback:
            fallback = href
    return fallback


def normalize_url(url: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(url.strip())
    except ValueError:
        return url.strip()
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [
        (key, value)
        for key, value in query
        if not key.lower().startswith("utm_") and key.lower() not in {"ref", "source"}
    ]
    path = parsed.path.rstrip("/") or "/"
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, urllib.parse.urlencode(query), "")
    )


@dataclass
class Item:
    id: str
    title: str
    url: str
    source: str
    source_group: str
    published: str
    summary: str
    category: str
    score: float


def parse_feed(xml_bytes: bytes, source: dict[str, Any]) -> list[Item]:
    root = ET.fromstring(xml_bytes)
    now = datetime.now(timezone.utc)
    records: list[Item] = []
    nodes = [node for node in root.iter() if local_name(node.tag) in {"entry", "item"}]
    for node in nodes:
        is_atom = local_name(node.tag) == "entry"
        title = clean_html(child_text(node, ("title",)))
        url = atom_link(node) if is_atom else child_text(node, ("link", "guid"))
        summary = clean_html(child_text(node, ("summary", "description", "content", "encoded")))
        date_raw = child_text(node, ("published", "updated", "pubDate", "date", "created"))
        published_dt = parse_date(date_raw) or now
        if not title or not url:
            continue
        url = normalize_url(url)
        text = f"{title} {summary}".lower()
        category, score = classify(text, float(source.get("weight", 1.0)), published_dt, now)
        item_id = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
        records.append(
            Item(
                id=item_id,
                title=truncate(title, 180),
                url=url,
                source=source["name"],
                source_group=source.get("group", "other"),
                published=published_dt.isoformat().replace("+00:00", "Z"),
                summary=truncate(summary, 360),
                category=category,
                score=round(score, 2),
            )
        )
    return records


def classify(
    text: str, source_weight: float, published: datetime, now: datetime
) -> tuple[str, float]:
    scores: dict[str, float] = defaultdict(float)
    for category, words in CATEGORY_KEYWORDS.items():
        for word in words:
            if word in text:
                scores[category] += 1.0 + min(1.5, len(word) / 18)
    category = max(scores, key=scores.get, default="general AI")
    keyword_score = scores.get(category, 0.0)
    high_signal = sum(2.5 for phrase in HIGH_SIGNAL if phrase in text)
    age_days = max(0.0, (now - published).total_seconds() / 86400)
    recency = max(0.0, 4.0 - age_days / 4.0)
    return category, source_weight + keyword_score + high_signal + recency


def fetch(url: str, attempts: int = 2) -> bytes:
    last_error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(
                url,
                headers={
                    "User-Agent": USER_AGENT,
                    "Accept": "application/atom+xml, application/rss+xml, application/xml, text/xml;q=0.9, */*;q=0.5",
                },
            )
            with urllib.request.urlopen(request, timeout=25) as response:
                return response.read(5_000_000)
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as exc:
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(2 + attempt)
    raise RuntimeError(str(last_error))


def is_allowed(item: Item, cutoff: datetime) -> bool:
    published = parse_date(item.published)
    if published and published < cutoff:
        return False
    lowered = item.title.lower()
    if any(re.search(pattern, lowered) for pattern in BLOCKED_TITLE_PATTERNS):
        return False
    return item.score >= 3.8


def select_items(items: list[Item], now: datetime) -> list[Item]:
    cutoff = now - timedelta(days=MAX_AGE_DAYS)
    deduped: dict[str, Item] = {}
    for item in items:
        if not is_allowed(item, cutoff):
            continue
        key = normalize_url(item.url)
        existing = deduped.get(key)
        if existing is None or item.score > existing.score:
            deduped[key] = item

    ranked = sorted(
        deduped.values(),
        key=lambda item: (item.score, item.published),
        reverse=True,
    )
    selected: list[Item] = []
    per_source: Counter[str] = Counter()
    for item in ranked:
        if per_source[item.source] >= PER_SOURCE_LIMIT:
            continue
        selected.append(item)
        per_source[item.source] += 1
        if len(selected) >= MAX_ITEMS:
            break
    return selected


def render_digest(
    items: list[Item], generated_at: datetime, errors: dict[str, str], sources_ok: int
) -> str:
    display = items[:DIGEST_ITEMS]
    grouped: dict[str, list[Item]] = defaultdict(list)
    for item in display:
        grouped[item.category].append(item)
    category_order = sorted(grouped, key=lambda category: (-len(grouped[category]), category))
    source_count = len({item.source for item in display})
    lines = [
        "# Robot Psychology Radar",
        "",
        f"Updated {generated_at.strftime('%d %B %Y, %H:%M UTC')} from {sources_ok} working sources.",
        "",
        f"{len(display)} high-relevance items across {source_count} sources. Auto-collected metadata; inclusion is not endorsement.",
        "",
    ]
    if not display:
        lines.extend(["No high-relevance items were collected in this run.", ""])
    for category in category_order:
        lines.extend([f"## {category.title()}", ""])
        for item in grouped[category]:
            date = parse_date(item.published)
            date_label = date.strftime("%d %b") if date else "Recent"
            lines.extend(
                [
                    f"### [{item.title}]({item.url})",
                    "",
                    f"**{item.source}** · {date_label} · relevance {item.score:.1f}",
                ]
            )
            if item.summary:
                lines.extend(["", item.summary])
            lines.append("")
    if errors:
        lines.extend(["<details>", "<summary>Sources unavailable during this run</summary>", ""])
        for name, message in sorted(errors.items()):
            lines.append(f"- **{name}:** `{truncate(message, 180)}`")
        lines.extend(["", "</details>", ""])
    lines.extend(
        [
            "---",
            "",
            "Generated by [`scripts/collect_daily.py`](./scripts/collect_daily.py) using [`data/sources.json`](./data/sources.json).",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--minimum-working-sources", type=int, default=1)
    args = parser.parse_args()

    now = datetime.now(timezone.utc)
    config = json.loads(SOURCES_PATH.read_text(encoding="utf-8"))
    collected: list[Item] = []
    errors: dict[str, str] = {}
    working_sources: list[str] = []

    for source in config["sources"]:
        try:
            raw = fetch(source["url"])
            parsed = parse_feed(raw, source)
            collected.extend(parsed)
            working_sources.append(source["name"])
            print(f"{source['name']}: {len(parsed)} entries")
        except Exception as exc:
            errors[source["name"]] = str(exc)
            print(f"WARNING {source['name']}: {exc}")

    if len(working_sources) < args.minimum_working_sources:
        raise SystemExit(
            f"Only {len(working_sources)} sources worked; refusing to overwrite the digest."
        )

    selected = select_items(collected, now)
    payload = {
        "generated_at": now.isoformat().replace("+00:00", "Z"),
        "working_sources": working_sources,
        "source_errors": errors,
        "item_count": len(selected),
        "items": [asdict(item) for item in selected],
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    DIGEST_PATH.write_text(
        render_digest(selected, now, errors, len(working_sources)), encoding="utf-8"
    )
    print(f"Wrote {len(selected)} ranked items from {len(working_sources)} sources.")


if __name__ == "__main__":
    main()
