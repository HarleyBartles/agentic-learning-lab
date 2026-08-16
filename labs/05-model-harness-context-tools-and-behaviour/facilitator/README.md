# Lab 5 facilitator guide

Status: **Mature and ready to run.**

## Lab learning goal

The learner should stop treating observed agent behaviour as a direct window into `the model`.

They should leave with a practical system model:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

and a working habit:

> **Diagnose the failing layer before intervening.**

The lab should earn that model through manipulation rather than explanation. The learner changes one project-level condition at a time and sees the worker behave differently.

## Why the setup is part of the lesson

Do not teleport the learner between prepared versions of the same project.

Labs 1–4 have already taught the learner to care about workspace boundaries, durable project state, Git status/diffs, and reversible change. Reuse those habits here.

Keep one local worker rooted at:

`labs/05-model-harness-context-tools-and-behaviour/project/`

The course also contains:

`labs/05-model-harness-context-tools-and-behaviour/toolbox/`

The human can inspect the toolbox in the editor/file browser. The worker must remain rooted at `project/` and its `AGENTS.md` explicitly tells it not to inspect parent or sibling material, including through shell, filesystem search, or Git back doors.

The central loop is:

```text
observe behaviour
        ↓
identify one layer to change
        ↓
change the project/environment
        ↓
inspect working-tree state
        ↓
rerun
        ↓
explain the behavioural difference
```

This makes setup part of the exercise. The learner is changing the conditions themselves rather than receiving a new mysterious worker.

## Callback to Lab 4: working-tree evidence and recovery

Useful transition:

> Last time, status and diffs told you what changed in the project. This time, we're going to use the same evidence to tell us what we changed about the worker's environment.

Keep the three Lab 5 interventions uncommitted through Exercise 4.

Use the Git tools the learner already knows, without introducing staging as new ceremony:

- `git status --short` shows the complete working-tree change set, including untracked files;
- `git diff -- AGENTS.md` shows the tracked standing-instruction edit;
- newly copied untracked files should be opened directly when their contents matter.

Do **not** describe the three interventions as one ordinary `git diff`: untracked files do not appear there.

Recovery should also reuse Lab 4 rather than become a new lesson:

- if the learner mistypes the `AGENTS.md` rule, edit only that rule or restore that tracked file if they intentionally want to restart Exercise 1;
- if a course file is copied to the wrong place, remove or move only that mistaken untracked file;
- do not use broad `git clean`, `reset --hard`, branch creation, or repository-wide recovery for these small mistakes;
- before continuing after a recovery, use `git status --short` to confirm the intended earlier Lab 5 changes remain.

The principle is familiar now: identify the bad change and undo only its blast radius.

## Initial project state

The worker's project begins as a coherent Riverside Makers Evening project:

```text
project/
    AGENTS.md
    README.md
    event/
        event-brief.md
    tasks/
        volunteer-lead-brief.md
        venue-layout.md
    work/
        schedule-constraints.md
        volunteer-schedule.csv
```

There is intentionally no `reference/venue-constraints.md` and no `tools/validate_schedule.py`.

The course-level toolbox contains both. Their absence from `project/` is part of the starting condition.

`project/README.md` describes only the Riverside project. It must not explain Lab 5, name the toolbox, or reveal later exercise choreography.

`project/AGENTS.md` is different: like Labs 1–4, it is facilitator-provisioned operating doctrine that protects the experimental boundary. It is deliberately visible and becomes part of the lesson in Exercise 1.

Before the session, confirm:

1. the worker is rooted at `project/`, not the Lab 5 directory;
2. `git status --short` is clean for the Lab 5 project;
3. `reference/venue-constraints.md` does not exist;
4. `tools/validate_schedule.py` does not exist;
5. the worker follows `project/AGENTS.md` and does not inspect parent/sibling teaching material;
6. the prepared validator remains unchanged in `toolbox/`.

## Exercise 1 — Reveal and change the instructions

Goal: demonstrate that observed behaviour can change substantially without changing the job, model, or harness, while explicitly cashing the `AGENTS.md` breadcrumb from Labs 1–4.

Start a fresh worker session rooted at `project/`.

Ask exactly:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Let the worker answer normally. Do not coach the output style yet.

Now ask what the learner would change if the facts are fine but they want this kind of briefing much tighter every time.

A useful target is:

- exactly four bullets;
- no heading, preamble, or closing sentence;
- each bullet 24 words or fewer;
- prioritise time, access, safety, and the volunteer lead's first action.

At this point, ask the learner to open `project/AGENTS.md` in the editor.

Spend a few minutes reading it together. The reveal should be simple:

> This file contains standing instructions supplied to agents working in this project. You have been benefiting from the same mechanism since Lab 1. Until now it was mostly experimental plumbing; now you can see and change the lever deliberately.

Do not teach a complete precedence model. Notice only what is useful now:

- these are durable project instructions rather than one-chat prompting;
- they apply to a fresh agent working in this project;
- some lines are ordinary project-working rules;
- some lines deliberately constrain the worker so a helpful agent cannot spoil the controlled exercise.

Have the **learner edit the file by hand**. Do not ask the current agent to rewrite its own operating instructions.

Append this at the bottom:

```md
## Volunteer-lead briefings

- Write volunteer-lead operational briefings as exactly four bullets.
- Do not add a heading, preamble, or closing sentence.
- Keep each bullet to 24 words or fewer.
- Prioritise time, access, safety, and the volunteer lead's first action.
```

The exact wording can vary if the learner proposes an equivalent rule. Keep the change narrowly scoped to volunteer-lead briefings so it does not contaminate later tasks.

Inspect:

`git diff -- AGENTS.md`

Ask:

- What changed on disk?
- What stayed the same?
- Did we swap model?
- Did we swap harness?
- Did we change the task or source facts?
- Why do we need a fresh agent context now?

Close the baseline conversation and start a fresh worker context rooted at the **same** project. This is the important injection boundary: the new worker starts with the changed standing project instructions rather than receiving the style rule as conversational carry-over.

Ask exactly the original task again:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Compare the outputs.

Earn:

> **Same model does not mean same behaviour.**

> **Instructions and configuration are part of the system.**

And cash the breadcrumb explicitly:

> **You have been benefiting from this mechanism since the beginning. Now you have touched the lever yourself.**

Do not turn this into self-modifying-agent design. Having an agent maintain its own project instructions is a useful later capability, but it is not needed to prove this lesson.

## Exercise 2 — Bring in the evidence

Goal: distinguish inability to observe required project evidence from inability to reason about the task.

Use the same evolving `project/`.

Ask:

> Read `tasks/venue-layout.md` and answer it from project evidence you can actually inspect.

The task asks whether a foyer welcome desk and a soldering demonstration in Studio B are allowed.

The project does not yet contain the venue rules needed to decide.

A good worker should say the evidence is missing rather than invent project-specific rules. If it guesses, use that as evidence about safe handling of missing context rather than pretending the context was present.

Now reveal to the human that the course repository contains:

`../toolbox/venue-constraints.md`

Do not widen the worker's root or ask the worker to fetch the file. The boundary is part of the observation.

Have the learner copy that file with the editor/file browser into:

`project/reference/venue-constraints.md`

No coding is required.

Run:

`git status --short`

The new file should appear as untracked. Open it directly to confirm what entered the worker's project. Do not expect normal `git diff` to display an untracked file.

Ask:

- Did the venue facts exist on the machine before?
- Did they exist inside the worker's assigned project before?
- What changed: intelligence, or available evidence?
- Why is putting the evidence in durable project state different from telling one conversation the answer?

Start a fresh worker context in the same project and repeat exactly:

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

Ask:

> We have a plausible judgment. What could we give this worker that would let it check the schedule reproducibly?

Reveal to the human:

`../toolbox/validate_schedule.py`

The learner does not need to read or understand Python. Explain only that it is a deterministic checker supplied by the course and that it encodes the prepared schedule checks.

Have the learner copy it into:

`project/tools/validate_schedule.py`

Run:

`git status --short`

The checker should appear as another untracked project file. Open it only if useful; do not turn the exercise into Python inspection.

Ask:

- Did the model change?
- Did the schedule change?
- What new project-specific capability is now available?
- What capability did the harness already provide that makes this tool executable?

This distinction matters: the harness already had shell/process execution. The learner has now provisioned a project-specific checking tool into that environment.

In the same worker conversation that made the provisional assessment, ask:

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

## Exercise 4 — Read the agent change set

Goal: reconstruct the system model from interventions the learner actually made, then apply it diagnostically.

Before any scenario cards, inspect the accumulated Lab 5 working-tree state.

Run:

`git status --short`

The meaningful state should be roughly:

```text
 M AGENTS.md
?? reference/venue-constraints.md
?? tools/validate_schedule.py
```

Then inspect `git diff -- AGENTS.md` and open the two new files as needed.

Ask:

> What did we change about the worker during this lab?

Build the answer from observed project state rather than presenting the formula first.

Map the interventions:

```text
model
    intentionally unchanged

harness
    intentionally unchanged

instructions
    human changed AGENTS.md

context / project knowledge
    human added venue evidence

tools
    human added a project-specific checker

feedback
    worker ran the checker and received deterministic evidence

observed behaviour
    changed after each intervention
```

Now reveal the compact model:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

Then use `learner/04-read-the-agent-change-set.md` scenarios one at a time.

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

## Bridge into Module 6

Close by looking at the accumulated working-tree state again.

The learner has already, experimentally:

- changed a persistent project instruction;
- provisioned relevant knowledge;
- provisioned a capability;
- used a verification mechanism.

Ask:

> We changed these things one at a time so we could diagnose behaviour. What happens if, before a real job starts, we deliberately design the worker's environment this way?

Lab 5 supplies the diagnosis.

Module 6 turns those same levers into deliberate worker design.

## Reset after the session

Return the project to its clean starting state before another learner runs the lab.

Use narrow recovery only:

1. restore `project/AGENTS.md` to its recorded baseline;
2. remove the learner-added `project/reference/venue-constraints.md`;
3. remove the learner-added `project/tools/validate_schedule.py`;
4. run `git status --short` from the project and confirm no Lab 5 exercise changes remain.

Do not delete the course copies in `toolbox/`.

If unrelated pre-existing working-tree changes exist, preserve them and clean only the Lab 5 exercise state.

## Do not teach yet

Do not turn this lab into:

- benchmark methodology;
- model leaderboards;
- token-window arithmetic;
- prompt-engineering folklore;
- a complete instruction-precedence lecture;
- self-modifying-agent design;
- skill design;
- MCP catalogue browsing;
- RAG implementation;
- fine-tuning or weight training;
- broad model-selection rules.

The learner needs one durable habit:

> **When the agent disappoints you, identify which layer failed before changing anything.**
