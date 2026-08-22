# 5 — Prove it and decide

Do not start with `the agent says it is done`.

Start with two questions from Lab 9.

## What source defines correct here?

For this project, that will usually be your approved intent plus any durable project decisions or requirements you chose to record.

The worker's latest output is not automatically the authority just because it is newest.

## What evidence would make you willing to accept the work?

For the default website, inspect at least:

- the rendered page in a browser;
- important links or interactions;
- more than one viewport size;
- the result against the intent you approved;
- the repository diff/history or current changed-file state;
- relevant checks the worker performed itself.

The worker should check its own work.

You still decide whether the evidence is enough.

Keep these boundaries separate:

```text
work is built
!=
work is accepted

work is accepted
!=
work is public

work is public
!=
other people have broad reuse rights
```

If you find a real defect, give the evidence back to the worker, let it repair the problem, and verify again.

When you are satisfied with the evidence, accept the result.

Then make a separate decision: do you actually want to publish it?

Publication is optional. A private, accepted project is still a completed capstone.

If you choose to publish, make sure you are comfortable with the content crossing the public boundary and that your visibility/licensing decisions still reflect what you intend.

## Course 1 reflection

Look back over the project and answer these in your own words:

- What did the model contribute?
- What did the agent harness make possible?
- What project state survived independently of conversation?
- What changed because you refined the proposal?
- Did extra domain expertise change the result?
- What evidence made you accept the work?
- Which decisions did you delegate?
- Which decisions remained yours?
- Did you repeat any stable guidance enough that it may deserve a durable home?

You do not need to remember every technical term.

A useful Course 1 endpoint is being able to say:

> **I can give an agent a real project, make important state durable, give it useful capabilities and expertise, steer it through results rather than manually implementing the work, check what it actually did, and decide whether I accept or publish it.**

## Return to the first invitation

At the start of Course 1, before you gave Codex its first task, you wrote down the exact invitation it showed while waiting for you to begin.

Find that wording now.

If the product wording has changed since then, keep the original wording you recorded. The comparison is about how *you* read the invitation, not about preserving a particular interface string.

Read it again and ask yourself:

- What did I think this question was asking me at the beginning?
- What did I think I needed to know before I could answer it?
- What did I think `we` meant?
- What do I think `we` means now?
- Do I still feel that I need to know exactly what can be built or how to build it before beginning?
- Could `I don't know yet — help me work out what would be worth building` now be a perfectly good answer?

At the beginning, a simple invitation may have hidden a pile of unanswered questions:

```text
What can we build?
What can't we build?
What does "we" mean?
How much do I need to build?
How much can the agent build for me?
How do I know whether the result is right?
```

At the end of Course 1, the same invitation can mean something much simpler:

> **What outcome should we work toward together?**

You bring intent, judgment, authority, preferences, and acceptance.

The agent brings proposal, exploration, implementation capability, and self-review.

The project carries durable state, instructions, sources, history, and constraints.

Together you iterate until there is enough evidence for you to accept the result.

The interface did not need to become more complicated. Your understanding of the collaboration did.

> **At the beginning of the course, the opening invitation sounded like a question you were expected to know how to answer. Now it can sound like the beginning of a collaboration.**
