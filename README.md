# Agentic Learning Lab

A conversational, practical learning environment for understanding agentic AI by using it.

This is not a formal course and the learner is not expected to become a programmer. The aim is to build useful mental models through discussion, examples, experiments, mistakes, recovery, and eventually a real project of the learner's own.

## Learning philosophy

The lab is built around a few ideas:

- Start from friction the learner has already experienced.
- Teach the problem before the mechanism that solves it.
- Prefer real demonstrations over abstract explanation.
- Keep early environments simple; add tools only when their value is visible.
- Break things deliberately in a safe environment.
- Make reversible experimentation feel normal.
- Treat source control as a recovery mechanism, not as programmer ceremony.
- Distinguish the model from the harness, context, tools, state, and feedback around it.
- Give agents both the tools they need and the operating knowledge to use those tools well.
- Treat local project access and connectors as complementary capabilities.
- Prefer evidence of completed work over confident agent claims.
- Teach the learner to direct, inspect, verify, question, and iteratively steer agent work rather than becoming the agent's manual implementation layer.
- Give the learner useful interim mental models, then deliberately break and refine them when later examples expose their limits.
- Teach agents how work moves through a lifecycle, not only how to perform isolated tasks.
- Treat delegation to specialist agents as a design choice rather than an automatic sign of maturity.
- Treat provisioning as selective design rather than accumulation: the right knowledge, at the right scope, when the worker needs it.
- Define observable success for agent behaviour and re-test it when instructions, skills, tools, profiles, or context change.

## Learner workspace from day one

Before Lab 1, the facilitator should help the learner fork this repository into the learner's own GitHub account.

The learner does not need to understand forks, remotes, upstreams, or synchronization yet. The practical explanation can simply be:

> This is your copy of the laboratory. You can break this one.

The intended roles are:

```text
upstream curriculum repository
facilitator-maintained teaching source
        ↓ fork
learner-owned repository
persistent laboratory for the whole curriculum
        ↓
local checkout / connectors / agent workspaces
```

Early synchronization can remain facilitator plumbing. Later modules can deliberately reveal the difference between local working state, the learner's remote fork, and upstream curriculum state.

Lab-scoped `AGENTS.md` files survive the fork. In Labs 1–4 they are facilitator-owned experimental controls: they establish stable agent behaviour and safety boundaries without making instruction architecture the subject of those labs. Lab 5 explicitly reveals this lever: the learner reads the project instructions with the facilitator, hand-edits one bounded standing rule, and starts a fresh agent to observe the resulting behaviour. Later, when the learner creates a real project, they own that instruction surface and can deliberately delegate its maintenance to an agent.

## Labs

A lab is the complete learning experience for one topic. Where useful, a lab contains separate surfaces for the learner, facilitator, and working mission/project environment.

Lab 1 is the stable reference structure:

```text
labs/01-chatbot-to-worker/
    README.md
    facilitator/
        README.md
    learner/
        01-complete-context.md
        02-missing-context.md
        03-on-disk-worker.md
        04-cloud-project.md
    mission/
        README.md
        source/
        output/
```

The responsibilities are intentionally local to the lab:

```text
lab
    the complete learning experience

facilitator/
    why and how to run it

learner/
    what the learner should do next

mission/ or project/
    the bounded environment the AI actually works in, when the lab needs one
```

Not every lab needs a mission. Labs should use whatever small set of exercises best demonstrates the lesson.

If a file only makes sense because a particular lab exists, it should usually live inside that lab. Cross-cutting doctrine belongs in `docs/`.

For Lab 1, learner cards should be revealed one at a time. The local Codex worker is scoped to the `mission/` folder rather than the whole lab so it does not see the teaching choreography.

## Curriculum

The numbering below is the current planning order, not a promise that every module will keep this exact position. Conceptual dependencies matter more than fixed numbering while later labs are still being designed.

1. [From chatbot to worker](labs/01-chatbot-to-worker/)
2. [Give the cloud agent the project](labs/02-give-the-cloud-agent-the-project/)
3. [The project has a home](labs/03-project-has-a-home/)
4. [Repositories, save points, and safe breakage](labs/04-repositories-save-points-and-safe-breakage/)
5. [Model, harness, context, tools, and behaviour](labs/05-model-harness-context-tools-and-behaviour/)
6. Tools, operating knowledge, and domain provisioning
7. What did we just create? Local work and connected systems
8. Source of truth and verification
9. Build a real agentic project
10. Autonomous human-in-the-loop workflows
11. Specialist sub-agents and orchestration
12. Selective provisioning, context, and evaluation
13. Trust boundaries and connected autonomy
14. Concurrent agents and isolation
15. Epilogue: show how this was built

Lab 2 is the direct continuation of Lab 1. Lab 1 showed that an agent which cannot see the project surface cannot know what project state is missing. Lab 2 changes that access condition by giving cloud ChatGPT a bridge to the learner's repository, then compares connector-mediated access with direct local workspace access.

Lab 3 stops treating cloud versus local as the organizing question and focuses on durable project state, deliberate promotion of conversational material, and conflicting durable artifacts.

Lab 4 makes the source-control machinery visible after the learner has already benefited from it: working state, recorded history, diffs, commit versus push, historical recovery, and the boundary where Git can no longer undo external consequences.

Labs 1–5 are mature and ready to run.

The middle curriculum deliberately compounds earlier ideas rather than replacing them. Lab 5 decomposes observed agent behaviour into model, harness, instructions, context, tools, environment, state, and feedback. Module 6 uses that model to provision a worker for a domain. Module 7 lets the learner temporarily treat the assembled worker as `an Agent`, then asks where that worker should operate and what it should be connected to. Later modules deliberately refine that conception again.

Modules 10 and 11 continue the same progression. Module 10 teaches one provisioned agent to carry work from vague intent through clarification, design, planning, execution, self-review, human approval gates, and finalisation. Module 11 then puts pressure on the `one worker does every stage` model and introduces specialist agent profiles, delegation, and orchestrator tradeoffs.

Module 12 deliberately breaks another useful but incomplete model: that good provisioning means continually adding more useful guidance and capability. It uses agent overwhelm to teach selective scope, finite context, retrieval/RAG as context selection, lightweight evaluation, and TDD-inspired agent design without requiring code.

Module 13 connects Lab 3's authority model to connected/autonomous systems: external content is evidence rather than operating authority, capability should follow responsibility, and autonomy needs explicit stopping conditions and provenance.

Module 14 finally breaks Module 4's intentionally simple `one worker, one mutable workspace` model. Concurrent specialists earn isolated workspaces, deliberate reconciliation, and verification of the integrated state rather than a premature Git branching lesson.

Module 9 should be treated as a synthesis checkpoint rather than graduation. Once the learner can create a real agentic project, that real project can become one of the surfaces used to learn the later operating patterns.

Existing files in `modules/` are working facilitator drafts for later curriculum material that has not yet been promoted into a mature lab.

See also [Core principles](docs/core-principles.md), [Learning methodology and origin](docs/learning-methodology.md), and [Curriculum threads, breadcrumbs, and future cash-ins](docs/curriculum-threads.md).

## Repository areas

- `labs/` contains complete learning experiences, including learner guidance, facilitator notes, and bounded working environments where appropriate.
- `docs/` contains cross-cutting principles and curriculum-wide guidance.
- `modules/` contains draft planning material for later labs that have not yet been fully promoted.

There is deliberately no separate root-level `guided/`, `projects/`, or stable facilitator hierarchy. Learner and facilitator material, fixtures, and project environments that belong to a lab live with that lab.

## Expected progression

The broad conceptual progression currently includes:

**chat without project access -> on-disk workspace -> connected cloud access -> persistent project state -> recoverable history -> model/harness/context/tools -> purpose-built capabilities and domain knowledge -> provisioned worker -> composed local/connected systems -> authority and verification -> real project -> autonomous human-in-the-loop workflow -> specialist delegation -> selective context/provisioning and evaluation -> trust boundaries -> concurrent isolation and integration -> retrospective on how the whole framework was built**

The exact module sequence can move while labs are expanded and tested. Preserve the causal links and breadcrumbs rather than treating today's numbering as immutable.

## Important safety model

This repository is a laboratory. The learner's fork should contain nothing precious.

The learner is expected to make bad changes, delete things, ask agents to do overly broad work, inspect the result, and recover it. The goal is to replace fear of breakage with the engineering question:

> What is the blast radius, and do I have a recovery path?

Be fearless with reversible project state. Be deliberate with irreversible or external side effects.
