# Lab 5 — Model, harness, context, tools, and behaviour

Status: **Runnable draft — ready for facilitator trial.**

Approximate duration: 60–75 minutes.

Lab 4 taught the learner to inspect and recover project state. Lab 5 changes the question from `what state did the agent change?` to:

> **What part of the agent system produced the behaviour I just saw?**

The working model is:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

The lab is built as a sequence of controlled comparisons. The learner should change one important condition at a time, inspect what changed, and resist reflexively attributing every good or bad result to the model.

The practical invariant is:

> **Diagnose the failing layer before intervening.**

## Exercises

1. `learner/01-same-job-different-behaviour.md` — run the same task with the same model and harness in two prepared workspaces whose standing instructions differ, then inspect the instruction layer that changed the output contract.
2. `learner/02-what-context-does-it-have.md` — run the same decision task in two otherwise-matched workspaces, one without the required project evidence and one with it, and distinguish missing context from weak reasoning.
3. `learner/03-plausible-is-not-verified.md` — make a provisional manual assessment of a volunteer schedule, then let the agent invoke a prepared validator and compare plausible judgment with tool-backed feedback.
4. `learner/04-diagnose-before-intervening.md` — classify mixed failure scenarios by likely layer, name the first evidence to inspect, and only then choose an intervention.

For Exercises 1–3, root the local agent at the exact experiment folder named by the facilitator rather than at the whole lab or `project/`. The workspace boundary is part of the experiment.

Use fresh sessions for controlled comparisons where practical. Keep the model and harness fixed unless the exercise explicitly says otherwise.

The core lab does not require a second AI product. A cross-harness or cross-model comparison is an optional extension only after the learner can state which variables were actually held constant.

Core lines to earn:

> The thing I experience as `the AI` is a system, not just a model.

> Same model does not mean same behaviour.

> Missing evidence is not evidence of a weaker model.

> A plausible answer and a verified answer are different states of knowledge.

> Separate capability from configuration.

> **Diagnosis before intervention.**

Do not turn this into benchmark methodology, model leaderboard discussion, or a catalogue of every possible instruction surface. The learner only needs a practical diagnostic model they can use before Lab 6 begins deliberate provisioning.
