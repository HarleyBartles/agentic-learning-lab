# Lab 3 facilitator guide — Exercise 1

Status: **Exercise 1 ready to run**.

## Learning goal

This exercise should eliminate a tempting but wrong takeaway from Lab 1:

> Local agents remember because they are on disk.

They do not.

A fresh local agent can recover whatever durable project state another agent left behind. If an important decision existed only in a lost conversation, direct filesystem access cannot recover it.

The learner should earn these formulations:

> Decisions that exist only in conversation are tears in the rain.

> The agent didn't remember. The project carried the result forward.

When unpacking the second line, be precise: the project is not cognitively remembering. One agent persisted information into durable, inspectable project state and another fresh agent later read it.

## Project fixture

Use `../project/` as the local agent's workspace.

It is a fictional community Repair Café pilot containing:

- settled project decisions;
- venue and volunteer information;
- mixed attendee feedback;
- a working pilot plan;
- one deliberately unresolved consequential question: the arrival and booking model.

The project files must not encode a secretly preferred answer. Drop-in, booked, and hybrid approaches should all be defensible from the evidence. The learner chooses the policy during the exercise.

Before the session, make sure the project is at its baseline state. In particular:

- `notes/open-questions.md` still says the arrival model is unresolved;
- `working/pilot-plan.md` still marks the arrival model as undecided;
- no learner-created arrival decision has already been persisted elsewhere in the project.

Root the prepared local agent at `labs/03-project-has-a-home/project/`, not at the Lab 3 teaching directory.

## Conversation 1 — create valuable knowledge without changing the project

Give the learner `../learner/01-tears-in-the-rain.md`.

The learner begins with a strong non-mutation instruction:

> Inspect this project and help me think through the unresolved arrival and booking model. We're just talking here. Do not create, edit, delete, rename, or otherwise change any files until I explicitly tell you to modify files. Discussion, agreement, decisions, or approval during this conversation are not permission to change the project.

Let the learner and agent genuinely discuss the tradeoffs. Do not steer them toward a predetermined policy.

Once the learner chooses an arrival policy, make sure they explicitly keep the no-mutation boundary while asking the agent to reason from the decision. The learner should say something equivalent to:

> That's the decision: [their policy]. Talk me through what that means for volunteers, queues, and how we should communicate the pilot. We are still only discussing it. Do not modify any files.

This second turn is important. It proves that the first agent understood and could reason from the decision. The later loss must not be explainable as a misunderstanding.

Before simulating the crash, quietly verify that the project really is unchanged. A local filesystem check or `git diff -- labs/03-project-has-a-home/project` is fine as facilitator plumbing. Do not turn that check into a Git lesson.

If the agent changed files despite the learner's explicit boundary, restore the baseline and repeat the discussion. The experiment depends on the decision existing only in conversational context.

## Simulate the loss

Tell the learner to treat the IDE as having crashed and the conversation as unrecoverable.

Close the thread and do not consult it again.

The exact failure mechanism is scenery. The lesson should remain valid for a crashed IDE, corrupted or unavailable thread, accidental loss, context reset, or simply returning later without usable conversational continuity.

Do not imply that local agents are uniquely vulnerable. The point is that a conversation is not a durable project record.

## Conversation 2 — reconstruct from durable state

Start a completely fresh local-agent conversation in the same workspace.

The learner asks:

> Inspect this project. Tell me its current state, the important decisions that have been made, and the important questions that are still unresolved. Do not change anything.

The expected answer should correctly recover the durable state and report the arrival model as unresolved.

That answer is deliberately interesting because it is:

- wrong according to what the learner knows happened in Conversation 1;
- correct according to the project state the fresh agent can inspect.

Let that discrepancy land before explaining it.

Ask the learner what is missing.

## Recovery — cross the mutation boundary deliberately

Once the learner identifies the missing arrival decision, they tell the fresh agent what was decided and explicitly authorize persistence:

> We actually decided [their policy]. That decision matters to the ongoing project. You may now modify project files. Persist the decision somewhere appropriate so another fresh agent can reconstruct the current state. Do not alter the source material.

Do not prescribe one sacred destination. A good result may update `notes/current-decisions.md`, resolve the item in `notes/open-questions.md`, update `working/pilot-plan.md`, or make another sensible bounded combination of changes.

The thing to inspect is whether the project now communicates the decision clearly enough for another agent to reconstruct it without the conversation.

## Conversation 3 — prove persistence

End Conversation 2.

Start a third completely fresh local-agent conversation in the same workspace.

Ask:

> Inspect the project from disk. Tell me its current state, the important decisions currently in force, and what remains unresolved.

The fresh agent should now report the learner's arrival policy.

Push the distinction strongly:

> The fresh agent did not remember Conversation 2.

It knows because the previous agent changed durable project state that the new agent can inspect.

## Reflection

Useful questions:

- Did Conversation 1's agent understand the arrival decision?
- Did it reason correctly from that decision?
- Why could Conversation 2 not recover it?
- Was Conversation 2 wrong based on the evidence it could inspect?
- What changed between Conversations 2 and 3?
- Did Conversation 3 need memory from the previous chat?
- What would happen six months later if the only record of an important decision were an old conversation?

The recovery pattern to reinforce is:

> Inspect what survived. Identify what is missing. Persist it. Verify with a fresh agent.

## Connection to Lab 1

If useful, call back to the west-bridge result from Lab 1 Exercise 4:

> The fresh local agent knew the bridge was safe because an earlier worker had written that information into the project. It was not remembering the earlier conversation.

Lab 3 Exercise 1 removes the cloud/local comparison and makes persistence itself the subject.

## Do not teach yet

Do not turn this exercise into:

- a Git lesson;
- a documentation taxonomy;
- an instruction-precedence lesson;
- a context-window or compaction lesson;
- a source-of-truth governance lesson.

Those later mechanisms will be easier to understand once the learner has experienced why durable project state matters.
