# Robot Psychology Field Notes

The profile carousel turns research findings into short, memorable notes. These are **experimental findings, not universal laws**: results can change across models, versions, languages, tasks, prompts, environments, and evaluation methods.

## 01 — Prompt tone

**Profile note:** Shouting is not reliably worse—or better. Tone effects vary by model, task, language, and benchmark.

Evidence is mixed. A cross-lingual study found that impolite prompts often reduced performance and that the best politeness level differed by language. Later studies found smaller, model-dependent effects; one limited GPT-4o experiment even reported higher multiple-choice accuracy for rude prompts. The useful conclusion is not “be rude” or “be polite,” but **treat tone as a behavioural variable and test it**.

- [Should We Respect LLMs? A Cross-Lingual Study on the Influence of Prompt Politeness on LLM Performance](https://arxiv.org/abs/2402.14531)
- [Does Tone Change the Answer? Evaluating Prompt Politeness Effects on Modern LLMs](https://arxiv.org/abs/2512.12812)
- [Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models](https://arxiv.org/abs/2604.02236)

## 02 — Input noise

**Profile note:** Typos can damage reasoning.

A multilingual evaluation of 18 open-source LLMs found that human-like typographical errors consistently degraded performance. Generative and reasoning tasks were particularly affected, and robustness varied by language.

- [Evaluating Robustness of Large Language Models Against Multilingual Typographical Errors](https://aclanthology.org/2026.acl-long.729/)

## 03 — Prompt language

**Profile note:** The same question can score differently across languages.

Multilingual ability is uneven. Prompt language can materially change performance, sometimes in surprising directions. English is not always the best prompt language for every task, but persistent gaps remain between English or high-resource languages and many low-resource languages.

- [Not All Languages Are Created Equal in LLMs](https://aclanthology.org/2023.findings-emnlp.826/)
- [To Ask LLMs about English Grammaticality, Prompt Them in a Different Language](https://aclanthology.org/2024.findings-emnlp.916/)
- [MuBench: Assessment of Multilingual Capabilities of Large Language Models Across 61 Languages](https://aclanthology.org/2026.findings-acl.794/)

## 04 — Confidence calibration

**Profile note:** Confidence is not truth.

In one controlled clinical-question experiment, misleading authority cues drove accuracy from 100% in the neutral condition to 1%, while model confidence remained high. This is a narrow experiment, but it demonstrates a crucial failure mode: fluent certainty can survive factual collapse.

- [Impact of authoritative and subjective cues on large language model reliability for clinical inquiries](https://www.nature.com/articles/s41598-026-38019-3)

## 05 — Prompt specification

**Profile note:** Specify. Do not overload.

Under-specified prompts are fragile across model and prompt changes. But adding every possible requirement is not a complete solution: models can fail when requirements conflict or exceed instruction-following capacity. Define the goal, constraints, and output format, then test them individually.

- [What Prompts Don’t Say: Understanding and Managing Underspecification in LLM Prompts](https://aclanthology.org/2026.findings-acl.441/)

## 06 — Prompt robustness

**Profile note:** One prompt is not a test.

Semantically equivalent prompt variations can produce different evaluations and outputs. Behavioural claims should use multiple paraphrases, repeated runs, and—where relevant—multiple models and versions.

- [All Prompts Are Created Equal? Evaluating Robustness of LLM Judges Against Non-Adversarial Prompt Variations](https://aclanthology.org/2026.findings-acl.1929/)

## 07 — Legible robot motion

**Profile note:** Good robot motion reveals intent, not just the destination.

Predictable motion matches what a person expects once the goal is known. Legible motion helps the person infer the goal from the motion. These properties are different and can conflict, so robot planners should account for human interpretation rather than optimizing only path efficiency.

- [Legibility and Predictability of Robot Motion](https://publications.ri.cmu.edu/legibility-and-predictability-of-robot-motion)
- [Generating Legible Motion](https://www.roboticsproceedings.org/rss09/p24.html)

## 08 — Robot gaze

**Profile note:** Gaze is context—not decoration.

A study of mobile-robot navigation found that person-oriented gaze was generally preferred when robot and human paths crossed, but its benefit diminished in scenes with less implicit interaction. A social cue should fit the interaction rather than run continuously.

- [Robot Gaze During Autonomous Navigation and its Effect on Social Presence](https://arxiv.org/abs/2305.05852)

---

**Working rule:** prefer precise, testable statements over universal prompt-engineering folklore.