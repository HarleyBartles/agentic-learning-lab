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

## Move tracked state out of Git's current view

The project currently tracks:

`production/radio-allocations.csv`

The `local/` folder is for operational state that should remain on this machine rather than being part of the current tracked project.

Ask the agent:

> Move `production/radio-allocations.csv` into `local/radio-allocations.csv`. This is local operational state now, so it should no longer be tracked. Commit and push the resulting project change.

Inspect what happened before moving on.

The current project history should now record that `production/radio-allocations.csv` was removed. The copy under `local/` exists on disk but is ignored by Git.

Ask:

> Is `local/radio-allocations.csv` tracked by Git now?

Then deliberately delete the local file:

> Delete `local/radio-allocations.csv`.

Now ask:

> We just deleted it and Git isn't tracking it. Can Git put it back?

Do not settle for the first yes/no answer. Follow with:

> Was this file ever tracked by Git, even though it is not tracked now?

Ask the agent to inspect history and recover the previous contents into `local/radio-allocations.csv` without adding the restored local file back to Git tracking.

Verify that the recovered file matches the earlier radio allocations.

## Compare with something Git never knew

Your facilitator may have placed one or two harmless scratch files in `local/` before the lab. Those files have always been ignored and have never entered Git history.

Ask the agent to identify one of them and answer:

> If this file were deleted, could Git reconstruct its contents? How is that different from `local/radio-allocations.csv`?

You should now have three different cases:

```text
tracked now
Git has a current recorded version

not tracked now, but tracked historically
Git may still have an older recorded version in history

never tracked
Git has no recorded content version to recover
```

## Reflect

Talk through:

- Was the agent remembering the deleted briefing?
- Where did the restored contents actually come from?
- What did the diff represent?
- What does a clean working tree mean?
- Is `not tracked now` the same thing as `never tracked`?
- Why could Git recover the radio allocations after they had moved into an ignored folder?
- Why can Git not promise the same recovery for a file that never entered its history?
- How does this change the question you would ask when someone says, `Git isn't tracking it`?

The useful ideas are:

> **The working project can be messy without destroying the last state you understood.**

> **Not tracked now is not the same as never tracked.**

and:

> **Git can only restore content that it has recorded somewhere in its history.**
