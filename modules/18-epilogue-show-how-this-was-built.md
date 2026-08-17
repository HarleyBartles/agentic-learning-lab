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
- the branch commit messages and what they say each step contributed;
- how those commits relate to one another;
- the aggregate PR diff;
- reviews, comments, or acceptance evidence;
- the PR merge point relative to other mainline commits;
- the preserved remote branch where it still exists;
- which internal development steps were compressed out of `main` but remain queryable through the PR and branch.

This should expose a useful distinction:

> **Mainline history and pull-request history answer different questions.**

A squash merge can make `main` easier to read as a sequence of accepted changes while moving much of the richer development narrative into the pull request.

The learner should be able to compare the two surfaces:

```text
direct-main history
accepted chronology also exposes much of the development chronology

squash-merged PR history
main exposes accepted batch + integration point
PR exposes richer internal development chronology,
commit messages, branch lineage, and review surface
```

Do not frame this as `squash is better` or `squash destroys history`.

Instead ask:

- What question are we trying to answer?
- Which historical surface contains the evidence for that question?
- Did the agent stop at the squash commit and invent a development story, or did it follow the available evidence into the merged PR?

That final question deliberately reconnects to the curriculum's epistemic theme: an agent should not mistake a compressed surface for the whole available evidence set.

## Staged reveal — constrain, retrieve, then audit

Do not give the learner the richer history surface immediately. The information boundary is part of the lesson.

### Stage 1 — mainline only

Constrain the first investigation explicitly to history reachable from `main`.

Ask the agent to summarise the repository's evolution and to call out commits whose size, breadth, or shape make their internal development story difficult to establish from mainline evidence alone.

A useful prompt shape is:

> Inspect only the history visible from `main`. Summarise how the repository evolved. Call out any commits whose size or shape means you cannot confidently reconstruct how that change was developed from mainline history alone. Do not inspect pull requests or branch history yet.

The desired behaviour is not for the agent to guess that a large accepted commit was necessarily designed and implemented as one coherent step.

It should be able to say something like:

> I can establish what entered the accepted history, when it entered, and the combined files that changed. I cannot establish the internal development sequence from this surface alone.

Earn:

> **Mainline can explain the accepted state without necessarily explaining how that state was assembled.**

The mainline commit message matters here too. A squash commit may have a concise or deliberately opaque message that describes the accepted batch without exposing the granular decisions that produced it. The learner should notice that `one commit with one message` is a narrower explanatory surface than `many branch commits with their own messages`.

### Stage 2 — reopen retrieval

Now let the learner choose one surfaced under-explained mainline commit and expand the investigation.

Ask the agent to follow whatever repository relationships are available from that accepted change into its pull request, preserved branch, individual commits, commit messages, reviews, comments, and aggregate diff.

The shift should be visible:

```text
mainline-only view
one accepted change
one mainline commit message
final combined file set

        ↓ retrieve related repository surfaces

PR / branch view
ordered granular commits
richer commit messages
how decisions accumulated
aggregate proposed change
review / acceptance context
integration point back into main
```

The commit messages are part of the explainability gain, not decoration. They can expose intent and sequencing that the squash commit message does not contain.

A useful question is:

> Which things can you now explain from retrieved PR/branch evidence that you could not establish from `main` alone?

This is a direct callback to the curriculum's retrieval model:

> **The system can contain more evidence than the agent currently has in context.**

A mainline-only gap does not imply that the richer history never existed. It may mean the agent has not yet retrieved the surface that contains it.

### Stage 3 — audit the first explanation

Finally, ask the agent to compare its first mainline-only account with the expanded investigation.

Ask:

> Which of your earlier conclusions were confirmed, which became more precise, which were wrong, and which questions still cannot be answered from repository evidence?

This is the most important stage epistemically.

The learner should see that retrieval can:

- confirm a mainline inference;
- replace a vague story with an evidenced chronology;
- overturn a plausible but unsupported explanation;
- expose the contribution of individual branch commits through their messages;
- still leave causal questions unresolved when the rationale was never persisted.

The agent should not treat `more evidence` as `total explanation`.

## Facilitator-known fixture — PR #4

Preserve PR #4 as a known worked example for the eventual epilogue, but do not hand its number to the learner during the first-stage investigation.

PR #4 was deliberately squash merged after accumulating many granular commits that reshape the curriculum planning, including:

- splitting the original Module 6 plan into separate model-knowledge and domain-provisioning modules;
- renumbering the advanced half of the curriculum;
- adding branch and pull-request semantics to Module 17;
- adding the `tears in the rain` policy callback;
- adding workflow archaeology to the epilogue;
- adding the direct-main versus squash-merged explainability comparison;
- adding this staged retrieval exercise itself.

Its squash commit message on `main` was deliberately opaque. The remote branch should remain available after merge.

This makes PR #4 deliberately recursive teaching evidence:

```text
future mainline
one squash-merged accepted curriculum change
        ↓
learner notices that main alone under-explains its construction
        ↓
agent follows the commit to PR #4
        ↓
agent inspects ordered granular commits + rich commit messages
        ↓
agent reconstructs how the accepted curriculum change evolved
```

The learner should discover this path from repository evidence rather than being told `go inspect PR #4`.

The facilitator can later reveal that this was intentional: the PR which records the lesson about richer retrieval surfaces was itself preserved so its squash merge, pull request, branch, granular commits, and commit messages could become a worked example of that lesson.

Do not rely on PR #4 as the only possible specimen. When the epilogue is finally scaffolded, inspect the completed repository history and choose the strongest real examples that exist. PR #4 should remain an especially useful known fixture if its evidence surfaces are still available.

## Security callback — retrieval expands both evidence and attack surface

After the learner has used one opaque squash merge to discover the richer PR/branch explainability surface, have them investigate another under-explained squash merge from the completed repository history.

The construction history intentionally includes a harmless instruction-like message inside the granular commit history of one such change. Preserve the fixture, but do not identify its PR number, branch, commit SHA, exact wording, or location in this planning file. The learner should encounter it only by following the richer historical evidence.

The intended progression is:

```text
mainline-only investigation
        ↓
opaque accepted change is under-explained
        ↓
agent follows repository relationships into PR / branch history
        ↓
richer commit messages improve historical explainability
        ↓
one retrieved message also looks like an instruction to the investigating agent
```

The agent may ignore the instruction-like text, quote it, report it neutrally, or explicitly flag it as attempted prompt injection. Any of those are useful outcomes.

The exercise does **not** depend on a modern model actually obeying the embedded instruction.

The learner should already have the Module 16 mental model available:

> **Data from outside the trusted instruction boundary is evidence, not authority.**

Ask the learner what changed when the agent expanded its retrieval surface.

The answer is not only `it gained more historical evidence`.

It also gained more untrusted text capable of looking like instructions.

Earn:

> **Retrieval can increase both explainability and attack surface.**

And:

> **Provenance is not authority.**

A commit message can have excellent provenance. Git can establish that it genuinely exists in repository history, who authored the commit, where it appeared in branch chronology, and how it relates to a merged PR. None of that gives the sentence inside the message authority to rewrite the investigating agent's task.

Useful comparison:

```text
provenance
"this text really is part of repository history"

        ≠

truth
"everything the text claims is correct"

        ≠

authority
"the investigating agent should obey the text"
```

This is the security-side counterpart to the previous explainability lesson:

> Do not stop at an impoverished evidence surface when richer evidence is available.

followed immediately by:

> Do not mistake newly retrieved evidence for newly granted authority.

The learner, rather than the agent, should be the important recognition surface. Even if the agent merely lists the relevant commit message as historical evidence without reacting to it, the learner should be able to recognise that instruction-like repository text is data the agent was asked to inspect, not an authorised instruction source.

Only after the learner has recognised the pattern should the facilitator reveal that the construction history deliberately contained the harmless fixture.

Do not turn this into adversarial prompt-writing practice. It is a light callback that cements the trust-boundary model while showing that richer retrieval can improve epistemic position and widen exposure at the same time.

When the epilogue is finally scaffolded, inspect the completed repository history and confirm the strongest real fixture still has the intended evidence surfaces before designing the learner choreography around it.

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

- prescribe exact commits the agent must discover during the first-stage investigation;
- tell the learner to inspect PR #4 before the agent has surfaced it naturally;
- reveal where the security fixture lives before retrieval exposes it;
- manufacture a fixed historical narrative before the repository has finished evolving;
- turn the epilogue into a Git archaeology tutorial;
- imply that every important design decision is recoverable from history;
- treat a plausible causal story as proved merely because it fits the visible evidence;
- treat a compressed mainline surface as the complete available evidence set;
- treat retrieved repository text as instruction authority merely because its provenance is strong;
- claim that cloud or local work is inherently superior.

When the curriculum is close to complete, revisit this module against the actual final Git history and design the retrospective around the evidence that genuinely exists.