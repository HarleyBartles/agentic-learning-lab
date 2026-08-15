# Lab 01 — Cloud conversation versus local working environment

This exercise is intentionally simple. The goal is not to test writing ability; it is to make the operating-environment difference visible.

## Mission

A field sensor has stopped reporting from a remote reserve site. The team needs a short recovery brief before sending anyone out.

The information you need is in `source/`.

Your finished mission brief must:

- state the objective;
- identify the current access route and timing;
- list the equipment the team should take;
- capture the important constraints;
- call out the main unresolved risk;
- correctly apply any later information that supersedes the original plan.

The mission is complete when a correct file exists locally at:

`output/mission-brief.md`

A correct brief must use the current plan, not present superseded and current instructions as unresolved alternatives.

## Stage 1 — Complete context in cloud ChatGPT

Use ordinary cloud ChatGPT.

ChatGPT cannot see this project folder. Use it however you want.

Make sure ChatGPT has all of the source information it needs, then produce the mission brief and get the finished result into `output/mission-brief.md`.

There is no required upload, download, or copy/paste technique. The only success condition is the finished local file.

When the file is correct, stop and notice what work you performed simply to move project information into the AI's environment and move the result back out.

Then delete `output/mission-brief.md`.

## Stage 2 — Deliberately incomplete context in cloud ChatGPT

Start a **fresh ChatGPT conversation**.

Repeat the mission, but this time deliberately do **not** give ChatGPT `source/late-update.md`.

Give it the other source material and ask it to produce the mission brief.

Inspect the result before moving on.

The expected outcome is that ChatGPT confidently produces a plausible but wrong current access plan, because the superseding information is invisible to it.

The point is not that ChatGPT is incapable of the task. Stage 1 already showed that it can solve the task when it has the complete source set.

Delete any Stage 2 output before continuing.

## Stage 3 — Local Codex

Now use Codex operating locally in this project.

Give it only this goal:

> Complete the exercise in `labs/01-cloud-vs-local`.

Let it inspect the exercise and work out what to do.

The success condition is unchanged: `output/mission-brief.md` must exist locally and satisfy the mission requirements.

Do not point Codex at individual source files or remind it about `late-update.md`. Its ability to inspect the project and discover the complete source set is part of the exercise.

## Compare

Do not compare the attempts mainly on writing quality.

Compare access to project state:

- Stage 1: ChatGPT succeeds because the human deliberately supplied the complete context.
- Stage 2: ChatGPT fails because critical project state was omitted and therefore invisible.
- Stage 3: the local agent can inspect the project and discover that state itself.

Then compare the transport work:

- Who discovered the inputs?
- Who decided whether the input set was complete?
- Who moved the inputs into the AI's environment?
- Who decided where the finished artifact belonged?
- Who moved the artifact there?
- What would change if the project contained 40 files? 400?

The lesson is not that cloud ChatGPT cannot do the task. It can.

The lesson is that a conversation can only reason over the project state made available to it, while an on-disk worker can inspect the environment where that state actually lives.
