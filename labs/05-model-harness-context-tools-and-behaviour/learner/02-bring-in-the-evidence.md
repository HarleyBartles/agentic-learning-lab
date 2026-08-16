# Exercise 2 — Bring in the evidence

Stay in the same evolving project.

Ask:

> Read `tasks/venue-layout.md` and answer it from project evidence you can actually inspect.

If the worker says it lacks the facts needed to decide, that is useful evidence. Do not reward confident guessing.

Now look outside the worker's project at the course material in:

`toolbox/venue-constraints.md`

The information exists on your machine, but it is outside the worker's assigned project.

Copy it with your editor or file browser into:

`project/reference/venue-constraints.md`

No coding is required.

Inspect the working-tree state:

`git status --short`

The new file is untracked, so a normal `git diff` will not display its contents. Open the copied file directly if you want to inspect what entered the project.

Ask yourself:

- Did the venue facts exist before?
- Could this worker inspect them before?
- What did you just change about the worker's environment?
- Why is putting the evidence in durable project state different from telling one conversation the answer?

Start a fresh worker context in the same project and repeat exactly:

> Read `tasks/venue-layout.md` and answer it from project evidence you can actually inspect.

Compare the justified conclusions.

Keep this line:

> **Missing evidence is not evidence of a weaker model.**
