# Module 18 — Epilogue: show how this was built

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

> Inspect this repository and its Git history. Work out how it developed from its earliest state into the curriculum that exists now. Show me the major stages, important changes in direction, ideas that were added or removed, changes in working practice that are visible in the shape of history, and evidence for your conclusions.

The agent should use repository state and Git history as evidence rather than inventing a neat retrospective from the current tree alone.

The learner should inspect and question the agent's reconstruction just as they have learned to inspect any other agent output.

Useful questions:

- What was present in the earliest repository state?
- Which ideas appeared first as rough planning and later became mature labs?
- Which planning files disappeared after their ideas were promoted into stable lab structures?
- Where did the curriculum visibly change direction?
- Which assumptions were simplified early and later made more nuanced?
- Did the way work entered the repository appear to change over time?
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

The upstream history can show how the curriculum's own mental models, labs, fixtures, principles, and working practices evolved.

Neither history is complete memory of the conversations or motives that produced it.

## Workflow archaeology — what, when, how, and why

Preserve a specific historical pattern for the final lab.

This teaching repository began with a long period of direct-main work. Later, branch-and-pull-request shaped work becomes visible in the Git history through branch commits and merge commits. By the time the final lab is scaffolded, inspect the actual completed history rather than freezing exact commit IDs now, but deliberately ask the learner's agent to find and explain this workflow transition.

The learner should be able to answer from repository evidence:

1. **What happened?** The repository moved from direct changes on the accepted main line toward proposed work being developed separately and accepted through pull requests/merges.
2. **When did it happen?** Identify the earliest defensible transition point from the actual history and show the supporting evidence.
3. **How did work change from that point onward?** Explain the new separation between proposed work and accepted main state, the review/acceptance boundary, and the resulting integration stage.

Then ask a fourth question:

> **Why did that workflow change at exactly that point?**

Git history alone may not be able to answer it.

This is a deliberate epistemic exercise, not a trick question.

> **Repository topology is evidence of process, not a complete explanation of intent.**

The learner should distinguish at least four states:

- directly evidenced by repository history;
- strongly inferred from repository evidence;
- facilitator-supplied causal context;
- genuinely unknown or unrecoverable.

If the agent says something like:

> The team decided to adopt pull requests because the repository had become mature and this was safer.

that may be a strong theory, but it is not automatically a proved fact. Ask:

- Which part of that sentence is visible in the history?
- Which part is inference?
- What alternative causes fit the same evidence?
- Did the agent have the full picture?
- Did it weight one clue more strongly than the evidence warrants because it wanted a coherent explanation?
- Is the apparent gap a gap in reality, a gap in the available evidence, or a gap in the agent's retained knowledge?

This should call back to the earlier uncertainty and model-reliability lessons: a confident explanation is not evidence merely because it is plausible.

## Compare explainability surfaces — direct mainline versus squash-merged PRs

Use the repository's own history to compare not just workflows, but the surfaces available to an investigating agent.

### Direct-main period

During the early direct-main period, the accepted mainline commit sequence is also much of the visible development sequence.

Ask the agent to investigate questions such as:

- can you establish the order in which changes happened?
- which commits appear related to each other?
- which ideas were introduced incrementally?
- where did one commit clearly build on or revise an earlier one?
- what can you infer from many small commits touching one or a few files at a time?

The mainline history may be comparatively verbose, but the agent can often reason directly over its chronology because the development steps themselves are visible on the accepted line.

### Squash-merged PR period

Then inspect a later pull request that was squash merged.

From `main` alone, the branch's internal development may appear compressed into one accepted commit containing the final combined file changes.

Ask:

> If the mainline only shows one squash commit, did we lose the ability to investigate how that accepted change was built?

Not necessarily.

Have the agent follow the accepted commit back to the merged pull request and inspect the richer PR surface where available:

- the PR's ordered branch commits;
- how those commits relate to one another;
- the aggregate PR diff;
- reviews, comments, or acceptance evidence;
- the PR merge point relative to other mainline commits;
- which internal development steps were compressed out of `main` but remain queryable through the PR.

This should expose a useful distinction:

> **Mainline history and pull-request history answer different questions.**

A squash merge can make `main` easier to read as a sequence of accepted changes while moving much of the richer development narrative into the pull request.

The learner should be able to compare the two surfaces:

```text
direct-main history
accepted chronology also exposes much of the development chronology

squash-merged PR history
main exposes accepted batch + integration point
PR exposes richer internal development chronology and review surface
```

Do not frame this as `squash is better` or `squash destroys history`.

Instead ask:

- What question are we trying to answer?
- Which historical surface contains the evidence for that question?
- Did the agent stop at the squash commit and invent a development story, or did it follow the available evidence into the merged PR?

That final question deliberately reconnects to the curriculum's epistemic theme: an agent should not mistake a compressed surface for the whole available evidence set.

## Same visible shift, different causes

The teaching repository and learner fork should deliberately provide a useful contrast.

### Upstream teaching repository

The historical workflow shift was not initially a consciously adopted project policy.

Facilitator backfill to preserve for the final lab:

```text
first cloud session
repo did not exist when the session began
→ working assumption remained "we are initialising this repository"
→ connector-backed work kept committing directly to main

fresh cloud session
encountered an already substantial repository
→ independently inferred that branch + pull request was the safer maintenance posture
```

The visible Git transition is real. The immediate causal explanation above is facilitator knowledge and should not be presented as something Git itself proves.

This makes the transition particularly valuable: a sensible workflow appeared because a fresh agent made a different environmental inference.

### Learner fork

Engineer an analogous visible transition in the learner's own history, but make its cause deliberately different.

Earlier labs use the intentionally simple mainline mental model. Module 17 then earns branches and pull requests through isolation, review, and integration pressure. At that point the learner deliberately changes the fork's contribution policy from direct-main work to branch-and-PR work.

The learner's agent should therefore be able to infer the same broad **what**, **when**, and **how** pattern from both histories, while the facilitator can reveal two different answers to **why then?**

```text
upstream
workflow changed because a fresh agent inferred a safer default

learner fork
workflow changed because the learner deliberately adopted a new policy
```

Use the contrast to ask:

- Did we decide to change policy, or did an agent assume a sensible policy for us?
- When is an inferred safe default sufficient?
- When should a useful inference become explicit project doctrine?
- Why might a small new repository reasonably tolerate direct-main work while a mature or multi-worker repository benefits from a stronger acceptance boundary?
- What do we gain by making the policy explicit instead of relying on each new agent to rediscover it?

## Tears in the rain — inference is not durable policy

Cash the earlier persistence lesson here.

A fresh agent may make an excellent decision. Unless that decision is persisted in a surface future workers actually receive, the next agent has no guarantee of reaching the same conclusion.

> **A safe default chosen by an agent is still an assumption until the project adopts it as policy.**

And:

> **If you did not write it down, the decision is tears in the rain.**

The point is not merely that documentation is nice to have. It is that agent reliability changes when an important choice moves from `please infer the safest behaviour` to `this project has an explicit rule`.

Where the workflow must be consistent, the strongest version may define not just the preferred decision but the only permitted one unless an authorised human changes policy.

This gives the learner a concrete reason for durable project instructions:

```text
one agent makes a good inference
        ↓
project notices the inference is worth keeping
        ↓
rule is persisted as project policy
        ↓
future agents receive the decision instead of having to recreate it
```

Module 17 should have introduced the branch/PR concepts shortly before this callback so the learner is recognising a familiar workflow pattern rather than relearning Git terminology during the final session.

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
- commit messages and other recorded project evidence;
- changes in the visible shape of how work was integrated.

Git does not necessarily show:

- the complete conversation that caused a decision;
- rejected alternatives that were never persisted;
- reasoning that existed only temporarily in chat;
- facilitator context that was never written into the project;
- why an apparently sensible workflow change happened at that exact moment.

This creates a natural callback to earlier curriculum principles:

> The conversation is not the project.

> Important knowledge survives when it is persisted somewhere future workers can inspect.

> Prefer evidence over confident prose.

The learner should compare the agent's historical reconstruction with the facilitator's oral account and ask what is evidenced, what is inferred, what is merely a strong theory, and what was lost because it never entered durable state.

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
- treat a plausible causal story as proved merely because it fits the visible evidence;
- claim that cloud or local work is inherently superior.

When the curriculum is close to complete, revisit this module against the actual final Git history and design the retrospective around the evidence that genuinely exists.