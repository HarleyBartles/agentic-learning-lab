# Module 3 — The project has a home

Approximate duration: 1 hour.

Status: **direction pinned / not yet expanded into a lab**.

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

## Broad lab shape

### Exercise 1 — Important knowledge exists only in the conversation

Start with a small, slightly half-formed project containing some source material, loose notes, working material, and an output.

Have the learner do a little useful work with an agent. During the conversation, make an important project decision which is **not** written back into the project.

Nothing needs to fail dramatically. The project should simply end the exchange with some of its current state living in files and one meaningful decision living only in conversational context.

Then end that conversation.

Start a fresh agent session with access to the same project and ask something like:

> Pick this project up. Tell me where things currently stand and what we decided to do next.

The fresh agent can reconstruct what exists in durable project state but cannot recover the decision which existed only in the previous conversation.

The observation to earn is:

> A conversation can contain project knowledge without that knowledge becoming project state.

### Exercise 2 — Give the project a deliberate home

Repeat the idea, but this time let the learner decide which information should survive beyond the conversation and ask the agent to record it somewhere sensible in the project.

A simple project shape may be useful, for example:

```text
project/
    README.md
    source/
    notes/
    working/
    output/
```

Do not teach this structure as doctrine. The folder names are scenery. The real exercise is classification:

- Is this something I am saying to the agent right now, or something the project itself needs to know tomorrow?
- Is this source material?
- Is this a current decision?
- Is this working material?
- Is this a result?

Then start another fresh session and ask:

> Pick up the project and tell me where we are.

This time the new session should be able to reconstruct the important state because the project itself contains it.

The contrast is:

```text
important fact only in conversation
        ↓
fresh conversation
        ↓
fact disappears from usable project state

important fact recorded in project
        ↓
fresh conversation / different agent
        ↓
project can be reconstructed
```

### Exercise 3 — Separate the project from the route into it

Do not turn this back into another cloud-versus-local comparison. Use discussion or a very light practical check to separate three facts which Labs 1 and 2 have now made meaningful:

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

The intended progression is:

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

Lab 3 should therefore earn the right for the source-control lab to treat project state as something worth preserving, inspecting, changing, and recovering.
