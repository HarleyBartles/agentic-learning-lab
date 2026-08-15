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
6. Tools and operating knowledge
7. Local work and connected systems
8. Source of truth and verification
9. Build a real agentic project

Lab 2 is the direct continuation of Lab 1. Lab 1 showed that an agent which cannot see the project surface cannot know what project state is missing. Lab 2 changes that access condition by giving cloud ChatGPT a bridge to the repository, then compares connector-mediated access with direct local workspace access.

Lab 3 is now being promoted from module planning into a real lab structure. Exercise 1 uses a Repair Café planning project to show that important project decisions disappear with a lost conversation unless they are persisted into durable project state.

Labs 1 and 2 have expanded lab structures and Lab 3 is in active scaffold development. Existing files in `modules/` are working facilitator drafts for curriculum material that has not yet been fully promoted into labs; they may be rewritten, folded into labs, combined, or reordered as those labs take shape.

See also [Core principles](docs/core-principles.md) for ideas that should recur throughout the conversations.

## Repository areas

- `labs/` contains complete learning experiences, including learner guidance, facilitator notes, and bounded working environments where appropriate.
- `docs/` contains cross-cutting principles and curriculum-wide guidance.
- `modules/` currently contains draft planning material for later labs or unpromoted portions of labs still being developed.
- `projects/` contains small example project environments that are not primarily software projects.

There is deliberately no separate root-level `guided/` or stable facilitator hierarchy. Learner and facilitator material that belongs to a lab lives with that lab.

## Expected progression

The broad progression currently begins:

**chat without project access -> on-disk workspace -> connected cloud access -> persistent project state -> recoverable history -> model/harness/context/tools -> purpose-built capabilities and operating knowledge -> composed local/connected systems -> source of truth -> verification -> real project**

The exact later sequence can continue to move as the labs are expanded and tested.

## Important safety model

This repository is a laboratory. Nothing in it should be precious.

The learner is expected to make bad changes, delete things, ask agents to do overly broad work, inspect the result, and recover it. The goal is to replace fear of breakage with the engineering question:

> What is the blast radius, and do I have a recovery path?

Be fearless with reversible project state. Be deliberate with irreversible or external side effects.
