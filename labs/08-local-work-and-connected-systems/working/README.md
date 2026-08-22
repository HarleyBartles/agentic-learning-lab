# Lab 8 working environment

This folder is the bounded agent workspace for the local exercises.

Start the local worker in `environment/`, not at the lab root.

The environment intentionally contains three different kinds of project surface:

- scoped `AGENTS.md` instructions;
- an `INDEX.md` navigation mesh;
- filesystem state that is accessible even when the mesh does not point to it.

Do not repair or complete the index mesh before the learner runs the blind-spot exercise.

Do not copy the facilitator's generator or pre-commit tooling into `environment/` before the learner reaches the `keep the mesh trustworthy` reveal.

The initial omission is deliberate experimental state, not a repository defect. Exercise 4 deliberately replaces that hand-maintained state with generated navigation and a local pre-commit freshness mechanism.