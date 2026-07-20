# Sources behind the carousel

The profile slides distill ideas from S Anand's public work from February–July 2026. They are observations and working hypotheses—not universal laws. Agent behaviour changes across models, versions, interfaces, tools, permissions, tasks, and users.

## Agents need actions, not just information

Anand's July workshop proposes that agent-oriented data should expose tools and functions, not merely human-readable tables. The distinction matters when the desired outcome is action rather than inspection.

- [When Data is for Agents — Workshop Summary](https://www.s-anand.net/blog/when-data-is-for-agents-workshop-summary/)
- [When Data is for Agents, Not Humans — workshop announcement](https://www.s-anand.net/blog/when-data-is-for-agents-not-humans-workshop/)

## Logs show behaviour; docs show intention

Documentation describes the intended system. Logs reveal the real paths, failures, workarounds, and usage patterns. Behavioural analysis needs both, but the second is often more diagnostic.

- [When Data is for Agents — Workshop Summary](https://www.s-anand.net/blog/when-data-is-for-agents-workshop-summary/)

## An agent without readable history has amnesia

Anand makes files, transcripts, conversations, browsing history, and activity logs searchable by agents. His argument is that agent-readable records let earlier work compound; information trapped in apps, screenshots, and memory is effectively unavailable.

- [Agent-consumable content](https://www.s-anand.net/blog/agent-consumable-content/)
- [How I use Local MCP](https://www.s-anand.net/blog/how-i-use-local-mcp/)

## Same instructions, different habits

In Anand's personal coding-agent sessions, the same reusable skill files were invoked very differently by Claude, Codex, and Copilot. For example, the `code` skill appeared in 6.1% of Claude sessions and 69.1% of Codex sessions. This is one person's workflow—not a benchmark—but it is a useful behavioural signal: identical scaffolding does not produce identical agent habits.

- [Agent Skills Usage](https://www.s-anand.net/blog/agent-skills-usage/)

## Models can confuse who said what

Anand highlighted work on project-injection attacks where role-like text such as `User:` can alter how a model interprets provenance and authority. The broader lesson is that models do not always preserve a reliable boundary between content and instruction.

- [Things I Learned — 05 Jul 2026](https://www.s-anand.net/blog/things-i-learned-05-jul-2026/)

## The interface can change the answer

Anand observed Claude reasoning that a mobile user might prefer a shorter response. This is anecdotal, but it exposes a useful hypothesis: device, interface, memory, permissions, and tool availability can become hidden behavioural context.

- [Things I Learned — 28 Jun 2026](https://www.s-anand.net/blog/things-i-learned-28-jun-2026/)

## Confident prose is not verification

For correctness-sensitive work, Anand recommends having agents execute code, tests, or formal checks rather than relying only on verbal reasoning. He has also used Z3 to prove properties of code and advocates cross-checking high-risk claims.

- [AI Advice](https://www.s-anand.net/blog/ai-advice/)
- [Proving Code Works with Z3](https://www.s-anand.net/blog/proving-code-works-with-z3/)

## Every failure should update the system

A blameless post-mortem turns a failed session into changes to prompts, reusable skills, tools, tests, or the environment. The goal is to remove a class of failures rather than patch one disappointing answer.

- [Post-mortem of AI coding session](https://www.s-anand.net/blog/prompts/post-mortem/)

---

The slides paraphrase these ideas for a robot-psychology profile. The linked posts remain the source of record.