# Lab 5 — Model, harness, context, tools, and behaviour

Status: **Mature and ready to run.**

Approximate duration: 60–75 minutes.

Lab 4 taught the learner to change project state safely and inspect what changed. Lab 5 turns that habit onto the agent itself:

> **Change one part of the worker's environment, rerun the work, and inspect what changed in the behaviour.**

The learner works in one evolving project rather than being moved between prepared copies. Across the lab they deliberately change three layers of the worker's environment:

1. standing instructions;
2. available project evidence;
3. an available verification tool.

The resulting working-tree change set remains visible throughout the lab. The final exercise uses that evidence to reconstruct the larger system model:

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
        README.md
        event/
        tasks/
        work/
```

Root the local worker at `project/` throughout the lab.

`project/` is a coherent Riverside Makers Evening project from the worker's point of view. It does not explain the surrounding lesson or advertise later inputs.

`toolbox/` is course material outside the worker's project boundary. The learner can see it, but the worker is instructed to treat the project folder as its complete working environment. Moving useful material across that boundary is part of the exercise rather than hidden facilitator setup.

## Exercises

1. `learner/01-change-the-instructions.md` — run a briefing task, open the standing project instructions with the facilitator, hand-edit one bounded briefing rule, inspect the tracked diff, start a fresh agent context, and rerun the same task.
2. `learner/02-bring-in-the-evidence.md` — encounter a task the worker cannot justify from current project evidence, deliberately add the missing venue reference to the project, and rerun.
3. `learner/03-give-it-a-checker.md` — make a provisional schedule assessment, deliberately add a prepared deterministic checker to the project, then compare unaided judgment with tool-backed feedback.
4. `learner/04-read-the-agent-change-set.md` — inspect the accumulated working-tree change set, map each intervention to a system layer, then diagnose mixed failure scenarios before choosing interventions.

The core lab does not require a second AI product. A cross-harness or cross-model comparison is optional only after the learner can state what variables were actually held constant.

Core lines to earn:

> The thing I experience as `the AI` is a system, not just a model.

> Same model does not mean same behaviour.

> Missing evidence is not evidence of a weaker model.

> A plausible answer and a verified answer are different states of knowledge.

> Separate capability from configuration.

> **Diagnosis before intervention.**

Do not turn this into benchmark methodology, model leaderboards, or a catalogue of every possible instruction surface. The learner needs a practical diagnostic model they have physically manipulated themselves before Module 6 begins deliberate provisioning.
