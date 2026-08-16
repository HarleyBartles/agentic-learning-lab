# Exercise 1 — Change the instructions

Use one project and one worker environment for this whole lab.

Start with a fresh worker session rooted at `project/`.

Ask exactly:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Read the result without improving it yet.

Now suppose the facts are useful but you want this kind of briefing to be much tighter every time: four short bullets, no heading or preamble, prioritising time, access, safety, and the volunteer lead's first action.

Do **not** put those requirements only in your next prompt.

Ask the worker to make that a standing project rule by editing `AGENTS.md`. Leave the change uncommitted.

Inspect the Git diff.

Before rerunning the task, answer:

- What changed?
- What stayed the same?
- Did we swap model?
- Did we swap harness?
- Did we change the task itself?

Start a fresh worker session in the same `project/` and use the original request again:

> Read `tasks/volunteer-lead-brief.md` and do the task.

Compare the two outputs.

Keep this line:

> **Same model does not mean same behaviour.**

You changed a durable instruction around the model, not the job the model was asked to do.
