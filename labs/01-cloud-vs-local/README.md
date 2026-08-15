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

## Attempt A — Cloud ChatGPT

Use ordinary cloud ChatGPT.

ChatGPT cannot see this project folder. Use it however you want.

You decide how the source material gets into ChatGPT and how the finished result gets back into `output/mission-brief.md`.

There is no required upload, download, or copy/paste technique. The only success condition is the finished local file.

When you have succeeded, stop and notice what work you performed simply to move project information into the AI's environment and move the result back out.

Then delete `output/mission-brief.md` so the mission is back at its starting state.

## Attempt B — Local Codex

Now use Codex operating locally in this project.

Give it only this goal:

> Complete the exercise in `labs/01-cloud-vs-local`.

Let it inspect the exercise and work out what to do.

The success condition is unchanged: `output/mission-brief.md` must exist locally and satisfy the mission requirements.

## Compare

Do not compare the two attempts mainly on writing quality.

Compare the transport work:

- Who discovered the inputs?
- Who moved the inputs into the AI's environment?
- Who decided where the finished artifact belonged?
- Who moved the artifact there?
- What would change if the project contained 40 files? 400?

The point is not that cloud ChatGPT failed. The point is to experience the difference between bringing a project to a conversation and letting an agent work where the project already lives.
