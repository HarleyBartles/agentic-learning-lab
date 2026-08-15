# Module 3 — The project has a home

Approximate duration: 1 hour.

Status: **Exercise 1 promoted into `labs/03-project-has-a-home/`; remainder still in development**.

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

## Exercise 1

Exercise 1 is now implemented in:

`labs/03-project-has-a-home/`

It uses a fictional Repair Café planning project to demonstrate that a local agent does not magically remember earlier conversations merely because it works on disk.

The learner makes a consequential project decision while explicitly forbidding file mutations, loses that conversation, then watches a fresh local agent reconstruct the durable project state without the missing decision. The learner then recovers and persists the decision and verifies it with a third fresh agent.

Key lines earned by the exercise:

> Decisions that exist only in conversation are tears in the rain.

> The agent didn't remember. The project carried the result forward.

> Inspect what survived. Identify what is missing. Persist it. Verify with a fresh agent.

Detailed learner choreography, facilitator checks, and project fixture content now belong in the Lab 3 scaffold rather than this module planning file.

## Exercise 2 — direction still open

The original direction was to help the learner classify what belongs in durable project state:

- Is this something I am saying to the agent right now, or something the project itself needs to know tomorrow?
- Is this source material?
- Is this a current decision?
- Is this working material?
- Is this a result?

Exercise 1 now earns much of the basic persistence lesson directly, so Exercise 2 should not simply repeat the same move. Its detailed mechanism is not yet pinned.

## Exercise 3 — Separate the project from the route into it

Do not turn this back into another cloud-versus-local comparison. Use discussion or a light practical check to separate three facts:

> The project exists.

> The project is stored somewhere.

> An agent currently has a route to it.

Useful questions:

> If the project folder disappeared but an AI vaguely remembered what we were doing, would we still have the project?

> If the project still existed but we opened a completely fresh conversation, would we still have the project?

> If the project were stored remotely but no current agent had access to it, would the project itself still exist?

The intended answer is that the project is independent of the particular conversation or agent currently accessing it.

## End with a source-of-truth itch

Finish with a small unresolved tension rather than another full lesson.

Place or discover two harmless project notes which disagree about a decision and ask:

> If the project is the durable state, what happens when the project itself disagrees with itself?

Do not solve governance here. The purpose is to create demand for later work on authority, source of truth, and verification.

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
