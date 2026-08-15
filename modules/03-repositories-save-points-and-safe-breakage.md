# Module 3 — Repositories, save points, and safe breakage

Approximate duration: 1 hour.

## Core idea

Source control is not mainly a programmer ritual. It is controlled history and a recovery mechanism.

The behavioural goal is to replace:

> I should not try this because I might break something.

with:

> What is the blast radius, and do I have a recovery path?

## Teach only the useful Git concepts first

- what the project looked like before;
- what changed;
- what changed it;
- how to get the old version back.

Treat commits as named save points where the project is in a state you understand.

## Deliberate breakage exercise

Ask the agent to make an intentionally broad or foolish change across several files.

Then inspect:

```text
git status
git diff
```

Discuss what actually changed. Then restore the files.

Repeat with a bad committed change, then recover from that too.

If useful later, push a deliberately bad commit to the shared remote and recover again. The point is to demonstrate that `committed` and `on GitHub` do not mean `irreversible`.

## Recovery loop

When an agent does something surprising:

1. Stop.
2. Inspect state.
3. Understand the diff.
4. Decide what to keep.
5. Revert or restore what is wrong.

The workflow should feel like iterative control, not `command -> pray`.

## Reversible versus external actions

Early exercises should mostly involve reversible project state: edits, creates, deletes of tracked files, renames, document rewrites, reorganisations, and commits.

Contrast those with actions Git cannot undo: sending mail, publishing, deleting remote records, spending money, changing access control, or modifying production services.

> Be fearless with reversible state. Be deliberate with irreversible or external side effects.

## Do not teach yet

Avoid branches, rebasing, merge strategies, and elaborate Git vocabulary until the learner understands why isolated changes or parallel work would be useful.
