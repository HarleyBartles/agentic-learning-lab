# Module 7 — Source of truth and verification

Approximate duration: 1 hour.

## Core idea

An agent saying something happened is not the same as it having happened correctly.

The learner should move from evaluating answers to evaluating work.

## Source of truth

A conversation may contain an old decision. Memory may recall something stale. An agent may claim success. None of those automatically outrank the project's authoritative state.

Ask questions such as:

- Which file is authoritative?
- Is this generated output or source material?
- Did the current branch actually contain the change?
- Did the remote receive it?

## Verification examples

For different kinds of work, verification may mean:

- inspect the diff;
- read the changed file;
- search for the old value;
- render a PDF and inspect it;
- check dimensions in a drawing;
- run tests or a validation script;
- verify the expected files exist;
- confirm a branch, commit, PR, or check exists remotely.

The right feedback mechanism depends on the work.

## Suggested exercise

Give the agent a task such as:

> Rename this concept everywhere in the project and tell me when it is done.

Do not accept the completion message as proof. Search the repository for the old term, inspect the diff, and check whether any unexpected files changed.

Then try a generated artifact: have the agent create a PDF or other rendered output and inspect the actual output rather than only the source file.

## Principle

> Prefer evidence over confident prose.

and:

> Do not trust that work happened when you can inspect whether it happened.

## Discussion prompts

- What evidence would convince us this task is actually complete?
- Can the agent perform that verification itself?
- Is the verification independent enough to catch the original failure?
- What is the authoritative state if sources disagree?
