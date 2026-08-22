# Module 9 — Source of truth and verification

Approximate duration: 1 hour.

## Core idea

Lab 8 should leave the learner with a precise observation problem:

> A worker can reach several pieces of evidence through different access and discovery routes. Which one should it trust, and what would actually prove the work is correct?

Module 9 owns that distinction.

Access and discovery answer:

> What can the worker observe, and how did that evidence reach it?

Authority and verification answer different questions:

> Which source defines the requirement or current truth?

and:

> What evidence establishes that the work actually satisfies it?

An agent saying something happened is not the same as it having happened correctly.

The learner should move from evaluating answers to evaluating work.

> Prefer evidence over confident prose.

Do not collapse authority and verification. A worker can verify perfectly against the wrong source of truth.

## Suggested session shape

### 0–15 minutes — Reopen the Lab 8 contradiction

Do not start Module 9 as a disconnected verification lecture.

Bring back the end of Lab 8: local project state, GitHub remote state, or another durable source may all be accessible while saying different things or answering different parts of the question.

Ask:

> The worker can see all of these. Which one wins?

Then separate the questions:

- Which source is authoritative for this claim?
- What evidence would prove that the required outcome actually happened?

This should cash the Lab 8 lesson without undoing it:

> **Observation method constrains what the worker can know. Authority constrains what it should treat as defining truth. Verification constrains what it may safely claim is complete.**

### 15–30 minutes — Separate claim from state

Use a simple example:

> The agent says it renamed a concept everywhere in the project.

Ask what would actually prove that.

Possible evidence:

- search for the old term;
- inspect the diff;
- read the changed files;
- confirm that only intended files changed.

The point is to make `completion message` and `completed work` feel like different objects.

### 30–45 minutes — Run a verification exercise

Give the local agent a task such as:

> Rename this concept everywhere in this disposable exercise and tell me when it is done.

When it reports completion, verify independently.

Search for the old value. Inspect the diff. Look for accidental changes. If something was missed, discuss why the verification caught a failure that the original task execution did not.

Then ask whether the agent itself could have performed those checks before declaring success.

### 45–55 minutes — Verification depends on the artifact

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

The Lab 8 GitHub Actions example should now pay off cleanly:

- local workflow source can establish what should run;
- remote GitHub state is required to establish whether a particular remote run actually occurred and what result GitHub recorded.

That does not make remote state universally authoritative. The claim determines which evidence surface is relevant.

### 55–60 minutes — Source of truth

Create or revisit a disagreement between conversation memory, a note, generated output, and an authoritative project file.

Ask:

- Which one wins?
- How does an agent know?
- Should generated output ever silently overwrite source material?
- Does a local commit prove that GitHub received the work?

Use this to reinforce that authoritative state should be explicit rather than inferred from whichever message is newest or easiest to access.

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

This callback pairs directly with Lab 8:

```text
Lab 8
not found through this current route
!=
does not exist now

Lab 9
not present in current state
!=
never existed in recorded history
```

Together they support:

> **Your observation method constrains what conclusions absence can support.**

Do not force historical archaeology into the first version of the Module 9 lab if it distracts from the main authority/verification lesson. Preserve it as a later exercise or advanced callback if necessary.

## Tools to experiment with

- repository search (`rg`/IDE search);
- Git diff/status;
- Git history inspection for historical recovery when appropriate;
- artifact rendering or preview;
- simple validation scripts;
- GitHub remote inspection when publication or CI state is part of the claim.

## Discussion prompts

- What evidence would convince us this task is actually complete?
- Which source defines what `correct` means here?
- Can the agent perform that verification itself?
- Is the check independent enough to catch the original failure?
- What is authoritative when sources disagree?
- Which checks should eventually become automatic?
- If something is missing now, what evidence would tell us whether it existed in recorded project history?

## Useful distinctions

A worker report is not durable proof.

For repo-backed work, distinguish:

- agent says it committed;
- commit exists locally;
- branch exists remotely;
- PR exists;
- checks pass;
- change is actually merged where expected.

Each is a different state and each requires evidence from the surface capable of establishing that claim.

Also distinguish:

```text
access/discovery
what evidence can the worker reach, and how?

authority
which source defines the requirement/current truth?

verification
what evidence establishes that the work satisfies it?
```

## Do not teach yet

Do not build a heavy CI system merely to demonstrate verification. Start with checks a human can understand and inspect. Automation should later encode a verification habit that already makes sense.