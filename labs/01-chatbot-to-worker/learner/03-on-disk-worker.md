# Lab 1 — Exercise 3: On-disk worker

## Start clean

Before starting, delete `mission/output/mission-brief.md` if it exists.

## Task

Open the preconfigured Codex project named:

`Lab 1 - Exercise 3`

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
