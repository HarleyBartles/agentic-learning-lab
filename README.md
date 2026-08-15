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

## Modules

Each module is designed to support roughly one hour of conversation, demonstration, and experimentation. They are facilitator guides rather than learner scripts.

1. [From chatbot to worker](modules/01-chatbot-to-worker.md)
2. [The project has a home](modules/02-project-has-a-home.md)
3. [Repositories, save points, and safe breakage](modules/03-repositories-save-points-and-safe-breakage.md)
4. [Model, harness, context, tools, and behaviour](modules/04-model-harness-context-tools.md)
5. [Tools and operating knowledge](modules/05-tools-and-operating-knowledge.md)
6. [Local work and connected systems](modules/06-local-work-and-connected-systems.md)
7. [Source of truth and verification](modules/07-source-of-truth-and-verification.md)
8. [Build a real agentic project](modules/08-build-a-real-agentic-project.md)

See also [Core principles](docs/core-principles.md) for the ideas that should recur throughout the conversations.

## Lab areas

- `modules/` contains facilitator guidance: learning goals, rationale, discussion prompts, and what not to teach yet.
- `guided/` contains short learner-facing stage cards intended to be revealed one at a time during a session.
- `labs/` contains the actual project exercises and their mission contracts: source material, output locations, and win conditions.
- `docs/` contains cross-cutting principles and facilitator guidance.
- `projects/` contains small example project environments that are not primarily software projects.

This separation is intentional:

```text
module document
    why we are teaching this and how to facilitate it

guided stage card
    what the learner should do right now

lab README
    what the actual project task is and what success means
```

For Module 1, start with `guided/module-01/stage-1.md` and reveal the later stage cards only when the previous stage and reflection are complete.

## Expected progression

The broad progression is:

**Chat -> workplace -> persistent state -> history -> model/harness/context/tools -> appropriate capabilities -> operating knowledge -> connectors -> source of truth -> verification -> real project**

The order beyond Module 1 is intentionally fluid. As the learner encounters real friction and develops interests, later modules may be rewritten, combined, or reordered.

## Important safety model

This repository is a laboratory. Nothing in it should be precious.

The learner is expected to make bad changes, delete things, ask agents to do overly broad work, inspect the result, and recover it. The goal is to replace fear of breakage with the engineering question:

> What is the blast radius, and do I have a recovery path?

Be fearless with reversible project state. Be deliberate with irreversible or external side effects.
