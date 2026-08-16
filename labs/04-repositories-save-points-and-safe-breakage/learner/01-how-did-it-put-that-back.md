# Lab 4 — Exercise 1: How did it put that back?

You are working in a small theatre-production project.

The project starts clean: the tracked files match the last recorded project state.

## Delete a tracked file

Ask the local agent:

> Delete `production/crew-briefing.md`, but do not commit or push anything.

Before restoring it, inspect the source-control view or ask the agent to show you the current Git status.

You should be able to see two things at once:

```text
recorded project state
crew-briefing.md exists

current working state
crew-briefing.md is deleted
```

Ask the agent:

> What does Git know about this deletion, and where could the old file contents come from?

Then ask:

> Restore `production/crew-briefing.md` to the recorded version. Do not commit or push anything.

Verify that the working tree is clean again.

## Now change content instead of deleting a file

Ask:

> Change the crew call in `production/crew-call.md` so it says everyone should arrive 30 minutes earlier. Leave the change uncommitted and unpushed.

Inspect the diff.

Ask the agent to explain what the diff means.

Then say:

> Restore `production/crew-call.md` to its recorded version.

Verify the project is clean again.

## Compare with local ignored state

The project also contains a local operational file at:

`local/radio-allocations.csv`

Ask the agent:

> Is this file tracked by Git? If it were deleted, could Git restore its contents? Inspect the project before answering.

Do not rely on the filename or `.gitignore` alone; let the agent establish whether Git actually has a recorded version.

## Reflect

Talk through:

- Was the agent remembering the deleted briefing?
- Where did the restored contents actually come from?
- What did the diff represent?
- What does a clean working tree mean?
- Why is the local radio-allocation file different?
- How does this explain why some local project state can be recoverable while other local state is not?

The useful ideas are:

> **The working project can be messy without destroying the last state you understood.**

and:

> **Git can only restore a version it has actually recorded.**
