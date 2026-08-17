# Module 8 — Source of truth and verification

Approximate duration: 1 hour.

## Core idea

An agent saying something happened is not the same as it having happened correctly.

The learner should move from evaluating answers to evaluating work.

> Prefer evidence over confident prose.

## Suggested session shape

### 0–15 minutes — Separate claim from state

Use a simple example:

> The agent says it renamed a concept everywhere in the project.

Ask what would actually prove that.

Possible evidence:

- search for the old term;
- inspect the diff;
- read the changed files;
- confirm that only intended files changed.

The point is to make `completion message` and `completed work` feel like different objects.

### 15–35 minutes — Run a verification exercise

Give the local agent a task such as:

> Rename this concept everywhere in this disposable exercise and tell me when it is done.

When it reports completion, verify independently.

Search for the old value. Inspect the diff. Look for accidental changes. If something was missed, discuss why the verification caught a failure that the original task execution did not.

Then ask whether the agent itself could have performed those checks before declaring success.

### 35–50 minutes — Verification depends on the artifact

Compare feedback mechanisms:

```text
text change       -> search + diff + read
PDF               -> render + inspect
technical drawing -> dimensional checks + render
software          -> tests + static checks + runtime behaviour
GitHub publication-> remote branch/commit/PR/check exists
research          -> source citations + provenance + contradiction checks
```

Discuss why `the source file looks right` may not prove that a generated artifact is right.

For example, a document-generation script may run successfully while the rendered PDF clips text or has broken layout.

### 50–60 minutes — Source of truth

Create or revisit a disagreement between conversation memory, a note, generated output, and an authoritative project file.

Ask:

- Which one wins?
- How does an agent know?
- Should generated output ever silently overwrite source material?
- Does a local commit prove that GitHub received the work?

Use this to reinforce that authoritative state should be explicit rather than inferred from whichever message is newest.

## Future callback — "is it tracked?" becomes "was it ever tracked?"

Lab 4 should teach the simple recovery question:

> Is the lost thing tracked?

That is the right first model because Git cannot restore content that never entered Git history.

Later, once the learner understands that Git is historical state rather than merely a snapshot of the current repository, deliberately deepen the question to:

> Was it ever tracked?

Use a scenario like this:

1. `production/cue-notes.md` was tracked for some time.
2. Later, the file was moved to an ignored local location such as `local/cue-notes.md` and removed from the current tracked project state.
3. The local ignored copy was then accidentally deleted by an agent.
4. The current filesystem contains no copy, and the current repository no longer tracks that path.

Ask the learner:

> Can Git save us?

The Lab 4 reflex may be:

> It is ignored now, so no.

The better historical question is:

> Did some earlier commit contain the content we need?

If so, Git history may still hold a recoverable version even though the file is absent now and its current destination is ignored.

The progression is:

```text
Lab 4 question:
Is it tracked?

Later question:
Was it ever tracked?

Deeper historical question:
Which recorded state contained the version we need?
```

The lesson should make clear that current `.gitignore` rules describe what Git should normally ignore now; they do not erase older repository history.

Useful lines to earn:

> Not tracked now does not necessarily mean never tracked.

> Current absence does not prove historical absence.

> Git is recorded project history, not just a backup of the files currently present.

This future callback fits naturally with verification because recovery starts with evidence: inspect history before concluding that a missing object is unrecoverable.

It also pairs usefully with the later discoverability lesson in Module 7:

- something can exist now but fail to be discovered through the agent's normal navigation path;
- something can be absent now but still be discoverable in historical project state.

Do not force historical archaeology into the first version of the Module 8 lab if it distracts from the main verification lesson. Preserve it as a later exercise or advanced callback.

## Tools to experiment with

- repository search (`rg`/IDE search);
- Git diff/status;
- Git history inspection for historical recovery when appropriate;
- artifact rendering or preview;
- simple validation scripts;
- GitHub remote inspection when publication is part of the task.

## Discussion prompts

- What evidence would convince us this task is actually complete?
- Can the agent perform that verification itself?
- Is the check independent enough to catch the original failure?
- What is authoritative when sources disagree?
- Which checks should eventually become automatic?
- If something is missing now, what evidence would tell us whether it existed in recorded project history?

## Useful distinction

A worker report is not durable proof.

For repo-backed work, distinguish:

- agent says it committed;
- commit exists locally;
- branch exists remotely;
- PR exists;
- checks pass;
- change is actually merged where expected.

Each is a different state.

## Do not teach yet

Do not build a heavy CI system merely to demonstrate verification. Start with checks a human can understand and inspect. Automation should later encode a verification habit that already makes sense.
