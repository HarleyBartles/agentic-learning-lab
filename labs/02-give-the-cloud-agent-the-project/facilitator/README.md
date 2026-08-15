# Lab 2 facilitator guide — Give the cloud agent the project

Approximate duration: 1 hour.

Status: **scaffolded / in active design**.

## Learning goal

Lab 1 established:

> If an agent cannot see the project surface, it cannot see what is missing from the context supplied to it.

Lab 2 changes one variable: cloud ChatGPT is given access to this repository through the GitHub connector.

The learner should experience that connector access genuinely removes much of the manual context transport from Lab 1, while also discovering that `has access to the project` is not a precise enough description on its own.

By the end of the lab, the learner should naturally start asking:

- Which state of the project is this agent looking at?
- Which parts of the working environment are actually on this surface?
- Can the agent perceive the representation needed for this task?
- What is it allowed to change through this surface?

Do not present those four questions as a lecture at the start. Let the exercises create them.

## The project fixture

All exercises happen in this repository under:

`labs/02-give-the-cloud-agent-the-project/project/`

The fixture is a small event-planning project for Riverside Hall. It includes:

- tracked text describing event setup and operational facts;
- a tracked venue plan image containing information that only exists visually;
- a tracked description of a local operational attendee database;
- a tracked reusable SQLite schema;
- a `.gitignore` rule excluding `local/`, where the operational database will be created during Exercise 3;
- a tracked disposable `scratch/` directory used for the deletion exercise;
- `AGENTS.md`, containing standing instructions for the on-disk worker.

This is deliberately one repository, not a second exercise repository.

## Before the session

### Cloud environment

Re-enable the GitHub connector for `HarleyBartles/agentic-learning-lab` before Lab 2.

The learner does not configure the connector. The visible change from Lab 1 is simply:

> ChatGPT can now reach the repository.

Use a fresh conversation for each exercise or each controlled run where stale conversational context could hide the observed difference.

Do not explain MCP, schemas, indexing, authentication, or connector implementation in this lab.

### Local environment

Use the learner's local checkout of this same repository.

Before the lab:

1. ensure the checkout starts synchronized with `main`;
2. ensure `project/local/attendees.db` does **not** exist;
3. confirm `project/local/` is ignored by Git;
4. prepare the on-disk agent with a working root at `labs/02-give-the-cloud-agent-the-project/project/`;
5. ensure the agent can inspect common image formats and use SQLite locally;
6. keep the `scratch/` content disposable;
7. confirm the worker reads and follows `project/AGENTS.md`.

The repository contains the reusable database schema in `project/local-setup/schema.sql`, but no attendee records. The learner will supply those records directly to the on-disk worker during Exercise 3, and the worker will create the operational database locally.

`AGENTS.md` is deliberately visible in the project. It is not part of the lesson yet, but it does not need to be hidden. If the learner asks what it is, explain briefly that it contains standing working instructions for the local agent so the exercise behaves consistently, and that a later lab will examine how project instructions work and where they belong.

Do not teach Git synchronization or SQLite setup mechanics while preparing this lab. They are facilitator plumbing here.

### Project operating instruction for Exercise 3

`project/AGENTS.md` contains the rule which keeps local operational database records from leaking onto the GitHub surface.

Its important intent is:

> Treat data in `local/` as local operational data. Never publish, reproduce, summarise, quote, encode, or otherwise leak database record contents into tracked files, generated receipts, commit messages, issues, pull requests, or other remote repository surfaces. Publish only project material appropriate for source control.

It also requires the worker to inspect proposed published changes and the commit message before pushing work involving local operational data.

This is experimental hygiene, not the Lab 2 lesson. Without it, an otherwise helpful worker might create a receipt, summary, log, commit message, or other tracked artifact that accidentally copies the attendee records onto GitHub and destroys the access-boundary experiment.

Do not unpack the instruction mechanism unless the learner asks. A later lab can explicitly return to `AGENTS.md`, show that ignored files alone do not prevent an agent from copying their contents into source control, and introduce project rules, pre-publication checks, scanning, or related mechanisms when those concepts have been earned.

The instruction must not teach the worker the attendee values or the answer to the later cloud question. It only defines what information is permitted to cross from local operational state into remote source-controlled state.

## Exercise 1 — Which state are you looking at?

Use `project/source/supplier.md`.

The exercise has three runs.

### Run A — synchronized baseline

Start with local and GitHub both saying the supplier arrival time is `09:00`.

Ask both agents the same question:

> What time is the supplier arriving at Riverside Hall?

Both should answer `09:00`.

The important first observation is positive:

> The cloud agent can now use the project directly. Lab 1's manual file transport is no longer necessary for this kind of task.

### Run B — local ahead

Change the local working copy of `source/supplier.md` to `10:30` without publishing that change.

Ask both agents again in fresh conversations.

Expected result:

- local agent: `10:30`;
- cloud agent through GitHub: `09:00`.

Do not teach `dirty working tree`, commit, push, or remote terminology yet. Just notice that two valid access routes can be observing different states.

### Run C — remote changes while local work remains

Do **not** restore or discard the local `10:30` change from Run B.

Ask the cloud agent, through its GitHub write capability, to change the supplier arrival time in the repository to `11:15`.

Let any normal connector confirmation/safety flow occur naturally.

Do **not** update the learner's local checkout yet.

Ask both agents again.

Expected visible result:

- cloud agent: `11:15`, because that is now the repository state it can observe;
- local agent: `10:30`, because the learner's working file still contains the uncommitted local edit.

There is also a third useful state underneath the local edit: the local checkout's previously saved version still corresponds to the earlier repository value, `09:00`.

Do not teach the mechanics yet. Simply make the three states visible conceptually:

```text
remote repository state        11:15
local working file             10:30
local saved baseline beneath   09:00
```

This is stronger than resetting between runs because the learner can see that `the project` is not a single magical object with one universally observed value. Different access surfaces can expose different states at the same time.

After the observation, resynchronize and clean the local checkout before the next exercise.

## Exercise 2 — Can you see it?

Use `project/source/venue-plan.png`.

The image contains a fact that is intentionally not duplicated in text: which labelled table is closest to the accessible entrance.

Run the same question three ways:

1. cloud ChatGPT using only the GitHub connector;
2. the local multimodal agent inspecting the repository file directly;
3. cloud ChatGPT with the same image provided directly in chat.

Question:

> According to the venue plan, which labelled table is closest to the accessible entrance?

The expected teaching pattern is:

- the GitHub connector can establish that the image belongs to the project, but if the current connector does not expose usable image pixels, the cloud agent cannot answer from that route;
- the local multimodal worker can inspect the file directly and answer;
- the same cloud model can answer when the image itself is directly visible in the conversation.

**Verify the real connector behaviour immediately before running the lab.** If GitHub image/pixel retrieval becomes supported, redesign this exercise around another representation the connector genuinely does not expose. Do not fake a limitation.

The observation is:

> The information can exist in an accessible project while the current access route still fails to expose the representation needed for the task.

Do not turn this into an explanation of binary transport, connector internals, or image APIs.

## Exercise 3 — Is the repository the whole project?

This exercise starts with no attendee database on disk.

The learner chooses five fictional attendee records, including name, confirmation state, and meal choice, and supplies those values directly to the on-disk worker. Those values must not already exist in a tracked file or cloud conversation.

The learner asks the local worker to set up the attendee database using those records, create any reusable database structure that properly belongs in source control, and push the appropriate project work when finished.

Expected local result:

- `project/local/attendees.db` is created and contains the records;
- the database remains ignored and is not published;
- reusable schema or setup material can remain tracked;
- the worker can commit/push appropriate source-controlled work without leaking any attendee values into tracked files, commit messages, receipts, logs, issues, PRs, or other remote surfaces.

Then start a fresh cloud ChatGPT conversation and ask it, using only repository access, to list the attendee records the on-disk worker just captured.

The learner has just watched the worker create the state and successfully publish appropriate project work, so the impossibility should feel concrete rather than staged.

Expected cloud result:

- it can discover that the project uses `local/attendees.db`;
- it can inspect the reusable schema and repository material;
- it cannot retrieve the actual attendee records because those records never crossed onto the GitHub surface.

Ask the on-disk agent for the same records and let it query the database directly.

This is not a fake limitation introduced purely for the lab. Operational database contents commonly do not live in source control. Source control often contains schema, migrations, setup/test material, and code which uses the database, while live mutable database state is managed separately. Reasons include privacy, mutable/environment-specific state, poor binary diff/merge behaviour, and practical repository size limits as databases grow.

Do not turn that side note into a database-policy lesson. The point is simply:

> Publishing the source-controlled work does not necessarily publish every piece of state in the project's working environment.

## Exercise 4 — What can this surface do?

Use only:

`project/scratch/`

The directory contains deliberately disposable files.

First ask the local agent:

> Delete everything in `scratch/`.

With ordinary local filesystem permissions, this should happen immediately.

Restore the scratch fixture.

Then ask the cloud agent through GitHub to perform the analogous deletion against the repository.

Observe the actual current connector behaviour. Depending on the enabled write surface and safety policy, the operation may be unavailable, may require explicit user confirmation, or may permit only bounded mutations.

The lesson is not:

> Cloud is safe and local is dangerous.

A local harness can also be configured with stronger permissions, approvals, or sandboxing.

The observation is:

> The access surface carries not only visibility but also permissions and guardrails.

Keep deletion strictly inside the disposable scratch fixture.

## Final reflection

Ask:

> At the beginning of the lab I kept saying both agents had access to the project. Does that sentence feel precise enough now?

Let the learner supply the missing qualifiers.

Useful follow-up prompts:

- Which copy or state?
- Which files and runtime state actually exist on that surface?
- Can it perceive the information in the form needed for this task?
- Can it modify the project through that route?
- What approvals or safety boundaries sit in the way?

A compact facilitator synthesis is:

> Project access is shaped by the surface the agent is given.

Avoid declaring a winner. In different runs of this lab, either cloud or local access should have the useful advantage.

## Do not teach yet

Do not teach Git command workflows, commits as recovery points, branch mechanics, connector protocol semantics, database administration, instruction precedence, data-scanning pipelines, skills, or elaborate permission configuration.

Lab 2 is about observing different access surfaces. Later labs explain the mechanisms and how to choose/configure them deliberately.
