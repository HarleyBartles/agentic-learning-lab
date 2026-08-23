# Lab 1 — Exercise 3: On-disk worker

## Start clean

Before starting, delete `mission/output/mission-brief.md` if it exists.

## Before you type anything

Open the preconfigured Codex project named:

`Lab 1 - Exercise 3`

Before entering the task, look at the invitation Codex shows you when it is waiting for your first instruction.

Write down its exact wording somewhere you can return to at the end of Course 1.

Do not analyse it yet and do not try to give a clever answer. Just record what the agent is asking you before the work begins.

The exact product wording is not part of the lesson and may change over time. Record whatever equivalent opening invitation Codex actually shows at delivery time.

## Task

Give it only this instruction:

> Complete the exercise.

Do not point it at individual source files and do not remind it about `late-update.md`.

## Exercise complete

Stop when `mission/output/mission-brief.md` exists locally and satisfies the same mission win condition used in Exercise 1.

Do not delete it yet.

## Reflect

Talk through:

- What project information did you have to transport manually this time?
- Who discovered the source files?
- Who determined which project state was current?
- Why was there no need for a completeness reminder?
- What changes if this project contains 40 files? 400?

The key observation is:

> A conversation can only work with the project state made visible to it. An on-disk worker can inspect the environment where that state lives.
