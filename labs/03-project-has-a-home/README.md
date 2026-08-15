# Lab 3 — The project has a home

Status: **Exercise 1 scaffolded; remainder in development**.

Labs 1 and 2 established that agents can work through different access surfaces. Lab 3 stops treating cloud versus local as the organising question and asks something more basic:

> Where does the project live when nobody is currently talking to an AI about it?

The learner should leave with the idea that important project state must survive independently of any particular conversation or agent.

Exercise 1 is ready to run:

1. `learner/01-tears-in-the-rain.md` — make an important project decision in conversation while explicitly forbidding file changes, simulate losing that conversation, recover from the project, persist the missing decision, then prove with another fresh agent that the project now carries it forward.

The shared working fixture lives in `project/` and is a fictional community Repair Café pilot. The on-disk agent should be rooted at that folder rather than at the teaching lab so it sees the project rather than the exercise choreography.

The memorable lesson is:

> Decisions that exist only in conversation are tears in the rain.

The operational version is:

> Important project knowledge should survive the conversation that created it.

Exercises 2 and later Lab 3 material are still being designed and should not be inferred from this scaffold.
