# Lab 01 — Cloud conversation versus local working environment

This exercise is intentionally simple. The goal is not to test writing ability; it is to make the operating-environment difference visible.

## Task

Create a concise briefing document that captures:

- the objective;
- the constraints;
- the decisions already made;
- the open questions.

Use all files in `source/` as input.

The finished briefing belongs in `output/briefing.md`.

## Run A — Cloud conversation

Use ordinary ChatGPT or another cloud chat surface.

Provide the source material however you normally would. When the briefing is complete, get it into this repository manually.

Notice what the human had to do to expose context and move the result.

## Run B — Local agent

Use an on-disk agent operating in this repository.

A suitable prompt is:

> Read this lab, work out what it is asking for, and create the finished briefing in `output/briefing.md`. Do not change the source material.

Notice what the agent can inspect and change directly.

## Optional extension

After both runs, change one source fact and ask which environment currently has the latest project state.
