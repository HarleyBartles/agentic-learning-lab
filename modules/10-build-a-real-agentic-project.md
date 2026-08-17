# Module 10 — Build a real agentic project

Approximate duration: 1 hour.

Status: structured planning. Treat this as a synthesis checkpoint, not as graduation from the curriculum.

## Core idea

Stop teaching abstractions and build something the learner genuinely wants.

The ideal outcome is that the learner starts to think:

> This deserves a proper project home and an agent that can work inside it.

By this point, the learner should have enough prior mental models to build a small but real agentic environment deliberately rather than copying a template without understanding why it exists.

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

Do not treat capability richness as automatically desirable. This module should already plant the question that later selective-provisioning work will deepen:

> Does this worker need this capability for the job in front of it?

### 40–50 minutes — Own and maintain persistent instructions

Lab 5 already revealed `AGENTS.md` as one of the layers shaping agent behaviour. The learner opened the prepared project instructions, changed one bounded rule by hand, and observed a fresh agent receive the changed environment.

This phase is therefore **not another reveal**.

The new step is that this is the learner's real project. There is no facilitator-owned answer for what its standing doctrine should be.

If the learner has repeatedly told the agent the same stable project rule, ask:

> Where should this live so we stop rebuilding it in every prompt?

Have the learner decide whether the rule really is stable project doctrine. If it is, they can now deliberately ask the agent to create or modify the project's `AGENTS.md`, then inspect that change before accepting it.

Examples:

- finished work belongs in `output/`;
- source material must not be modified;
- use British English;
- always render and inspect PDFs before calling the task complete;
- prefer local repository inspection over GitHub retrieval when the repository is already on disk.

Explicitly connect this to Lab 5:

> In Lab 5 you changed one standing instruction yourself so you could see the lever clearly. This project is yours, so now you decide what stable working doctrine belongs here — and you can delegate maintaining that file because you understand what it does.

A useful rule remains:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

But do not imply that every useful rule should be accumulated forever. A later module will deliberately pressure-test over-provisioning and instruction scope.

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
- reference/domain material = what does competent work mean here?
- verification = how will we know the result is good enough?
- task = what are we doing now?

Do not create a skill merely because skills exist. The learner should be able to point to the repeated workflow it replaces.

## Knowledge has a destination

Use this real project to reinforce a question that becomes more important as the learner gains more agentic levers:

> What kind of knowledge did we just discover, and therefore where should it live?

Useful mapping:

- project fact -> durable project state;
- stable project rule -> project instructions;
- reusable procedure -> skill/workflow;
- source convention/standard -> reference material;
- quality requirement -> verification/evaluation criterion;
- task-specific choice -> current task/conversation unless it should become project state.

The goal is not merely to save knowledge. It is to put it in the right layer.

## Tools to experiment with

Choose them based on the real project rather than curriculum requirements:

- Git and a remote repository;
- Codex or another on-disk agent;
- one or two project-specific local tools;
- a carefully chosen MCP/connector if needed;
- learner-owned `AGENTS.md` maintained deliberately once repeated project guidance exists;
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
- Which knowledge belongs in which layer?
- Which tools or context does this worker not need?

## Signs the learning plan has worked so far

The learner does not need to know every technical term.

More useful signs are that they naturally ask:

- Should this have a repo/project home?
- Can the agent inspect the source directly instead of me copying it around?
- Is this a model problem or an environment/tool problem?
- What tool is actually appropriate for this output?
- How do we verify the result?
- Can I revert this if it is wrong?
- Is this repeated guidance a project instruction or a reusable workflow?
- Which source is authoritative?
- What should this worker actually be allowed to touch?

## This is a synthesis checkpoint, not the end

Do not frame this module as `you now know agentic AI`.

The learner now knows enough to build a genuine project environment. That gives later curriculum somewhere real to land.

From this point onward, use both:

- bounded teaching fixtures when a controlled comparison matters;
- the learner's real project when the new operating pattern naturally belongs there.

Important later concepts still remain to be earned, including:

- agent self-introspection, local review, behavioural prediction, and test-first probes;
- autonomous human-in-the-loop lifecycle orchestration;
- specialist agent profiles and delegation;
- harness portability, effective-worker verification, observability, and current model/reasoning control surfaces;
- agent-system economics: capability, context, and inference should earn their cost;
- selective provisioning and agent overwhelm;
- context transport/materialisation, lazy/eager loading, and N+1-style repeated context work;
- finite context and retrieval/RAG;
- lightweight evaluation and TDD-inspired agent design;
- untrusted-content and capability boundaries;
- concurrent agents, isolation, integration, and re-verification.

The learning lab can increasingly become reference material without ceasing to be the source of deliberate conceptual pressure tests.