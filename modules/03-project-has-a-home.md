# Module 3 — The project has a home

Approximate duration: 1 hour.

Status: **Exercises 1 and 2 promoted into `labs/03-project-has-a-home/`; remainder still in development**.

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

## Exercises 1 and 2

Exercises 1 and 2 are now implemented in:

`labs/03-project-has-a-home/`

Exercise 1 uses the Repair Café project to show that a local agent does not magically remember earlier conversations merely because it works on disk. The learner makes a consequential decision while explicitly forbidding file mutations, loses that conversation, recovers the missing state, persists it, and verifies it with a fresh agent.

Key lines:

> Decisions that exist only in conversation are tears in the rain.

> The agent didn't remember. The project carried the result forward.

> Inspect what survived. Identify what is missing. Persist it. Verify with a fresh agent.

Exercise 2 uses Repair Café meeting minutes to teach the complementary problem: persistence can itself be sloppy if the agent is forced to guess what conversation material deserves authority in the project.

The learner compares three runs over the same minutes:

1. vague `save the important stuff` delegation;
2. verbatim evidence preservation without promoting anything into current project state;
3. verbatim evidence plus explicit human direction about which points are confirmed project state and which remain unresolved.

Runs 1 and 2 are left uncommitted, inspected, and discarded by the learner's agent. The good Run 3 state is inspected, committed, and pushed, then reconstructed once by a fresh agent as the final proof.

Key lines:

> Preserve evidence honestly. Promote meaning deliberately.

> Don't make the agent guess which meeting chatter became project truth.

Detailed learner choreography, facilitator checks, and fixture content belong in the Lab 3 scaffold rather than this module planning file.

## Remaining Lab 3 direction

The lab still needs a final exercise or closing move that advances beyond basic persistence and deliberate promotion without prematurely teaching the later source-control or source-of-truth modules.

One useful unresolved tension remains:

> If the project is the durable state, what happens when the project itself disagrees with itself?

A small conflict between two durable artifacts may be enough to create demand for later authority and source-of-truth work. Do not solve the full governance problem here.

The earlier idea of separating these three facts can likely be retained as closing discussion rather than a full exercise:

> The project exists.

> The project is stored somewhere.

> An agent currently has a route to it.

## What this lab is not

This is not a lesson about folder structures.

It is not another local-versus-cloud comparison.

It is not yet a Git lesson, source-of-truth system, knowledge-management taxonomy, RAG design, or elaborate instruction architecture.

The project should remain understandable at a glance.

## Curriculum handoff

```text
Lab 1
An agent can work where the project state lives.

Lab 2
"Has access to the project" is incomplete;
different surfaces expose different state and capabilities.

Lab 3
So what actually is the project?
It is durable state with a deliberate home,
independent of any particular conversation or agent.

Lab 4
Now that the project has durable state:
how do we change it fearlessly and recover when we screw it up?
```

Lab 3 should earn the right for the source-control lab to treat project state as something worth preserving, inspecting, changing, and recovering.
