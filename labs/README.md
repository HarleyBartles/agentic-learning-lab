# Labs

A lab is the complete learning experience for a curriculum topic.

A lab may contain three distinct surfaces:

```text
facilitator/
    rationale, setup, teaching guidance, observations, and things to defer

learner/
    learner-facing exercise cards or reference material, revealed as needed

mission/ or another working folder
    the bounded project environment where the task itself lives
```

These are not separate root-level systems. They belong together because they describe and run the same learning experience.

The working environment should be scoped deliberately. If an agent only needs the mission workspace, point the agent at that workspace rather than the whole teaching lab. This keeps facilitator and learner choreography out of the agent's project context and creates a clean boundary between teaching material and project state.

Some setup may be performed in advance by the facilitator so early labs can teach an abstraction without first teaching all of its machinery. That setup should use normal capabilities of the harness rather than artificial tricks. Later labs can reveal the hidden configuration and explore its alternatives and tradeoffs.

## Course-local numbering

Lab numbers reset at each course boundary.

- Course 1 is Labs 1–10.
- Course 2 begins again at Lab 1.
- Course 3 will begin again at Lab 1.

Do not carry the old global planning numbers `11–18` into mature lab names. Those numbers may still appear on legacy planning drafts because they record how the curriculum was originally sketched; the current course-local indexes define the teaching sequence.

## Current labs

Labs 1–10 are mature and ready to run. Together they form **Course 1 — Agentic Engineering 101: Zero to Hero**.

- `01-chatbot-to-worker/` — compare ordinary cloud conversations, an on-disk worker, and a persistent cloud workspace to expose how environment changes context and artifact transport.
- `02-give-the-cloud-agent-the-project/` — examine how project access depends on state, representation, scope, and allowed operations.
- `03-project-has-a-home/` — three Repair Café exercises covering conversational knowledge that never became project state, deliberate promotion of meeting material into durable state, and conflicting durable artifacts whose authority is not explicitly defined.
- `04-repositories-save-points-and-safe-breakage/` — a theatre-production fixture that reveals working state versus recorded state, diffs and restore, commit versus push, unpublished versus published recovery, historical recovery, and the repository boundary around external side effects.
- `05-model-harness-context-tools-and-behaviour/` — one evolving project where the learner changes standing instructions, available evidence, and verification capability, then diagnoses which system layer produced observed agent behaviour.
- `06-what-does-the-model-know/` — a closed-book/open-book experiment where the learner predicts retained model knowledge, probes its epistemic boundary, restores retrieval, and compares remembered knowledge with evidence-backed judgment before asking why software engineering appears unusually deep.
- `07-tools-operating-knowledge-and-domain-provisioning/` — three before/after experiments that move domain judgment from facilitator-grounded software engineering, through shared non-authoritative provision from external expertise, to a learner-grounded expert domain while keeping final verification with the human.
- `08-local-work-and-connected-systems/` — reconstruct the provisioned worker, inspect scoped harness-supplied instructions, follow and then break an `INDEX.md` navigation mesh, prove that accessible state can remain undiscovered, and widen the observation surface from local project state to connected GitHub state.
- `09-source-of-truth-and-verification/` — reopen the Repair Café contradiction with an explicit authority map, execute one bounded current-state repair, independently verify the worker's completion claim, separate verification from mutation, and generalise how different claims require different evidence.
- `10-build-a-real-agentic-project/` — create a learner-owned real project, shape intent before implementation, inspect and improve one genuine result, verify it against explicit authority, and make publication and reuse-rights decisions deliberately.

Course 2 planning lives under [`../modules/course-2/`](../modules/course-2/) and starts at Course 2 Lab/Module 1.

## Safety

Nothing in these labs should be precious. The learner should be free to make bad changes, delete generated outputs, inspect surprising results, and later learn how to recover more consequential state safely.