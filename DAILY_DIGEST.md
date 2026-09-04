# Robot Psychology Radar

Updated 04 September 2026, 07:25 UTC from 16 working sources.

24 high-relevance items across 5 sources. Auto-collected metadata; inclusion is not endorsement.

## Evaluation

### [Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198v1)

**arXiv — AI, language and HCI** · 03 Sep · relevance 16.7

Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow. We audited that assumption in two preregistered campaigns with every threshold fixed in advance; neither got…

### [Interface-Induced Trajectory Censoring](https://arxiv.org/abs/2609.03966v1)

**arXiv — AI, language and HCI** · 03 Sep · relevance 15.9

Agent evaluations report a tool-call rate read off the serving stack. That number can be zero while the model is emitting well-formed calls: the interface censors the trajectory before anything downstream sees it. On BFCL v4's own data, executor and scorer, holding weights, cases, decoding and seeds fixed and changing only the serving adapter, the same…

### [A comparative study on the accuracy & repeatability of mobile robotic platforms for the delivery of precision NDE measurement](https://arxiv.org/abs/2609.03794v1)

**arXiv — Robotics** · 03 Sep · relevance 15.3

Mobile robotic platforms offer a flexible alternative to fixed manipulators for non-destructive evaluation (NDE) of large aerospace structures, but their base-positioning accuracy and how that accuracy should inform deployment have not been assessed under a common, externally referenced protocol. This work presents a laser tracker-based evaluation workflow…

### [TAP-Path: Task-Adaptive Structural and Token Pruning for Efficient and Trustworthy Pathology Foundation Models](https://arxiv.org/abs/2609.04071v1)

**arXiv — AI, language and HCI** · 03 Sep · relevance 14.9

Pathology foundation models improve transferable representation learning for histopathology, but recent gains often rely on encoders with hundreds of millions of parameters and high inference cost. We propose TAP-Path, a task-adaptive compression framework that directly restructures a pretrained Virchow2 encoder rather than distilling it into a separate…

### [Representational alignment yields generalizable safety in language models](https://arxiv.org/abs/2609.04022v1)

**arXiv — AI, language and HCI** · 03 Sep · relevance 13.7

Aligning large language models (LLMs) is essential for their safe deployment. Current alignment methods mainly optimize observable responses, yet models remain vulnerable when the same harmful intent is recast in unfamiliar or adversarial forms that humans can easily recognize. Prototype theory offers an account of this adaptability. Human concepts are…

### [R2S-Eval: Robot Evaluation with Real-to-Sim Calibration via Vision-Language Models](https://arxiv.org/abs/2609.03276v1)

**arXiv — Robotics** · 03 Sep · relevance 13.6

Evaluating robot manipulation policies is becoming increasingly important as generalist models, particularly vision-language-action (VLA) models, are deployed on physical robots. However, conventional real-world evaluation remains labor-intensive, unstable, and insufficiently informative. It requires repeated hardware trials, manual scene resets, and…

### [Subspace Inference Enables Efficient Active Reward Learning from Preferences](https://arxiv.org/abs/2609.04066v1)

**arXiv — Robotics** · 03 Sep · relevance 12.5

Reinforcement learning from human feedback (RLHF) has emerged as a powerful yet sample-inefficient approach for learning reward models from human preferences, making active learning a critical component in synthesizing informative preference queries. However, effective uncertainty quantification required for active learning remains a key challenge for…

### [Things I Learned - 30 Aug 2026](https://www.s-anand.net/blog/things-i-learned-30-aug-2026)

**S Anand** · 30 Aug · relevance 9.4

This week, I learned: I know that fact-checking 2000 page PDFs is error-prone, so’d do it manually for a few pages, then refine. Agents would know this if they’ve tried and failed and added it to their memory systems. So I intervene when agents don’t remember well (increasingly rare) or I think they haven’t seen it before (again, increasingly rare). My…

## Machine Behaviour

### [Things I Learned - 23 Aug 2026](https://www.s-anand.net/blog/things-i-learned-23-aug-2026)

**S Anand** · 23 Aug · relevance 11.4

This week, I learned: DuckDB 2.0 adds a CONNECT command that can connect to databases like MySQL, PostgreSQL, etc. making DuckDB the only DB client I need. EQ-Bench evaluates models on capabilities like: does it follow direction, does it challenge you, how good are its insights, does it build rapport, etc. Very interesting to see that the Gemini models are…

### [Things I Learned - 09 Aug 2026](https://www.s-anand.net/blog/things-i-learned-09-aug-2026)

**S Anand** · 09 Aug · relevance 10.7

This week, I learned: Kamakoti: “Entry (to the course) is relatively easy but the exit is extremely hard”. Generalizing, quality is determined by the exit criteria; loosening entry criteria is just openness / diversity. The Hindu “Once I have a persistent system that I pay to keep thinking, learning, and acting 24/7, I think that will decisively look like…

### [llm-gemini 0.34](https://simonwillison.net/2026/Sep/2/llm-gemini)

**Simon Willison — LLMs** · 02 Sep · relevance 10.2

Release: llm-gemini 0.34 New model gemini-3.8-flash for Gemini 3.8 Flash , with low, medium and high thinking levels. #146 Fixed async responses failing to record the resolved model version. Thanks, Charlie Tonneslan . #137 Google released Gemini 3.8 Flash (and 3.8 Flash Cyber, but that's available to "trusted defenders" only) today. Here are the pelicans…

### [Quoting Rick Brewster](https://simonwillison.net/2026/Sep/2/rick-brewster)

**Simon Willison — LLMs** · 02 Sep · relevance 10.1

Direct2D has always been the biggest hurdle for Paint.NET on WINE, and it's clear that it will never be completed enough for Paint.NET's use. And I can't just "disable" the use of Direct2D. So, instead, Paint.NET now has an internal, from-scratch, clean-room reverse-engineered rewrite of Direct2D that it uses on WINE (triggered by using /wine ). It lives…

## Systems

### [WISE: World-model-guided Imagination Scheduling for Efficient Post-training of Vision-Language-Action Models](https://arxiv.org/abs/2609.03681v1)

**arXiv — Robotics** · 03 Sep · relevance 14.1

Post-training VLA policies typically rely on supervised fine-tuning with costly expert demonstrations or reinforcement learning with expensive and potentially unstable real-world exploration. World models offer a promising alternative by evaluating candidate behaviors through imagined futures, yet effective post-training requires more than accurate…

### [Rethinking On-Policy Distillation of Large Language Models II: One Training Example](https://arxiv.org/abs/2609.04172v1)

**arXiv — AI, language and HCI** · 03 Sep · relevance 13.9

On-policy distillation (OPD) combines student-generated rollouts with dense token-level supervision from a teacher. Existing work has mainly studied its algorithmic behavior, leaving the role of training data unclear. We examine this role at the data-minimal limit by training on a single query. One-shot OPD keeps improving for hundreds of steps and…

### [Sequential Beats Joint: On the Interplay between On-Policy Distillation and RLVR](https://arxiv.org/abs/2609.04108v1)

**arXiv — AI, language and HCI** · 03 Sep · relevance 13.9

Reinforcement learning with verifiable rewards (RLVR) and on-policy distillation (OPD) have emerged as two dominant methods for post-training reasoning LLMs. Prior work uses OPD's dense token-level supervision to complement the sparse RL reward, fusing the two signals within a single step: either as a \emph{weighted-additive combination} or a…

### [MINERVA: How Small Can a Manipulation Policy Be and Still Solve LIBERO?](https://arxiv.org/abs/2609.03715v1)

**arXiv — Robotics** · 03 Sep · relevance 12.6

Vision-language-action (VLA) models with billions of parameters now dominate the LIBERO manipulation benchmark, but the model capacity actually required by the benchmark remains unclear. We introduce MINERVA (MINimal Efficient Robotic Vision-Action policy), a family of deliberately compact visuomotor policies designed to measure this task-specific capacity…

## Agents

### [Understanding ChatGPT Work](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work)

**Simon Willison — LLMs** · 30 Aug · relevance 14.6

OpenAI announced ChatGPT Work on July 9th, and have been furiously iterating on it ever since. It is an extraordinarily confusing and very powerful product. Here's what I've figured out about it so far. ChatGPT Work is actually two products The more interesting version of ChatGPT Work is the one that runs in the cloud. This can be accessed via chatgpt.com…

### [My predictions in 2025](https://www.s-anand.net/blog/my-predictions-in-2025)

**S Anand** · 17 Aug · relevance 13.3

In 2025, I made a number of predictions on this blog. (Not intentionally. I just said stuff.) I asked ChatGPT to audit them. It selected 440 claims, filtered out vague or pending ones, and verified the rest. Here’s what I got right and wrong. 🟢 “My chat will overtake search in 12-18 months. When ChatGPT becomes my primary lens on knowledge…” (…

### [Claude's new system prompt really doesn't want to reproduce song lyrics](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt)

**Simon Willison — LLMs** · 02 Sep · relevance 11.7

Anthropic publish the system prompts for their Claude consumer applications ( Claude.ai and the Claude mobile apps - sadly not for Claude Cowork or Claude Code). I love that they do this, and that they share not just the current prompts but historic changes to their prompts as well. They used to keep all of the prompts on a single page, but when I checked…

## Robotics

### [MulDP: Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation across Complex Terrains](https://arxiv.org/abs/2609.03984v1)

**arXiv — Robotics** · 03 Sep · relevance 12.7

Quadruped robots have demonstrated impressive agility in parkour locomotion across complex terrains. However, most systems still rely on human intervention for high-level planning, and autonomous parkour navigation remains underexplored. The key challenges include fine-grained velocity regulation, long-horizon anticipatory behaviors, and tight coupling…

### [Video Friday: Meet Microduck](https://spectrum.ieee.org/video-friday-microduck-robot)

**IEEE Spectrum Robotics** · 28 Aug · relevance 12.2

Video Friday is your weekly selection of awesome robotics videos, collected by your friends at IEEE Spectrum robotics. We also post a weekly calendar of upcoming robotics events for the next few months. Please send us your events for inclusion. Humanoids Summit Seoul : 22–23 September 2026, SEOUL IROS 2026 : 27 September–1 October 2026, PITTSBURGH CoRL…

### [Video Friday: Do We Need Superhuman Humanoid Robots?](https://spectrum.ieee.org/video-friday-unitree-superhuman)

**IEEE Spectrum Robotics** · 21 Aug · relevance 11.0

Video Friday is your weekly selection of awesome robotics videos, collected by your friends at IEEE Spectrum robotics. We also post a weekly calendar of upcoming robotics events for the next few months. Please send us your events for inclusion. Humanoids Summit Seoul : 22–23 September 2026, SEOUL IROS 2026 : 27 September–1 October 2026, PITTSBURGH CoRL…

## Safety

### [Breaking Claude Code Opus 5 Auto Mode](https://simonwillison.net/2026/Aug/27/breaking-claude-code-opus-5-auto-mode)

**Simon Willison — LLMs** · 27 Aug · relevance 12.1

Breaking Claude Code Opus 5 Auto Mode Anthropic are putting a great deal of faith in Claude Code's auto mode for protecting their coding agent users against prompt injection attacks. They recently made that the default and have made bold claims about its effectiveness. Johann Rehberger is one of the most credible prompt injection researchers active today.…

### [AI Companion Robots Are Closing the Human Connection in Modern Homes](https://spectrum.ieee.org/ollobot-ai-companion-robot)

**IEEE Spectrum Robotics** · 25 Aug · relevance 9.7

This article is brought to you by Ollobot . From about 2017, individuals began to truly connect with the initial wave of companion robots. These devices had personality, moved around, joked, and answered when you spoke to them. Most early companion robots, however, were still limited by simple voice-command interactions and narrow functionality. Once the…

<details>
<summary>Sources unavailable during this run</summary>

- **Berkeley AI Research:** `<urlopen error timed out>`

</details>

---

Generated by [`scripts/collect_daily.py`](./scripts/collect_daily.py) using [`data/sources.json`](./data/sources.json).
