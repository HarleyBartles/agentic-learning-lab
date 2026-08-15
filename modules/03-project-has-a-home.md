# Module 3 — The project has a home

Approximate duration: 1 hour.

Status: **direction pinned; Exercise 1 pinned; remainder not yet expanded into a lab**.

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

### Exercise 1 — Decisions that exist only in conversation are tears in the rain

Exercise 1 should make the Lab 1 persistence observation explicit without turning this into another cloud-versus-local comparison.

Run it with a local agent in a local workspace. That choice is deliberate: the learner should see that direct access to a project on disk does **not** mean a fresh local agent somehow remembers decisions from earlier conversations.

The lesson is:

> Decisions that exist only in conversation are tears in the rain.

And the operational version is:

> Important project knowledge should survive the conversation that created it.

A useful test is:

> If another fresh agent needs to know it, the project needs to contain it.

#### Project fixture — Repair Café pilot

Use a small non-code planning project for a fictional community Repair Café pilot.

The project should be immediately understandable and contain enough durable state for a fresh agent to reconstruct most of it correctly.

A suitable shape is:

```text
project/
    README.md
    source/
        venue.md
        volunteers.md
        attendee-feedback.md
    notes/
        current-decisions.md
        open-questions.md
    working/
        pilot-plan.md
    output/
```

The folder names are not doctrine. They are scenery for the persistence lesson.

The durable project should already contain several settled facts and decisions, for example:

- the pilot happens on a Saturday morning;
- it uses a community hall;
- it is free;
- visitors bring one broken item each;
- four volunteers are available;
- the broad purpose and operating constraints are already understood.

One consequential decision must remain explicitly unresolved in the files:

> How should arrivals work?

The source material should make at least two approaches plausible. For example:

- mostly drop-in attendance is flexible and sociable;
- booked time slots reduce queue uncertainty;
- attendee feedback provides support for both concerns.

There must be no objectively deducible correct answer in the project. `notes/open-questions.md` and `working/pilot-plan.md` should both make clear that the arrival model has not yet been decided.

This is what makes the later loss reproducible: a fresh agent inspecting only durable project state cannot legitimately infer the decision that was made in a lost conversation.

#### Conversation 1 — understand and decide, but do not persist

The learner opens a fresh local-agent conversation rooted at this project.

The learner card should give a strong non-mutation boundary, close to:

> Inspect this project and help me think through the unresolved arrival and booking model. We're just talking here. **Do not create, edit, delete, rename, or otherwise change any files until I explicitly tell you to modify files.** Discussion, agreement, decisions, or approval during this conversation are not permission to change the project.

The learner and agent then discuss the tradeoffs naturally.

The learner should choose the policy rather than being handed a scripted answer. A plausible outcome might be:

> Drop-in by default, with two pre-bookable accessibility slots each hour.

The exact policy does not matter. What matters is that the learner and agent reach a clear, consequential project decision.

When the learner settles the decision, do **not** end the conversation immediately after saying something like `that's the decision`. A competent agent could reasonably infer that an approved decision should now be recorded.

Instead, the learner should explicitly preserve the no-mutation boundary while proving that the agent understood the decision. For example:

> That's the decision: we'll use drop-in by default, with two pre-bookable accessibility slots each hour. Talk me through what that means for volunteers, queues, and how we should communicate the pilot. **We are still only discussing it. Do not modify any files.**

The agent should now reason correctly from the decision while leaving the project completely unchanged.

This matters. The later failure must not be explainable as `the first agent never really understood the decision`.

The intended state is:

```text
Agent 1 clearly understands the decision.
Agent 1 reasons from the decision.
Agent 1 is explicitly forbidden from persisting it.

Project files remain unchanged.
```

As an implementation check, the facilitator should verify after this conversation that the relevant project files really are unchanged. This verification can use a filesystem check or diff without turning Git into learner material.

#### Simulate losing the conversation

Now simulate a mundane operational failure:

> The IDE crashed and that conversation is unrecoverable.

Close the conversation and do not consult it again for the rest of the exercise.

The exact failure mechanism is not the lesson. A crashed IDE, corrupted thread, accidental deletion, unavailable history, or simply returning much later can all expose the same architectural weakness.

The invariant is:

> A conversation is not a durable project record.

#### Conversation 2 — recover what the project actually contains

Start a completely fresh local-agent conversation in the exact same project.

Ask something close to:

> Inspect this project. Tell me its current state, the important decisions that have been made, and the important questions that are still unresolved. Do not change anything.

The agent should reconstruct the durable state correctly: venue, timing, volunteers, operating constraints, and the decisions that actually exist in project files.

It should also report the arrival model as unresolved.

That answer is simultaneously:

- wrong according to what the learner knows happened in Conversation 1;
- correct according to the durable project state the fresh agent can inspect.

This is the moment the exercise is designed to earn.

Ask the learner to compare the agent's reconstruction with what they remember deciding and identify what is missing.

#### Recovery — deliberately persist the missing decision

The learner now tells the fresh agent what was lost and explicitly crosses the mutation boundary.

A suitable prompt is:

> We actually decided to use drop-in by default, with two pre-bookable accessibility slots each hour. That decision matters to the ongoing project. **You may now modify project files. Persist the decision somewhere appropriate so another fresh agent can reconstruct the current state.** Do not alter the source material.

Do not prescribe `decisions.md` or another sacred location. Let the agent make a sensible project-local choice based on the existing structure. It may update `current-decisions.md`, resolve the item in `open-questions.md`, update `pilot-plan.md`, or make another reasonable bounded change.

The learner is learning that important state should be persisted, not a universal documentation taxonomy.

#### Conversation 3 — prove that the project now carries the decision

End Conversation 2 as well.

Start a third completely fresh local-agent conversation rooted at the same project.

Ask something close to:

> Inspect the project from disk. Tell me its current state, the important decisions currently in force, and what remains unresolved.

This time the arrival policy should appear in the reconstruction.

Push the distinction strongly:

> The fresh agent did not remember the previous conversation.

and:

> The agent didn't remember. The project carried the result forward.

Be precise when unpacking the second line. The project is not cognitively remembering. One agent persisted information into durable, inspectable project state, and another fresh agent later read it.

The full exercise progression is:

```text
Conversation 1
project state + important decision in chat
→ decision is understood and reasoned from
→ filesystem deliberately remains unchanged

conversation becomes unavailable

Conversation 2
fresh agent inspects project
→ reconstructs durable state
→ arrival decision is still unresolved

learner identifies missing state
→ explicitly authorises persistence
→ agent records the decision in the project

conversation ends

Conversation 3
fresh agent inspects project
→ reconstructs durable state
→ arrival decision is present
```

#### Connection back to Lab 1

Lab 1 Exercise 4 already showed a fresh local agent discovering a bridge fact because an earlier worker had written it into a project artifact.

Exercise 1 of Lab 3 removes the cloud/local comparison and makes that mechanism the subject of the lesson.

Useful callback:

> Remember when the fresh local agent knew the bridge was safe? It wasn't remembering the earlier conversation. It was reading what that earlier agent had left in the project.

The learner should leave Exercise 1 with the stronger understanding that local agents do not gain magical continuity merely by operating on disk.

The observation to earn is:

> A conversation can contain project knowledge without that knowledge becoming project state.

And the memorable line is:

> Decisions that exist only in conversation are tears in the rain.

The recovery behaviour to practise is:

> Inspect what survived. Identify what is missing. Persist it. Verify with a fresh agent.

### Exercise 2 — Give the project a deliberate home

The original broad direction for Exercise 2 was to repeat the contrast by deciding what should survive beyond a conversation and recording it somewhere sensible in the project.

Exercise 1 now earns most of that lesson directly through loss and recovery, so Exercise 2 should not simply repeat the same move.

Keep the broader intended classification questions for later expansion:

- Is this something I am saying to the agent right now, or something the project itself needs to know tomorrow?
- Is this source material?
- Is this a current decision?
- Is this working material?
- Is this a result?

The detailed Exercise 2 mechanism is not yet pinned.

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
