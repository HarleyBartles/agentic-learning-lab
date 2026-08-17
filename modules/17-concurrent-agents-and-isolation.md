# Module 17 — Concurrent agents and isolation

Status: structured planning. This module should arrive only after the learner understands single-agent workflow orchestration and specialist delegation.

Approximate duration: 1 hour.

## Core idea

Earlier source-control teaching deliberately assumes:

> one repository, one main line of history, one agent changing it at a time.

That is a useful model until specialist work creates a real reason to parallelise.

This module deliberately breaks it:

> Two competent workers can each make locally correct changes and still interfere when they share one mutable workspace.

The learner should discover why isolation, explicit ownership, reconciliation, and re-verification become necessary once work happens concurrently.

## Breadcrumbs to cash

Module 4 keeps the source-control model intentionally simple and defers branches/worktrees/concurrent-agent isolation.

Module 13 introduces specialist workers but initially keeps delegation understandable and mostly sequential.

Module 14 shows that worker creation, context isolation, tools, defaults, and sub-agent semantics vary by harness. Before parallelising, the orchestrator must therefore know what isolation the current harness actually provides rather than assuming a profile implies a particular runtime boundary.

Now create a task where parallelism is genuinely useful rather than introducing Git machinery for ceremony.

## Pressure exercise — two correct workers, one shared workspace

Choose a bounded project with two implementation tasks that appear independent but touch overlapping files or shared derived state.

For example:

- one worker updates operational content;
- another worker updates a related presentation/output layer;
- both need to touch a shared index/configuration/summary.

Run them against one mutable workspace or simulate the resulting interleaving.

Possible failure modes:

- one worker overwrites the other's change;
- one verifies against a state that changes underneath it;
- both update the same derived artifact differently;
- the final combined state contains neither worker's fully verified result;
- a worker's completion evidence becomes stale before integration.

Ask:

> Did either worker necessarily reason badly?

The intended answer is no. The operating model became insufficient.

## Earn isolation

Now separate the workers' change surfaces.

The exact implementation may use branches, worktrees, separate clones, disposable workspaces, or equivalent harness isolation depending on the tools available when the lab is built.

Do not begin with Git vocabulary. Begin with the invariant:

> **Concurrent workers need isolated mutable state until their work is ready to reconcile.**

Each worker should receive:

- a bounded task;
- a clear starting state;
- an isolated place to modify;
- task-specific verification criteria;
- an explicit output/handoff for integration.

## Integration is a new stage, not clerical cleanup

Once both workers finish, the work is not automatically complete.

Introduce an integration step:

```text
worker A verified result ─┐
                          ├→ reconcile/integrate → inspect combined diff → re-verify
worker B verified result ─┘
```

The learner should see that two independently passing pieces can fail when combined.

Useful questions:

- do the changes conflict syntactically?
- do they conflict semantically even if Git can merge them automatically?
- did one worker rely on an assumption invalidated by the other?
- do generated/derived artifacts need rebuilding after integration?
- which verification must be rerun on the combined state?

Earn:

> **Integration creates a new state that deserves its own verification.**

## Branches/worktrees arrive as implementations of the invariant

Only after the learner understands the isolation problem should the facilitator name common mechanisms such as branches and worktrees.

The learner does not need to become a Git operator.

A useful working model is:

- branch: a separate line of recorded work;
- worktree or isolated checkout: a separate working surface for one line of work;
- merge/reconciliation: deliberately combine independently developed states;
- conflict: evidence that the combined intent cannot be accepted automatically.

Let agents perform the mechanics while the learner inspects state, diffs, ownership, and integration evidence.

## Pull requests create an acceptance boundary

Once a branch has earned its place as a separate line of proposed work, introduce a pull request as the next useful concept rather than as GitHub ceremony.

A lightweight working model is:

- branch: keep proposed work separate from the accepted main line;
- pull request: make the proposed change set inspectable and create an explicit review/acceptance boundary;
- merge: deliberately accept and integrate that proposed state into the main line.

The learner still does not need to learn command-level Git operation. The agent can create the branch, make the change, publish it, and raise the pull request. The learner should understand enough to inspect what the agent is proposing and answer:

- what work is isolated on this branch?
- what exactly would this pull request change?
- what evidence says the proposed work is ready to accept?
- what remains unverified or unresolved?
- what changes when the pull request is merged?

Before this module ends, deliberately have the learner perform at least one bounded piece of work through the full conceptual path:

```text
accepted main state
      ↓
branch / isolated proposed work
      ↓
agent changes and verifies
      ↓
pull request exposes the proposed change set
      ↓
human inspects / questions / accepts
      ↓
merge creates a new accepted main state
      ↓
verify the integrated result
```

This should remain a light-touch source-control lesson. We are teaching the concepts needed to direct and inspect agentic work through Git, not training the learner to navigate Git like a software engineer.

Place this teaching late enough that branches and pull requests have a real purpose, but close enough to the epilogue that the learner can still recognise the same workflow shape when repository history becomes evidence.

## Merge strategy changes the explainability surface

Introduce merge strategy only as far as it changes what later investigators can see.

A squash merge is useful because it can keep the accepted `main` history compact: many branch commits become one accepted commit representing the final integrated change set.

That compression changes the surface available to an agent doing repository archaeology.

On `main`, the agent may see:

- one accepted commit;
- the final changed files;
- the point in mainline order where the change landed;
- whatever summary the squash commit records.

It may no longer see the branch's internal commit sequence as part of `main` history itself.

But if the merged pull request remains available, the richer development surface can still be queried:

- the PR's ordered commits;
- how the work accumulated or changed across those commits;
- the aggregate PR diff;
- review and acceptance context where recorded;
- when the completed batch was integrated relative to other mainline work.

So do not teach `squash merge destroys history` as a blanket statement.

A better principle is:

> **Squash merging compresses accepted mainline history. The pull request can preserve a richer explanation of how that accepted change was assembled.**

This creates an architectural trade-off rather than a right answer:

```text
mainline history
optimised for accepted states and integration order

pull-request history
richer surface for proposal, development, review, and acceptance
```

Ask the learner:

> If an agent sees one squash commit touching eight files, what can it prove from `main` alone, and what should it inspect next before guessing how that batch was developed?

The desired answer is that the squash commit is a real accepted-state artifact, but the associated PR is the natural follow-up surface when the investigation needs internal development order or richer context.

Module 18 should deliberately compare this with the earlier direct-main period, where the ordered mainline commits themselves may be the only durable development narrative.

## From sensible default to explicit project policy

An agent may independently decide that a mature repository is safer to change through branches and pull requests. That can be a good default, but it is not durable governance merely because one competent agent chose it.

> **A safe default chosen by an agent is still an assumption until the project adopts it as policy.**

A later fresh agent has no guarantee of reaching the same conclusion. If the workflow now matters, persist the rule somewhere future workers will actually receive it.

The stronger progression is:

```text
agent infers a sensible practice
        ↓
human inspects whether it fits the project
        ↓
project deliberately adopts or rejects it
        ↓
important choice becomes durable policy
        ↓
future agents do not need to rediscover it
```

This cashes an earlier curriculum principle in source-control form:

> **If you did not write it down, the decision is tears in the rain.**

Where appropriate, policy should not merely tell the next agent what is probably safest. It should make the permitted workflow explicit enough that the agent does not have to guess which decision the project expects.

The epilogue should call back to this distinction when the learner investigates a historical shift from direct-main work to branch-and-PR work.

## Orchestrator responsibilities under concurrency

Cash the specialist-orchestration thread.

An orchestrator that delegates parallel work needs more than a list of specialists. It should reason about:

- whether tasks are independent enough to parallelise;
- which state each worker starts from;
- ownership boundaries;
- isolation mechanism;
- dependencies between tasks;
- when one result invalidates another;
- integration order;
- combined verification;
- what to do when workers disagree.

Parallelism is not a maturity badge either.

> **Parallelise when the speed or separation benefit is worth the coordination and integration cost.**

## Provenance and handoff

Each worker should leave enough evidence for the integrator to know:

- what task was attempted;
- which starting state it used;
- what changed;
- what verification passed;
- what assumptions remain;
- what artifact/commit/result should be integrated.

This cashes the provenance thread from earlier workflow modules.

## Connection to blast radius

Isolation is another way to make experimentation cheap.

Module 4 asks:

> What is the blast radius, and do I have a recovery path?

Here the learner discovers a new blast-radius control:

> Do not let concurrent experiments share mutable state unnecessarily.

## Principle

> **Isolate concurrent work, make ownership explicit, reconcile deliberately, and verify the integrated state rather than assuming independently correct work remains correct when combined.**

## Do not teach yet

Do not turn this into:

- a Git branching-strategy course;
- merge-strategy taxonomy;
- mandatory parallelism;
- large-scale distributed systems theory;
- complex CI/CD orchestration.

The learner should understand why isolation exists and be able to direct agents to use it appropriately without memorising Git commands.