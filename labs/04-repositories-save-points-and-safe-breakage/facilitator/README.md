# Lab 4 facilitator guide

Status: **Mature and ready to run.**

## Lab learning goal

Lab 4 explains the source-control mechanics the learner has already benefited from in Labs 1–3.

The learner should finish with a recovery model, not a Git command syllabus.

The central behavioural shift is:

> I should not try this because I might break something.

becoming:

> **What is the blast radius, and do I have a recovery path?**

The lab should make experimentation feel cheap when state is reversible, while making the learner increasingly deliberate as changes move from working state to committed history, from local history to published history, or outside the repository altogether.

## Callbacks to earlier labs

Use the callbacks conversationally rather than as a recap lecture.

Lab 1: the learner threw away a generated mission brief because it was disposable.

Lab 2: the learner deleted tracked scratch files and asked the agent to put them back, while a local attendee database remained outside tracked project history.

Lab 3: the learner repeatedly worked from a clean baseline, inspected uncommitted diffs, discarded bad runs, and only committed/pushed work worth keeping.

Useful transition:

> You've already been using this recovery model. This lab makes the machinery visible.

## Project fixture

Root the local agent at:

`labs/04-repositories-save-points-and-safe-breakage/project/`

The fixture is a fictional theatre production called **Northstar**.

Tracked project material includes:

- `production/crew-briefing.md`
- `production/crew-call.md`
- `production/venue-notes.md`
- `production/access-and-load-in.md`
- `production/radio-allocations.csv`
- `working/handover-notes.md`

The `local/` folder exists in a fresh checkout, but operational contents under it are ignored by Git. Only `local/README.md` is tracked so the directory survives clone/fork.

The README should not front-load the Git lesson. It describes `local/` in operational language: temporary venue/day-of-production material that only matters on this machine or current on-site session.

Do not pre-seed local scratch files. The learner and agent create a few legitimate disposable local-concern files during Exercise 1 so the folder's apparent meaning emerges naturally from use.

Do not create `local/radio-allocations.csv` during setup. The learner creates that state themselves by moving the tracked `production/radio-allocations.csv` during Exercise 1.

## Standing project instructions

`project/AGENTS.md` continues the Lab 3 review-stop convention:

- inspect before acting;
- requested changes remain uncommitted/unpushed by default;
- commit/push require explicit authorization;
- `discard that run` restores only the current run's uncommitted changes;
- source material should not be modified casually;
- explain recovery position before history-changing actions where useful.

This is facilitator control, not yet an instruction-architecture lesson.

## Exercise 1 — How did it put that back?

Goal: first distinguish working state from recorded state, then earn the stronger realization that Git is history rather than merely a snapshot of the current repo.

Start clean.

Learner asks the agent to delete `production/crew-briefing.md` without committing.

Inspect `git status` and/or the IDE source-control view before restoring it.

Make the two states explicit:

```text
recorded state
crew-briefing.md exists

working state
crew-briefing.md is deleted
```

Then ask the agent to restore it.

Repeat with a content edit to `production/crew-call.md`, inspect the diff, and restore that too.

### Build a plausible meaning for `local/`

Have the learner read `local/README.md` and ask the agent to create a few genuinely useful but disposable on-site files there.

Suitable examples:

```text
local/console-position.txt
local/dressing-room-labels.md
local/channel-scratch.txt
```

The exact files do not matter. They should feel like temporary venue/day-of-production concerns that it would be reasonable to throw away and recreate.

Do not tell the learner yet that the important property is Git ignoring them. Let the operational interpretation lead.

### Make the reasonable misunderstanding

The project still tracks:

`production/radio-allocations.csv`

By now, `local/` contains several things that sound like on-site local-production concerns. It is reasonable for the learner to infer that radio assignments belong there too.

Have the learner say approximately:

> Move `production/radio-allocations.csv` into `local/radio-allocations.csv` with the other local on-site stuff. Then commit and push all the changes so we're safe.

The wording matters. The learner is not behaving recklessly. They believe `commit and push` means the moved file has been safely captured upstream.

The agent should move the file. Because the destination is ignored, Git records only the deletion of the old tracked path. The local destination survives on disk but is absent from the published repository.

Allow a brief inspection that confirms a commit and push happened, but do not force the learner to notice the ignored-file implication yet. The simulation works even if they suspect it.

### Clear the local folder

Now make the cleanup request deliberately confident:

> Clear out the `local/` folder. Hard delete everything in there, no recycle bin. It's become a mess; I'll start again. After that we'll compare what's in the repo upstream with what we deleted and rewrite anything we still want.

This is a reasonable instruction under the learner's mistaken model:

- the folder appears disposable;
- the learner believes pushed changes are safely upstream;
- the scratch files are intentionally recreatable.

The hard-delete/no-recycle-bin phrasing matters because the later recovery should come from Git history, not an OS trash mechanism.

After deletion, reveal or simulate the learner noticing:

> Oh no — it deleted the radio assignments file as well. I moved that into `local/` earlier. Are we stuffed?

### Inspect current remote state

First ask whether `local/radio-allocations.csv` exists in the repository upstream/current learner fork.

It does not.

Then inspect the commit that moved it.

The crucial discovery is:

> `local` meant local to this machine from Git's point of view, not merely `local venue/on-site concerns`.

The earlier `commit and push all the changes` published the deletion of `production/radio-allocations.csv`; it did not publish the ignored new path.

At this point, the learner's current-state model should say the file is gone:

```text
old tracked path
absent from current repo

new local path
hard-deleted from disk

remote/current repo
contains no radio-allocation file
```

### Aha — current repo is not all Git knows

Now ask:

> Was this file ever tracked before we moved it into `local/`?

Have the agent inspect history.

Recover the last tracked version of `production/radio-allocations.csv` from an earlier commit into `local/radio-allocations.csv`, without re-adding the ignored local destination to tracking.

Verify the recovered contents.

This is the intended aha moment:

> **Git is not just a snapshot of now. It is a history of recorded project states.**

The learner should see that all of these can be true at once:

- the file is not tracked now;
- it is not present in the current remote state;
- the current local copy was hard-deleted;
- Git can still recover it because an earlier committed state contains the content.

This also earns:

> **Not tracked now is not the same as never tracked.**

Do not overcomplicate this with Git object internals or retention edge cases. The useful mental model is historical recorded state.

Useful reflection questions:

- Why was the learner's interpretation of `local/` reasonable?
- What did `commit and push all the changes` actually publish?
- Why did comparing only with the current remote state make recovery appear impossible?
- Where did the recovered contents come from?
- What does the repository contain besides its current file tree?
- What question becomes useful after `Git isn't tracking it`?

Earn:

> **The working project can be messy without destroying the last state you understood.**

> **Not tracked now is not the same as never tracked.**

> **Git is not just a snapshot of now. It is a history of recorded project states.**

## Exercise 2 — Make a mess, then choose what survives

Goal: make the diff the primary evidence surface and show that broad experiments are safe when they remain reversible.

Use this request or equivalent:

> Reorganise this production pack so a crew member arriving cold can understand the handover quickly. Improve structure, reduce needless duplication, and make related information easier to find. Make whatever project-file changes you think are useful, but leave everything uncommitted for review.

The fixture contains deliberate overlap between the crew briefing, venue notes, access notes, and handover notes. A competent agent should plausibly touch several files.

Do not require one exact transformation.

Inspect the diff before reading the agent's prose summary.

Then compare the summary against the diff.

Ask the learner to preserve only part of the experiment. A suitable direction is:

> Keep the crew-briefing and handover improvements, but restore the venue and access notes to their previous state.

If the agent chose a different shape, adapt the partial-keep instruction to the actual diff.

Inspect the reduced diff again.

Only after the learner understands the remaining changes should they explicitly ask the agent to commit them.

End Exercise 2 with exactly this state:

```text
working tree
clean

local history
contains the reviewed Exercise 2 commit

learner fork
still ends at the previous published commit
```

Do not push the Exercise 2 commit yet.

That local/remote gap is not cleanup work. It is the starting fixture for Exercise 3.

Earn:

> **Don't tell me you changed it. Show me the diff.**

> **A commit is a state you understand and want a recovery point for.**

## Exercise 3 — Commit is not push

Goal: make working state, local recorded history, and learner-fork published history visibly separate without manufacturing a duplicate demonstration.

Exercise 3 begins exactly where Exercise 2 ended.

Do not align local and remote history first. Do not create another harmless wording commit.

### Part A — inspect the existing gap, then publish it

The learner already has a reviewed, committed Exercise 2 change locally that is absent from the fork.

Inspect both sides:

- local working tree is clean;
- local history contains the Exercise 2 commit;
- learner's GitHub fork still shows the previous published state.

Ask:

> What exists locally now that the remote repository does not have yet?

Then:

> Push the reviewed Exercise 2 commit.

Inspect the fork again.

This makes the distinction concrete using real work the learner already understands:

> **Commit records work. Push publishes recorded work.**

### Part B — wrong but unpublished

Now create a new harmless operational mistake: change the load-in start in `production/access-and-load-in.md` from `08:00` to `07:30`, commit it locally, and do not push.

Then reveal:

> That was wrong. The load-in remains 08:00.

Ask the agent to explain the recovery position before acting.

Let the agent reshape unpublished local history using an appropriate mechanism. The learner does not need reset/rebase syntax.

Verify that the local history and working state are correct and that nothing incorrect reached the fork.

### Part C — wrong and published

Now make a different harmless wrong change: change the crew-call assembly point in `production/crew-call.md` from `Stage Door` to `Loading Bay`, commit it, and push it.

Then reveal:

> That was wrong. Crew still assemble at Stage Door.

Ask the agent to explain the recovery situation first.

Use a forward corrective commit and push it.

The learner should see:

```text
known-good history
↓
wrong published change
↓
corrective change
```

Do not teach history erasure as the default for already-published work.

Earn:

> **Committed does not mean irreversible.**

> **Published history can be corrected without pretending the mistake never happened.**

## Exercise 4 — Can Git save us?

Goal: apply the model rather than recite it.

Use the learner card one scenario at a time. Do not dump all answers in advance.

Encourage one diagnostic question before classification.

Three useful buckets:

1. Git can recover the project state.
2. Git can repair the project, but something has escaped the repository boundary.
3. Git has no recorded recovery path for the lost thing.

Use the four core scenarios in the learner card:

- deleted tracked crew-call document;
- wrong call time, then reveal publication and WhatsApp propagation;
- supplier quantity edit, then reveal supplier-portal submission;
- credential committed then removed.

Keep additional reserve scenarios available verbally if the learner is moving quickly: automatic deployment and live lighting-desk change.

Train these counter-questions:

> Was it tracked?

> Was it published?

> Did anything escape the project boundary?

Close on:

> **Be fearless with reversible state. Be deliberate with irreversible or external side effects.**

## Recovery loop to practise throughout

When an agent does something surprising:

1. Stop.
2. Inspect state.
3. Understand the diff and history position.
4. Decide what should survive.
5. Restore, reshape, or correct as appropriate.
6. Verify the resulting state.

Let the learner ask the agent to explain unfamiliar Git actions, but verify the resulting state rather than trusting the explanation alone.

## Do not teach yet

Do not turn this into:

- a Git command course;
- branches;
- PR workflows;
- worktrees;
- merge strategies;
- detached HEADs;
- Git object internals;
- rebasing as a manual skill;
- concurrent-agent isolation.

The simplifying model remains:

> one repository, one main line of history, one agent changing it at a time.

Later curriculum deliberately breaks that model when concurrency creates a real reason for isolation.
