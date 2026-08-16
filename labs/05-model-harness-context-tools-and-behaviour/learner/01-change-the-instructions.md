# Exercise 1 — Change the instructions

Use one project and one worker environment for this whole lab.

Start with a fresh worker session rooted at `project/`.

Ask exactly:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Read the result without improving it yet.

Now suppose the facts are useful but you want this kind of briefing to be much tighter every time: four short bullets, no heading or preamble, prioritising time, access, safety, and the volunteer lead's first action.

At this point, open `AGENTS.md` yourself with the facilitator.

This is the standing project-instruction file. You have been working inside projects with files like this since Lab 1; until now they were mostly part of the prepared environment.

Read it briefly together. Do not try to learn every rule or instruction-precedence detail.

At the bottom of the file, add:

```md
## Volunteer-lead briefings

- Write volunteer-lead operational briefings as exactly four bullets.
- Do not add a heading, preamble, or closing sentence.
- Keep each bullet to 24 words or fewer.
- Prioritise time, access, safety, and the volunteer lead's first action.
```

You are editing this by hand. Do not ask the current agent to modify its own operating instructions.

Inspect:

`git diff -- AGENTS.md`

Before rerunning the task, answer:

- What changed?
- What stayed the same?
- Did we swap model?
- Did we swap harness?
- Did we change the task itself?

Now close the original agent conversation and start a **fresh agent context** in the same `project/`.

Use the original request again:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Compare the two outputs.

Keep these lines:

> **Same model does not mean same behaviour.**

> **You have been benefiting from project instructions since the beginning. Now you have touched the lever yourself.**
