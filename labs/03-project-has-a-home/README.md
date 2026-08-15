# Lab 3 — The project has a home

Status: **Exercises 1 and 2 scaffolded; remainder in development**.

Labs 1 and 2 established that agents can work through different access surfaces. Lab 3 stops treating cloud versus local as the organising question and asks something more basic:

> Where does the project live when nobody is currently talking to an AI about it?

The learner should leave with the idea that important project state must survive independently of any particular conversation or agent, and that conversational material should become durable project state deliberately rather than by accident.

The current exercises are:

1. `learner/01-tears-in-the-rain.md` — make an important project decision in conversation while explicitly forbidding file changes, simulate losing that conversation, recover from the project, persist the missing decision, then prove with another fresh agent that the project now carries it forward.
2. `learner/02-meeting-minutes.md` — run the same Repair Café meeting minutes through three different persistence instructions: vague `important stuff`, verbatim evidence only, then verbatim evidence plus explicit human authority about which points become current project state. Inspect and discard the first two uncommitted runs; keep, commit, and push the third.

The shared working fixture lives in `project/` and is a fictional community Repair Café pilot. The on-disk agent should be rooted at that folder rather than at the teaching lab so it sees the project rather than the exercise choreography.

Exercise 1 earns:

> Decisions that exist only in conversation are tears in the rain.

> Important project knowledge should survive the conversation that created it.

Exercise 2 adds:

> Preserve evidence honestly. Promote meaning deliberately.

> Don't make the agent guess which meeting chatter became project truth.

Later Lab 3 material is still being designed and should not be inferred from this scaffold.
