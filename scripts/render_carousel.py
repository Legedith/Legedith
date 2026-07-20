#!/usr/bin/env python3
"""Render the weekly GitHub profile insight carousel and its source index."""

from __future__ import annotations

import html
import json
import os
import random
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "insights.json"
SVG_PATH = ROOT / "assets" / "field-notes-carousel.svg"
NOTES_PATH = ROOT / "FIELD_NOTES.md"
SLIDE_LIMIT = 10
SECONDS_PER_SLIDE = 7

ICONS: dict[str, str] = {
    "loop": '''<circle cx="112" cy="105" r="72" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><circle cx="112" cy="105" r="40" fill="#071326" stroke="#8b5cf6" stroke-width="3"/><path d="M112 45a60 60 0 0 1 54 34M168 78l-4-22 21 8" fill="none" stroke="#f472b6" stroke-width="6"/><path d="M112 165a60 60 0 0 1-54-34M56 132l4 22-21-8" fill="none" stroke="#22d3ee" stroke-width="6"/><circle cx="112" cy="105" r="10" fill="#f8fafc"/><circle cx="112" cy="45" r="8" fill="#22d3ee"/><circle cx="168" cy="135" r="8" fill="#f472b6"/><circle cx="56" cy="135" r="8" fill="#8b5cf6"/>''',
    "harness": '''<rect x="30" y="28" width="164" height="154" rx="24" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><rect x="65" y="60" width="94" height="75" rx="18" fill="#071326" stroke="#22d3ee" stroke-width="3"/><circle cx="90" cy="94" r="8" fill="#f472b6"/><circle cx="134" cy="94" r="8" fill="#f472b6"/><path d="M88 118h48" stroke="#22d3ee" stroke-width="5" stroke-linecap="round"/><path d="M48 55h-20M48 88h-20M48 121h-20M176 55h20M176 88h20M176 121h20" stroke="#64748b" stroke-width="5" stroke-linecap="round"/><circle cx="28" cy="55" r="7" fill="#22d3ee"/><circle cx="28" cy="88" r="7" fill="#8b5cf6"/><circle cx="28" cy="121" r="7" fill="#f472b6"/><circle cx="196" cy="55" r="7" fill="#f472b6"/><circle cx="196" cy="88" r="7" fill="#22d3ee"/><circle cx="196" cy="121" r="7" fill="#8b5cf6"/>''',
    "terminal": '''<rect x="24" y="34" width="176" height="142" rx="20" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><circle cx="48" cy="58" r="5" fill="#f472b6"/><circle cx="66" cy="58" r="5" fill="#8b5cf6"/><circle cx="84" cy="58" r="5" fill="#22d3ee"/><path d="M50 92l26 21-26 21M93 135h63" fill="none" stroke="#f8fafc" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M145 82h29M145 101h20" stroke="#64748b" stroke-width="5"/>''',
    "compose": '''<path d="M34 44h68v32c13-12 39-3 39 19s-26 31-39 19v32H34z" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><path d="M122 44h68v102h-35c12-13 3-39-19-39s-31 26-19 39h5z" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><path d="M48 166h142" stroke="#64748b" stroke-width="5" stroke-dasharray="9 8"/><path d="M95 165l28-26 28 26" fill="none" stroke="#f472b6" stroke-width="7"/>''',
    "benchmark": '''<rect x="32" y="37" width="160" height="132" rx="20" fill="#0f172a" stroke="#f472b6" stroke-width="3"/><path d="M57 67h100M57 98h76M57 129h110" stroke="#64748b" stroke-width="6"/><ellipse cx="139" cy="98" rx="31" ry="25" fill="#071326" stroke="#22d3ee" stroke-width="3"/><path d="M139 74v48M117 87h44M119 111h40" stroke="#22d3ee" stroke-width="4"/><path d="M111 67l-14-15M168 67l14-15M111 129l-14 15M168 129l14 15" stroke="#8b5cf6" stroke-width="4"/>''',
    "deployment": '''<rect x="28" y="36" width="168" height="136" rx="22" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><rect x="49" y="57" width="126" height="94" rx="14" fill="#071326" stroke="#334155"/><path d="M67 82h67M67 107h89M67 132h47" stroke="#22d3ee" stroke-width="6"/><circle cx="167" cy="80" r="24" fill="#2a0d2a" stroke="#f472b6" stroke-width="3"/><path d="M157 80l8 8 14-18" fill="none" stroke="#f472b6" stroke-width="5"/><path d="M42 184h140" stroke="#64748b" stroke-width="4" stroke-dasharray="8 8"/>''',
    "expertise": '''<circle cx="78" cy="78" r="35" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><path d="M39 168c5-42 25-63 39-63s34 21 39 63" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><path d="M125 152l22-28 22 13 28-50" fill="none" stroke="#f472b6" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 88l14-2-3 14" fill="none" stroke="#f472b6" stroke-width="6"/><circle cx="78" cy="76" r="7" fill="#8b5cf6"/>''',
    "safety": '''<path d="M112 22l75 28v55c0 46-30 71-75 90-45-19-75-44-75-90V50z" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><rect x="76" y="70" width="72" height="62" rx="16" fill="#071326" stroke="#8b5cf6" stroke-width="3"/><rect x="91" y="86" width="13" height="31" rx="6" fill="#f472b6"/><rect x="120" y="86" width="13" height="31" rx="6" fill="#f472b6"/><path d="M67 151h90" stroke="#64748b" stroke-width="5" stroke-dasharray="8 7"/>''',
    "language": '''<circle cx="108" cy="103" r="76" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><path d="M32 103h152M108 27c-28 25-42 50-42 76s14 51 42 76M108 27c28 25 42 50 42 76s-14 51-42 76M49 62h118M49 144h118" fill="none" stroke="#22d3ee" stroke-width="2"/><text x="108" y="112" text-anchor="middle" fill="#f8fafc" font-family="ui-monospace, monospace" font-size="23" font-weight="800">A / अ / 文</text>''',
    "values": '''<rect x="35" y="35" width="154" height="142" rx="22" fill="#0f172a" stroke="#f472b6" stroke-width="3"/><path d="M63 70h98M63 105h98M63 140h98" stroke="#64748b" stroke-width="5"/><circle cx="91" cy="70" r="11" fill="#22d3ee"/><circle cx="145" cy="105" r="11" fill="#8b5cf6"/><circle cx="112" cy="140" r="11" fill="#f472b6"/><path d="M189 69h23M189 104h23M189 139h23" stroke="#22d3ee" stroke-width="4"/>''',
    "robot": '''<rect x="70" y="35" width="84" height="66" rx="18" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><circle cx="94" cy="67" r="7" fill="#f472b6"/><circle cx="130" cy="67" r="7" fill="#f472b6"/><path d="M91 87h42M112 19v16" stroke="#8b5cf6" stroke-width="5" stroke-linecap="round"/><circle cx="112" cy="14" r="7" fill="#8b5cf6"/><rect x="57" y="111" width="110" height="46" rx="18" fill="#071326" stroke="#8b5cf6" stroke-width="3"/><path d="M57 133H32M167 133h25M76 157l-18 28M148 157l18 28" stroke="#22d3ee" stroke-width="7" stroke-linecap="round"/>''',
    "control": '''<path d="M30 162c36-84 75-112 116-75 20 18 31 13 56-35" fill="none" stroke="#22d3ee" stroke-width="9" stroke-linecap="round"/><path d="M30 162c28-10 39-70 70-31s50-22 102-79" fill="none" stroke="#64748b" stroke-width="5" stroke-dasharray="7 8"/><circle cx="30" cy="162" r="9" fill="#f472b6"/><circle cx="202" cy="52" r="10" fill="#8b5cf6"/><path d="M181 47l21 5-7 20" fill="none" stroke="#8b5cf6" stroke-width="6"/>''',
    "trust": '''<path d="M64 63c0-24 29-31 46-12 17-19 46-12 46 12 0 34-46 62-46 62S64 97 64 63z" fill="#2a0d2a" stroke="#f472b6" stroke-width="3"/><path d="M44 160h132M110 125v35" stroke="#64748b" stroke-width="5"/><circle cx="61" cy="160" r="24" fill="#071326" stroke="#22d3ee" stroke-width="3"/><path d="M50 160h22M61 149v22" stroke="#22d3ee" stroke-width="5"/><circle cx="159" cy="160" r="24" fill="#071326" stroke="#8b5cf6" stroke-width="3"/><path d="M147 160h24" stroke="#8b5cf6" stroke-width="5"/>''',
    "spatial": '''<path d="M112 24l70 40v80l-70 40-70-40V64z" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><path d="M42 64l70 41 70-41M112 105v79" fill="none" stroke="#8b5cf6" stroke-width="3"/><path d="M73 82l78 45M151 82l-78 45" stroke="#64748b" stroke-width="3" stroke-dasharray="7 6"/><circle cx="112" cy="105" r="9" fill="#f472b6"/>''',
    "pipeline": '''<rect x="24" y="50" width="72" height="56" rx="14" fill="#0f172a" stroke="#22d3ee" stroke-width="3"/><rect x="128" y="50" width="72" height="56" rx="14" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><path d="M96 78h32M116 68l12 10-12 10" fill="none" stroke="#f472b6" stroke-width="6"/><circle cx="99" cy="145" r="31" fill="#071326" stroke="#22d3ee" stroke-width="3"/><path d="M122 168l25 25M83 145h32M99 129v32" stroke="#8b5cf6" stroke-width="5" stroke-linecap="round"/>''',
    "learning": '''<rect x="45" y="38" width="134" height="138" rx="20" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><path d="M70 73h84M70 106h63M70 139h76" stroke="#64748b" stroke-width="6"/><path d="M25 105a87 87 0 0 1 33-67M42 35l20 3-9 18" fill="none" stroke="#22d3ee" stroke-width="6"/><path d="M199 105a87 87 0 0 1-33 67M182 175l-20-3 9-18" fill="none" stroke="#f472b6" stroke-width="6"/><circle cx="112" cy="106" r="11" fill="#f472b6"/>''',
    "memory": '''<path d="M34 54c0-27 22-49 49-49 19 0 35 10 43 25 8-15 24-25 43-25 27 0 49 22 49 49 0 43-47 76-92 111C81 130 34 97 34 54z" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><path d="M72 59h32l13-24 19 57 14-33h31" stroke="#22d3ee" stroke-width="6" fill="none"/><path d="M55 171h145" stroke="#64748b" stroke-width="4" stroke-dasharray="9 8"/><circle cx="62" cy="171" r="7" fill="#f472b6"><animate attributeName="cx" values="62;193;62" dur="4.5s" repeatCount="indefinite"/></circle>''',
    "logs": '''<rect x="20" y="28" width="184" height="158" rx="22" fill="#0f172a" stroke="#8b5cf6" stroke-width="3"/><text x="43" y="66" fill="#64748b" font-family="ui-monospace, monospace" font-size="16">SHOULD</text><path d="M43 78h130" stroke="#64748b" stroke-width="5"/><text x="43" y="119" fill="#22d3ee" font-family="ui-monospace, monospace" font-size="16">DID</text><path d="M43 132h72M43 158h120" stroke="#22d3ee" stroke-width="6"/><circle cx="166" cy="131" r="10" fill="#f472b6" filter="url(#glow)"><animate attributeName="opacity" values=".35;1;.35" dur="1.7s" repeatCount="indefinite"/></circle>''',
}


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def select_insights(insights: list[dict[str, Any]], seed: int) -> list[dict[str, Any]]:
    """Select a deterministic, category-diverse weekly deck."""
    rng = random.Random(seed)
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for insight in insights:
        groups[insight["category"]].append(insight)
    categories = list(groups)
    rng.shuffle(categories)
    for items in groups.values():
        rng.shuffle(items)
    selected: list[dict[str, Any]] = []
    for category in categories:
        if len(selected) >= SLIDE_LIMIT:
            break
        selected.append(groups[category].pop())
    remaining = [item for items in groups.values() for item in items]
    rng.shuffle(remaining)
    selected.extend(remaining[:max(0, SLIDE_LIMIT - len(selected))])
    rng.shuffle(selected)
    return selected


def render_svg(slides: list[dict[str, Any]]) -> str:
    total = len(slides) * SECONDS_PER_SLIDE
    key_times = f"0;{0.45 / total:.6f};{(SECONDS_PER_SLIDE - 0.6) / total:.6f};{SECONDS_PER_SLIDE / total:.6f};1"
    out = [f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 340" role="img" aria-labelledby="title desc"><title id="title">Rotating insights about LLM, agent, and robot behaviour</title><desc id="desc">A weekly-changing animated carousel about artificial behaviour.</desc><defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050816"/><stop offset="0.5" stop-color="#0b1026"/><stop offset="1" stop-color="#160b2d"/></linearGradient><linearGradient id="neon" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22d3ee"/><stop offset="0.52" stop-color="#8b5cf6"/><stop offset="1" stop-color="#f472b6"/></linearGradient><radialGradient id="orb" cx="50%" cy="50%" r="65%"><stop offset="0" stop-color="#8b5cf6" stop-opacity=".22"/><stop offset="1" stop-color="#8b5cf6" stop-opacity="0"/></radialGradient><pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="#64748b" stroke-opacity=".09"/></pattern><filter id="glow" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><rect width="1200" height="340" rx="26" fill="url(#bg)"/><rect width="1200" height="340" rx="26" fill="url(#grid)"/><circle cx="180" cy="170" r="230" fill="url(#orb)"/><circle cx="1060" cy="140" r="180" fill="url(#orb)" opacity=".55"/><rect x="38" y="34" width="1124" height="260" rx="25" fill="#050a19" stroke="#334155" stroke-width="2"/><rect x="39" y="35" width="1122" height="258" rx="24" fill="none" stroke="url(#neon)" stroke-opacity=".35"/><path d="M326 56V272" stroke="#334155" stroke-opacity=".72"/>''']
    for index, slide in enumerate(slides):
        fallback = "1" if index == 0 else "0"
        values = "1;1;1;0;0" if index == 0 else "0;1;1;0;0"
        out.append(f'''<g opacity="{fallback}"><animate attributeName="opacity" values="{values}" keyTimes="{key_times}" dur="{total}s" begin="{index * SECONDS_PER_SLIDE}s" repeatCount="indefinite"/><g transform="translate(55 58)">{ICONS[slide["icon"]]}</g><g font-family="ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace">''')
        for i, line in enumerate(slide["title"]):
            fill = "#f8fafc" if i == 0 else "url(#neon)"
            out.append(f'<text x="372" y="{125 + i * 44}" fill="{fill}" font-size="35" font-weight="800">{esc(line)}</text>')
        for i, line in enumerate(slide["body"]):
            out.append(f'<text x="372" y="{218 + i * 27}" fill="{"#cbd5e1" if i == 0 else "#94a3b8"}" font-size="{18 if i == 0 else 16}">{esc(line)}</text>')
        out.append('</g></g>')
    out.append(f'''<rect x="48" y="313" width="1104" height="3" rx="1.5" fill="#1e293b"/><rect x="48" y="313" width="0" height="3" rx="1.5" fill="url(#neon)" filter="url(#glow)"><animate attributeName="width" values="0;1104" dur="{total}s" repeatCount="indefinite"/></rect><rect x="1" y="1" width="1198" height="338" rx="25" fill="none" stroke="#fff" stroke-opacity=".08" stroke-width="2"/></svg>''')
    return "".join(out)


def render_notes(insights: list[dict[str, Any]]) -> str:
    lines = ["# Sources behind the carousel", "", "The profile rotates through a larger library each week. The library deliberately mixes independent builders, research labs, human–computer interaction, multilingual NLP, AI safety, and embodied robotics.", "", "The profile lines are paraphrases—not endorsements or universal laws. Artificial behaviour depends on the model, harness, body, interface, tools, language, data, incentives, and evaluation.", ""]
    for insight in insights:
        lines.extend([f'## {" ".join(insight["title"])}', "", insight["explanation"], ""])
        lines.extend(f'- [{source["label"]}]({source["url"]})' for source in insight["sources"])
        lines.append("")
    lines.extend(["---", "", "This page is generated from `data/insights.json`. Edit that file to add, remove, or refine a slide.", ""])
    return "\n".join(lines)


def main() -> None:
    insights = json.loads(DATA_PATH.read_text(encoding="utf-8"))["insights"]
    iso = datetime.now(timezone.utc).isocalendar()
    seed = int(os.environ.get("CAROUSEL_SEED", f"{iso.year}{iso.week:02d}"))
    selected = select_insights(insights, seed)
    SVG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SVG_PATH.write_text(render_svg(selected), encoding="utf-8")
    NOTES_PATH.write_text(render_notes(insights), encoding="utf-8")
    print(f"Rendered {len(selected)} slides from {len(insights)} insights using seed {seed}.")


if __name__ == "__main__":
    main()
