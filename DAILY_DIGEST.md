# Robot Psychology Radar

Updated 14 October 2026, 08:02 UTC from 17 working sources.

24 high-relevance items across 5 sources. Auto-collected metadata; inclusion is not endorsement.

## Systems

### [Things I Learned - 11 Oct 2026](https://www.s-anand.net/blog/things-i-learned-11-oct-2026)

**S Anand** · 11 Oct · relevance 13.9

This week, I learned: Python 3.15 is out . My favorite features are: frozendict is hashable . So frozen dicts can be dict keys. Unpacking in Comprehensions . [*x for x in [[1, 2], [3, 4]]] = [1, 2, 3, 4] . {**x for x in [{1: 2}, {3: 4}]} = {1: 2, 3: 4} . Once you start thinking this way, it gets easier. UTF-8 is the default . In source and text processing.…

### [Geometric Calibration of Supervised Fine-Tuning](https://arxiv.org/abs/2610.18634v1)

**arXiv — AI, language and HCI** · 13 Oct · relevance 13.3

Recent studies investigate the weight geometry through its spectral structure, which characterizes how the weights transform different input directions. Within this view, supervised fine-tuning (SFT) is shown to induce dense updates that perturb the spectral geometry of pre-SFT weights along their principal directions, potentially disrupting the model's…

### [LoopWAM: Closed-Loop Generalist Policy Improvement from Deployment Rollouts](https://arxiv.org/abs/2610.18873v1)

**arXiv — Robotics** · 13 Oct · relevance 12.6

Scaling expert demonstrations alone does not enable generalist robot policies to improve from deployment. Real-world rollouts contain successes, suboptimal behavior, and failures: imitating every recorded action can reinforce poor behavior, while filtering out failures discards evidence of physical interactions and their consequences. We introduce…

### [What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869v1)

**arXiv — Robotics** · 13 Oct · relevance 12.6

How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations…

### [GeoReader: Learning Latent Geometry for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.18694v1)

**arXiv — AI, language and HCI** · 13 Oct · relevance 12.3

Vision-language models (VLMs) struggle with metric and multi-view relationships that remain implicit in RGB observations. Geometry foundation models recover this structure from RGB, but existing methods either fuse the estimated features with visual tokens and learn to use them from question answering alone, or align VLM latents with geometry features.…

### [Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with Tool-Augmented Judges](https://arxiv.org/abs/2610.18766v1)

**arXiv — AI, language and HCI** · 13 Oct · relevance 12.2

Rubric-based reward models (RMs) evaluate responses against explicit criteria. However, existing methods often derive criteria from observed response candidates, introducing response-induced bias that may limit rubric generalizability. Their judges also struggle with mechanical constraints when relying on reading alone, and commonly used pairwise judges…

## Robotics

### [This Disembodied Hand Is All the Robot You Need](https://spectrum.ieee.org/walking-robotic-hand)

**IEEE Spectrum Robotics** · 08 Oct · relevance 15.0

A hand attached to the end of an arm is a given for most humans, but what if robots didn’t have to play by the same rules as we do? Researchers from ETH Zurich have turned an off-the-shelf robotic hand into a completely self-contained robot that walks on its fingertips while using those same fingers to manipulate its environment. Besides making the perfect…

### [Video Friday: Robot Decommissioning Takes a Fun Turn](https://spectrum.ieee.org/video-friday-reachy-mini-raps)

**IEEE Spectrum Robotics** · 09 Oct · relevance 14.2

Video Friday is your weekly selection of awesome robotics videos, collected by your friends at IEEE Spectrum robotics. We also post a weekly calendar of upcoming robotics events for the next few months. Please send us your events for inclusion. CoRL 2026 : 9–12 November 2026, AUSTIN Humanoids 2026 : 6–9 December 2026, SANTA CLARA, CA Enjoy today’s videos!…

### [Video Friday: Albatross Falls, Spins, Self-Rights, and Sails Away](https://spectrum.ieee.org/video-friday-bioinspired-robotics)

**IEEE Spectrum Robotics** · 02 Oct · relevance 13.6

Video Friday is your weekly selection of awesome robotics videos, collected by your friends at IEEE Spectrum robotics. We also post a weekly calendar of upcoming robotics events for the next few months. Please send us your events for inclusion. CoRL 2026 : 9–12 November 2026, AUSTIN Humanoids 2026 : 6–9 December 2026, SANTA CLARA, CA Enjoy today’s videos!…

### [HiPHI: A Large-Scale Benchmark for High-Precision Human Motion and Object Interaction](https://content.knowledgehub.wiley.com/hiphi-a-large-scale-benchmark-for-high-precision-human-motion-and-object-interaction)

**IEEE Spectrum Robotics** · 07 Oct · relevance 12.9

This White Paper gives robotics researchers and engineers an overview of a new large-scale motion capture dataset built to close the data gap limiting humanoid robot learning. It also shows how policies trained on the dataset transfer to a real humanoid robot. What you will learn about: Why humanoid robot learning, a central problem in embodied AI and…

### [Video Friday: Life’s Better With a Little Robot Goose](https://spectrum.ieee.org/video-friday-goose-household-robots)

**IEEE Spectrum Robotics** · 25 Sep · relevance 10.9

Video Friday is your weekly selection of awesome robotics videos, collected by your friends at IEEE Spectrum robotics. We also post a weekly calendar of upcoming robotics events for the next few months. Please send us your events for inclusion. IROS 2026 : 27 September–1 October 2026, PITTSBURGH CoRL 2026 : 9–12 November 2026, AUSTIN, TEXAS Humanoids 2026…

## Evaluation

### [EgoExplorer: A Vision-Motion-Touch Observatory for Human Loco-Manipulation In Situ](https://arxiv.org/abs/2610.18872v1)

**arXiv — Robotics** · 13 Oct · relevance 15.3

Learning humanoid loco-manipulation from human demonstrations rests on observing how locomotion, posture, and object interaction evolve together as tasks unfold. Scaling collection across diverse environments, in turn, favors lightweight, portable capture systems. Yet, existing datasets provide only partial views of this coordination. Thus, we introduce…

### [LIBERO-RIG: A Hardware-Setup Robustness Benchmark for Vision-Language-Action Models](https://arxiv.org/abs/2610.18843v1)

**arXiv — Robotics** · 13 Oct · relevance 15.2

Robot policies are expected to generalize across deployment environments, including variations in the robot itself: cameras are bumped and remounted, calibrations drift, controllers run at different rates, and end-effector pads wear down. We present LIBERO-RIG, a benchmark that perturbs only the robot's hardware and setup while holding every LIBERO task…

### [WorldOracle: Benchmarking Action-Conditioned World Models against Real-World Executions](https://arxiv.org/abs/2610.18826v1)

**arXiv — Robotics** · 13 Oct · relevance 12.7

We introduce WorldOracle, a benchmark specifically designed to evaluate action-conditioned world models (ACWMs) against paired real-world executions. Given the same initial observation and low-level action sequence, WorldOracle asks whether a predicted rollout reproduces what happens in the real world, including physical consequences and task-state…

### [2026 in LLMs (so far)](https://simonwillison.net/2026/Sep/27/2026-in-llms-so-far)

**Simon Willison — LLMs** · 27 Sep · relevance 9.6

On Friday I gave the closing keynote at the WeAreDevelopers World Congress North America in San Jose. I tied together the key trends from the past year into a chronological exploration of everything that happened in 2026. The video is on YouTube ; here are my annotated slides and notes to accompany the talk. And as an annotated presentation : # I'm going…

## Agents

### [BLADE: Auditing Information Use for Failure Attribution in LLM Multi-Agent Systems](https://arxiv.org/abs/2610.18780v1)

**arXiv — AI, language and HCI** · 13 Oct · relevance 12.3

Large language model multi-agent systems extend individual agents' capabilities through collaboration across specialized roles, tools, and workflows. Yet collaboration makes failures harder to diagnose: one agent may misinterpret a correct result while others carry the mistake forward. Failure attribution therefore seeks to identify the responsible agent…

### [Innovations 12 Oct 2026](https://www.s-anand.net/blog/innovations-12-oct-2026)

**S Anand** · 12 Oct · relevance 11.7

Our Innovation team built a few demos over the last couple of weeks. Three interesting things: Agents can build navigable 3D spaces Specialized vision models can outperform frontier LLMs on narrow tasks Simple search tools can beat elaborate document-retrieval systems. New capabilities Build an interactive 3D room from an image . A coding agent used…

### [Things I Learned - 04 Oct 2026](https://www.s-anand.net/blog/things-i-learned-04-oct-2026)

**S Anand** · 04 Oct · relevance 10.9

This week, I learned: Harvard authored a paper : living near nuclear power plants associated with more cancer. Several other papers published similar findings. The trouble is, there’ll always be SOME places near which cancer rates are higher - and there are enough causes that you can p-hack . But, it’s not easy to think of this upfront and very easy to…

## Machine Behaviour

### [Q&A: Mars Perseverance Rover Distance Record](https://spectrum.ieee.org/mars-rover-distance-record)

**IEEE Spectrum Robotics** · 13 Oct · relevance 14.1

On October 11 , the Perseverance rover completed a drive that brought its total distance traveled on Mars to 28.10 miles (45.22 kilometers). This is a new record for Mars rovers, enabled in large part by Perseverance’s ability to drive with much more autonomy than its predecessors. Over the last five years, Perseverance’s autonomy software has been…

### [Communicating Uncertainty in AI-Supported Nurse Scheduling: Expert Co-Design and Evaluation of an Explainable AI Prototype](https://arxiv.org/abs/2610.18679v1)

**arXiv — AI, language and HCI** · 13 Oct · relevance 13.1

Nurse scheduling is a complex optimization problem in which nurses are assigned to shifts to meet staffing demands while complying with working-time limits, qualification requirements, and other operational and regulatory constraints. Artificial intelligence is increasingly being used to support this process by forecasting future staffing needs and…

### [Things I Learned - 27 Sep 2026](https://www.s-anand.net/blog/things-i-learned-27-sep-2026)

**S Anand** · 27 Sep · relevance 10.7

This week, I learned: trafilatura is a Python library that extracts the main content as Markdown from a web page. A useful alternative to Jina Reader for text. It’s better at main content extraction but can’t handle non-HTML / JS generated / bot-protected URLs. The Remote Desktop Commander ChatGPT plugin is a good alternative to my mcpserver.py . Both let…

## Multimodal

### [Thinker-WM: A Unified World Model with Shared Multimodal Representations for Embodied Intelligence](https://arxiv.org/abs/2610.18447v1)

**arXiv — Robotics** · 13 Oct · relevance 13.8

World models have emerged as a promising paradigm for embodied AI, yet existing systems often remain fragmented in the modalities they model and the functions they support. In particular, visual dynamics, geometric structure, and executable action are commonly coupled through separate interfaces or downstream modules rather than being jointly represented…

### [OmniCompass: A Holistic Benchmark for Omni-Modal Video Grounding and Understanding](https://arxiv.org/abs/2610.18829v1)

**arXiv — AI, language and HCI** · 13 Oct · relevance 12.5

With the rapid development of multimodal large language models (MLLMs), evaluating their video understanding capabilities has become increasingly important. Existing video understanding benchmarks cover only part of the evaluation dimensions, limiting systematic diagnosis of omni-modal video understanding. We introduce OmniCompass, a holistic benchmark for…

### [Looks Right. Isn’t.](https://www.s-anand.net/blog/looks-right-isnt)

**S Anand** · 07 Oct · relevance 9.8

I conducted a session on Wed, 07 Oct 2026 at ED5518: Data Visualization for Engineers - Department of Engineering Design, IIT Madras, Chennai (remote). Speakers : Anand S Summary : AI makes pictures cheap to create but harder to trust: the reader may be another AI, and a chart, map or CAD model that looks right still needs an independent check. Takeaways :…

---

Generated by [`scripts/collect_daily.py`](./scripts/collect_daily.py) using [`data/sources.json`](./data/sources.json).
