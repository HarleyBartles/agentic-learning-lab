# Lab 5 facilitator guide

Status: **Runnable draft — ready for facilitator trial.**

## Lab learning goal

The learner should stop treating observed agent behaviour as a direct window into `the model`.

They should leave with a practical system model:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

and a working habit:

> **Diagnose the failing layer before intervening.**

The lab should earn that model through manipulation rather than explanation. The learner changes one project-level condition at a time and sees the worker behave differently.

## Why the setup is part of the lesson

Do not teleport the learner between prepared versions of the same project.

Labs 1–4 have already taught them to care about workspace boundaries, durable project state, and diffs. Reuse those habits here.

The learner keeps one worker rooted at:

`labs/05-model-harness-context-tools-and-behaviour/project/`

The course also contains:

`labs/05-model-harness-context-tools-and-behaviour/toolbox/`

The learner can inspect that course material in their editor/file browser, but the worker should not be rooted high enough to see it directly.

The central loop is:

```text
observe behaviour
        ↓
identify one layer to change
        ↓
change the project/environment
        ↓
inspect the diff
        ↓
rerun
        ↓
explain the behavioural difference
```

This gives the setup work pedagogical value. The learner is not receiving a new mysterious worker; they are building the changed conditions themselves.

## Callback to Lab 4

Useful transition:

> Last time, the diff told you what changed in the project. This time, we're going to use the diff to tell us what we changed about the worker's environment.

Keep Lab 5 changes uncommitted during the session so the accumulated diff remains visible for Exercise 4.

## Initial project state

The project begins with:

```text
project/
    AGENTS.md
    event/
        event-brief.md
    tasks/
        volunteer-lead-brief.md
        venue-layout.md
    work/
        schedule-constraints.md
        volunteer-schedule.csv
```

`AGENTS.md` contains only stable safety/accuracy boundaries and the review-stop convention. It does not initially contain a special response-style rule.

There is intentionally no `reference/venue-constraints.md` and no `tools/validate_schedule.py`.

The course-level toolbox contains both. Their absence from `project/` is part of the starting condition.

## Exercise 1 — Change the instructions

Goal: demonstrate that observed behaviour can change substantially without changing the underlying job, model, or harness.

Start a fresh worker session rooted at `project/`.

Ask exactly:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Let the worker answer normally.

Do not coach the output style yet.

Now ask the learner what they would change if the facts are fine but they want a much tighter operational briefing.

A useful target is:

- exactly four bullets;
- no heading, preamble, or closing sentence;
- each bullet 24 words or fewer;
- prioritise time, access, safety, and the volunteer lead's first action.

The important move is not to put those requirements in the next one-off prompt.

Ask the learner to tell the worker to make that a standing project rule for this kind of briefing by editing `AGENTS.md`.

Suggested instruction:

> Make future volunteer-lead operational briefings exactly four short bullets with no heading or preamble. Prioritise time, access, safety, and the lead's first action. Put that in the project's standing instructions, not just this conversation. Leave the change uncommitted.

Inspect the Git diff before rerunning anything.

Ask:

- What changed on disk?
- What did not change?
- Did we swap model?
- Did we swap harness?
- Did the task file change?

Start a fresh worker session rooted at the **same** `project/`. A fresh session is useful because it proves the standing instruction is durable project state rather than conversational carry-over.

Ask exactly the original task again:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Compare the outputs.

Earn:

> **Same model does not mean same behaviour.**

> **Instructions and configuration are part of the system.**

This also cashes the curriculum breadcrumb that early `AGENTS.md` files were facilitator-owned experimental apparatus. The learner has now touched the lever themselves.

Do not turn this into a full instruction-precedence lesson. That comes later.

## Exercise 2 — Bring in the evidence

Goal: distinguish inability to observe required project evidence from inability to reason about the task.

Use the same evolving `project/`.

Ask:

> Read `tasks/venue-layout.md` and answer it from project evidence you can actually inspect.

The task asks whether a foyer welcome desk and a soldering demonstration in Studio B are allowed.

The project does not yet contain the venue rules needed to decide.

A good worker should say the evidence is missing rather than invent project-specific rules. If it guesses, use that as evidence about safe handling of missing context rather than pretending the context was present.

Now reveal that the course repository contains:

`../toolbox/venue-constraints.md`

Do not widen the worker's root to expose the toolbox. The boundary is the lesson.

Have the learner copy that file into the worker's project as:

`project/reference/venue-constraints.md`

Dragging/copying it in the editor is fine. The learner is deliberately promoting useful evidence into the worker's world.

Inspect the diff.

Ask:

- Did the venue facts exist before?
- Did they exist inside the worker's project before?
- What changed: intelligence, or available evidence?
- Why is copying the reference into durable project state different from merely telling this one conversation the answer?

Start a fresh session rooted at the same project and repeat the exact task:

> Read `tasks/venue-layout.md` and answer it from project evidence you can actually inspect.

The new project evidence establishes:

- a welcome desk is allowed in the foyer if the 1.5 metre accessible exit route remains clear;
- soldering is not allowed in Studio B.

Earn:

> **Missing evidence is not evidence of a weaker model.**

> **Context and access constrain what conclusions the agent can justify.**

This should feel like a synthesis of Labs 1–3: access, context, and durable state are now named as layers in the agent system.

## Exercise 3 — Give it a checker

Goal: show that tools and feedback change the evidence available to the system even when the reasoning task is unchanged.

The project already contains:

- `work/schedule-constraints.md`;
- `work/volunteer-schedule.csv`.

Ask:

> Read the schedule constraints and volunteer schedule. Give me an initial assessment of whether the schedule works. Do not use or create a checker. Label the conclusion provisional.

The worker may catch all, some, or none of the seeded problems manually. Do not force a miss.

The known fixture problems are:

- Lee is assigned to Repair despite the restriction;
- Sam is double-booked in the 18:00–20:00 shift;
- Jordan is double-booked in the 20:00–22:00 shift.

Now ask:

> We have a plausible judgment. What could we give this worker that would let it check the schedule reproducibly?

Reveal the prepared course material:

`../toolbox/validate_schedule.py`

The learner does not need to read or understand Python. Explain only that it is a deterministic checker supplied by the course and that it encodes the prepared schedule checks.

Have the learner copy it into:

`project/tools/validate_schedule.py`

Inspect the diff before running it.

Ask:

- Did the model change?
- Did the schedule change?
- What new thing can the worker do now that it could not do from project state alone?
- What capability did the harness already provide that makes this tool executable?

This distinction matters: the harness already had shell/process execution. The learner has now provisioned a project-specific checking tool into that environment.

Ask the worker:

> Run the prepared schedule validator and compare its evidence with your provisional assessment. Tell me what changed in your confidence.

Expected checker result:

```text
FAIL
- Lee is assigned to Repair at 20:00-22:00 but cannot work that station.
- Sam is double-booked at 18:00-20:00: Welcome, Repair.
- Jordan is double-booked at 20:00-22:00: Welcome, Repair.
```

If the manual assessment already found all three, the exercise still succeeds. The transition is from unaided judgment to reproducible evidence.

Earn:

> **A plausible answer and a verified answer are different states of knowledge.**

> **Tools change what the agent can do; feedback changes what the system can know about the result.**

Do not teach Python.

## Exercise 4 — Read the agent diff

Goal: reconstruct the system model from interventions the learner actually made, then apply it diagnostically.

Before any scenario cards, inspect the accumulated Git diff for Lab 5.

The meaningful changes should be roughly:

```text
AGENTS.md
    changed standing instructions

reference/venue-constraints.md
    added project evidence

tools/validate_schedule.py
    added checking capability
```

Ask:

> What did we change about the worker during this lab?

Build the answer from the diff rather than presenting the formula first.

Map the interventions:

```text
model
    intentionally unchanged

harness
    intentionally unchanged

instructions
    changed AGENTS.md

context / project knowledge
    added venue evidence

tools
    added a project-specific checker

feedback
    ran the checker and received deterministic evidence

observed behaviour
    changed after each intervention
```

Now reveal the compact model:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

Then use `learner/04-read-the-agent-diff.md` scenarios one at a time.

For each scenario ask for three things:

1. What layer or layers are plausible suspects?
2. What evidence would you inspect first?
3. What is the smallest justified intervention after that inspection?

Reward `I do not know yet; I would inspect X` when that is the evidence-honest answer.

The mature rule is not `never blame the model`.

It is:

> **Diagnosis before intervention. Sometimes the diagnosis really is model capability.**

## Optional extension — fairer cross-harness comparison

Only use this if a second agentic harness is already available and setup will not dominate the session.

Run the original volunteer-lead task in both harnesses using the same current project state.

Before comparing quality, have the learner list what was and was not held constant:

- model family/version if known;
- project files;
- prompt;
- standing instructions;
- tools and permissions;
- memory or prior conversation;
- opportunity to inspect files;
- opportunity to verify work;
- default response behaviour.

The point is not to pick a winner. The point is to notice that `product A felt better` may describe a real preference without proving that the underlying model is the sole cause.

## Bridge into Lab/Module 6

Close by looking at the accumulated diff again.

The learner has already, experimentally:

- persisted an instruction;
- provisioned relevant knowledge;
- provisioned a capability;
- used a verification mechanism.

Ask:

> We changed these things one at a time so we could diagnose behaviour. What happens if, before a real job starts, we deliberately design the worker's environment this way?

Lab 5 supplies the diagnosis.

Module 6 turns those same levers into deliberate worker design.

## Do not teach yet

Do not turn this lab into:

- benchmark methodology;
- model leaderboards;
- token-window arithmetic;
- prompt-engineering folklore;
- a complete instruction-precedence lecture;
- skill design;
- MCP catalogue browsing;
- RAG implementation;
- fine-tuning or weight training;
- broad model-selection rules.

The learner needs one durable habit:

> **When the agent disappoints you, identify which layer failed before changing anything.**
