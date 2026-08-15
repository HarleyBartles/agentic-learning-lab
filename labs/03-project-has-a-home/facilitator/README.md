# Lab 3 facilitator guide

Status: **Exercises 1 and 2 ready to run**.

## Lab learning goal

Lab 3 is about durable project state: what survives independently of any particular conversation or agent, and how deliberately conversational material should become part of that state.

Exercise 1 earns:

> Decisions that exist only in conversation are tears in the rain.

Exercise 2 adds the complementary lesson:

> Preserve evidence honestly. Promote meaning deliberately.

Together they should prevent two opposite mistakes:

- leaving important project knowledge trapped in conversation;
- casually converting conversation into project truth without enough human authority.

## Shared project fixture

Use `../project/` as the local agent's workspace.

It is a fictional community Repair Café pilot containing settled project decisions, source material, open questions, and a working plan.

Root the prepared local agent at `labs/03-project-has-a-home/project/`, not at the Lab 3 teaching directory.

The project `AGENTS.md` now contains standing discussion-mode doctrine. When the user frames work as discussion, exploration, brainstorming, thinking through, or planning, the agent should treat that as discussion-only until the user explicitly authorizes project changes.

This is useful operating doctrine, but it is not the same thing as an enforced permission boundary.

Keep this distinction available for later curriculum use:

> Instructions describe the intended boundary. Permissions enforce the possible boundary.

# Exercise 1 — Tears in the rain

## Learning goal

This exercise should eliminate a tempting but wrong takeaway from Lab 1:

> Local agents remember because they are on disk.

They do not.

A fresh local agent can recover whatever durable project state another agent left behind. If an important decision existed only in a lost conversation, direct filesystem access cannot recover it.

The learner should earn these formulations:

> Decisions that exist only in conversation are tears in the rain.

> The agent didn't remember. The project carried the result forward.

When unpacking the second line, be precise: the project is not cognitively remembering. One agent persisted information into durable, inspectable project state and another fresh agent later read it.

## Exercise 1 fixture state

The project contains:

- settled project decisions;
- venue and volunteer information;
- mixed attendee feedback;
- a working pilot plan;
- one deliberately unresolved consequential question: the arrival and booking model.

The project files must not encode a secretly preferred answer. Drop-in, booked, and hybrid approaches should all be defensible from the evidence. The learner chooses the policy during the exercise.

Before Exercise 1, make sure:

- `notes/open-questions.md` still says the arrival model is unresolved;
- `working/pilot-plan.md` still marks the arrival model as undecided;
- no learner-created arrival decision has already been persisted elsewhere in the project.

## Choose the operating surface

Keep the main Exercise 1 experiment on one agent surface from Conversation 1 through Conversation 3 so the persistence result is not confounded by changing products mid-experiment.

Use whichever local agent surface is most convenient and supports the needed boundary cleanly.

Current good options include:

- Codex in a surface that exposes read-only permissions;
- Codex CLI or IDE where a read-only sandbox/permission mode can be selected;
- another agentic IDE such as Devin Desktop if it exposes an equivalent Plan/read-only control.

The exact UI and terminology may vary by harness and can change over time. Verify the chosen surface immediately before running the lab rather than baking product-specific clicks into the conceptual lesson.

The point is not `Codex has the right button`. The point is:

> Different harnesses expose different operating controls, capability boundaries, and risk profiles.

This should remain a light-touch observation here. A later lab will explicitly unpack model versus harness versus instructions versus tools.

For Codex specifically, current OpenAI documentation distinguishes Plan mode from read-only permissions. Plan mode supports planning behaviour; read-only permissions/sandboxing are the stronger mechanism for preventing filesystem writes. Prefer an actual read-only boundary for this experiment when available.

## Conversation 1 — create valuable knowledge without changing the project

Give the learner `../learner/01-tears-in-the-rain.md`.

Before the learner starts discussing the Repair Café decision, put the agent into read-only or equivalent non-mutation mode if the chosen surface provides one.

The learner can now speak naturally:

> Inspect this project and help me think through the unresolved arrival and booking model. We're just discussing it for now.

There are now three separate layers cooperating:

```text
user intent
"We're just discussing."

project doctrine
AGENTS.md says discussion means no mutation

harness boundary
read-only mode prevents filesystem mutation
```

Do not teach this as a formal framework yet. Use it as robust exercise plumbing and, if useful, point out that the environment is enforcing the important boundary rather than trusting a long prompt.

Let the learner and agent genuinely discuss the tradeoffs. Do not steer them toward a predetermined policy.

Once the learner chooses an arrival policy, have them state it explicitly and ask the agent to reason from it while staying in discussion mode. Something like:

> That's the decision: [their policy]. Talk me through what that means for volunteers, queues, and how we should communicate the pilot. We're still only discussing it.

This second turn is important. It proves that the first agent understood and could reason from the decision. The later loss must not be explainable as a misunderstanding.

Before simulating the crash, quietly verify that the project really is unchanged. A local filesystem check or diff is fine as facilitator plumbing. Do not turn that check into a Git lesson.

If the chosen harness lacks a reliable read-only mechanism, the standing `AGENTS.md` rule plus explicit discussion framing is the fallback. In that case verify the working tree carefully before continuing.

## Simulate the loss

Tell the learner to treat the IDE or agent surface as having crashed and the conversation as unrecoverable.

Close the thread and do not consult it again.

Be precise about causality:

- starting a fresh conversation removes the conversational context;
- the earlier read-only boundary merely ensured that nothing from that context was persisted into project files before the loss.

The exact failure mechanism is scenery. The lesson should remain valid for a crashed IDE, corrupted or unavailable thread, accidental loss, context reset, or simply returning later without usable conversational continuity.

Do not imply that local agents are uniquely vulnerable. The point is that a conversation is not a durable project record.

## Conversation 2 — reconstruct from durable state

Start a completely fresh local-agent conversation in the same workspace and keep it read-only for the reconstruction step.

The learner asks:

> Inspect this project. Tell me its current state, the important decisions that have been made, and the important questions that are still unresolved. Do not change anything.

The expected answer should correctly recover the durable state and report the arrival model as unresolved.

That answer is deliberately interesting because it is:

- wrong according to what the learner knows happened in Conversation 1;
- correct according to the project state the fresh agent can inspect.

Let that discrepancy land before explaining it.

Ask the learner what is missing.

## Recovery — cross the mutation boundary deliberately

Once the learner identifies the missing arrival decision, explicitly move the agent out of read-only/discussion-only operation and authorize project changes.

The learner tells the fresh agent what was decided:

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

## Exercise 1 reflection

Useful questions:

- Did Conversation 1's agent understand the arrival decision?
- Did it reason correctly from that decision?
- Why could Conversation 2 not recover it?
- Was Conversation 2 wrong based on the evidence it could inspect?
- What changed between Conversations 2 and 3?
- Did Conversation 3 need memory from the previous chat?
- What would happen six months later if the only record of an important decision were an old conversation?
- What did read-only mode guarantee that a prose instruction alone could not guarantee?
- What role did the standing project instruction play even though the harness had the stronger boundary?

The recovery pattern to reinforce is:

> Inspect what survived. Identify what is missing. Persist it. Verify with a fresh agent.

## Connection to Lab 1

If useful, call back to the west-bridge result from Lab 1 Exercise 4:

> The fresh local agent knew the bridge was safe because an earlier worker had written that information into the project. It was not remembering the earlier conversation.

Lab 3 Exercise 1 removes the cloud/local comparison and makes persistence itself the subject.

# Exercise 2 — Don't make the agent guess

## Learning goal

Exercise 1 says that important state must be persisted. Exercise 2 asks the next question:

> What exactly should be persisted, and who decides what a messy conversation means for the project?

The exercise uses the same Repair Café project and the same set of meeting minutes three times.

The learner's local agent performs all changes and all resets. The facilitator does not restore the fixture between runs.

Each experimental run stays uncommitted and unpushed until the learner has inspected it. After Runs 1 and 2, the learner tells the agent to discard those uncommitted changes. Only the satisfactory Run 3 result is committed and pushed.

This quietly reinforces reversible experimentation without turning Lab 3 into the later source-control lesson.

## Exercise 2 baseline

Exercise 2 follows Exercise 1, so the arrival-policy decision from Exercise 1 should remain part of the project.

Before Run 1, ensure that completed Exercise 1 work is committed and pushed. If it is still uncommitted, have the learner ask the agent to commit and push it.

Then verify that the project has no other uncommitted changes.

The important invariant is:

> Run 1, Run 2, and Run 3 all begin from the same committed project state.

## The meeting minutes

The learner card contains these seven numbered points:

1. Alex suggested that a future session for children could be fun if safeguarding and volunteer numbers ever made it practical. No decision was made.
2. The group discussed whether visitors should be allowed to bring a second item late in the session if things are quiet. No decision was reached.
3. The group agreed that every soldering station at the pilot will use a heatproof mat.
4. Alex confirmed that he will bring two suitable heatproof mats for the pilot.
5. The group discussed whether to accept voluntary donations at the pilot. Opinions were mixed and the question remains unresolved.
6. Priya said the tea at the last community event was terrible and volunteered to bring better biscuits this time.
7. The group agreed that repairs involving exposed mains wiring will only be handled by volunteers who are comfortable and competent doing that work.

These points deliberately mix:

- speculation;
- unresolved discussion;
- a settled operational rule;
- a confirmed commitment;
- incidental chatter/action texture.

Do not pre-teach those categories to the learner. The learner should experience why status and authority matter by comparing the three runs.

## Run 1 — vague delegation

The learner says, with the minutes pasted after it:

> Here are the minutes from the latest Repair Café planning meeting. Sort through them and put the important stuff in the repo. Make whatever project-file changes you think are appropriate, but leave all changes uncommitted and do not push anything. Stop when the changes are ready for me to review.

The agent's output does not need to be ridiculous to make the exercise work. A polished, sensible-looking result is better if it reveals that the agent silently had to decide:

- what `important` meant;
- which statements deserved durable representation;
- whether discussion implied a decision;
- whether to preserve the original meeting record;
- where different information belonged;
- what should change the current plan.

Inspect the actual diff rather than accepting the completion message.

The key question is:

> Who decided what `important` meant?

The answer is that the vague prompt delegated semantic authority to the agent, whether the learner intended that or not.

After inspection, the learner asks the agent to discard all Run 1 changes and restore the previous committed state without changing committed history or pushing anything.

Verify the working tree is clean before Run 2.

## Run 2 — preserve evidence without promotion

The learner pastes the same minutes and says:

> Here are the same meeting minutes. Persist them verbatim in the project as an honest meeting record. Do not interpret any point as a settled decision, commitment, rule, or resolved question, and do not update the rest of the project state from them. Leave the changes uncommitted and do not push anything. Stop when the meeting record is ready for review.

Inspect the diff.

This run should demonstrate a different kind of correctness: the project gains an honest durable artifact, but no claim is made that the meeting artifact itself has automatically changed operational project state.

The important distinction is:

> Preserving evidence is not the same thing as updating project state.

After inspection, the learner tells the agent to discard all Run 2 changes and restore the previous committed state.

Verify the working tree is clean before Run 3.

## Run 3 — preserve evidence and promote selected meaning

The learner pastes the minutes again and says:

> Persist these meeting minutes verbatim as the meeting record. Then update the durable project state to reflect them. Points 3, 4 and 7 are confirmed project state and should affect the current plan. Points 2 and 5 remain unresolved questions. Do not promote points 1 or 6 into current project state; they should remain only in the meeting record. Make the project-file changes you think are appropriate, but leave everything uncommitted and do not push anything. Stop for review when you are done.

The human now supplies the authority boundary while leaving implementation details to the agent.

A good result should show both:

- provenance: the original meeting record survives as an honest artifact;
- deliberate state: only the explicitly authorized points affect current project decisions, commitments, rules, or open questions.

Inspect the diff carefully. In particular:

- point 3 should affect the operational plan or durable rule state;
- point 4 should be represented as a current commitment;
- point 7 should be represented as a current safety/operating rule;
- points 2 and 5 should remain unresolved;
- points 1 and 6 should not silently become current policy simply because they were mentioned.

If the learner is satisfied, they tell the agent to keep the Run 3 changes, commit them, and push them.

## Final proof

Do not run a fresh-agent persistence proof after Runs 1 or 2. Earlier labs and Exercise 1 have already established that durable state survives conversations.

Use one final proof after the good Run 3 state has been committed and pushed.

Start a fresh local agent and ask:

> Inspect the Repair Café project as it exists now. Tell me which decisions, rules, and commitments from the latest planning meeting are reflected in the current project state, and which questions from that meeting remain unresolved.

If time allows, ask a fresh cloud agent through repository access the same question.

The cloud/local comparison is only a callback here, not the organizing axis. Both should be able to reconstruct the published project state available through their respective surfaces.

## Exercise 2 reflection

The two lines to earn are:

> Preserve evidence honestly. Promote meaning deliberately.

and:

> Don't make the agent guess which meeting chatter became project truth.

A useful summary is:

```text
Run 1
vague instruction
→ agent must infer importance and authority
→ inspect
→ discard

Run 2
verbatim evidence only
→ honest record survives
→ operational state deliberately unchanged
→ inspect
→ discard

Run 3
verbatim evidence
+ explicit human authority about status
→ deliberate durable project state
→ inspect
→ commit and push

Final proof
fresh agent reconstructs the published state
```

# Do not teach yet

Do not turn these exercises into:

- a deep Git lesson;
- a documentation taxonomy;
- an instruction-precedence lesson;
- a context-window or compaction lesson;
- a full source-of-truth governance lesson.

Exercise 2 may naturally create questions about authority and conflicting durable artifacts. Preserve that itch for the remaining Lab 3 work and the later source-of-truth module rather than solving the whole problem here.
