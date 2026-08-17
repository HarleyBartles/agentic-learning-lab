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

## Current labs

Labs 1–6 are mature and ready to run.

- `01-chatbot-to-worker/` — compare ordinary cloud conversations, an on-disk worker, and a persistent cloud workspace to expose how environment changes context and artifact transport.
- `02-give-the-cloud-agent-the-project/` — examine how project access depends on state, representation, scope, and allowed operations.
- `03-project-has-a-home/` — three Repair Café exercises covering conversational knowledge that never became project state, deliberate promotion of meeting material into durable state, and conflicting durable artifacts whose authority is not explicitly defined.
- `04-repositories-save-points-and-safe-breakage/` — a theatre-production fixture that reveals working state versus recorded state, diffs and restore, commit versus push, unpublished versus published recovery, historical recovery, and the repository boundary around external side effects.
- `05-model-harness-context-tools-and-behaviour/` — one evolving project where the learner changes standing instructions, available evidence, and verification capability, then diagnoses which system layer produced observed agent behaviour.
- `06-what-does-the-model-know/` — a closed-book/open-book experiment where the learner predicts retained model knowledge, probes its epistemic boundary, restores retrieval, and compares remembered knowledge with evidence-backed judgment before asking why software engineering appears unusually deep.

## Safety

Nothing in these labs should be precious. The learner should be free to make bad changes, delete generated outputs, inspect surprising results, and later learn how to recover more consequential state safely.
