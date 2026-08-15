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

## Tools to experiment with

- repository search (`rg`/IDE search);
- Git diff/status;
- artifact rendering or preview;
- simple validation scripts;
- GitHub remote inspection when publication is part of the task.

## Discussion prompts

- What evidence would convince us this task is actually complete?
- Can the agent perform that verification itself?
- Is the check independent enough to catch the original failure?
- What is authoritative when sources disagree?
- Which checks should eventually become automatic?

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
