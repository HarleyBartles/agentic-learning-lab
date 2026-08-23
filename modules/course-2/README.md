# Course 2 planning — Advanced Agentic Engineering: Mastering Agents

Status: **planning index**.

Course 2 has its own numbering. It begins at **Lab 1**, not Lab 11.

The current planning sequence is:

1. **Agent self-introspection and local review**
2. **Autonomous human-in-the-loop workflows**
3. **Specialist sub-agents and orchestration**
4. **Harnesses, portability, and agent observability**
5. **The 20-Agent Bonfire and context transport**
6. **Selective provisioning, context, and evaluation**
7. **Trust boundaries and connected autonomy**
8. **Concurrent agents and isolation**
9. **Epilogue: show how this was built**

These are planning modules, not a promise that the mature course will contain exactly nine labs. As the drafts are expanded into runnable labs, a topic may remain one lab or split where the learner needs another experiential step. Ten labs is a useful target if the material naturally earns it, not a quota.

The old root-level draft filenames such as `11-agent-self-introspection-and-local-review.md`, `14a-20-agent-bonfire-and-context-transport.md`, and `18-epilogue-show-how-this-was-built.md` pre-date the course-local numbering decision. Treat their numeric prefixes as **legacy source-history identifiers**, not current curriculum numbers.

The old `14A` exception is deliberately retired in the new taxonomy. **The 20-Agent Bonfire is simply Course 2 Module 5.** There is no lettered module in the current sequence.

The course-local planning files in this directory are the authoritative numbering surface for Course 2.

## Course boundary

Course 1 ends with the learner able to collaborate competently with agents on real work.

Course 2 starts by revealing another layer:

> **Being good at collaborating with agents is not the same thing as deliberately engineering how agents behave.**

The learner should not feel that Course 1 competence was fake or naive. It was real. Course 2 expands the design boundary from directing work to shaping the worker, its workflow, its boundaries, and the systems in which multiple workers operate.

The course promise is **agent mastery**: the learner should become able to reason about and deliberately shape self-review, workflow, delegation, context, runtime realization, evaluation, bounded autonomy, trust boundaries, concurrency, isolation, integration, and the evidence left behind by the system.

## Current sequence

### 1 — Agent self-introspection and local review

Source draft: [`../11-agent-self-introspection-and-local-review.md`](../11-agent-self-introspection-and-local-review.md)

Make cheap local behavioural prediction, self-review, test-first probes, and evidence ladders explicit before adding workflow machinery.

### 2 — Autonomous human-in-the-loop workflows

Source draft: [`../12-autonomous-human-in-the-loop-workflows.md`](../12-autonomous-human-in-the-loop-workflows.md)

Turn repeatedly requested agent behaviours into deliberate transitions, loops, gates, stop conditions, escalation routes, and human approval points.

### 3 — Specialist sub-agents and orchestration

Source draft: [`../13-specialist-subagents-and-orchestration.md`](../13-specialist-subagents-and-orchestration.md)

Pressure-test the one-worker-does-everything model and introduce specialization only when separation buys something material.

### 4 — Harnesses, portability, and agent observability

Source draft: [`../14-harnesses-portability-and-agent-observability.md`](../14-harnesses-portability-and-agent-observability.md)

Distinguish intended worker profiles from effective runtime workers, then inspect portability, model/reasoning controls, observability, and economics.

### 5 — The 20-Agent Bonfire and context transport

Source draft: [`../14a-20-agent-bonfire-and-context-transport.md`](../14a-20-agent-bonfire-and-context-transport.md)

Use deliberately wasteful over-delegation to make context transport, worker defaults, coordination overhead, and economics painfully visible. In the new taxonomy this is a normal module, not `4A`, `5A`, or any other lettered exception.

### 6 — Selective provisioning, context, and evaluation

Source draft: [`../15-selective-provisioning-context-and-evaluation.md`](../15-selective-provisioning-context-and-evaluation.md)

Break the accumulation model: give the worker the right knowledge, at the right scope, when it needs it, then evaluate whether the engineered behaviour actually improved.

### 7 — Trust boundaries and connected autonomy

Source draft: [`../16-trust-boundaries-and-connected-autonomy.md`](../16-trust-boundaries-and-connected-autonomy.md)

Extend agent engineering into consequential connected work: distinguish evidence from authority, access from permission, and useful autonomy from uncontrolled reach.

### 8 — Concurrent agents and isolation

Source draft: [`../17-concurrent-agents-and-isolation.md`](../17-concurrent-agents-and-isolation.md)

Let multiple capable workers create the shared-state problem, then earn isolation, reconciliation, integration, and verification of the integrated result.

### 9 — Epilogue: show how this was built

Source draft: [`../18-epilogue-show-how-this-was-built.md`](../18-epilogue-show-how-this-was-built.md)

Use the Agentic Learning Lab repository itself as the Course 2 capstone investigation. The learner should reconstruct and critique how the agent system, curriculum, repository history, and evidence surfaces were engineered rather than merely consume them.

## Expansion rule

When a planning module becomes too cognitively dense to support one clear experiential lab, split it.

Do not preserve old numbering pressure. Course 2 currently has nine planning modules and may naturally become ten mature labs as the material is expanded. The important invariants are:

- Course 2 starts at Lab 1;
- numbering is local and linear inside Course 2;
- there is no `14A`-style lettered exception in the new taxonomy;
- the old 11–18 drafts, including old 14A, all feed the Course 2 mastery arc;
- the causal order between concepts is preserved;
- the learner ends with a coherent sense of **agent mastery** rather than a bag of disconnected advanced tricks;
- the repository retrospective remains the Course 2 capstone unless later planning deliberately replaces it with something stronger.

Course 3 will reset to Lab 1 again and should be planned as a genuinely new course rather than inheriting material merely because it used to sit after global Module 15.
