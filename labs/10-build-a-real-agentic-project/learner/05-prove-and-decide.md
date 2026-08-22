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