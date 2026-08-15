# Module 8 — Build a real agentic project

Approximate duration: 1 hour.

## Core idea

Stop teaching abstractions and build something the learner genuinely wants.

The ideal outcome is that the learner starts to think:

> This deserves a proper project home and an agent that can work inside it.

## Suggested starting shape

```text
project/
    README.md
    source/
    working/
    output/
    AGENTS.md
```

Put the project under source control, choose only the tools it actually needs, and add external connectors only where they serve a clear purpose.

## Introduce persistent instructions when earned

If the learner repeatedly tells the agent the same rule, move that rule into the environment.

Examples:

- finished work belongs in `output/`;
- source material must not be modified;
- use British English;
- always render and inspect PDFs before calling the task complete;
- prefer local repository inspection over GitHub retrieval when the repo is already on disk.

Use `AGENTS.md` for durable project-specific working rules.

## Introduce a skill when earned

If a repeated task becomes a reusable workflow rather than a project fact, capture it as a skill.

Examples:

- safely publish repo work through GitHub;
- generate, render, and verify a PDF;
- create and check a technical drawing;
- investigate source material with provenance preserved.

Remember the distinction:

- tool/MCP = what can I do?
- skill = how should I do this kind of work?
- project instructions = what rules apply here?
- task = what are we doing now?

## Choose a real use case

Possible projects include:

- research for a purchase;
- a DIY or engineering project;
- family history;
- a substantial writing project;
- event planning;
- organising a collection;
- learning a subject;
- maintaining personal records;
- designing something physical or digital.

The project does not need to involve programming.

## Reflect on the full stack

By this point, discuss the system as a whole:

**model + harness + instructions + context + tools + persistent state + feedback**

Ask:

- What belongs on disk?
- What belongs in chat?
- What should be connected externally?
- What should the agent be allowed to modify?
- How will we know when its work is correct?
- Which repeated behaviours should become persistent instructions or skills?

## After this module

Advanced topics can now arrive as needed rather than as curriculum requirements: branches and worktrees, PR workflows, richer MCPs, multiple agents, RAG, hooks, CI/CD, automation, scheduling, or more formal governance.
