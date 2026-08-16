# Module 4 — Repositories, save points, and safe breakage

Approximate duration: 1 hour.

Status: structured planning. The lab shape is now fairly mature, but do not scaffold it yet.

## Core idea

Source control is not mainly a programmer ritual. It is controlled history and a recovery mechanism.

The behavioural goal is to replace:

> I should not try this because I might break something.

with:

> What is the blast radius, and do I have a recovery path?

The learner should leave this lab willing to let an agent experiment with reversible project state, while becoming more deliberate as changes move from working state to committed history, from local history to published history, or outside the repository altogether.

## Teaching shape — cash in the opaque behaviour from earlier labs

This lab should be callback-heavy.

The learner has already used source-control discipline successfully without being asked to understand the mechanics. Lab 4 reveals what was underneath those earlier smooth workflows.

The teaching principle is:

> Explain the mechanism after the learner has already experienced the benefit.

### Callback to Lab 1

In Lab 1, the learner casually deleted `output/mission-brief.md` before asking the on-disk worker to regenerate it.

That was safe because the artifact was disposable and easy to reproduce.

Use that memory as the first conceptual bridge:

> Remember when we threw the mission brief away because nothing important depended on that copy? Source control lets us make more consequential project experimentation feel similarly recoverable.

### Callback to Lab 2

In Lab 2, the learner deleted tracked scratch files locally and then simply asked the agent to put them back. The learner card deliberately said not to worry about the source-control mechanics yet.

Lab 4 should explicitly cash that cheque:

> Remember when we deleted those files, changed our mind, and just restored them? Here is what made that possible.

Lab 2 also established that some project state can exist locally without entering the repository, using the ignored attendee database as the example. Lab 4 should refresh that distinction because it matters to recovery:

> Git can only recover content that entered Git history.

Do not overstate this as ignored files being literally invisible to Git. The important point is that Git has no recorded content version to restore if the content was never tracked.

### Callback to Lab 3

In Lab 3, the learner repeatedly used a workflow containing:

- clean baselines;
- uncommitted experimental runs;
- diffs;
- `Discard that run.`;
- explicit approval before commit;
- `Commit and push it.` only for work worth keeping.

The project instructions carried those mechanics so the learner did not have to reconstruct them in every task prompt.

Lab 4 should now explain why that convention worked:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

and:

> A commit is a state you understand and want a recovery point for.

## Fixture direction

Lab 4 should have its own isolated fixture, as every lab should.

Use a small fictional theatre-production project. The learner should be able to understand the operational meaning of the files without learning a new domain, while still being able to mentally scale the same problems up to a large production.

Possible material:

- crew call information;
- access and load-in notes;
- venue notes;
- crew briefing;
- working production notes;
- a small local/operational artifact excluded by `.gitignore`.

The exact filenames can be chosen when the lab is scaffolded.

The fixture should begin:

- clean;
- committed;
- pushed;
- with standing project instructions that preserve the review-stop convention learned in Lab 3 unless the learner explicitly asks to commit or push.

Keep the operating model deliberately simple:

> one repository, one main line of history, one agent changing it at a time.

Do not introduce branches, PRs, worktrees, or concurrent-agent isolation here. A later lab can deliberately break this simple model by demonstrating why it stops being safe when parallel work arrives.

## Proposed exercise structure

### Exercise 1 — How did it put that back?

Purpose: reveal working state, recorded state, diffs, restore, and the tracked/untracked recovery boundary.

Start from the clean fixture.

Ask the agent to make a simple destructive local change to a tracked file, such as deleting the crew briefing. Standing instructions should leave the change uncommitted.

Do not immediately restore it.

Inspect the source-control view and/or `git status` and diff. Make the learner see two simultaneously true states:

```text
recorded project state
tracked file exists

current working state
tracked file is deleted
```

Ask the agent what Git knows about the change, then ask it to restore the file.

Repeat once with an edit rather than a deletion so the learner sees a content diff as well as file-level deletion/restoration.

Then refresh the Lab 2 ignored-state lesson. The fixture should contain a harmless local artifact under an ignored path. Ask:

> If this were deleted, could Git put it back too?

Have the agent inspect whether the object is tracked before answering. Do not destroy anything valuable merely to prove the point.

The intended distinction is:

```text
tracked content
Git has recorded a version
→ Git can compare and recover it

never-tracked local content
Git has no recorded content version
→ Git has no version to restore
```

Reflection:

- What actually disappeared when we deleted the tracked file locally?
- Where did the restored version come from?
- What did the diff represent?
- What does a clean working state mean?
- Was the agent remembering the old file?
- Why could Git protect the tracked file but not promise recovery of a never-tracked ignored file?
- How does this explain the attendee-database behaviour from Lab 2?

Useful line to earn:

> The working project can be messy without destroying the last state you understood.

And:

> Git only protects content that entered Git history.

### Exercise 2 — Make a mess, then choose what survives

Purpose: cash in the Lab 3 experiment/review/discard workflow and make the diff the primary evidence surface.

From a clean committed state, ask the agent for a deliberately broad but plausible restructuring of the theatre project, for example reorganising the production pack to make the crew handover easier to use.

The task should be subjective enough that several reasonable changes are possible. The learner should not know in advance exactly which files the agent will touch.

The agent stops for review without committing.

Inspect the diff before relying on the completion message.

Then ask the agent to explain what it changed and compare that explanation with the actual diff.

Have the learner keep some useful changes and reject others. For example:

> Keep the crew-briefing improvements, but put the venue and access notes back the way they were.

Inspect the reduced diff again.

Only once the learner understands and approves the resulting state should they ask for a commit.

Reflection:

- Why was it reasonable to let the agent make a broad experiment?
- What limited the blast radius?
- Which artifact told us what actually changed?
- Was the agent's prose summary sufficient evidence?
- What did `Discard that run.` in Lab 3 really mean mechanically?
- Why wait until after review to commit?

Useful lines to earn:

> Don't tell me you changed it. Show me the diff.

> A commit is a state you understand and want a recovery point for.

### Exercise 3 — Commit is not push

Purpose: make the learner understand local working state, local committed history, and published remote history as separate states.

This is not merely a recovery exercise. It should answer:

> Why does Git have two operations here at all?

The basic sequence to make visible is:

```text
change files
↓
inspect
↓
commit
"record this point in local project history"
↓
possibly do more local work and make more commits
↓
push
"publish the local history that has not reached the remote yet"
```

#### Part A — observe the intermediate state

Make one harmless approved change and tell the agent:

> Commit that change, but do not push it.

Inspect both sides:

- locally, the working tree is clean and the new commit exists;
- remotely, GitHub still shows the previous published state.

Then say:

> Push it.

Inspect again.

The learner should physically observe that `commit` and `push` are two sequential actions, even when later issued together as `commit and push`.

#### Part B — wrong but unpublished

Create another plausible change, review it, commit it locally, and stop before push.

Then discover that it was wrong.

Recover while it is still unpublished.

The learner does not need to learn reset/rebase mechanics. It is enough to lightly name the fact that Git has ways to reshape unpublished local history and that this is a different recovery situation from published history. The agent may perform the mechanics while the learner inspects the resulting state.

#### Part C — wrong and published

Create another harmless wrong operational change, commit it, and push it.

Then reveal the correction.

Ask the agent to explain the recovery situation before acting.

For published/shared history, use a forward corrective commit rather than teaching the learner to erase the historical event. Hands-on, the learner should see a history like:

```text
known good state
↓
wrong change
↓
correction restoring the right state
```

The current project is correct again even though history still records the mistake.

Reflection:

- What changed when we committed?
- What changed when we pushed?
- Why might somebody deliberately commit without immediately pushing?
- Could useful local work contain several understandable commits before any of them are published?
- If three local commits existed and then we pushed once, what would that push mean?
- Why does `commit and push` remain two deliberate actions even when the agent performs both from one instruction?
- Why did the unpublished mistake give us more freedom than the published one?
- Why is a new corrective commit a sensible default once other people or systems may have consumed published history?
- Can the current state be correct even though history contains a mistake?

Useful lines to earn:

> Commit records work. Push publishes recorded work.

> `Commit and push` is two instructions, not one state called `finished`.

> Committed does not mean irreversible.

> Published history can be corrected without pretending the mistake never happened.

### Exercise 4 — Can Git save us?

Purpose: close the lab with a game that requires the learner to apply the recovery model rather than merely repeat slogans.

Present scenarios one at a time. Before classifying the situation, allow or require the learner to ask one diagnostic question.

Possible buckets:

1. **Git can recover the project state.**
2. **Git can repair the project, but something has escaped the repository boundary.**
3. **Git has no recorded recovery path for the lost thing.**

The scenarios should have hidden details or progressive reveals so they are not trivial without the concepts learned earlier.

Examples:

#### Deleted crew-call document

> An agent deleted tomorrow's crew-call document. Can Git save us?

The useful counter-question is:

> Was it tracked?

If yes, recoverable. If it was never tracked, Git has no recorded copy.

#### Wrong call time

> An agent changed tomorrow's call time and committed it. Can Git save us?

Useful question:

> Was it pushed?

If not, unpublished-history recovery options remain.

Then replay with the commit pushed. Git can still correct project state, but the recovery method changes.

Then reveal:

> The stage manager already copied the wrong time into the crew WhatsApp.

Now Git can repair the project but cannot recall the external message or its consequences.

#### Supplier order

> The agent changed a tracked supplier order from 20 lamps to 200.

Recoverable while this is only project state.

Then reveal:

> It submitted the order through the supplier portal.

Git is no longer the recovery system for the external transaction.

#### Automatic publication

> The agent made a bad public-information edit and pushed it.

Git can correct the source history.

Then reveal:

> Every push automatically deploys the public site.

The project can be repaired and redeployed, but people may already have seen the bad information.

#### Secret exposure

> The agent accidentally committed a production credential, then reverted the file immediately.

The repository contents can be corrected, but the credential may no longer be secret. The external recovery action is credential rotation, not merely another Git edit.

#### Live system

> The agent changed a lighting cue in the production project.

Likely recoverable as project state.

Then reveal:

> It changed the live lighting desk during the performance.

Git may help reconstruct intended configuration later, but it cannot undo the real-world event that already happened.

The game should train three increasingly natural counter-questions:

> Was it tracked?

> Was it published?

> Did anything escape the project boundary?

The learner should reach the broader conclusion:

> Reversibility depends on where the change happened, whether Git recorded it, whether recorded history was published, and whether consequences escaped the project boundary.

Close on:

> Be fearless with reversible state. Be deliberate with irreversible or external side effects.

and:

> Make experimentation cheap by controlling the blast radius.

## Recovery loop to practise throughout

When an agent does something surprising:

1. Stop.
2. Inspect state.
3. Understand the diff and history position.
4. Decide what should survive.
5. Restore, reshape, or correct as appropriate.
6. Verify the resulting state.

Have the learner direct the agent to explain its own changes, but verify against Git rather than trusting the explanation.

## Tools to experiment with

- Git status and diff;
- IDE source-control/diff UI;
- local agent editing several files;
- restore operations;
- local commit history;
- GitHub remote inspection;
- forward corrective/revert commits for published mistakes.

Prefer visual inspection over command memorisation.

## What this lab should not become

Do not turn this into a general Git course.

Do not teach:

- branching models;
- pull-request workflows;
- worktrees;
- merge strategies;
- detached HEADs;
- Git object internals;
- rebasing as a hands-on skill.

It is acceptable to lightly acknowledge that unpublished local history can be reshaped using tools such as reset/rebase, but the learner does not need those mechanics yet.

Branches, worktrees, PRs, and concurrent-agent isolation should arrive later when the simple assumption of one agent changing one main line is deliberately shown to be insufficient.
