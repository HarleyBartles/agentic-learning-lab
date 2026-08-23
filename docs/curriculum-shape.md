# Curriculum shape

The curriculum has a deliberate three-course structure.

The exact shape of an individual lab can still evolve while it is being designed, but the course boundaries are now part of the curriculum contract. Preserve the cognitive progression rather than treating every lab across all three courses as one globally numbered run.

```text
Course 1
Agentic Engineering 101: Zero to Hero
Labs 1–10
        ↓
Course 2
Advanced Agentic Engineering: Mastering Agents
Labs 1–N
        ↓
Course 3
Beyond the Agent: Engineering Agent Systems
Labs 1–N
```

**Lab numbering resets at each course boundary.** Course 2 begins at Lab 1, not Lab 11. Course 3 will also begin at Lab 1. The final number of labs in Courses 2 and 3 remains open while planning modules are expanded into mature labs. Ten labs per course is a useful target where the material naturally earns it, not a quota.

The three courses are related but should each reach a coherent stopping point. In particular, Course 1 is not an intentionally incomplete prelude. A learner who stops after Lab 10 should leave with a sound, self-contained foundation for competent agentic engineering rather than carrying known stale misconceptions that only a later course repairs.

Later courses may deepen, qualify, or pressure-test earlier models, but they should build on models that were already useful and substantially correct at the prior course boundary.

## Course 1 — Agentic Engineering 101: Zero to Hero

Current range: Labs 1–10.

Course 1 takes the learner from ordinary chat use to competent practical agentic engineering, ending with a real project of their own.

The learner should finish Course 1 able to reason about an agentic system without treating it as one mysterious AI blob. They should understand the major surfaces that shape agent behaviour, know how a worker observes and acts on a project, distinguish access from discovery, distinguish evidence from authority, verify completed work rather than trusting completion prose, recover reversible mistakes, and deliberately shape a useful worker environment.

The current progression includes:

1. conversation versus worker behaviour;
2. project access and context transport;
3. durable project state;
4. repositories, recovery, and safe breakage;
5. model, harness, context, tools, instructions, environment, state, and feedback;
6. model knowledge versus supplied/retrieved evidence;
7. domain provisioning under different human-authority arrangements;
8. agent environment, navigation, scoped instructions, access surfaces, discovery, local work, and connectors;
9. source of truth, authority, verification, and evidence;
10. a real learner-owned agentic project that synthesizes the course.

Lab 10 is the Course 1 synthesis project, not a separate macro-part between foundation and advanced material.

The project should make the learner apply the first course in a real setting:

- create and own a project home;
- make visibility, ownership, and licensing decisions deliberately;
- identify authoritative state;
- establish recovery;
- select capabilities deliberately;
- decide what should and should not be connected;
- introduce persistent project instructions when justified;
- capture reusable workflow knowledge when justified;
- define how completed work will be verified;
- direct, inspect, refine, and accept agent work without manually implementing it themselves.

The learner's project can then become one of the working surfaces used by Courses 2 and 3 alongside bounded teaching fixtures.

A useful summary is:

> **Course 1 teaches the learner to direct, understand, verify, and deliberately shape useful agents competently.**

The course boundary matters. Do not deliberately leave a learner at the end of Lab 10 holding a mental model that the curriculum already knows is materially false. Progressive disclosure is welcome; deferred correction of a known misconception across a course break is not.

## Course 2 — Advanced Agentic Engineering: Mastering Agents

Current planning range: Course 2-local Labs 1 onward.

Course 2 starts from a learner who can already operate and verify a useful worker. The emphasis changes from competent collaboration to deliberate engineering of agent behaviour.

This shift should feel expansive rather than corrective. The learner's Course 1 competence is real: they can collaborate with agents to produce useful outcomes. Course 2 opens another layer by showing that deliberately shaping how an agent behaves, checks itself, receives context, delegates work, and moves through a workflow is a discipline in its own right.

The learner should learn to shape how work proceeds, how the worker checks itself, when humans intervene, when specialist workers are justified, how context moves, how harnesses realise intended worker profiles, and how changes to an agentic system are evaluated rather than merely admired.

Current Course 2 threads include:

- agent self-introspection, behavioural prediction, cheap local self-review, and test-first probes;
- autonomous human-in-the-loop workflows;
- loops, graphs, retries, stopping conditions, escalation routes, and escape hatches;
- success conditions and legal workflow transitions;
- specialist sub-agents, delegation, and orchestrator trade-offs;
- specialist profiles as intended worker contracts;
- harness portability and effective runtime worker verification;
- model/reasoning selection, defaults, inheritance, and observability;
- agent-system economics: capability, context, inference, latency, quality, independence, and risk;
- **The 20-Agent Bonfire** as a context/economics/orchestration pressure test for deliberately wasteful over-delegation, worker-default inspection, context transport, and usage comparison;
- selective provisioning rather than accumulation;
- context transport and materialisation;
- lazy versus eager loading and N+1-style repeated context work;
- finite context and retrieval/RAG as context selection;
- lightweight evaluation and TDD-inspired agent design.

Keep the Bonfire boundary explicit: it is an economics/context/orchestration pressure test, not yet the shared-mutable-state concurrency lesson. If many workers would mutate one workspace simultaneously, constrain the exercise so Course 3 can earn isolation and reconciliation from the real problem later.

The current Course 2 planning sequence is indexed at [`modules/course-2/README.md`](../modules/course-2/README.md). Older root-level draft filenames with prefixes such as `11-`, `14-`, or `14a-` are legacy source-history identifiers only; they are not current curriculum numbering.

The conceptual shift is:

```text
Course 1
How do I collaborate with a useful agent competently?

Course 2
How do I deliberately engineer the agent's behaviour,
workflow, context, delegation, verification,
evaluation, and autonomy?
```

A useful summary is:

> **Course 2 teaches the learner to engineer agent behaviour rather than merely collaborate with agents.**

The intended emotional arc matters too. At the end of Course 1 the learner should plausibly feel that a new world has opened and that they can collaborate with agents to tackle real work. Course 2 should preserve that confidence while revealing a second world underneath it: engineering the workers themselves.

## Course 3 — Beyond the Agent: Engineering Agent Systems

Current planning range: Course 3-local Labs 1 onward.

Course 3 widens the design boundary again.

The learner now treats individual agents as components inside a larger operational system. Concepts introduced in Course 2 such as specialist coordination and resource economics remain active, but the pressure moves to the wider system around them: trust, connected authority, concurrent work, isolation, integration, provenance, and reconstruction of how system state came to exist.

Current Course 3 threads include:

- trust boundaries and connected autonomy;
- external content as evidence rather than operating authority;
- permissions, least capability, and consequential human gates;
- provenance across connected stages, workers, and systems;
- specialist coordination under wider system constraints;
- operational economics as a system property rather than only a per-worker choice;
- concurrent agents and shared mutable state;
- isolated workspaces/branches/worktrees where appropriate;
- deliberate reconciliation and integration;
- verification of integrated state rather than trusting individually successful worker returns;
- repository and workflow archaeology;
- compressed versus richer evidence surfaces;
- source provenance without confusing provenance for authority;
- the curriculum repository itself as a final system-level investigation surface.

The current retrospective/epilogue planning theme belongs to Course 3. It is not a separate fourth part.

The epilogue should function as a final worked system problem rather than only a retrospective lecture. The learner should inspect and reason about the repository they have inhabited throughout the curriculum, reconstruct how it developed, identify major changes in direction, distinguish what available evidence proves from what it cannot establish, and direct an agent through that investigation rather than manually performing all of the archaeology.

If the learner has used their own fork throughout the curriculum, the final investigation can compare two related histories:

```text
upstream curriculum history
how the teaching framework itself evolved

learner fork history
how this learner actually worked through and changed their laboratory
```

A useful summary is:

> **Course 3 teaches the learner to engineer the system around agents: trust, coordination, concurrency, integration, provenance, and operational behaviour.**

## The three cognitive grades

The intended progression can be summarized as:

```text
Course 1 — competent agentic engineer
I can direct, understand, provision, navigate, verify,
and safely operate useful agent work.

Course 2 — advanced agentic engineer
I can deliberately design agent behaviour, workflow,
context, delegation, evaluation, and autonomy.

Course 3 — agent-systems engineer
I can design the wider system in which agents coordinate,
act under trust and capability boundaries, work concurrently,
integrate state, preserve provenance, and spend resources proportionately.
```

These are cognitive grades, not job titles. Course 2's title deliberately promises **Mastering Agents**; that promise means mastery of the agent-engineering layer taught by the course, not a claim that the learner has exhausted a fast-moving field.

## Editorial test for future topics

When adding or moving material, ask which course boundary the concept serves.

If the concept is required for a learner to competently direct, understand, navigate, recover, provision, and verify ordinary agentic work, it belongs in Course 1.

If it assumes that competence and teaches deliberate design of worker behaviour, workflow, delegation, context, self-checking, evaluation, or bounded autonomy, it belongs in Course 2.

If it widens the unit of reasoning from one worker/workflow to the surrounding multi-agent or connected system — trust boundaries, coordination, concurrency, integration, provenance, operational economics, or system archaeology — it belongs in Course 3.

Do not force advanced material earlier merely because it is important. Equally, do not knowingly leave Course 1 with a materially false model simply because a later course could repair it. Each course boundary should be a credible place for the learner to stop.
