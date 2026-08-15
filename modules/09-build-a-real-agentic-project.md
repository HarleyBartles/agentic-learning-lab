# Module 9 — Build a real agentic project

Approximate duration: 1 hour.

## Core idea

Stop teaching abstractions and build something the learner genuinely wants.

The ideal outcome is that the learner starts to think:

> This deserves a proper project home and an agent that can work inside it.

## Suggested session shape

### 0–15 minutes — Find the real use case

Ask what has occurred to the learner during the previous sessions.

Good prompts:

- What job have you caught yourself thinking AI might help with?
- What do you repeatedly copy, organise, compare, rewrite, research, or maintain?
- Is there a project where useful information currently lives across folders, notes, emails, or conversations?
- What would be useful even if it involved no programming at all?

Possible projects include research for a purchase, DIY/engineering work, family history, substantial writing, event planning, organising a collection, learning a subject, maintaining personal records, or designing something physical or digital.

### 15–30 minutes — Give it a project home

Start small:

```text
project/
    README.md
    source/
    working/
    output/
```

Put it under source control and make a clean initial checkpoint.

Ask which material is authoritative, which can be regenerated, and what should never be modified automatically.

### 30–40 minutes — Choose capabilities deliberately

Ask what the agent actually needs to do.

Select only the tools that serve those jobs. Add connectors only when the project needs to cross an external boundary.

Questions:

- Does it need web access?
- Does it need document/PDF tooling?
- Does it need a deterministic drawing tool?
- Does it need GitHub or email access?
- Which permissions should be read-only?
- Which systems have no reason to be connected at all?

### 40–50 minutes — Introduce persistent instructions when earned

If the learner has repeatedly told the agent the same rule, move that rule into the environment.

Examples:

- finished work belongs in `output/`;
- source material must not be modified;
- use British English;
- always render and inspect PDFs before calling the task complete;
- prefer local repository inspection over GitHub retrieval when the repository is already on disk.

This is the right point to introduce `AGENTS.md` as durable project-specific working guidance.

A useful rule:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

### 50–60 minutes — Capture the first reusable workflow

If a repeated task is a reusable way of working rather than a project fact, capture it as a skill.

Examples:

- safely publish repo work through GitHub;
- generate, render, and verify a PDF;
- create and check a technical drawing;
- investigate source material while preserving provenance.

Keep the distinction visible:

- tool/MCP = what can I do?
- skill = how should I do this kind of work?
- project instructions = what rules apply here?
- task = what are we doing now?

Do not create a skill merely because skills exist. The learner should be able to point to the repeated workflow it replaces.

## Tools to experiment with

Choose them based on the real project rather than curriculum requirements:

- Git and a remote repository;
- Codex or another on-disk agent;
- one or two project-specific local tools;
- a carefully chosen MCP/connector if needed;
- `AGENTS.md` once repeated project guidance exists;
- one small skill once a reusable workflow exists.

## Reflect on the full system

By this point, discuss:

**model + harness + instructions + context + tools + persistent state + feedback**

Ask:

- What belongs on disk?
- What belongs in chat?
- What should be connected externally?
- What should the agent be allowed to modify?
- How will we know when its work is correct?
- Which repeated behaviours should become persistent instructions or skills?
- What is the recovery path when an experiment goes wrong?

## Signs the learning plan has worked

The learner does not need to know every technical term.

More useful signs are that they naturally ask:

- Should this have a repo/project home?
- Can the agent inspect the source directly instead of me copying it around?
- Is this a model problem or an environment/tool problem?
- What tool is actually appropriate for this output?
- How do we verify the result?
- Can I revert this if it is wrong?
- Is this repeated guidance a project instruction or a reusable workflow?

## After this module

Advanced topics can arrive because real work demands them: branches and worktrees, PR workflows, richer MCPs, multiple agents, RAG, hooks, CI/CD, automation, scheduling, or more formal governance.

The learning lab should now become reference material rather than the centre of the work.
