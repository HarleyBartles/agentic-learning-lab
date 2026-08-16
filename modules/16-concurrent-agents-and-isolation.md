# Module 15 — Concurrent agents and isolation

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

Module 12 introduces specialist workers but initially keeps delegation understandable and mostly sequential.

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
