# Module 10 — Agent self-introspection and local review

Status: structured planning. This module turns a technique first encountered incidentally in Module 6 into a deliberate agentic-engineering primitive before workflow loops, graphs, and specialist delegation are introduced.

Approximate duration: 1 hour.

## Core idea

An agent can be asked to reason about its own likely behaviour under a deliberately described state: a fresh arrival in a workspace, a closed-book version of itself, a worker receiving a risky task, a reviewer encountering work it did not supposedly author, or an agent operating after a new instruction or skill has been added.

This is useful because it gives the agentic engineer a cheap local probe before paying the cost of a fresh context, sub-agent, isolated worker, or larger orchestration step.

A useful principle to earn:

> **Ask the agent to model the agent-state you care about, use that self-introspection to form a behavioural hypothesis, then test the hypothesis when stronger evidence is justified.**

Do not teach this as magical access to hidden model state or a reliable transcript of internal reasoning. The agent is constructing a useful counterfactual from the instructions, environment, skills, task, and knowledge available to it.

## Callback to Module 6

Module 6 should be the learner's first encounter with the technique, without naming it as a full engineering pattern yet.

The learner asks a closed-book agent questions about knitting and crochet, predicts what it may know, asks it to reason about the edge of its knowledge, and observes how it handles a premise that may be false or historically anachronistic.

That exercise already contains the primitive:

```text
ask the agent what it expects to know / how it expects to behave
        ↓
put it under the described constraint
        ↓
observe what actually happens
        ↓
compare self-model with behaviour
```

Module 10 now makes the technique explicit and reusable.

Useful line:

> **An agent can be used as an instrument for interrogating the agent system itself.**

## Distinguish introspection from proof

Start with the central caveat.

A self-introspective answer is a behavioural hypothesis, not proof that a fresh agent will actually behave that way.

The current agent may know things a future worker will not know. It may remember why a rule or skill was written. It may overestimate how discoverable a trigger is. It may reconstruct an intended route more cleanly than a genuinely fresh worker would.

Therefore teach an evidence ladder:

```text
self-introspection
cheap prediction from the current context
        ↓
fresh-context or sub-agent simulation
cleaner behavioural test with less authoring contamination
        ↓
real bounded execution
observed behaviour under the intended conditions
        ↓
verification
compare outcome with explicit success criteria
```

The point is not to always climb the whole ladder. The point is to know which rung is enough for the risk and uncertainty of the task.

> **Do not spend an isolated worker when a cheap local self-review is sufficient. Do not treat cheap local self-review as independent evidence when isolation matters.**

## Exercise 1 — predict a fresh agent's first move

Use the learner's real project from Module 9.

Add or strengthen one clear, binding project instruction in the root `AGENTS.md`. The instruction should have an observable consequence on a fresh agent's first relevant turn.

Before actually starting a fresh agent, ask the current agent something like:

> Introspect as a new agent arriving in this workspace on your first turn with no conversation history. Based on the workspace you would discover, what is the first action you would take and which instruction would cause it?

The learner should see that the current agent can construct the fresh-arrival state and predict the behaviour the environment is intended to cause.

Ask:

- What did the agent inspect in order to answer?
- Which instruction did it think would bind the new worker?
- Did it identify the expected first action?
- Have we proved the future worker will actually do that?

Earn:

> **Self-introspection can cheaply test whether the environment makes the intended behaviour legible to an agent.**

Then, where practical, start a genuinely fresh context or worker and compare the prediction with observed behaviour.

If they differ, treat the mismatch as useful engineering evidence rather than as embarrassment.

## Exercise 2 — introspect a newly created safeguard

Use a harmless fixture representing a risky or consequential action.

Have the agent create or modify a small skill/workflow whose trigger should naturally apply to that action and whose procedure mitigates the risk.

The authoring agent now has unusually strong knowledge of the skill because it just wrote it.

Ask it:

> Introspect as though you have now been given this risky task and must complete it. Assume you must invoke any skills that would naturally be discovered as applicable. Which skills do you expect to discover, what route do you expect to follow, and where would the safeguard change your behaviour?

This is useful precisely because the agent can reason across:

```text
task shape
→ skill trigger
→ skill discovery
→ procedure
→ expected behavioural change
```

But now challenge the result:

> Would a fresh worker that did not author this skill discover it as reliably as you expect?

This exposes authoring contamination.

If the consequence matters, hand the same bounded task to a fresh sub-agent or clean context and observe whether the skill is actually discovered.

The lesson is not `always spawn a reviewer`.

It is:

> **Use self-introspection as the cheapest plausible test; buy cleaner context separation when the question requires stronger evidence.**

## Agent introspection is not sub-agent simulation

Keep these concepts separate.

### Self-introspection / counterfactual self-simulation

The current agent reasons about another plausible state of itself or another worker.

Benefits:

- nearly zero orchestration overhead;
- retains rich local understanding of the environment;
- excellent for catching obvious omissions, routing problems, missing instructions, likely misunderstandings, and cheap review findings;
- useful inside tight loops.

Limitations:

- inherits the current context;
- may know the intended answer;
- may preserve assumptions from authoring/implementation;
- is not independent review.

### Fresh context or sub-agent simulation

Another worker actually receives a cleaner or differently provisioned context.

Benefits:

- stronger context separation;
- less contamination from the current worker's narrative;
- can test discoverability and handoff quality more realistically;
- useful when independent perspective is the thing being purchased.

Costs:

- context transport and handoff overhead;
- extra worker/tool cost and latency;
- more provenance/state to manage;
- may be unnecessary for cheap obvious corrections.

Useful decision question:

> **What does isolation buy us here that a local self-review does not?**

## Exercise 3 — cheap local self-review

Give the agent a bounded artifact or change to produce.

Before asking for independent review, ask the same agent to deliberately change epistemic posture.

Useful prompt shapes:

> Introspect as a fresh reviewer arriving after this work was completed. What assumptions would you challenge first?

> Assume this result contains a material defect. What is the strongest plausible reason it could fail its stated success criteria?

> Re-read the requirement as though you had not authored the implementation. Which part of the result is least well justified by evidence?

The agent may catch an obvious defect cheaply.

If it does, repair and verify inline.

If it remains uncertain, the work is consequential, or contamination from the implementation narrative is itself a meaningful risk, escalate to a genuinely isolated reviewer later in the curriculum.

This creates a practical review ladder:

```text
local self-check
        ↓ sufficient
repair / verify inline

        ↓ insufficient or high-risk
clean-context review

        ↓ role/context separation materially valuable
specialist reviewer
```

Module 12 will later deepen why a specialist reviewer can be worth the coordination cost. Do not prematurely teach that every review requires a second agent.

## Exercise 4 — test-first thinking as another local primitive

Introduce TDD as a broader agentic-engineering discipline rather than only a coding technique.

The transferable idea is:

> **State what observable evidence would prove success before asking the agent to make the change.**

Coding example:

```text
write or identify failing test
→ implement
→ test passes
→ review
```

Technical-drawing example:

```text
state dimensional / representation checks
→ produce drawing
→ run deterministic checks
→ inspect render
```

Document example:

```text
state required claims, sections, constraints, and prohibited drift
→ draft
→ check against the contract
→ inspect and revise
```

Agent-behaviour example:

```text
state expected safeguard behaviour
→ introspect predicted route
→ run bounded behavioural test
→ observe whether safeguard triggers
```

Do not force software red/green/refactor terminology into every domain. Preserve the underlying discipline: define observable success before modifying the system that is meant to satisfy it.

## Build the local agentic-engineering toolbag

By the end of this module, the learner should have a small set of cheap primitives they can deliberately ask an agent to perform inline:

```text
introspect a counterfactual state
predict likely behaviour
challenge the task premise
challenge its own assumptions
state success criteria first
self-review
inspect evidence
repair a bounded defect
retry once when justified
identify when stronger isolation is worth paying for
```

These are not a workflow yet.

That distinction matters.

The learner is currently choosing and invoking the primitives manually.

## Bridge into workflows, loops, and graphs

End by making the repetition visible.

Ask:

> We keep asking the agent to act, inspect itself, test the result, repair if needed, and decide whether to continue or escalate. What happens when that sequence becomes a normal way this project should work?

Draw the smallest loop:

```text
act
→ self-review
→ verify
→ pass: continue
→ fail: repair
      ↺ review again
```

Then ask what happens when there are several stages, several possible return routes, human gates, stop conditions, or escalation paths.

Do not teach the full answer here.

The next module should cash the need:

> **Local agentic primitives become workflow when we deliberately compose them into repeatable transitions, loops, gates, and legal routes.**

That is the handoff into autonomous human-in-the-loop workflows.

## Connection to later specialist delegation

Leave another question unresolved:

> When is the current agent's own self-review enough, and when is the cost of a clean independent worker justified?

The learner should already have the first half of the answer:

- use local self-review for cheap obvious pressure-testing;
- use stronger separation when different context, permissions, expertise, or independence buys something material.

The specialist-agent module later formalises that tradeoff.

## Principles

> **Agent self-introspection is a cheap local engineering probe, not proof of independent behaviour.**

> **Introspect → predict → test → observe → compare.**

> **Use the cheapest review surface that can establish what you need to know.**

> **Define observable success before changing the system that is supposed to produce it.**

> **Escalate from self-review to context isolation or specialist review because the separation buys something, not because more agents look more sophisticated.**

## Do not teach yet

Do not turn this module into:

- claims that the model can inspect its training corpus or hidden internal state;
- chain-of-thought extraction;
- a claim that self-reported behaviour proves future behaviour;
- mandatory sub-agent review;
- full workflow graphs;
- specialist-agent orchestration;
- a software-only TDD lesson.

The learner should leave with a practical instinct: before adding orchestration, another worker, or another human interruption, ask whether the current agent can cheaply introspect, challenge, test, or review enough of the problem locally.