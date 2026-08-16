# Curriculum shape

The curriculum has a deliberate four-part macro-structure.

The exact module numbering can still move while later labs are designed. Preserve the shape and conceptual dependencies even if individual topics are renumbered.

```text
Agents 101: zero to hero
        ↓
mid-curriculum project
        ↓
Advanced agentic concepts: mastering agents
        ↓
epilogue / final project task
```

## Part 1 — Agents 101: zero to hero

Current planning range: Modules/Labs 1–8.

This is the foundational run from ordinary chat use to basic agentic competence.

The learner should finish this section able to reason about an agentic system without treating it as one mysterious AI blob.

The current conceptual progression includes:

- conversation versus workspace;
- project access and context transport;
- durable project state;
- recovery and source-control save points;
- model versus harness/configuration/context/tools;
- provisioning tools and operating/domain knowledge;
- local work, connectors, and access surfaces;
- source of truth, authority, verification, and evidence.

The learner is not expected to master advanced orchestration here.

The goal is that they can successfully direct useful agent work, inspect what happened, recover from mistakes, and reason about the main layers that produced the behaviour they observed.

A useful summary is:

> **Part 1 teaches the learner how to use and understand agents competently.**

## Part 2 — Mid-curriculum project

Current planning anchor: Module 9, `Build a real agentic project`.

This is a synthesis checkpoint rather than graduation.

The learner stops working only through prepared curriculum fixtures and creates a genuine agentic project around something they actually care about.

The project should force them to apply the first half of the curriculum in a real setting:

- choose a project home;
- identify authoritative state;
- establish recovery;
- select capabilities deliberately;
- decide what should and should not be connected;
- introduce persistent project instructions when justified;
- capture reusable workflow knowledge as skills when justified;
- define how completed work will be verified.

It should feel less like another lesson and more like:

> You now know enough to build one of these for real.

The learner's real project can then become one of the surfaces used in the advanced half of the curriculum alongside bounded teaching fixtures.

A useful summary is:

> **Part 2 proves that the foundational mental models transfer into a real project.**

## Part 3 — Advanced agentic concepts: mastering agents

Current planning range: Modules 10–16.

The emphasis changes here.

The learner is no longer mainly learning how to get an agent to work. They are learning how to deliberately design the operating system around capable agents.

Current advanced threads include:

- agent self-introspection, counterfactual self-simulation, cheap local self-review, behavioural prediction, and test-first probes;
- autonomous human-in-the-loop workflows;
- loops, graphs, retries, stopping conditions, escalation routes, and escape hatches;
- defining success conditions and legal workflow transitions;
- specialist sub-agents and orchestration;
- harness portability, runtime-specific sub-agent contracts, profile translation, model/reasoning selection, inheritance/defaults, and verification of the effective worker;
- harness observability and scan-reading visible activity for churn, looping, drift, and missing progress;
- separating durable agent concepts from volatile product control surfaces;
- selective provisioning rather than accumulation;
- finite context and retrieval/RAG as context selection;
- instruction scope, hierarchy, provenance, and runtime injection;
- inspectable agent reasoning/activity and diagnosis;
- lightweight evaluation and TDD-inspired agent design;
- trust boundaries, external content, permissions, and connected autonomy;
- provenance and observability across stages/workers;
- concurrent agents, isolation, reconciliation, and re-verification.

The conceptual shift is:

```text
foundation
How do I use an agent effectively?

advanced
How do I design the environment, workflow, authority, context,
and success conditions that make agent behaviour reliable?
```

A useful summary is:

> **Part 3 teaches the learner to engineer agent behaviour rather than merely operate agents.**

## Part 4 — Epilogue as the final project task

Current planning anchor: Module 17, `Epilogue: show how this was built`.

The epilogue is not only a retrospective lecture.

It should function as the final project task.

The learner is asked to inspect and reason about the repository they have been working in throughout the curriculum.

A suitable task direction is:

> Inspect this repository and its history. Reconstruct how it developed, identify major changes in direction, explain which mental models were introduced and later refined or broken, and distinguish what the available evidence proves from what it cannot recover.

This should require the learner to use many of the capabilities developed across the course:

- project exploration;
- repository/Git history;
- source-of-truth reasoning;
- evidence versus confident narrative;
- context and retrieval choices;
- instruction and provenance awareness;
- directing an agent rather than manually performing the archaeology;
- questioning the agent's reconstruction;
- recognizing when a plausible explanation is not adequately evidenced.

If the learner has used their own fork throughout the curriculum, the epilogue can compare two histories:

```text
upstream curriculum history
how the teaching framework itself evolved

learner fork history
how this learner actually worked through and changed their laboratory
```

These are related but answer different questions.

The symmetry with the start of the curriculum is intentional:

```text
beginning
learner enters a prepared project
and directs an agent through a bounded task

ending
learner enters the whole accumulated project
and directs an agent to understand the project itself
```

The environment has become more complex, but the learner has changed more than the environment.

At the beginning, the curriculum must heavily prepare the conditions around them.

At the end, the learner should be able to decide what evidence matters, provision and direct the worker appropriately, interrogate uncertainty, trace authority and provenance, and judge whether the resulting explanation is actually credible.

A useful summary is:

> **Part 4 uses the curriculum repository itself as the final worked problem and proof of the learning method.**

## Editorial test for future topics

When adding or moving material, ask which layer of the curriculum it serves.

If the concept is required for basic competence with agents, it probably belongs in Part 1.

If it tests whether foundational understanding transfers into a real project, it belongs in Part 2.

If it becomes useful only after the learner can already operate agents and now needs to design more reliable, autonomous, explainable, selective, portable, or scalable agent systems, it probably belongs in Part 3.

If it asks the learner to synthesize the whole course and reason from the project they have built and inhabited, it belongs in the epilogue.

Do not force every interesting advanced concept into the first eight modules merely because it is important. Let the learner earn the need for richer models.
