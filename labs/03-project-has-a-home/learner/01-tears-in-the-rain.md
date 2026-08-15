# Lab 3 — Exercise 1: Tears in the rain

You are working in a small Repair Café planning project.

The project already contains some settled decisions, some source material, and one important question that has not yet been resolved.

For the first part of this exercise, you are only discussing ideas with the agent.

## Conversation 1 — decide without changing the project

Start a fresh local-agent conversation rooted at the Lab 3 project folder.

Before discussing the project, put the agent into a read-only or equivalent non-mutation mode if your agent surface provides one.

The point is simple: during this first conversation the agent may inspect and reason about the project, but the environment should not allow it to change project state.

Then ask:

> Inspect this project and help me think through the unresolved arrival and booking model. We're just discussing it for now.

Discuss the options with the agent until you reach a policy you are happy with.

Choose the policy yourself. There is no single answer hidden in the project.

Once you have decided, tell the agent clearly what the decision is and ask it to discuss the consequences while remaining in discussion mode.

For example:

> That's the decision: we'll use drop-in by default, with two pre-bookable accessibility slots each hour. Talk me through what that means for volunteers, queues, and how we should communicate the pilot. We're still only discussing it.

You do not have to choose that policy. Use the policy you actually decided on.

Make sure the agent understands the decision and can reason from it.

Do not ask it to record the decision anywhere yet.

If your agent surface has a visible Plan or read-only mode, leave it enabled throughout this conversation.

## The conversation is gone

Now treat the IDE or agent surface as having crashed.

The conversation is unrecoverable. Close it and do not consult it again for the rest of this exercise.

Starting a fresh conversation is what removes the conversational context. The earlier read-only boundary simply made sure that context could not leak into project files before the conversation disappeared.

## Conversation 2 — what survived?

Start a completely fresh local-agent conversation in the same project folder.

Keep this reconstruction step read-only as well.

Ask:

> Inspect this project. Tell me its current state, the important decisions that have been made, and the important questions that are still unresolved. Do not change anything.

Compare the answer with what you know happened in the previous conversation.

What important decision is missing?

## Recover the missing state

Tell the agent what you actually decided.

Now explicitly move out of discussion-only/read-only operation and allow project changes.

Then ask it to update the project so that another fresh agent can recover that decision later.

For example:

> We actually decided to use drop-in by default, with two pre-bookable accessibility slots each hour. That decision matters to the ongoing project. You may now modify project files. Persist the decision somewhere appropriate so another fresh agent can reconstruct the current state. Do not alter the source material.

Again, use your own decision rather than the example if you chose something different.

Let the agent decide where the decision belongs in the project.

Inspect the changes it makes.

## Conversation 3 — prove it survived

End Conversation 2.

Start a third completely fresh local-agent conversation in the same project folder.

Ask:

> Inspect the project from disk. Tell me its current state, the important decisions currently in force, and what remains unresolved.

Compare this answer with Conversation 2.

## Reflect

Talk through:

- Did the first agent understand your decision?
- Did it reason from that decision correctly?
- Why could the second agent not recover it?
- Was the second agent wrong according to the project state it could actually inspect?
- What changed between the second and third conversations?
- Did the third agent remember the previous conversation?
- Where did it actually find the decision?
- What did the read-only boundary guarantee that a prose instruction alone could not guarantee?

The important idea is:

> Decisions that exist only in conversation are tears in the rain.

And the practical version is:

> Important project knowledge should survive the conversation that created it.
