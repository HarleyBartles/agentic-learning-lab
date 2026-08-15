# Lab 3 — The project has a home

Status: **Exercises 1, 2, and 3 scaffolded and ready to run**.

Labs 1 and 2 established that agents can work through different access surfaces. Lab 3 stops treating cloud versus local as the organising question and asks something more basic:

> Where does the project live when nobody is currently talking to an AI about it?

The learner should leave with the idea that important project state must survive independently of any particular conversation or agent, that conversational material should become durable project state deliberately rather than by accident, and that durable artifacts can still disagree.

The exercises are:

1. `learner/01-tears-in-the-rain.md` — discuss and make an important Repair Café decision while the agent is operating read-only, simulate losing that conversation, reconstruct the project without the missing decision, then explicitly re-enable mutation, persist the decision, and prove it with a fresh agent.
2. `learner/02-meeting-minutes.md` — run the same Repair Café meeting minutes through three different persistence instructions: vague `important stuff`, verbatim evidence only, then verbatim evidence plus explicit human authority about which points become current project state. Inspect and discard the first two uncommitted runs; keep, commit, and push the third.
3. `learner/03-which-truth-wins.md` — have one fresh agent produce a visitor information sheet, a second fresh agent perform a deliberately narrow time update only in `notes/current-decisions.md`, then ask a third fresh agent what time the event starts, which durable artifact is authoritative, and how it decided.

The shared working fixture lives in `project/` and is a fictional community Repair Café pilot. The on-disk agent should be rooted at that folder rather than at the teaching lab so it sees the project rather than the exercise choreography.

Exercise 1 deliberately uses more than one safety layer:

- natural user intent such as `we're just discussing`;
- standing project doctrine in `project/AGENTS.md` which defines discussion-only behaviour;
- an enforced read-only or equivalent non-mutation mode where the chosen harness provides one.

The distinction matters even though it is only lightly surfaced to the learner here:

> Instructions describe the intended boundary. Permissions enforce the possible boundary.

The exact control may look different across Codex desktop, Codex CLI/IDE, Devin Desktop, or another agentic environment. Keep the main Exercise 1 experiment on one surface so the persistence result stays clean, but use the variation as a small reminder that different harnesses expose different benefits, capabilities, and risk controls.

Exercise 1 earns:

> Decisions that exist only in conversation are tears in the rain.

> Important project knowledge should survive the conversation that created it.

Exercise 2 adds:

> Preserve evidence honestly. Promote meaning deliberately.

> Don't make the agent guess which meeting chatter became project truth.

Exercise 3 adds:

> Persisted does not mean current.

> Durable does not automatically mean authoritative.

And leaves one deliberate question unresolved:

> When the project disagrees with itself, how does an agent know what to trust?
