# Lab 3 — Exercise 3: Which truth wins?

The Repair Café project now contains durable decisions, meeting evidence, working plans, and outputs created from that state.

This exercise introduces a normal project problem: two agents can both do exactly what they were asked, yet leave behind durable artifacts that no longer agree.

Start only after Exercise 2's good result has been committed and pushed.

## Agent 1 — produce a visitor information sheet

Start a fresh agent conversation in the Repair Café project.

Ask:

> Using the current Repair Café project state, produce a short visitor information sheet with the practical information someone needs before attending. Save it as `output/visitor-information.md`. Review it for accuracy, then commit and push it.

Inspect the finished file before moving on.

At this point the visitor sheet should honestly reflect the project as it exists now.

End the conversation.

## Agent 2 — make a deliberately scoped update

Start a completely fresh agent conversation in the same project.

A confirmed operational change has arrived:

> The Repair Café public session now starts at 10:00 and finishes at 13:00.

Give Agent 2 a narrow maintenance task:

> The Repair Café public session time has changed to 10:00-13:00. Update only `notes/current-decisions.md` to reflect that new confirmed time. Do not search for or update other references. Commit and push that one-file change.

Agent 2 may warn you that changing only one file could leave other project artifacts stale. That is a good warning.

In normal project work, you would usually want the agent to find and update related references rather than knowingly leave the project inconsistent. For this exercise, though, we are deliberately creating that inconsistency so Agent 3 has a real conflict to investigate.

If Agent 2 warns you, acknowledge it and ask it to continue with the scoped change only:

> Yes, I understand that may leave other references stale. For this exercise, make only the scoped change I requested.

Inspect the change and confirm that Agent 2 did exactly the bounded job it was given.

Do not ask it to search for or repair anything else.

End the conversation.

## Agent 3 — ask a simple question

Start a third completely fresh agent conversation.

Keep this conversation read-only if your agent surface makes that convenient. The purpose is to inspect and reason, not repair anything yet.

Ask only:

> What time does the Repair Café start?

Let the agent answer before giving it any hint that there may be a problem.

Then ask:

> Show me the project evidence for that answer.

Inspect what it found.

Now ask:

> Which truth is authoritative?

Then:

> How did you decide that truth wins?

Do not rush to correct the project. Examine the rule the agent is using.

If it says that `notes/current-decisions.md` wins because it sounds authoritative, ask:

> Does the project explicitly say that file outranks the other files, or did you infer that?

If it relies on the most recently changed file or Git history, ask:

> Does newer always mean authoritative, or is that another inference?

If it prefers the visitor information sheet because it is public-facing, ask:

> Why should a visitor-facing output outrank a file explicitly called current decisions?

If it refuses to choose and reports the conflict, ask:

> What would the project need to tell you so you could resolve this without guessing?

There is no required Agent 3 answer. The important thing is to expose how it decided which durable artifact to trust.

## Reflect

Talk through:

- Did Agent 1 do anything wrong when it created the visitor sheet?
- Was Agent 2 right to warn about stale references if it noticed the risk?
- Why did we deliberately override that good warning for this exercise?
- How did the project nevertheless end up disagreeing with itself even though each agent followed its assigned task?
- Did Agent 3 discover an explicit authority rule, or construct one from clues?
- Would a reasonable agent always make the same choice?
- What happens as a project accumulates more outputs, summaries, plans, and historical artifacts?

This Repair Café project is tiny. There are only a handful of files and the contradiction is easy to inspect once you know to look for it.

Now imagine the project is organising a production of *Cats*: cast calls, rehearsal schedules, technical plans, venue arrangements, publicity, ticketing information, supplier details, and working notes can all repeat the same facts in different forms.

Then imagine organising Glastonbury Festival. The number of teams, suppliers, schedules, safety plans, artist information, transport arrangements, site operations, public communications, and derived outputs becomes enormous. A stale fact no longer sits conveniently beside the newer one waiting for a human to notice it.

At that scale, keeping project truth coherent stops being a tidiness problem. The project needs ways to communicate what is authoritative, what is derived, what is stale, and what should change when an important fact changes.

The key ideas are:

> Persisted does not mean current.

> Durable does not automatically mean authoritative.

And the uncomfortable question to leave open is:

> When the project disagrees with itself, how does an agent know what to trust?

Do not repair the contradiction yet. Leave it visible at the end of the exercise.
