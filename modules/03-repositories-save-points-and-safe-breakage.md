# Module 3 — Repositories, save points, and safe breakage

Approximate duration: 1 hour.

## Core idea

Source control is not mainly a programmer ritual. It is controlled history and a recovery mechanism.

The behavioural goal is to replace:

> I should not try this because I might break something.

with:

> What is the blast radius, and do I have a recovery path?

## Suggested session shape

### 0–10 minutes — Name the fear

Ask what the learner is actually worried will happen when an agent edits files. Separate vague computer anxiety from concrete failure modes.

Explain that this lab contains nothing precious. It is designed to be broken.

### 10–25 minutes — Introduce only four Git ideas

Teach:

- what the project looked like before;
- what changed;
- what changed it;
- how to get the old version back.

Treat commits as named save points where the project is in a state you understand.

Use `git status`, `git diff`, and the IDE's source-control view. Prefer visual inspection over command memorisation.

### 25–45 minutes — Break things on purpose

Use exercises from `labs/` or create them conversationally.

Progression:

1. Make a bad edit to one tracked file and restore it.
2. Ask the agent for an intentionally broad change across several files; inspect the diff and undo it.
3. Delete a tracked file and recover it.
4. Commit a bad change and then recover from the committed state.

If the learner is comfortable, later push a harmless bad commit to the shared remote and recover that too.

The point is to demonstrate that `committed` and `on GitHub` do not mean `irreversible`.

### 45–55 minutes — Practise the recovery loop

When an agent does something surprising:

1. Stop.
2. Inspect state.
3. Understand the diff.
4. Decide what to keep.
5. Restore or revert what is wrong.

Have the learner direct the agent to explain its own changes, but verify against Git rather than trusting the explanation.

### 55–60 minutes — Introduce external side effects

Contrast reversible local state with actions Git cannot undo: sending mail, publishing content, deleting remote records, spending money, changing permissions, or modifying production services.

> Be fearless with reversible state. Be deliberate with irreversible or external side effects.

## Tools to experiment with

- Git status and diff;
- IDE source-control/diff UI;
- local agent editing several files;
- restore/revert operations;
- GitHub remote only if the learner is ready.

## Discussion prompts

- What exactly can we lose here?
- Which copy would we recover from?
- What does Git protect and what does it not protect?
- When should we checkpoint before an experiment?
- Which agent actions deserve approval because they escape the repo boundary?

## Do not teach yet

Avoid rebasing, merge strategies, detached HEADs, complex branching models, or Git internals. Branches can arrive when isolated work solves a problem the learner actually understands.
