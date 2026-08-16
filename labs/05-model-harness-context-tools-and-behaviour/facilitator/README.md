# Lab 5 facilitator guide

Status: **Runnable draft — ready for facilitator trial.**

## Lab learning goal

The learner should stop treating observed agent behaviour as a direct window into `the model`.

They should leave with a practical system model:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

and a working habit:

> **Diagnose the failing layer before intervening.**

The goal is not to make the learner an evaluator or benchmark designer. It is to make their next debugging question better.

Instead of:

> This AI is bad at this.

we want:

> What changed, what evidence do I have, and which layer should I inspect first?

## Why this lab belongs here

Labs 1–4 have already exposed several layers without naming the whole system:

- Lab 1 changed conversation and workspace conditions and showed that access to project material changes what the agent can know and do.
- Lab 2 made project access, representation, scope, and local-versus-connected surfaces visible.
- Lab 3 separated conversational context from durable project state.
- Lab 4 made working state, recorded history, publication, and verification evidence visible.

Lab 5 names the larger diagnostic model before Lab 6 asks the learner to deliberately provision a worker.

Useful transition:

> You've already changed the agent system several times. This lab is about noticing which part you changed.

## Experimental discipline

This lab uses controlled comparisons rather than claims about particular products.

For the core exercises:

- use the same local agent harness for both sides of a comparison;
- keep the same model selected where the harness exposes that choice;
- use fresh sessions where earlier conversation would contaminate the comparison;
- root the agent at the exact experiment folder named below;
- use the same prompt text on both sides unless the exercise explicitly changes it;
- inspect the prepared files only after the learner has observed the relevant behaviour when delaying that reveal helps the lesson.

Do not claim that a single run proves a universal property of a model. The exercise proves that changing one surrounding condition can materially change observed behaviour.

If the harness does not expose or guarantee model identity, say so. The useful claim becomes narrower:

> We held the visible task and harness conditions as constant as this product allows, and changed this prepared layer.

That is enough for the lesson.

## Project fixture

The fixture lives at:

`labs/05-model-harness-context-tools-and-behaviour/project/`

Do **not** root the agent at `project/` for the controlled exercises. Each experiment folder is intended to be its own workspace boundary.

The fixture contains:

```text
project/
    behaviour-baseline/
    behaviour-configured/
    context-missing/
    context-complete/
    verification/
```

The two behaviour folders contain the same source and task but different standing project instructions.

The two context folders contain the same task and the same standing instructions, but only one contains the project evidence required to answer confidently.

The verification folder contains a deliberately flawed volunteer schedule and a prepared validator.

## Exercise 1 — Same job, different behaviour

Goal: demonstrate that observed behaviour can change substantially without changing the underlying job, model, or harness.

### Run A

Root a fresh local agent session at:

`project/behaviour-baseline/`

Use exactly:

> Read `task.md` and do the task.

Let the agent answer in chat. Do not coach its style.

### Run B

Root another fresh session in the same harness, with the same model selection if available, at:

`project/behaviour-configured/`

Use exactly the same prompt:

> Read `task.md` and do the task.

The configured workspace has a strict output contract: exactly four bullets, no heading or preamble, short bullets, and prioritisation of time, access, safety, and the volunteer lead's first action.

Compare the outputs before discussing why they differ.

Ask:

- Did the job change?
- Did the source material change?
- Did we intentionally change model?
- Did we intentionally change harness?
- What observable behaviour changed?

Now inspect the `AGENTS.md` files in both workspaces.

The baseline file supplies only safety/accuracy boundaries. The configured file adds a strong response contract.

Earn:

> **Same model does not mean same behaviour.**

> **Instructions and settings are part of the system.**

Do not conclude that the configured result is inherently `better`. It is better only if the configured behaviour matches the user's goal.

If the baseline happens to produce something similarly concise, compare compliance with the exact four-bullet contract rather than chasing a more dramatic run.

## Exercise 2 — What context does it have?

Goal: distinguish inability to observe required project evidence from inability to reason about the task.

The two workspaces use the same `AGENTS.md` and the same `task.md`.

### Run A — evidence absent

Root a fresh session at:

`project/context-missing/`

Use:

> Read `task.md` and answer it from the project evidence you can actually inspect.

The task asks whether two proposed event-layout choices comply with venue constraints. The workspace intentionally contains no venue-constraint file.

A good response should identify the missing evidence rather than inventing project rules.

If the agent guesses, that is useful diagnostic evidence: the failure is not `the model had no access`; it is that the system did not respond safely to missing context.

### Run B — evidence present

Root a fresh session at:

`project/context-complete/`

Use the exact same prompt.

This workspace contains `venue-constraints.md`, which establishes that a welcome desk is allowed in the foyer if the exit route remains clear, while soldering is not allowed in Studio B.

Now ask:

- Which layer changed between runs?
- Did the reasoning task change?
- Would swapping the model have been the first sensible intervention in Run A?

Earn:

> **Missing evidence is not evidence of a weaker model.**

> **Context and access constrain what conclusions the agent can justify.**

This is a callback to Labs 1–3, but the learner is now explicitly naming the layer rather than merely experiencing it.

## Exercise 3 — Plausible is not verified

Goal: show that tools and feedback change the evidence available to the system even when the reasoning task is unchanged.

Root the agent at:

`project/verification/`

The folder contains:

- `constraints.md` — the human-readable scheduling rules;
- `candidate.csv` — a proposed volunteer schedule;
- `validate_schedule.py` — a prepared deterministic checker;
- `AGENTS.md` — instructions that keep the first assessment manual and provisional, then allow the checker when explicitly requested.

### Part A — provisional judgment

Ask:

> Read `constraints.md` and `candidate.csv`. Give me an initial assessment of whether the schedule works. Do not run the validator yet.

The agent may catch all, some, or none of the seeded problems manually. Do not force a miss.

The known fixture problems are:

- Lee is assigned to Repair despite the restriction;
- Sam is double-booked in the 18:00–20:00 shift;
- Jordan is double-booked in the 20:00–22:00 shift.

The interesting label is **provisional**.

### Part B — add the verification capability and feedback

Ask:

> Now run the prepared validator. Compare its evidence with your initial assessment and tell me what changed in your confidence.

Expected checker result:

```text
FAIL
- Lee is assigned to Repair at 20:00-22:00 but cannot work that station.
- Sam is double-booked at 18:00-20:00: Welcome, Repair.
- Jordan is double-booked at 20:00-22:00: Welcome, Repair.
```

If the manual assessment already found all three, the exercise still succeeds. The transition is from unaided judgment to reproducible evidence.

If the manual assessment missed something, ask which layer the validator changed:

- the model did not change;
- the task did not change;
- the system gained a deterministic checking capability and feedback channel.

Earn:

> **A plausible answer and a verified answer are different states of knowledge.**

> **Tools change what the agent can do; feedback changes what the system can know about the result.**

Do not use this to teach Python. The learner can ask what the checker does in ordinary language if curious.

## Exercise 4 — Diagnose before intervening

Goal: apply the model to mixed failures without insisting every case has exactly one cause.

Use `learner/04-diagnose-before-intervening.md` one scenario at a time.

For each scenario, ask the learner for three things:

1. What layer or layers are plausible suspects?
2. What evidence would you inspect first?
3. What is the smallest justified intervention after that inspection?

Reward `I do not know yet; I would inspect X` when that is the evidence-honest answer.

The scenarios deliberately cover:

- instruction/configuration problems;
- context/access problems;
- tool or permission limitations;
- missing persistent project knowledge;
- missing verification feedback;
- harness differences;
- a case where model capability remains a legitimate suspect after other conditions are held reasonably constant.

The mature rule is not `never blame the model`.

It is:

> **Diagnosis before intervention. Sometimes the diagnosis really is model capability.**

## Optional extension — fairer cross-harness comparison

Only use this if a second agentic harness is already available and setup will not dominate the session.

Run the exact `behaviour-baseline/` task in both harnesses.

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

Close with:

> If we can identify which layer caused the behaviour, can we deliberately change the right layer before the next task begins?

Examples:

- repeated project-rule mistakes → persistent project instructions;
- missing capability → provision a tool;
- missing domain understanding → provide domain references/examples;
- weak process → provide reusable workflow knowledge;
- plausible but unverifiable work → add checks and quality criteria.

Lab 5 supplies the diagnosis.

Module 6 turns diagnosis into deliberate worker design.

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
