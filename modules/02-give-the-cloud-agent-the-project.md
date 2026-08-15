# Module 2 — Give the cloud agent the project

Approximate duration: 1 hour.

Status: fluid / next expansion target.

## Core idea

Lab 1 established that an agent which cannot see the project surface cannot know what project state is missing from the context the human supplied.

Module 2 changes one important variable: the facilitator gives cloud ChatGPT access to the learning repository through the GitHub connector.

The learner should experience two things in order:

1. giving the cloud agent a bridge to the project removes much of the manual context transport seen in Lab 1;
2. access through a connector is useful, but it is not necessarily the same access an on-disk agent has to a native working copy.

The lesson is not about connector implementation. The facilitator configures access in advance; the learner experiences the capability.

## Starting point from Lab 1

Lab 1 gave us:

> If the agent cannot see the surface, it cannot see what is missing from that surface.

Module 2 asks:

> What changes when we let the cloud agent see the project too?

The first result should be positive. Cloud ChatGPT should now be able to answer useful project questions without the learner manually uploading or pasting the repository files.

Do not frame this as a trick or as evidence that the Lab 1 comparison was wrong. The environment has changed.

## Suggested session shape

### 0–15 minutes — Give the cloud agent the missing bridge

Quietly re-enable the GitHub connector for the learning repository before the exercise.

Return to a project task similar to the kind of work used in Lab 1, but do not upload project files manually.

Let the learner discover that cloud ChatGPT can now retrieve project state itself.

A useful observation is:

> Access changes the problem.

### 15–30 minutes — Let connector access work well

Use focused repository questions or a small bounded task where the required information is ordinary text in the repository.

Both the cloud agent through GitHub and the on-disk agent should be capable of succeeding.

The learner should leave this section with a correction to any overly broad conclusion from Lab 1:

> A cloud agent can work from project state directly when it has an appropriate bridge to that state.

### 30–50 minutes — Compare the shape of access

Now give both environments tasks that require broader inspection or a capability that may not be exposed through the connector.

Useful comparisons include:

- focused retrieval versus broad exploration;
- following references across many files;
- inspecting local generated artifacts;
- using local tools;
- inspecting an information-bearing image or other binary asset when the connector does not expose the underlying content in a usable form.

The exact exercises should be verified against the real connector capabilities before the lab is locked. Do not manufacture a limitation that the current connector no longer has.

The general lesson is:

> Something can exist in the underlying project and still be invisible to an agent through its current access surface.

and:

> Connectivity is not environmental parity.

### 50–60 minutes — Synthesize without teaching connector internals

Compare the two routes to the same project:

```text
cloud agent
    |
    | connector
    v
GitHub project surface

on-disk agent
    |
    v
native working copy + local tools
```

A useful distinction to preserve for later is:

> Retrieval asks for something. Exploration discovers what is there.

Neither route is universally better. The important question is what project surface the agent can actually observe and what capabilities that surface exposes.

## Facilitator setup

Keep the machinery invisible in this module.

The facilitator should enable the repository connector and any required permissions before the relevant exercise. Do not turn the session into a lesson about MCP, APIs, connector schemas, authentication, indexing, or configuration screens.

Those are later topics.

The learner-facing experience should simply be that the same cloud agent which could not inspect the repository in Lab 1 can now do so.

## Discussion prompts

- What manual work from Lab 1 disappeared once ChatGPT could reach the repository?
- Does `the project contains this file` automatically mean `the agent can observe everything inside that file`?
- What can the local worker discover by exploring the working copy that a focused connector request may not expose as naturally?
- When is connector access entirely sufficient?
- What would make a different project surface a better home for some kinds of information?

## Connection forward

This module deliberately leaves several questions open:

- What exactly is the persistent project that both environments are reaching?
- Why keep project state in a repository at all?
- What does Git add beyond a folder full of files?
- What other project homes exist besides repositories?
- How do we choose and compose access surfaces for a real project?

Those questions belong to later labs.

## Do not teach yet

Do not teach connector protocol semantics, MCP internals, detailed Git workflows, alternate project stores, skills, or elaborate permission models here.

Change one variable from Lab 1 and let the learner experience the consequence:

> The cloud agent can now see the project — but the way it sees the project still matters.
