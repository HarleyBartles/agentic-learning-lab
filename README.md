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

1. [From chatbot to worker](labs/01-chatbot-to-worker/)
2. [Give the cloud agent the project](labs/02-give-the-cloud-agent-the-project/)
3. [The project has a home](labs/03-project-has-a-home/)
4. Repositories, save points, and safe breakage
5. Model, harness, context, tools, and behaviour
6. Tools, operating knowledge, and domain provisioning
7. What did we just create? Local work and connected systems
8. Source of truth and verification
9. Build a real agentic project
10. Autonomous human-in-the-loop workflows
11. Specialist sub-agents and orchestration
12. Epilogue: show how this was built

Lab 2 is the direct continuation of Lab 1. Lab 1 showed that an agent which cannot see the project surface cannot know what project state is missing. Lab 2 changes that access condition by giving cloud ChatGPT a bridge to the repository, then compares connector-mediated access with direct local workspace access.

Lab 3 is stable and ready to run. Its three Repair Café exercises show that important decisions must enter durable project state, that conversation should not be promoted into that state without deliberate authority, and that durable project artifacts can later drift and disagree about the same fact.

The middle curriculum deliberately compounds earlier ideas rather than replacing them. Module 5 decomposes observed agent behaviour into model, harness, instructions, context, tools, environment, state, and feedback. Module 6 uses that model to provision a worker for a domain. Module 7 lets the learner temporarily treat the assembled worker as `an Agent`, then asks where that worker should operate and what it should be connected to. Later modules deliberately refine that conception again.

Modules 10 and 11 continue the same progression. Module 10 teaches one provisioned agent to carry work from vague intent through clarification, design, planning, execution, self-review, human approval gates, and finalisation. Module 11 then puts pressure on the `one worker does every stage` model and introduces specialist agent profiles, delegation, and orchestrator tradeoffs.

Labs 1, 2, and 3 now have mature lab structures. Existing files in `modules/` are working facilitator drafts for later curriculum material that has not yet been promoted into a mature lab.

See also [Core principles](docs/core-principles.md) and [Learning methodology and origin](docs/learning-methodology.md) for curriculum-wide doctrine and the method this repository itself is intended to demonstrate.

## Repository areas

- `labs/` contains complete learning experiences, including learner guidance, facilitator notes, and bounded working environments where appropriate.
- `docs/` contains cross-cutting principles and curriculum-wide guidance.
- `modules/` contains draft planning material for later labs that have not yet been fully promoted.
- `projects/` contains small example project environments that are not primarily software projects.

There is deliberately no separate root-level `guided/` or stable facilitator hierarchy. Learner and facilitator material that belongs to a lab lives with that lab.

## Expected progression

The broad progression currently begins:

**chat without project access -> on-disk workspace -> connected cloud access -> persistent project state -> recoverable history -> model/harness/context/tools -> purpose-built capabilities and domain knowledge -> provisioned worker -> composed local/connected systems -> source of truth and verification -> real project -> autonomous human-in-the-loop workflow -> specialist delegation and orchestration -> retrospective on how the whole framework was built**

The exact later sequence can continue to move as the labs are expanded and tested.

## Important safety model

This repository is a laboratory. Nothing in it should be precious.

The learner is expected to make bad changes, delete things, ask agents to do overly broad work, inspect the result, and recover it. The goal is to replace fear of breakage with the engineering question:

> What is the blast radius, and do I have a recovery path?

Be fearless with reversible project state. Be deliberate with irreversible or external side effects.
