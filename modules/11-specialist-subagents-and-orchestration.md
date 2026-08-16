# Module 11 — Specialist sub-agents and orchestration

Status: structured planning. Preserve the conceptual progression and tradeoffs now; exact product mechanics and lab implementation should be verified later.

Approximate duration: 1 hour.

## Core idea

The previous module teaches one provisioned agent to carry work through a disciplined lifecycle: clarify, design, plan, execute, self-review, and hand off to the human at meaningful gates.

This module deliberately breaks the next useful mental model:

> One competent agent can perform every stage itself.

Ask what changes when the same worker is responsible for understanding the problem, designing the solution, planning the work, implementing it, and reviewing its own assumptions.

The learner should discover that specialist agent profiles can package different combinations of role, instructions, tools, domain scope, permissions, workflows, and quality criteria, and that an orchestrating agent can delegate work to the profile best suited to a stage or task.

The goal is not to teach that multi-agent work is inherently superior.

A useful principle to earn is:

> **Delegation is a design choice, not a maturity badge.**

## Start from the previous lab's success

Begin by recalling the end state of the autonomous-workflow lab.

The single agent could already:

- discover missing requirements;
- produce and self-review a specification;
- hand off for human approval;
- produce and self-review a plan;
- execute bounded tasks;
- verify each task;
- perform whole-work review;
- hand off for final human approval;
- publish/merge and clean up after authorization.

Do not undermine that achievement.

Ask instead:

> Is there any reason we might not want the same worker doing every one of those jobs?

Let the learner propose weaknesses before introducing specialist profiles.

Possible pressures include:

- the implementer carries its own design assumptions into review;
- different stages benefit from different tools;
- some stages need broader context while others benefit from narrower context;
- permissions appropriate for implementation may be excessive for review;
- a domain specialist may know more than the general worker;
- independent review can catch self-confirming errors;
- large tasks may benefit from parallel or isolated work;
- orchestration overhead may outweigh these benefits on small work.

## Break the earlier Agent model carefully

Earlier in the curriculum, it is useful for the learner to treat the provisioned worker/environment as `the Agent`.

Now make the distinction more precise.

A broad project environment may provide shared capabilities and state:

```text
shared environment
- project state
- tools
- connectors
- source/reference material
- reusable skills
- permissions infrastructure
- verification mechanisms
```

Within that environment, a specialist agent profile can bind a more specific working identity:

```text
agent profile
- role
- instructions
- preferred/relevant skills
- permitted tools
- domain scope
- context expectations
- quality criteria
- operating boundaries
```

When invoked for a task, that profile becomes a specialist worker for that piece of work.

Do not present this as a contradiction that invalidates earlier teaching.

The earlier model was useful at the earlier level of abstraction. This module exposes a case where it is no longer precise enough.

## Suggested specialist roles

Use a small number of roles that map directly onto the workflow the learner already understands.

For example:

```text
designer
- explores requirements and tradeoffs
- produces design/specification
- does not publish implementation

planner
- consumes approved design
- decomposes it into executable work
- identifies dependencies and verification steps

implementer
- consumes approved plan tasks
- performs bounded execution
- verifies local acceptance criteria

reviewer
- independently evaluates completed work
- should not inherit implementation assumptions unnecessarily
- checks against approved design and plan
```

The exact names are less important than the meaningful differences in role and operating conditions.

## The orchestrator

The primary agent now takes on a new role: workflow orchestrator.

It should know that specialist profiles exist, what they are for, and how to select between doing work inline and delegating it.

A useful model:

```text
human
  ↓
orchestrator agent
  ├─ designer
  ├─ planner
  ├─ implementer
  └─ reviewer
```

The orchestrator remains responsible for the lifecycle and handoffs, while specialist workers perform bounded stages or tasks.

The learner should understand that specialists are not magical personalities. They are deliberately provisioned workers.

Useful question:

> What is actually different between these workers besides their names?

If the answer is `nothing`, the specialisation is mostly theatre.

Meaningful specialisation should usually involve some combination of different:

- instructions;
- context;
- tools;
- permissions;
- skills;
- domain material;
- verification criteria;
- responsibilities.

## Teach the orchestrator that specialists exist

A specialist is only useful if the orchestrating agent can discover and select it appropriately.

The environment should expose a clear catalogue or operating description, conceptually like:

```text
available specialists

designer
use for ambiguous requirements, design choices, and tradeoff analysis

planner
use after design approval to turn the approved design into executable tasks

implementer
use for bounded implementation work

reviewer
use for independent verification of completed work
```

The orchestrator needs a selection policy, not merely a list.

A useful question is:

> Do I have enough context and competence to do this inline, or does this stage benefit from a specialist profile?

Avoid teaching `always delegate`.

## Worked comparison — inline versus delegated execution

Use a task whose lifecycle has already been understood in the previous module, or a comparable fresh fixture if repeating that domain would add no conceptual value.

Run or inspect two versions:

### Version A — one agent does everything

```text
orchestrator/worker
→ design
→ plan
→ implement
→ review
```

### Version B — orchestrator delegates meaningful stages

```text
orchestrator
→ designer
→ planner
→ implementer
→ reviewer
```

Keep human approval gates where they were already justified.

Compare the resulting work and process rather than assuming a winner.

## Benefits and drawbacks of specialist delegation

The learner should explicitly discuss both sides.

### One agent doing the work inline

Potential benefits:

- less handoff overhead;
- less duplicated context;
- simpler state management;
- lower orchestration complexity;
- often lower cost and latency;
- useful continuity across stages.

Potential drawbacks:

- assumptions can persist unchallenged across stages;
- self-review may confirm the worker's own interpretation;
- one context may become overloaded;
- broad permissions may be carried into stages that do not need them;
- a general worker may be weaker than a specialist in a narrow domain.

### Delegating to specialists

Potential benefits:

- role separation;
- different tools/permissions per worker;
- narrower relevant context;
- independent review;
- specialist domain knowledge;
- clearer bounded responsibilities;
- potential for isolation or parallelism later.

Potential drawbacks:

- handoff loss;
- duplicated context;
- stale assumptions between workers;
- orchestration complexity;
- disagreement between workers;
- additional cost/latency;
- more state and provenance to manage.

Intended conclusion:

> **Use delegation when the separation buys something worth the coordination cost.**

## Handoff contracts matter

The learner already understands that skills can harmonise through artifacts and workflow contracts.

Apply the same principle to specialist agents.

A planner should not be asked to reconstruct the design from vague conversation if an approved design artifact exists.

An implementer should receive a bounded task and the relevant approved context rather than an unbounded dump of the entire project unless that is genuinely necessary.

A reviewer should know what standards and evidence define success.

Useful questions:

- What artifact does this specialist consume?
- What artifact must it produce?
- What evidence proves its work completed?
- What context does it need?
- What context should it not need?
- What can it modify?
- Who receives the output next?

This connects specialist-agent orchestration back to source of truth, durable state, verification, and bounded authority.

## Independent review as the first compelling specialist

A reviewer is a strong first specialist because the learner can readily understand the problem it solves.

Ask:

> If the same agent designed and implemented the work, what assumptions might it carry into its own review?

Then compare with a review profile that receives the approved specification, plan, completed artifacts, and relevant evidence but is not asked to continue the implementation narrative.

Do not claim an independent agent is unbiased or infallible.

The point is that role separation can create a useful second pass with different instructions and context pressure.

## Connect back to workflow graphs

The previous module lightly introduces a graph-shaped lifecycle.

Now the learner sees that nodes in the workflow do not all have to be executed by the same worker.

Conceptually:

```text
node = a stage of work
worker = who/what performs that stage
```

A workflow graph can therefore route both:

- between stages;
- between specialist workers.

Do not teach orchestration engines or graph execution semantics in depth.

The point is simply that workflow structure and worker selection are separate design decisions.

## Possible later extensions

Once the core specialist model is understood, later work can introduce when genuinely needed:

- multiple implementation specialists;
- parallel work;
- isolated branches/worktrees;
- specialist toolchains;
- specialist domain packs;
- reviewer/critic roles;
- context budgeting between workers;
- retries and fallback profiles;
- routing based on risk or confidence;
- richer graph orchestration;
- governance for agent permissions and external side effects.

These are not prerequisites for understanding the core idea.

## Principle

> **Provision specialists when different stages genuinely benefit from different instructions, tools, context, permissions, expertise, or review perspective.**

And:

> **The orchestrator's job is not to delegate everything. It is to choose where delegation improves the work.**

## Do not teach yet

Do not turn this module into:

- a claim that more agents are always better;
- multi-agent hype;
- complex parallel execution;
- worktree or branch choreography unless the fixture genuinely requires it;
- orchestration-framework internals;
- agent-personality roleplay without meaningful provisioning differences.

The learner should leave able to reason about why a specialist exists, what makes it specialist, when the orchestrator should use it, and what tradeoff delegation introduces.
