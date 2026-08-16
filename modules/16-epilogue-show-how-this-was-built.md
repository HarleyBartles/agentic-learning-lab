# Module 16 — Epilogue: show how this was built

Status: early planning. Preserve the intent and evidence requirements without pretending the session is fully designed yet.

## Core idea

End the curriculum by using this repository itself as the worked example of the methodology the learner has just been taught.

The learner should discover that the Agentic Learning Lab did not begin as a fully specified framework. It emerged iteratively from a vague goal, repeated agent work, human inspection, questioning, explanation, correction, and persistence.

The final retrospective should make the curriculum's central methodology visible in its own history:

> **Learner instruct -> Agent do -> Learner inspect, verify and question -> Agent explain -> Learner instruct again.**

And:

> **The learner can use agents to accomplish things before fully understanding the implementation, while using the work itself to progressively build that understanding.**

## Session shape — show, don't merely tell

This should be a show-and-tell session rather than another conventional concept lab.

Do not begin by having the facilitator narrate the whole origin story.

First, have the learner direct an agent to inspect the repository and its Git history.

A suitable prompt direction is:

> Inspect this repository and its Git history. Work out how it developed from its earliest state into the curriculum that exists now. Show me the major stages, important changes in direction, ideas that were added or removed, and evidence for your conclusions.

The agent should use repository state and Git history as evidence rather than inventing a neat retrospective from the current tree alone.

The learner should inspect and question the agent's reconstruction just as they have learned to inspect any other agent output.

Useful questions:

- What was present in the earliest repository state?
- Which ideas appeared first as rough planning and later became mature labs?
- Which planning files disappeared after their ideas were promoted into stable lab structures?
- Where did the curriculum visibly change direction?
- Which assumptions were simplified early and later made more nuanced?
- What can Git history prove?
- What can Git history not tell us about why a decision was made?

## Compare two histories

If the learner has worked from their own fork throughout the curriculum, inspect two different histories:

```text
upstream curriculum history
how the teaching framework itself evolved

learner fork history
how this learner actually moved through and modified their laboratory
```

These histories are related but answer different questions.

The learner's fork can show their experiments, recoveries, persisted decisions, configuration changes, and later ownership of agent instructions/workflows.

The upstream history can show how the curriculum's own mental models, labs, fixtures, and principles evolved.

Neither history is complete memory of the conversations or motives that produced it.

## Facilitator reveal — the missing origin context

After the learner has investigated the repository history, the facilitator supplies the part Git cannot reconstruct by itself: the original conversational starting point.

The curriculum began with a vague, conversational request rather than a specification.

The learner should be shown the first prompt **verbatim**, from `docs/learning-methodology.md`.

Do not rewrite it into a cleaner brief before the reveal.

The contrast is the point:

```text
starting point
"I want to teach my brother some AI stuff"
+ partial intuitions
+ assumptions that later changed

versus

finished repository
structured labs
fixtures
facilitator doctrine
learner exercises
cross-cutting principles
recovery and verification models
```

The learner should see that the finished framework did not have to be known in advance.

## Minimal manual setup is part of the proof

Preserve this history accurately.

At the point when the early mature curriculum and Lab 4 planning had been built, Harley's direct manual setup had been small:

1. create the repository;
2. connect it to the GitHub connector;
3. converse with the agent, inspect work, question it, reject or refine ideas, and authorize repository changes.

The substantial repository work itself was performed through cloud ChatGPT over the GitHub connector.

An on-disk agent had not been required to produce the mature framework that existed at that stage.

Use this to deliberately break any residual `on-disk good, cloud bad` interpretation of the earlier labs.

The correct conclusion is:

> Different agent surfaces are useful for different work. This repository became substantial through a cloud agent with an appropriate bridge to its source of truth.

The important capability was not manual button pressing or writing files by hand. It was critical steering.

## The facilitator did not already know the final answer

The learner may reasonably think:

> Sure, but Harley already knew how to build all this.

The more useful truth is:

> Harley knew enough to drive the process critically. He did not need to know the complete shape of the finished thing before beginning.

The facilitator brought experience, judgment, examples, corrections, preferences, and domain knowledge. The agent proposed, wrote, reorganised, and persisted implementation. The framework emerged from the loop between them.

This should be connected directly to the learner's future work:

> You do not need to know the complete implementation before you start. You need enough judgment to state a goal, inspect what happens, ask good questions, notice when something is wrong, and keep steering.

## Git history is evidence, not complete memory

The retrospective should also expose the limits of repository archaeology.

Git can show:

- what changed;
- when recorded states changed;
- which files appeared, moved, changed, or disappeared;
- commit messages and other recorded project evidence.

Git does not necessarily show:

- the complete conversation that caused a decision;
- rejected alternatives that were never persisted;
- reasoning that existed only temporarily in chat;
- facilitator context that was never written into the project.

This creates a natural callback to earlier curriculum principles:

> The conversation is not the project.

> Important knowledge survives when it is persisted somewhere future workers can inspect.

> Prefer evidence over confident prose.

The learner should compare the agent's historical reconstruction with the facilitator's oral account and ask what is evidenced, what is inferred, and what was lost because it never entered durable state.

## Desired final realisation

The repository should function as proof of the method, not merely as course material.

The final message is approximately:

> Start before you know everything.
>
> Give the agent a real goal and an environment where useful work can happen.
>
> Inspect what it does.
>
> Verify the result.
>
> Ask why.
>
> Correct it.
>
> Persist what matters.
>
> Then instruct again.

The learner can apply this loop to goals the curriculum itself never teaches directly, including learning to code.

## Do not over-design yet

This module intentionally records the destination rather than a finished runbook.

Do not yet:

- prescribe exact commits the agent must discover;
- manufacture a fixed historical narrative before the repository has finished evolving;
- turn the epilogue into a Git archaeology tutorial;
- imply that every important design decision is recoverable from history;
- claim that cloud or local work is inherently superior.

When the curriculum is close to complete, revisit this module against the actual final Git history and design the retrospective around the evidence that genuinely exists.
