# Lab 4 — Exercise 2: Make a mess, then choose what survives

Start from a clean working tree.

This exercise is about letting the agent make a broad but reversible experiment, then deciding what is actually worth keeping.

Ask:

> Reorganise this production pack so a crew member arriving cold can understand the handover quickly. Improve structure, reduce needless duplication, and make related information easier to find. Make whatever project-file changes you think are useful, but leave everything uncommitted and unpushed for review.

Let the agent work.

## Inspect before trusting the summary

Do not begin with the agent's completion message.

Open the source-control/diff view first, or ask the agent to show you the diff.

Look at:

- which files changed;
- which lines were added or removed;
- whether anything moved;
- whether repeated information was removed or consolidated;
- whether the agent changed more than you expected.

Then read the agent's summary and compare it with what the diff actually proves.

Ask:

> Does your summary account for everything in this diff? Walk me through any change I might otherwise miss.

## Keep only part of the experiment

Choose some changes you like and some you do not.

A likely instruction is:

> Keep the crew-briefing and handover improvements, but put the venue and access notes back the way they were. Leave the result uncommitted.

If your agent changed a different set of files, adapt that instruction to what actually happened rather than forcing this exact wording.

Inspect the reduced diff again.

Ask yourself:

- Do I understand every remaining change?
- Is there anything still present only because the agent said it was useful?
- If I had to recover this state later, would this be a sensible save point?

When you are satisfied, tell the agent:

> Commit this result, but do not push it yet.

Stop there.

Do not align the remote repository yet. Exercise 3 begins from exactly this state:

```text
working tree
clean

local history
contains the reviewed Exercise 2 commit

GitHub fork
still ends at the previous published commit
```

That intentional gap is the starting material for the next exercise.

## Reflect

Talk through:

- Why was it reasonable to let the agent make a broad experiment?
- What limited the blast radius?
- Which artifact told you what actually changed?
- Was the prose summary enough by itself?
- Why did you wait until after review to commit?
- What would `Discard that run` have meant if you had rejected the whole experiment?
- What changed when you committed, even though you have not pushed anything yet?

Useful ideas:

> **Don't tell me you changed it. Show me the diff.**

> **A commit is a state you understand and want a recovery point for.**
