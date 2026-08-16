# Lab 2 facilitator guide — Give the cloud agent the project

Approximate duration: 1 hour.

Status: **locked / stable**.

## Learning goal

Lab 1 established:

> If an agent cannot see the project surface, it cannot see what is missing from the context supplied to it.

Lab 2 changes one variable: cloud ChatGPT is given access to the learner's repository fork through the GitHub connector.

The learner should experience that connector access genuinely removes much of the manual context transport from Lab 1, while also discovering that `has access to the project` is not a precise enough description on its own.

By the end of the lab, the learner should naturally start asking:

- Which state of the project is this agent looking at?
- Which parts of the working environment are actually on this surface?
- Can the agent perceive the representation needed for this task?
- What is it allowed to change through this surface?

Do not present those four questions as a lecture at the start. Let the exercises create them.

## The project fixture

All exercises happen in the learner's fork under:

`labs/02-give-the-cloud-agent-the-project/project/`

The fixture is a small event-planning project for Riverside Hall. It includes:

- tracked text describing event setup and operational facts;
- a tracked venue plan image containing information that only exists visually;
- a tracked description of a local operational attendee database;
- a `.gitignore` rule excluding `local/`, where the operational database will be created during Exercise 3;
- an initially empty `local-setup/` area where the worker will create reusable database schema during Exercise 3;
- a tracked disposable `scratch/` directory used for the deletion exercise;
- `AGENTS.md`, containing standing instructions for the on-disk worker.

This is deliberately one repository, not a second exercise repository.

## Before the session

### Cloud environment

Enable the GitHub connector for the learner's fork before Lab 2.

Do not target the canonical upstream `HarleyBartles/agentic-learning-lab` for learner mutations. Upstream remains the curriculum source; the learner fork is the learner's project state.

The learner does not configure the connector. The visible change from Lab 1 is simply:

> ChatGPT can now reach your repository.

Use a fresh conversation for each exercise or controlled run where stale conversational context could hide the observed difference.

Where the product/harness exposes cross-chat memory or similar continuity features, configure the teaching environment so those features cannot supply the hidden answer for runs intended to prove persistence or access-surface differences. This is facilitator environment setup, not an `AGENTS.md` responsibility.

Do not explain MCP, schemas, indexing, authentication, memory controls, or connector implementation in this lab unless needed to troubleshoot the setup.

### Local environment

Use the learner's local checkout of the same fork.

Before the lab:

1. ensure the checkout starts synchronized with the learner fork's current main line;
2. ensure `project/local/attendees.db` does **not** exist;
3. confirm `project/local/` is ignored by Git;
4. confirm `project/local-setup/` contains no attendee schema yet;
5. prepare the on-disk agent with a working root at `labs/02-give-the-cloud-agent-the-project/project/`;
6. ensure the agent can inspect common image formats and use SQLite locally;
7. keep the `scratch/` content disposable;
8. confirm the worker reads and follows `project/AGENTS.md`;
9. confirm local push configuration targets the learner fork rather than canonical upstream.

The learner will supply the attendee records directly to the on-disk worker during Exercise 3. The worker should create both the reusable schema and the operational database. The schema is legitimate source-controlled work; the current attendee records remain local runtime state.

`AGENTS.md` is deliberately visible in the project. It is not part of the lesson yet, but it does not need to be hidden. If the learner asks what it is, explain briefly that it contains standing working instructions for the local agent so the exercise behaves consistently, and that a later lab will examine how project instructions work and where they belong.

Do not teach Git synchronization or SQLite setup mechanics while preparing this lab. They are facilitator plumbing here.

### Project operating instructions

`project/AGENTS.md` controls the experimental conditions for the on-disk worker.

Its important intents include:

- deliberately divergent local/remote state must not be silently synchronized;
- ordinary local changes stop for review unless commit/push is explicitly authorized;
- pushes must target the learner fork, not canonical upstream;
- local operational database records and attendee-specific derived content must not cross onto the GitHub surface;
- inaccessible file representations must not be guessed at;
- disposable `scratch/` work stays bounded and is not backed up or widened into unrelated cleanup.

These are experimental hygiene, not the Lab 2 lesson. Without them, an otherwise helpful worker could pull remote changes, publish local-only data, create an attendee summary, force-add an ignored database, back up scratch files, or otherwise remove the difference the learner is meant to observe.

Do not unpack the instruction mechanism unless the learner asks. A later lab can explicitly return to `AGENTS.md` and project instruction architecture.

The instructions must not teach the worker the answers to the exercises. They control what state may move between surfaces and what kinds of helpful automation are out of scope.

## Exercise 1 — Which state are you looking at?

Use `project/source/supplier.md`.

The exercise has three runs.

### Run A — synchronized baseline

Start with local and the learner fork both reporting the same supplier arrival time.

Ask both agents:

> What time is the supplier arriving at Riverside Hall?

Both should agree.

The important first observation is positive:

> The cloud agent can now use the project directly. Lab 1's manual file transport is no longer necessary for this kind of task.

### Run B — learner creates local-only state

Ask the learner to choose a different supplier arrival time themselves. The chosen value should exist only in the learner's prompt to the local agent; do not encode it in facilitator notes or tracked learner material.

Have the learner tell the on-disk agent to change the supplier arrival time to that value and stop for review without committing or publishing.

Ask both agents again in fresh conversations.

Expected result:

- local agent reports the learner's chosen local time;
- cloud agent through GitHub reports the unchanged repository time.

The learner has caused the divergence themselves. Do not teach `dirty working tree`, staging, commit, or push terminology yet. Just notice that two valid access routes can be observing different states.

### Run C — learner creates remote state while local work remains

Do **not** restore or discard the local change from Run B.

Ask the learner to choose another supplier arrival time, different from their Run B value. Again, the value should be created in the learner-to-cloud-agent conversation rather than encoded in the repository.

Have the learner ask cloud ChatGPT, through its GitHub write capability, to change the supplier arrival time directly in the learner fork to that second value.

Let any normal connector confirmation/safety flow occur naturally.

Do **not** update the learner's local checkout.

Once the remote mutation is complete, start a fresh cloud conversation and a fresh local-agent conversation before asking for the supplier time again. Ensure the environment is not carrying the answer across conversations through a separate memory feature.

Expected visible result:

- cloud agent reports the learner's Run C value from the repository;
- local agent still reports the learner's Run B value from the uncommitted working file.

There is also a third state underneath the local edit: the saved local version from before Run B.

Now have the learner tell the local agent:

> I changed my mind. Abandon my local change to the supplier file and restore that file to the saved local version. Then tell me the supplier arrival time again.

Expected result: the local agent now reports the older saved local value, which is still stale relative to the repository because the learner has not synchronized after the cloud-side change.

Do not unpack the Git mechanics yet. The learner has now experienced three simultaneously meaningful states:

```text
remote repository state        learner's Run C value
local working file             learner's Run B value
local saved version beneath    original synchronized value
```

A key reflection question is:

> At any stage, was an agent lying or giving a wrong answer based on the project state it could actually see?

The intended answer is no. Each agent honestly reported the correct value according to the project state visible through its own access route. The disagreement comes from state divergence, not deception or necessarily bad reasoning.

After the observation, synchronize and clean the local checkout before the next exercise.

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

This exercise starts with no attendee database on disk and no pre-existing attendee schema in `local-setup/`.

The learner chooses five fictional attendee records, including name, confirmation state, and meal choice, and supplies those values directly to the on-disk worker. Those values must not already exist in a tracked file or cloud conversation.

The learner asks the local worker to set up the attendee database using those records, create the reusable database schema as source-controlled project material, and push the appropriate project work when finished.

Expected local result:

- `project/local/attendees.db` is created and contains the records;
- the database remains ignored and is not published;
- a reusable schema is created in `project/local-setup/` and is committed/pushed;
- the worker can publish that legitimate source-controlled work without leaking any attendee values or attendee-specific derived content into tracked files, commit messages, receipts, logs, issues, PRs, or other remote surfaces.

Then start a fresh cloud ChatGPT conversation and ask it, using only repository access, to list the attendee records the on-disk worker just captured.

The learner has just watched the worker create the state and successfully publish legitimate related work, so the impossibility should feel concrete rather than staged.

Expected cloud result:

- it can discover that the project uses `local/attendees.db`;
- it can inspect the newly published reusable schema and repository material;
- it cannot retrieve the actual attendee records because those records never crossed onto the GitHub surface.

Then start a **fresh** on-disk-agent conversation rooted at the same local project and ask for the same records. Ensure cross-chat memory or equivalent continuity is disabled for this proof. The agent should answer from the persistent local database, not from carried conversational context.

This is not a fake limitation introduced purely for the lab. Operational database contents commonly do not live in source control. Source control often contains schema, migrations, setup/test material, and code which uses the database, while live mutable database state is managed separately. Reasons include privacy, mutable/environment-specific state, poor binary diff/merge behaviour, and practical repository size limits as databases grow.

Do not turn that side note into a database-policy lesson. The point is simply:

> Publishing the source-controlled work does not necessarily publish every piece of state in the project's working environment.

## Exercise 4 — What can this surface do?

Use only:

`project/scratch/`

The directory contains deliberately disposable files.

### Run A — local deletion and cheap rollback

Have the learner ask the local agent:

> Delete everything in `scratch/`, but do not commit or publish the deletion. Stop for review when the files are gone locally.

Inspect the result.

Then have the learner tell the same local agent:

> I changed my mind. Abandon those local changes and restore the scratch files.

Inspect the restored files.

Do not teach Git commands or recovery mechanics here. This is a small preview of a later source-control lesson: when a destructive local change has not been published and a saved project version exists underneath it, changing your mind can be cheap.

### Run B — analogous remote deletion

Ask the cloud agent through GitHub to perform the analogous deletion against the learner fork.

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

## Reset after the session

Return the learner fork and local checkout to a known starting state before the next run:

1. restore the remote supplier arrival time in `project/source/supplier.md` to the original baseline;
2. synchronize the learner's local checkout and leave no local supplier edit behind;
3. remove `project/local/attendees.db`;
4. remove the attendee schema created during Exercise 3 from `project/local-setup/` so the next learner creates it themselves;
5. restore `project/scratch/` remotely if the cloud-side deletion succeeded;
6. confirm the scratch fixture exists locally after synchronization;
7. immediately before teaching the lab again, verify that the GitHub connector still exposes `venue-plan.png` only as encoded/binary content rather than usable image pixels;
8. confirm the cloud connector and local push remote still target the learner fork, not canonical upstream;
9. confirm any cross-chat memory/continuity features that could contaminate the fresh-conversation proofs are disabled for the relevant surfaces.

The reset mechanics are facilitator work. They are not part of the Lab 2 lesson.

## Do not teach yet

Do not teach Git command workflows, commits as recovery points, branch mechanics, connector protocol semantics, database administration, instruction precedence, data-scanning pipelines, skills, elaborate permission configuration, or memory configuration.

Lab 2 is about observing different access surfaces. Later labs explain the mechanisms and how to choose/configure them deliberately.
