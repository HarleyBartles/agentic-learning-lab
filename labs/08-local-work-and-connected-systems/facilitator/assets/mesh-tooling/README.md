# Lab 8 facilitator mesh tooling

These files are facilitator-owned reveal assets. Keep them outside the learner worker's root until Exercise 4.

They are not prerequisites for the learner and are not a coding exercise.

## Files

- `generate_index_mesh.py` — deterministic/idempotent index generator for rebuilding the complete navigation mesh from represented Git project state.
- `test_generate_index_mesh.py` — executable contract tests for regeneration, idempotence, stale detection, obsolete-index removal, and ignoring unrelated untracked local drafts.

## Lab 8 teaching contract

The learner-facing lesson is deliberately smaller than the tool's full interface.

The worker should be given the generator and asked to regenerate the complete mesh. The learner should observe that a derived navigational representation can be reproduced from source state instead of being hand-maintained.

Earn:

> **Do not hand-maintain derived navigation when the project can regenerate it deterministically.**

> **If a representation is important enough for agents to rely on, make it reproducible.**

The generator is intentionally a reasonably behaved CLI. It exposes `--help`, a non-mutating inspection path, explicit mutation, useful exit status, deterministic output, and idempotent regeneration.

Do **not** turn those interface details into the Lab 8 lesson. They are preserved as a future Course 2 breadcrumb about why self-describing, managed CLIs are particularly useful to agents.

## Deliberately unsolved here

Do not install or supply a Git hook in Lab 8.

Do not add CI enforcement.

Do not add standing workflow instructions telling the worker to regenerate before every commit.

Lab 8 should leave this true:

```text
generator exists
+
worker can use it
!=
worker will remember to use it at the right lifecycle point
```

A later module should deliberately let the mesh go stale despite the generator being available, then ask why the human is still repeatedly reminding the worker to run it.

That is the future cash-in for:

> **Things you keep telling the agent need to become things you stop telling the agent.**