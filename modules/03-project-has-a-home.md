# Module 3 — The project has a home

Approximate duration: 1 hour.

Status: **Exercises 1, 2, and 3 promoted into `labs/03-project-has-a-home/`**.

## Core idea

Labs 1 and 2 have already paid the cost of comparing cloud and local access. From this point onward, cloud versus local should stop being the organising axis of the curriculum. Later differences can be highlighted when useful, but the environment should be chosen to serve the lesson rather than to keep proving the comparison.

Lab 3 changes the question from:

> Which agent can see the project?

to:

> Where does this project live when nobody is currently talking to an AI about it?

The learner should leave with the idea that a project has a deliberate home containing the durable state needed to pick the work up again, independent of any particular conversation or agent.

Useful formulations:

> The conversation is not the project. The project is the project.

> Context is temporary. State is persistent.

> Memory is context. Files are state.

The last line is deliberately simplified for this stage. The deeper point is that information which matters to the ongoing project should live in a durable, inspectable project surface rather than depending on a particular conversation continuing to exist.

## Exercise 1 — Tears in the rain

Exercise 1 uses the Repair Café project to show that a local agent does not magically remember earlier conversations merely because it works on disk. The learner makes a consequential decision while the agent is intentionally non-mutating, loses that conversation, reconstructs the project without the missing decision, then deliberately allows mutation, persists the decision, and verifies it with a fresh agent.

The implementation uses layered controls rather than relying on one oversized prompt:

- the learner can speak naturally and frame the interaction as discussion;
- project-local `AGENTS.md` defines discussion-only operating doctrine;
- where available, the chosen harness supplies an actual read-only or equivalent non-mutation boundary.

Keep the conceptual distinction available for later teaching:

> Instructions describe the intended boundary. Permissions enforce the possible boundary.

The exact control may vary across Codex desktop, Codex CLI/IDE, Devin Desktop, or another agentic environment. Keep the core Exercise 1 experiment on one surface so the persistence result is not confounded by changing harnesses mid-run. Different surfaces can be mentioned lightly as examples of different capability and risk profiles, then explored properly in a later harness-focused lab.

Key lines:

> Decisions that exist only in conversation are tears in the rain.

> The agent didn't remember. The project carried the result forward.

> Inspect what survived. Identify what is missing. Persist it. Verify with a fresh agent.

## Exercise 2 — Don't make the agent guess

Exercise 2 uses Repair Café meeting minutes to teach the complementary problem: persistence can itself be sloppy if the agent is forced to guess what conversation material deserves authority in the project.

The learner compares three runs over the same minutes:

1. vague `save the important stuff` delegation;
2. verbatim evidence preservation without promoting anything into current project state;
3. verbatim evidence plus explicit human direction about which points are confirmed project state and which remain unresolved.

Runs 1 and 2 are left uncommitted, inspected, and discarded by the learner's agent. The good Run 3 state is inspected, committed, and pushed, then reconstructed once by a fresh agent as the final proof.

Key lines:

> Preserve evidence honestly. Promote meaning deliberately.

> Don't make the agent guess which meeting chatter became project truth.

## Exercise 3 — Which truth wins?

Exercise 3 makes durable project state disagree through believable, correctly scoped work.

Agent 1 creates and commits a visitor information sheet from the current project state.

Agent 2 later receives a confirmed time change but is deliberately instructed to update only `notes/current-decisions.md`, without searching the project for other copies of the old time. It commits and pushes that narrowly scoped update.

Agent 3 then receives a simple factual question:

> What time does the Repair Café start?

The learner asks it to show the project evidence, identify which truth is authoritative, and explain how it decided that truth wins.

The point is not to force a predetermined answer. The point is to expose whether the agent discovered an explicit project authority rule or inferred one from filenames, recency, output purpose, or other clues.

Key lines:

> Persisted does not mean current.

> Durable does not automatically mean authoritative.

The unresolved question is intentional:

> When the project disagrees with itself, how does an agent know what to trust?

Do not solve that governance problem here. Lab 3 should create the demand that the later source-of-truth material will answer.

Detailed learner choreography, facilitator checks, and fixture content belong in the Lab 3 scaffold rather than this module planning file.

## Closing distinction

A useful final discussion can still separate these three facts without turning them into another exercise:

> The project exists.

> The project is stored somewhere.

> An agent currently has a route to it.

The project remains independent of the particular conversation or agent currently accessing it.

## What this lab is not

This is not a lesson about folder structures.

It is not another local-versus-cloud comparison.

It is not yet a Git lesson, full source-of-truth system, knowledge-management taxonomy, RAG design, or elaborate instruction architecture.

The project should remain understandable at a glance.

## Curriculum handoff

```text
Lab 1
An agent can work where the project state lives.

Lab 2
"Has access to the project" is incomplete;
different surfaces expose different state and capabilities.

Lab 3
The project needs durable state with a deliberate home.
Conversation does not automatically become state.
Durable state can still drift and disagree.

Lab 4
Now that project state matters:
how do we change it fearlessly and recover when we screw it up?
```

Lab 3 should therefore earn the right for the source-control lab to treat project state as something worth preserving, inspecting, changing, and recovering, while leaving a later source-of-truth lab with a concrete authority problem to solve.
