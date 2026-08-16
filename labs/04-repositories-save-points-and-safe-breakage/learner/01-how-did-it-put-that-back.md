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

## Put some genuinely local working material in `local/`

The project contains a `local/` folder.

Read its README, then ask the agent to help create a few plausible on-site, day-of-production working files there. Keep them lightweight and disposable.

For example, ask:

> We're going to use `local/` for little on-site things that only matter on this machine during the current production day. Put a few realistic disposable notes in there: something like a temporary console position note, a quick dressing-room label list, and a scratch channel note. Nothing important or durable.

Inspect what the agent creates.

These files should feel genuinely local and disposable.

## Move the radio assignments into `local/`

The project currently tracks:

`production/radio-allocations.csv`

Reason from the folder name and the other files you have just created there.

A perfectly reasonable interpretation is that radio assignments are another local, on-the-day operational concern.

Ask the agent:

> Move `production/radio-allocations.csv` into `local/radio-allocations.csv` with the other local on-site stuff. Then commit and push all the changes so we're safe.

Let the agent do it.

Inspect the result just enough to confirm the change was committed and pushed.

At this point, act on the reasonable assumption that because everything was committed and pushed, you have a safe copy upstream.

## Clear out the local mess

The `local/` folder now contains several disposable files plus the radio assignments you moved there.

Tell the agent:

> Clear out the `local/` folder. Hard delete everything in there, no recycle bin. It's become a mess; I'll start again. After that we'll compare what's in the repo upstream with what we deleted and rewrite anything we still want.

Let the agent delete the ignored local files.

Now realise the mistake:

> Oh no — it deleted the radio assignments file as well. I moved that into `local/` earlier. Are we stuffed?

Do not jump straight to the answer.

First ask:

> Is `local/radio-allocations.csv` in the repo upstream now?

Then inspect what the earlier commit actually did.

The important reveal is that `local/` means local to this machine from Git's point of view. Its operational contents are ignored.

Your earlier `commit and push all the changes` did not publish the moved file at its new location. It published the deletion of the old tracked file from `production/`.

So the current published project no longer contains the radio assignments at all.

Now ask:

> If the file is not in the current repo and we hard-deleted the local copy, is it gone for good?

Then:

> Was this file ever tracked before we moved it into `local/`?

Ask the agent to inspect Git history and recover the last tracked version of `production/radio-allocations.csv` into `local/radio-allocations.csv` without re-adding the local path to tracking.

Verify the recovered contents.

## What just happened?

The useful surprise is that Git is not only a snapshot of what exists now.

The current published state says the tracked production copy was deleted.

But earlier history still contains the file and its contents.

That is why the agent can recover something that is:

- not tracked now;
- not present in the current remote state;
- hard-deleted locally;
- but previously committed in Git history.

The distinction is:

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

- Was `commit and push all the changes` enough to preserve the new `local/radio-allocations.csv` path?
- What did Git actually publish when the tracked file was moved into an ignored folder?
- Why was the learner's interpretation of `local/` reasonable?
- Why was Git's interpretation different?
- After the hard delete, where did the recovered radio assignments actually come from?
- Is `not in the repo now` the same as `never existed in Git`?
- How does this change your mental model of a repository?

The useful ideas are:

> **The working project can be messy without destroying the last state you understood.**

> **Not tracked now is not the same as never tracked.**

and the main reveal:

> **Git is not just a snapshot of now. It is a history of recorded project states.**
