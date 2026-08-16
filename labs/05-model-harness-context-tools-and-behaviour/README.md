# Lab 5 — Model, harness, context, tools, and behaviour

Status: **Runnable draft — ready for facilitator trial.**

Approximate duration: 60–75 minutes.

Lab 4 taught the learner to change project state safely and inspect what changed. Lab 5 turns that habit onto the agent itself:

> **Change one part of the worker's environment, rerun the work, and inspect what changed in the behaviour.**

The learner works in one evolving project rather than being moved between prepared copies. Across the lab they deliberately change three layers of the worker's environment:

1. standing instructions;
2. available project evidence;
3. an available verification tool.

Those changes accumulate in one visible Git diff. The final exercise uses that diff to reconstruct the larger system model:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

The practical invariant is:

> **Diagnose the failing layer before intervening.**

## Shape

```text
labs/05-model-harness-context-tools-and-behaviour/
    README.md
    facilitator/
    learner/
    toolbox/
        venue-constraints.md
        validate_schedule.py
    project/
        AGENTS.md
        event/
        tasks/
        work/
```

Root the local worker at `project/` throughout the lab.

`toolbox/` is course material outside the worker's project boundary. The learner can see it, but the worker should not be scoped to it. Moving useful material across that boundary is part of the exercise rather than facilitator setup hidden between runs.

## Exercises

1. `learner/01-change-the-instructions.md` — run a briefing task, deliberately change the project's standing instructions, inspect the diff, start a fresh session, and rerun the same task.
2. `learner/02-bring-in-the-evidence.md` — encounter a task the worker cannot justify from current project evidence, then deliberately add the missing venue reference to the project and rerun.
3. `learner/03-give-it-a-checker.md` — make a provisional schedule assessment, deliberately add a prepared deterministic checker to the project, then compare unaided judgment with tool-backed feedback.
4. `learner/04-read-the-agent-diff.md` — inspect the accumulated project diff, map each intervention to a system layer, then diagnose mixed failure scenarios before choosing interventions.

The core lab does not require a second AI product. A cross-harness or cross-model comparison is optional only after the learner can state what variables were actually held constant.

Core lines to earn:

> The thing I experience as `the AI` is a system, not just a model.

> Same model does not mean same behaviour.

> Missing evidence is not evidence of a weaker model.

> A plausible answer and a verified answer are different states of knowledge.

> Separate capability from configuration.

> **Diagnosis before intervention.**

Do not turn this into benchmark methodology, model leaderboards, or a catalogue of every possible instruction surface. The learner needs a practical diagnostic model they have physically manipulated themselves before Lab 6 begins deliberate provisioning.
