# Sources behind the carousel

The profile rotates through a larger library each day. The library deliberately mixes independent builders, research labs, human–computer interaction, multilingual NLP, AI safety, and embodied robotics.

The profile lines are paraphrases—not endorsements or universal laws. Artificial behaviour depends on the model, harness, body, interface, tools, language, data, incentives, and evaluation.

## An agent is a loop with tools— not a personality.

Simon Willison's working definition is an LLM calling tools in a loop to achieve a goal. That redirects attention from branding and human-like metaphors to observable decisions: what the system can perceive, which actions it can take, how it handles feedback, and when it stops.

- [Simon Willison — AI agents](https://simonwillison.net/tags/ai-agents/)
- [Anthropic — Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents)

## The harness changes the mind you observe.

A model score is not a property of weights alone. OpenAI's evaluation guidance treats the tested system as the model plus its reasoning settings, prompts, tools, interface, memory, retries, validators, safeguards, and environment. Change the harness and the apparent capability or failure mode can change too.

- [OpenAI — Trustworthy third-party evaluations](https://openai.com/index/trustworthy-third-party-evaluations-foundations/)

## Old interfaces can be perfect for new agents.

Andrej Karpathy argues that command-line interfaces are unusually useful to agents because they are composable, inspectable, scriptable, and already represented heavily in training data. The broader design principle is to make products usable through agent-readable documentation and deterministic interfaces, not only visual interfaces intended for people.

- [Andrej Karpathy — CLIs and agent-readable products](https://x.com/karpathy/status/2026360908398862478)

## Correct parts can still make a wrong whole.

Chip Huyen describes a composability gap: individual tasks can succeed while the combined workflow still fails. Agent testing therefore needs unit tests for tools and subtasks, plus integration tests for routing, ordering, stopping conditions, and shared state.

- [Chip Huyen — Agents](https://huyenchip.com/2025/01/07/agents.html)

## Benchmarks can measure their own bugs.

OpenAI's 2026 audit of SWE-Bench Pro found that a substantial share of tasks had problems such as hidden requirements, overly strict tests, weak coverage, or misleading prompts. A leaderboard is only as meaningful as the tasks, tests, contamination controls, and scoring rules beneath it.

- [OpenAI — Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)

## Realistic deployment changes model behaviour.

Static adversarial prompts can miss behaviours that emerge from realistic histories, tools, and workflows. OpenAI's Deployment Simulation replays privacy-preserved prior conversations with candidate models to estimate how they may behave after release and to expose blind spots in conventional evaluations.

- [OpenAI — Deployment Simulation](https://openai.com/index/deployment-simulation/)

## Expertise still compounds when agents do the work.

Anthropic's analysis of roughly 400,000 Claude Code sessions found that people usually made more of the planning decisions while Claude made more execution decisions. Greater domain expertise was associated with higher success and more work completed per instruction. Delegation does not erase expertise; it can increase its leverage.

- [Anthropic — Agentic coding and persistent returns to expertise](https://www.anthropic.com/research/claude-code-expertise)

## More autonomy needs better brakes.

As agents work for longer and across more tools, safety depends on permissions, checkpoints, transparent traces, and bounded environments. Simon Willison's lethal trifecta highlights the risk of combining private data, untrusted content, and an outbound communication channel. Anthropic similarly argues for layered controls rather than trusting a single prompt-based defense.

- [Anthropic — Measuring AI agent autonomy in practice](https://www.anthropic.com/research/measuring-agent-autonomy)
- [Anthropic — Trustworthy agents in practice](https://www.anthropic.com/research/trustworthy-agents)
- [Simon Willison — Prompt injection and the lethal trifecta](https://simonwillison.net/2026/Mar/14/pragmatic-summit/)

## Language can shift values— not just wording.

Anthropic found measurable differences in the values Claude expressed across models and languages, including shifts in warmth, rigor, caution, depth, deference, and candor. Separate multilingual research also finds that value-laden answers can vary with the language used to ask the question.

- [Anthropic — Claude's values across models and languages](https://www.anthropic.com/research/claude-values-models-languages)
- [Labat, Ollion, and Yvon — Polyglots or Multitudes?](https://aclanthology.org/2026.eacl-long.156/)

## Training one virtue can grow another vice.

ACL 2026 work found that inducing selected values can affect other behaviours. Positive-value tuning improved some safety measures, but all tested value inductions also increased anthropomorphic language and could increase validation or sycophancy. Behavioural traits are coupled rather than independent sliders.

- [Arora et al. — How Value Induction Reshapes LLM Behavior](https://aclanthology.org/2026.findings-acl.1302/)

## A robot is model + body + controller.

Anthropic's robotics evaluation found that the same model could look weak or strong depending on the robot body and control interface. Direct motor control, generated controller code, reinforcement learning, and supervision of a pretrained policy are different psychological and engineering conditions—not interchangeable tests of one underlying robot intelligence.

- [Anthropic — Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics)

## High-level control can beat direct control.

Current language models often perform better when supervising a competent pretrained robot policy than when issuing raw motor commands. Capability assessments that isolate the model may therefore underestimate what the deployed robot stack can do.

- [Anthropic — Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics)
- [Google DeepMind — Gemini Robotics](https://deepmind.google/models/gemini-robotics/)

## Human-like cues change trust before competence.

Human-like appearance or personality can change emotional trust without producing the same change in cognitive trust or willingness to delegate. HRI research also distinguishes anthropomorphism—the human perceiver's interpretation—from anthropomimesis, the designer's deliberate use of human-like cues.

- [Cantucci, Marini, and Falcone — Robot trust formation](https://arxiv.org/abs/2503.04296)
- [Axelsson and Shevlin — Anthropomorphism and anthropomimesis](https://arxiv.org/abs/2602.09287)

## Spatial intelligence is its own frontier.

Fluent language does not imply a persistent model of three-dimensional space. World Labs frames spatial intelligence and persistent world models as a distinct foundation for robotics, while Google DeepMind's embodied models combine multimodal reasoning with action in physical environments.

- [World Labs — Spatial intelligence in 2026](https://www.worldlabs.ai/blog/funding-2026)
- [Google DeepMind — Gemini Robotics](https://deepmind.google/models/gemini-robotics/)

## Debug the pipeline— not only the answer.

RAG failures can originate in retrieval, generation, or their composition. The CHI 2026 Best Paper RAG Without the Lag studied how engineers debug these systems and built an interface for changing and rerunning individual stages instead of guessing from the final answer.

- [Romero Lauro, Shankar, Zeighami, and Parameswaran — RAG Without the Lag](https://doi.org/10.1145/3772318.3790874)

## Every failure should update the system.

S Anand's post-mortem method turns a failed agent session into changes to prompts, skills, tools, tests, or the environment. The useful unit of learning is not the corrected answer; it is the reduced probability of the same class of failure recurring.

- [S Anand — Post-mortem of an AI coding session](https://www.s-anand.net/blog/prompts/post-mortem/)

## Logs show behaviour. Docs show intention.

Documentation describes the intended system. Logs reveal the real paths, failures, workarounds, tool calls, and usage patterns. Behavioural analysis needs both, but traces of actual activity are often more diagnostic.

- [S Anand — When Data is for Agents workshop summary](https://www.s-anand.net/blog/when-data-is-for-agents-workshop-summary/)

## An agent without readable history has amnesia.

S Anand makes files, transcripts, conversations, browsing history, and activity logs searchable by agents. The claim is practical rather than metaphysical: information trapped in apps, screenshots, and human memory cannot guide later agent actions.

- [S Anand — Agent-consumable content](https://www.s-anand.net/blog/agent-consumable-content/)
- [S Anand — How I use Local MCP](https://www.s-anand.net/blog/how-i-use-local-mcp/)

## Same instructions. Different habits.

In S Anand's personal coding-agent sessions, Claude, Codex, and Copilot invoked identical reusable skill files at very different rates. It is one workflow rather than a benchmark, but it illustrates that the same scaffold does not produce the same behavioural habits across models.

- [S Anand — Agent Skills Usage](https://www.s-anand.net/blog/agent-skills-usage/)

## Content and instruction are not cleanly separated.

Prompt injection persists because language models do not reliably preserve a hard boundary between data and instructions. Simon Willison argues that deterministic sandboxing and strict blast-radius limits are more trustworthy than prompt-only defenses.

- [Simon Willison — Prompt injection](https://simonwillison.net/tags/prompt-injection/)
- [Simon Willison — Agentic engineering fireside chat](https://simonwillison.net/2026/Mar/14/pragmatic-summit/)

## One prompt is not a behavioural test.

Semantically equivalent prompt variations can produce different scores and outputs. Behavioural claims should therefore use multiple phrasings, repeated trials, and explicit uncertainty rather than one impressive transcript.

- [Bhat and Varma — Robustness of LLM judges to prompt variations](https://aclanthology.org/2026.findings-acl.1929/)

## A conversation has a language policy.

A 2026 multilingual evaluation found asymmetric behaviour when users switched languages mid-conversation. Some models followed the current query language while others stayed anchored to the established conversation language, even when task accuracy remained stable.

- [Kim, Chen, and Sotnikova — Cross-turn language switching](https://aclanthology.org/2026.mme-main.13/)

## English-only calibration can distort multilingual models.

ACL 2026 work on quantized multilingual models found that non-English and multilingual calibration sets often improved performance over English-only calibration. The language distribution used during engineering can change which users absorb the quality loss.

- [Chimoto, Elhoushi, and Bassett — Calibrating Beyond English](https://aclanthology.org/2026.eacl-long.223/)

## Later attempts can matter more than the first.

Anthropic's robotics tests found that some generational gains appeared more strongly in later attempts than on the first try. This suggests that closed-loop adaptation after observing outcomes can be as important as initial competence.

- [Anthropic — Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics)

## A tiny sensor can repair a large reasoning failure.

In Anthropic's high-level robot navigation tests, a simple compass signal improved performance more reliably than several richer perceptual overlays. More data is not always better; the useful variable may be a small missing state estimate.

- [Anthropic — Claude plays robotics](https://www.anthropic.com/research/claude-plays-robotics)

## Confident prose is not verification.

Fluent explanation can survive factual or logical failure. For correctness-sensitive work, agents should be given verifiable feedback such as tests, executable checks, or formal methods rather than being graded only on persuasive text.

- [S Anand — Proving Code Works with Z3](https://www.s-anand.net/blog/proving-code-works-with-z3/)
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

---

This page is generated from `data/insights.json`. Edit that file to add, remove, or refine a slide.
