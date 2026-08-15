# Lab 3 facilitator guide

Status: **Stable and ready to run**.

## Lab learning goal

Lab 3 is about durable project state: what survives independently of any particular conversation or agent, how deliberately conversational material should become part of that state, and what happens when durable artifacts no longer agree.

Exercise 1 earns:

> Decisions that exist only in conversation are tears in the rain.

Exercise 2 adds:

> Preserve evidence honestly. Promote meaning deliberately.

Exercise 3 adds:

> Persisted does not mean current.

> Durable does not automatically mean authoritative.

Together the exercises should prevent three mistakes:

- leaving important project knowledge trapped in conversation;
- casually converting conversation into project truth without enough human authority;
- assuming that everything durable in the project is equally current or authoritative.

## Shared project fixture

Use `../project/` as the local agent's workspace.

Root the prepared local agent at `labs/03-project-has-a-home/project/`, not at the Lab 3 teaching directory.

The project `AGENTS.md` carries standing operating doctrine. It now does two useful jobs:

- discussion-mode behaviour: discussion, exploration, brainstorming, thinking through, and planning are non-mutating until the user explicitly authorizes changes;
- review workflow: ordinary requested changes remain uncommitted and unpushed for review unless the user explicitly asks to commit or push, and `discard that run` means undo only the current run's uncommitted changes without rewriting history or disturbing unrelated work.

This is intentional. The learner should spend prompt effort on task meaning, not repeatedly reconstructing routine operating rules.

Keep this distinction available for later curriculum use:

> Instructions describe the intended boundary. Permissions enforce the possible boundary.

And this one:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

Do not turn either into a formal instruction-architecture lesson yet.

# Exercise 1 — Tears in the rain

## Learning goal

Eliminate the tempting but wrong takeaway:

> Local agents remember because they are on disk.

They do not.

A fresh local agent can recover durable project state left by another agent. If an important decision existed only in a lost conversation, filesystem access cannot recover it.

The learner should earn:

> The agent didn't remember. The project carried the result forward.

Be precise when unpacking that line: the project is not cognitively remembering. One agent persisted information into durable, inspectable state and another fresh agent later read it.

## Fixture state

Before Exercise 1, verify:

- `notes/open-questions.md` still says the arrival model is unresolved;
- `working/pilot-plan.md` still marks it undecided;
- no learner-created arrival decision has already been persisted elsewhere.

There is no hidden preferred answer. Drop-in, booked, and hybrid approaches should all be defensible.

## Operating surface

Keep the whole Exercise 1 experiment on one agent surface so the persistence result is not confounded by changing products mid-run.

Use whichever local surface gives the cleanest non-mutation boundary. Codex read-only permissions, Codex CLI/IDE sandboxing, Devin Desktop Plan/read-only controls, or an equivalent mechanism are all acceptable.

The exact UI may vary over time. The conceptual point is:

> Different harnesses expose different operating controls, capability boundaries, and risk profiles.

For Codex, prefer an actual read-only boundary over relying on Plan mode alone when the surface exposes one.

## Conversation 1

Put the agent into read-only or equivalent non-mutation mode if available.

The learner can speak naturally:

> Inspect this project and help me think through the unresolved arrival and booking model. We're just discussing it for now.

The three layers are:

```text
user intent
"We're just discussing."

project doctrine
AGENTS.md says discussion means no mutation

harness boundary
read-only mode prevents filesystem mutation
```

Do not formally teach the stack yet. Use it as exercise plumbing.

Let the learner choose a real policy. Once chosen, have them say something equivalent to:

> That's the decision: [their policy]. Talk me through what that means for volunteers, queues, and how we should communicate the pilot. We're still only discussing it.

This proves the first agent understood and could reason from the decision.

Before the simulated loss, verify the project is unchanged. Do not turn that check into a Git lesson.

If the chosen harness has no reliable read-only mechanism, the standing `AGENTS.md` rule plus explicit discussion framing is the fallback; verify the working tree carefully.

## Simulate the loss

Close the conversation and treat it as unrecoverable.

Be precise:

- starting a fresh conversation removes the conversational context;
- read-only merely ensured that nothing from that context leaked into project state first.

## Conversation 2

Start fresh in the same workspace, preferably read-only for reconstruction.

Ask:

> Inspect this project. Tell me its current state, the important decisions that have been made, and the important questions that are still unresolved. Do not change anything.

The agent should correctly report the arrival model as unresolved.

That answer is wrong according to the learner's lived history but correct according to the state the fresh agent can inspect.

Let that discrepancy land.

## Recovery

Move out of read-only/discussion-only operation and explicitly authorize persistence:

> We actually decided [their policy]. That decision matters to the ongoing project. You may now modify project files. Persist the decision somewhere appropriate so another fresh agent can reconstruct the current state. Do not alter the source material.

Do not prescribe a sacred destination. Inspect whether the resulting project communicates the decision clearly enough for another agent to reconstruct it.

## Conversation 3

Start fresh and ask:

> Inspect the project from disk. Tell me its current state, the important decisions currently in force, and what remains unresolved.

Push the distinction:

> The fresh agent did not remember Conversation 2.

It knows because durable project state changed.

Useful reflection questions include what survived, what was missing, where the third agent found the decision, and what read-only guaranteed that prose alone did not.

# Exercise 2 — Don't make the agent guess

## Learning goal

Exercise 1 says important state must be persisted. Exercise 2 asks:

> What exactly should be persisted, and who decides what messy conversation material means for the project?

The same meeting minutes are used three times.

The local agent performs all changes and resets. The facilitator does not restore the fixture between runs.

The standing `AGENTS.md` workflow now carries the mechanics:

- requested changes stop uncommitted and unpushed for review by default;
- commit/push happens only when explicitly requested;
- `discard that run` reverts only the current run's uncommitted changes and does not rewrite history or discard unrelated work.

This means the learner prompts can focus almost entirely on semantic authority.

## Baseline

Exercise 2 follows Exercise 1, so the arrival decision should remain in the project.

Before Run 1, ensure completed Exercise 1 work is committed and pushed. Then verify there are no unrelated uncommitted changes.

The invariant is:

> Run 1, Run 2, and Run 3 all begin from the same committed project state.

## Meeting minutes

The learner card contains seven points mixing speculation, unresolved discussion, settled operational rules, confirmed commitments, and incidental chatter.

Do not pre-teach those categories. Let the learner experience why status and authority matter.

## Run 1 — vague delegation

The learner says, with the minutes pasted after it:

> Here are the minutes from the latest Repair Café planning meeting. Sort through them and put the important stuff in the repo.

Because the project doctrine handles review state, the agent should make the changes and stop with them uncommitted and unpushed.

Inspect the actual diff. A polished result is useful if it exposes that the agent had to decide:

- what `important` meant;
- which statements deserved durable representation;
- whether discussion implied a decision;
- whether the original meeting record should survive;
- where information belonged;
- what should alter current project state.

Ask:

> Who decided what `important` meant?

The vague prompt delegated semantic authority to the agent.

Then the learner says simply:

> Discard that run.

Verify the working tree returns to the clean baseline.

## Run 2 — preserve evidence without promotion

The learner says:

> Here are the same meeting minutes. Persist them verbatim in the project as an honest meeting record. Do not interpret any point as a settled decision, commitment, rule, or resolved question, and do not update the rest of the project state from them.

Inspect the diff.

Earn:

> Preserving evidence is not the same thing as updating project state.

Then:

> Discard that run.

Verify the same clean baseline before Run 3.

## Run 3 — preserve evidence and promote selected meaning

The learner says:

> Persist these meeting minutes verbatim as the meeting record. Then update the durable project state to reflect them. Points 3, 4 and 7 are confirmed project state and should affect the current plan. Points 2 and 5 remain unresolved questions. Do not promote points 1 or 6 into current project state; they should remain only in the meeting record.

The human now supplies the authority boundary while leaving implementation details to the agent.

A good result should show:

- provenance: the original meeting record survives honestly;
- deliberate state: only the explicitly authorized points affect current decisions, commitments, rules, or open questions.

Inspect carefully. Point 3 should affect the operational plan/rule state, point 4 should appear as a current commitment, point 7 as a current operating/safety rule, points 2 and 5 should remain unresolved, and points 1 and 6 should not silently become policy.

If satisfied, the learner says:

> Keep this result. Commit and push it.

That explicit instruction overrides the standing review-stop default.

## Final proof

After the good Run 3 state is committed and pushed, start one fresh agent and ask:

> Inspect the Repair Café project as it exists now. Tell me which decisions, rules, and commitments from the latest planning meeting are reflected in the current project state, and which questions from that meeting remain unresolved.

If time permits, ask a fresh cloud agent through repository access too. This is a callback, not the organizing axis.

The lines to earn are:

> Preserve evidence honestly. Promote meaning deliberately.

> Don't make the agent guess which meeting chatter became project truth.

A secondary observation can be surfaced lightly:

> The project carried its routine operating conventions, so the learner did not have to keep rebuilding them in every prompt.

# Exercise 3 — Which truth wins?

## Learning goal

Make the project disagree with itself through believable, correctly scoped work.

Two agents can both do their assigned jobs correctly and still leave durable artifacts with different values for the same fact.

The exercise should create demand for authority rules without solving the authority system yet.

## Baseline

Run only after Exercise 2's good result has been committed and pushed. Verify a clean working tree.

The committed project should still contain the original 09:30-12:30 session time in `notes/current-decisions.md` and `working/pilot-plan.md`.

Do not pre-seed a visitor information sheet.

## Agent 1

Fresh agent:

> Using the current Repair Café project state, produce a short visitor information sheet with the practical information someone needs before attending. Save it as `output/visitor-information.md`. Review it for accuracy, then commit and push it.

Inspect it. This is a correct derived output at the time it is produced.

## Agent 2

Fresh agent:

> The Repair Café public session time has changed to 10:00-13:00. Update `notes/current-decisions.md` to reflect that new confirmed time. Do not inspect the rest of the project for other references; this is a deliberately scoped update. Change only that file, then commit and push it.

Do not mention the visitor sheet or hint that other copies exist.

This should naturally leave:

```text
notes/current-decisions.md
10:00-13:00

working/pilot-plan.md
09:30-12:30

output/visitor-information.md
09:30-12:30
```

Agent 2 has not necessarily made a reasoning error. It performed the bounded task it was given.

## Agent 3

Start fresh, preferably read-only, and ask only:

> What time does the Repair Café start?

Then:

> Show me the project evidence for that answer.

Then:

> Which truth is authoritative?

And:

> How did you decide that truth wins?

The important observation is not whether it chooses 10:00 or 09:30. It is whether the project contains an explicit authority rule supporting that choice.

Probe the policy it exposes:

- filename semantics: does `current-decisions.md` actually outrank other files, or did the agent infer that?
- recency/Git history: does newer always mean authoritative?
- public-facing output: why should an output outrank a file called current decisions?
- refusal to choose: what would the project need to say so the conflict could be resolved without guessing?

Do not force a canonical Agent 3 answer.

Earn:

> Persisted does not mean current.

> Durable does not automatically mean authoritative.

Leave unresolved:

> When the project disagrees with itself, how does an agent know what to trust?

Do not repair the contradiction during this exercise.

# Do not teach yet

Do not turn Lab 3 into:

- a deep Git lesson;
- a documentation taxonomy;
- an instruction-precedence lesson;
- a context-window or compaction lesson;
- a full source-of-truth governance lesson.

Exercise 3 deliberately creates demand for authority and source-of-truth rules. Preserve that demand for the later source-of-truth lab rather than solving the whole governance problem here.
