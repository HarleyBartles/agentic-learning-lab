# Lab 4 facilitator guide

Status: **Scaffolded; ready for dry-run refinement.**

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

The `local/` folder exists in a fresh checkout but its operational contents are ignored by Git. Only `local/README.md` is tracked so the directory itself survives the clone/fork.

Before the learner starts, add one or two harmless ignored scratch files locally under `project/local/`, for example:

```text
local/console-layout.txt
local/temp-channel-note.txt
```

Their contents should be inconsequential. They exist only so Exercise 1 has a genuine `never tracked` comparison after the learner moves a previously tracked file into the same ignored area.

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

Goal: distinguish current working state from recorded state, then distinguish `not tracked now` from `never tracked`.

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

Now make the stronger history experiment.

The learner tells the agent to move:

`production/radio-allocations.csv`

into:

`local/radio-allocations.csv`

and explicitly commit and push the resulting project change.

Because `local/*` is ignored, the published Git history records the tracked production file disappearing while the operational copy remains only on the learner's machine.

Pause and inspect:

- `local/radio-allocations.csv` exists locally;
- Git does not track that current path;
- the old tracked file no longer exists at `production/radio-allocations.csv` in current project state;
- history still contains the earlier tracked content.

Then have the learner delete the local radio-allocation file.

The learner asks whether Git can restore it. The first useful question is:

> Is it tracked now?

The stronger follow-up is:

> Was it ever tracked?

The agent should inspect history and recover the previous contents from the old tracked location into the ignored `local/radio-allocations.csv` path, without re-adding that path to tracking.

This earns the three-state model:

```text
tracked now
→ Git has a current recorded version

not tracked now, but tracked historically
→ Git may still contain a recoverable historical version

never tracked
→ Git has no recorded content version to recover
```

Now compare the restored radio-allocation file with one of the harmless ignored scratch files created during setup. The scratch file has never existed in Git history, so if it disappears Git cannot reconstruct its contents.

Useful questions:

- Was the agent remembering the deleted file?
- Where did the restored contents come from?
- What exactly did the diff show?
- What does `clean` mean here?
- Is `not tracked now` equivalent to `never tracked`?
- How did moving a file across the tracked/ignored boundary change its current recovery story without erasing its history?

Earn:

> **The working project can be messy without destroying the last state you understood.**

> **Not tracked now is not the same as never tracked.**

> **Git can only restore content it recorded somewhere in history.**

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

Do not push yet unless needed to reset the baseline before Exercise 3.

Earn:

> **Don't tell me you changed it. Show me the diff.**

> **A commit is a state you understand and want a recovery point for.**

## Exercise 3 — Commit is not push

Goal: make working state, local recorded history, and learner-fork published history visibly separate.

Before this exercise, get the project back to a clean baseline. If Exercise 2 produced a useful commit, push it now so local and remote begin aligned.

### Part A — visible intermediate state

Use a harmless change such as improving the wording in `working/handover-notes.md`.

Learner says:

> Commit that change, but do not push it.

Inspect:

- local working tree is clean;
- local history contains the new commit;
- learner's GitHub fork still shows the previous published state.

Then:

> Push it.

Inspect the remote again.

This is where the learner-owned fork becomes concrete. Do not introduce upstream synchronization yet.

Earn:

> **Commit records work. Push publishes recorded work.**

### Part B — wrong but unpublished

Use a harmless operational change: change the load-in start in `production/access-and-load-in.md` from `08:00` to `07:30` and commit it locally without pushing.

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
