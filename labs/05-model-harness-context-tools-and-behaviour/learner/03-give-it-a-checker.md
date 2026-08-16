# Exercise 3 — Give it a checker

The project already contains a proposed volunteer schedule and its constraints.

Ask:

> Read the schedule constraints and volunteer schedule. Give me an initial assessment of whether the schedule works. Do not use or create a checker. Label the conclusion provisional.

Treat the answer as provisional even if it sounds confident.

Now ask yourself:

> What could we give this worker that would let it check the schedule reproducibly?

The course includes a prepared checker outside the worker's project:

`toolbox/validate_schedule.py`

You do not need to understand or edit the Python. Copy the supplied file into:

`project/tools/validate_schedule.py`

Inspect the working-tree state:

`git status --short`

The checker is an untracked addition, so normal `git diff` will not display it.

Before running it, answer:

- Did the model change?
- Did the schedule change?
- What new project-specific capability is now available?
- What does the harness already provide that lets the worker execute that tool?

Now ask the same worker that made the provisional assessment:

> Run the prepared schedule validator and compare its evidence with your provisional assessment. Tell me what changed in your confidence.

Keep this distinction:

> **A plausible answer and a verified answer are different states of knowledge.**
