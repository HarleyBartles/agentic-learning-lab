# Module 12 — Autonomous human-in-the-loop workflows

Status: structured planning. The exercise spine is strong enough to preserve now; exact fixture files and lab choreography can still change.

Approximate duration: 1 hour.

## Core idea

A capable agent does not become usefully autonomous merely because it has tools, project knowledge, and domain expertise.

It also needs operating knowledge for how to move work from vague intent to verified completion.

The learner should discover that autonomy is not the absence of human control. It is moving human judgment to deliberate approval points while teaching the agent how to perform the mechanical and cognitive work between those gates.

A mature single-agent lifecycle can look like:

```text
vague human intent
        ↓
agent explores and clarifies
        ↓
agent writes a design/specification
        ↓
agent self-reviews
        ↓
human review and approval
        ↓
agent writes a plan
        ↓
agent self-reviews
        ↓
human review and approval
        ↓
agent executes one task at a time
        ↓
agent self-reviews and verifies each task
        ↓
agent performs whole-work review
        ↓
human review and approval
        ↓
agent publishes/merges and cleans up
```

The learner should not begin by being told this workflow. The exercises should make each improvement necessary.

A useful principle to earn:

> **A self-sufficient agent is not one that no longer needs a human. It is one that knows what it can carry forward itself, what it must verify before continuing, and when it must hand control back to the human.**

## Why this belongs after environment and domain provisioning

Earlier modules teach how to give an agent:

- project state;
- appropriate tools;
- operating instructions;
- reusable skills;
- domain knowledge and examples;
- verification criteria;
- safe boundaries.

That creates a competent worker.

This module asks a new question:

> Why is the human still manually shepherding the worker through every transition?

The learner should see that repeatedly saying `now ask questions`, `now write the design`, `now make a plan`, `now review it`, and `now do the next task` is itself a workflow that can be provisioned.

## Fixture/domain

Use a fresh domain unless deliberate reuse of an earlier domain is needed to expand the exact previous end state.

Current preferred fixture: planning a house move.

The domain works because a generic answer is genuinely useful while hidden circumstances can make generic output inadequate.

Canonical vague request:

> I'm planning to move house, write me a checklist.

Prepared exceptional requirements should include at least one memorable fixed constraint, such as a 4,000-gallon aquarium, plus one or more additional unusual circumstances such as a piano, several pets, accessibility constraints, difficult access, storage, timing, or specialist handling.

At least one exceptional circumstance should be chosen by the learner rather than scripted by the facilitator. This prevents the workflow from appearing overfitted to the prepared aquarium example.

## Facilitator-controlled AGENTS.md

The demonstration environment should prevent the baseline agent from accidentally discovering the lesson before skills are introduced.

A suitable direction is approximately:

> When the user asks you to create or write something, produce the requested artifact using your best reasonable assumptions. Do not ask preliminary clarifying questions unless an applicable skill instructs you to do so. Invoke any applicable skills available in the environment and follow their workflow.

The purpose is not to make the baseline agent artificially stupid. It should still use its best judgment and produce useful work.

The control makes the comparison meaningful:

- without skills, execute the request using reasonable assumptions;
- with skills, the same project instructions naturally permit the skill to require clarification, design, planning, review, and handoff.

## Exercise spine

### Exercise 1 — vague input, immediate execution

Use the baseline environment with no workflow skills.

Prompt:

> I'm planning to move house, write me a checklist.

Let the agent produce a normal generic checklist.

Do not frame the answer as a failure. It should likely contain useful items such as removals, utilities, mail forwarding, packing, address changes, and keys.

Ask:

- Is this useful?
- Would you actually use it?
- What assumptions has the agent made about the move?

Then reveal the prepared exceptional circumstances.

For example:

- a 4,000-gallon aquarium;
- a piano;
- four dogs and three cats.

Ask how much of the original checklist would meaningfully handle those requirements.

Intended insight:

> **Generic input plus immediate execution tends toward generic output.**

The output was not necessarily bad. The problem definition was thin.

### Exercise 2 — spoon-feed the missing detail

Still use the baseline environment with no workflow skills.

Give a much more specific request containing the exceptional circumstances explicitly.

For example:

> I'm planning to move house. I have a 4,000-gallon aquarium, a piano, four dogs and three cats. Write me a checklist.

The result should be materially more useful and specific.

This proves that the model is already capable of using the information when it is supplied.

Ask:

- What improved?
- Did the model suddenly become more capable?
- Who had to know which details mattered?

Intended insight:

> **The agent can use specific information, but the human currently has to know what information matters and remember to provide it.**

### Exercise 3 — manually ask the agent to discover the requirements

Remain in the baseline environment without workflow skills.

Return to a vague request, but explicitly tell the agent how to work:

> I'm planning to move house. Before you write the checklist, ask me questions so you understand my specific needs.

The agent should now ask clarifying questions and discover the exceptional circumstances through conversation.

The learner should answer naturally when the agent reaches relevant areas. Do not require one exact wording such as `Do you own a giant aquarium?`; the point is that competent questioning discovers categories of unusual constraints.

This proves that the model already knows how to perform requirements discovery when explicitly asked.

Ask:

- Could the agent do this all along?
- What did the human have to provide this time?
- What repeated instruction are we giving the agent about how to begin work?

Intended insight:

> **The missing capability was not question-asking. The human was manually supplying the workflow.**

### Exercise 4 — vague input plus provisioned workflow skills

Reset to the original vague request.

Provision the mature skill set or a teaching version of it, while keeping the baseline `AGENTS.md` instruction unchanged.

Prompt again:

> I'm planning to move house, write me a checklist.

Do not front-load an explanation of the skills.

The intended wow moment is that the agent does not immediately write the checklist. An applicable skill causes it to enter discovery/brainstorming, ask clarifying questions, and turn the vague request into a sufficiently explicit specification.

The learner should see the same useful behaviour from Exercise 3 without having to request the behaviour manually.

Ask:

- Did the model get smarter?
- Did we give it the hidden requirements?
- Did we write a more detailed task prompt?
- What changed?

Intended conclusion:

> **The skill did not give the model a capability it lacked. It turned a behaviour the human previously had to request into the agent's normal operating procedure.**

This is a stronger version of the earlier rule:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

## Continue the workflow — specification, planning, execution, review

Do not stop after the clarification demonstration.

Let the skilled workflow continue so the learner experiences the larger lifecycle.

### Specification/design handoff

The discovery skill should produce a durable design or requirements artifact rather than leaving the understanding only in conversation.

For the house-move fixture it might contain:

```text
move requirements
- origin and destination
- date/window
- occupants
- pets
- large/specialist possessions
- access constraints
- storage needs
- critical dates
- budget constraints
- specialist services
- risks/open questions
- success criteria
```

The agent should self-review the artifact for accuracy, completeness, ambiguity, and missing requirements before handing it to the learner.

The learner reviews and either approves or redirects.

### Planning handoff

Once the design/specification is approved, the agent should invoke the appropriate planning workflow.

The plan should make the requirements operational rather than merely repeating them.

The learner should inspect whether the unusual circumstances survive the handoff.

For example:

- aquarium present in specification;
- specialist aquarium moving work present in plan;
- timing, access, livestock, or sequencing considerations become actual actions rather than a note saying `move aquarium`.

The agent self-reviews the plan before human handoff.

The learner approves or redirects.

### Execution

The agent executes the approved plan one bounded task at a time.

Each task should have a small internal loop:

```text
execute task
→ inspect result
→ verify against acceptance criteria
→ pass: continue
→ fail: repair/retry or escalate
```

The point is not that the agent can never fail. The point is that it should not require the human to request routine self-review after every step.

### Whole-work review and final handoff

After task execution, the agent reviews the completed body of work against the approved specification and plan.

The learner then performs the final human review.

Only after approval should the agent perform consequential finalisation such as merge/publish and cleanup.

## Trace exceptional requirements through the whole workflow

The unusual requirements are proof artifacts for the lesson.

At every handoff ask:

```text
requirement discovered
        ↓
represented in specification?
        ↓
made operational in plan?
        ↓
actually affects execution/output?
        ↓
verified in final review?
```

If the aquarium appears in the design but disappears from the plan, orchestration failed.

If it survives the plan but the final work contains only a vague `move aquarium` item, execution did not adequately operationalise the requirement.

The learner-chosen exceptional circumstance is especially useful because it proves the process can discover and preserve something that was not hard-coded into the fixture.

## Human-in-the-loop autonomy

Use the workflow to distinguish three modes:

```text
micromanagement
human drives every transition

unsupervised autonomy
agent decides and performs everything

bounded autonomy
agent drives the workflow
human controls meaningful gates
```

The human should not have to push the agent through mechanical transitions.

The agent can often:

- clarify;
- structure;
- design;
- plan;
- execute;
- self-review;
- verify;
- retry bounded failures;
- prepare a handoff.

Human judgment remains important for:

- intent;
- important ambiguity;
- design approval;
- plan approval;
- acceptance of the final work;
- consequential publication or external side effects.

Useful line:

> **Autonomy is not the absence of human control. It is moving human control to the points where human judgment adds the most value.**

## Skills can drive workflows and harmonise with other skills

Earlier curriculum material can introduce a skill as procedural knowledge: `how should I do this kind of work?`

This module should deepen that model.

A skill can:

- implement a self-contained workflow;
- contain loops, review gates, retries, and stopping conditions;
- hand work to another skill;
- expect an artifact produced by an earlier skill;
- participate in a larger orchestration framework.

For example:

```text
discovery/design skill
        ↓
approved specification
        ↓
planning skill
        ↓
approved plan
        ↓
execution workflow
        ↓
review workflow
```

The learner should notice that order matters.

Planning before design approval may be premature. Execution without an approved plan may discard useful decomposition. Review has different evidence available after execution than before it.

The skills are not merely a bag of independent tricks. They can form contracts and handoffs.

## Light touch: loops versus graphs

The worked workflow initially appears linear:

```text
idea
→ design
→ plan
→ execute
→ review
→ finish
```

On inspection it contains micro-loops at handoff and verification points:

```text
design
↺ self-review / revise
↓
human gate
↓
plan
↺ self-review / revise
↓
human gate
↓
execute task
↺ inspect / repair / retry
↓
whole-work review
↺ return to implementation if needed
```

A real problem may also force a return to an earlier stage. For example, planning may expose a design assumption that cannot be satisfied, or execution may reveal that the plan itself is wrong.

Ask:

> Is this actually a straight line anymore?

Introduce terminology only lightly:

- a loop repeats a step or route until a condition is satisfied;
- a graph becomes a useful way to think when there are several meaningful stages and several legal routes between them.

Do not teach graph theory or workflow-engine semantics here.

The learner only needs the design insight:

> **A useful agent workflow is rarely just a checklist. It can contain decision points, return paths, stopping conditions, and approval gates.**

## Pressure exercise — a loop that cannot converge

Do not leave loops, graphs, and stopping conditions as abstract vocabulary. Make the failure mode visible.

Use a small review fixture containing two authoritative requirements that cannot both be satisfied at the same time. The contradiction should be real enough that fixing one necessarily recreates the other defect.

Give the agent a review skill whose initial logic is intentionally plausible but incomplete:

> Review the current state. If you find a defect, correct it and review the resulting state again. Continue until the review passes.

Do not encode the expected loop into the task prompt. Let the skill create it naturally.

The likely behaviour is:

```text
A is broken
→ fix A

B is now broken
→ fix B

A is now broken
→ fix A

B is now broken
→ ...
```

Each individual review decision can be locally reasonable while the workflow as a whole fails.

Ask:

> Is the agent failing to solve the next step, or is there no reachable state that satisfies the success condition it has been given?

Earn:

> **A loop needs a termination model, not only a rule for continuing.**

The learner should see that repeated competent action is not the same as progress.

## Add a stop condition and escalation route

Run the same fixture again with the same model, task, and project state, but improve only the review skill.

Add a stop condition along the lines of:

> If successive review cycles substantially repeat a previously seen state or alternate between the same incompatible defects, stop modifying the work. Preserve the best-understood state, record the incompatible requirements and evidence, and escalate to the user for an authority decision.

Now the route becomes:

```text
review
↓
defect A
↓
repair A
↓
review
↓
defect B
↓
repair B
↓
review
↓
defect A again
↓
recurrence / incompatibility condition reached
↓
stop modifying
↓
explain evidence
↓
human handoff
```

Distinguish three concepts:

- **stop condition:** when the loop must not continue;
- **escalation path:** what happens after it stops;
- **escape hatch:** an exceptional legal route out of the normal workflow.

A stop with no destination can still leave the work stranded. A useful escape hatch says both when normal progress is no longer justified and where control should go next.

## Escape hatches can be missing or too easy

Use the same idea to pressure the opposite failure mode.

### No escape hatch

If a workflow has no legitimate exit for impossible or authority-blocked work, the agent may:

- churn;
- burn time/tokens/cost;
- repeatedly damage and repair the same state;
- invent increasingly speculative fixes;
- or eventually stop only because of an arbitrary harness/runtime limit.

Useful line:

> **A workflow without an escape hatch can turn an impossible task into endless activity.**

### Escape hatch too broad

Now deliberately make the escape condition too easy, for example:

> If uncertain, ask the user.

A capable agent may now encounter ordinary difficulty and immediately hand the task back.

Ask:

> Did we solve the loop problem, or did we create a legal route around doing difficult but solvable work?

Earn:

> **Exceptional exits need explicit entry conditions.**

And:

> **An escape hatch should be easier than endless failure, but harder than doing the ordinary work.**

A stronger escape condition may require evidence such as:

- the same defect class reappears after repair;
- a previously visited state recurs;
- authoritative constraints are demonstrably incompatible;
- no new evidence appears across repeated cycles;
- a bounded retry threshold is reached;
- the missing decision belongs to human/project authority rather than execution.

## Are agents looking for escape hatches?

Answer this explicitly because the behaviour can look cheeky or lazy.

Not really.

At this stage of the curriculum, a better model is:

> **The agent is looking for a legal route to something that appears to satisfy the task success condition.**

Then ask:

- Who defined the success condition?
- Who defined the legal routes from the start state to the goal?
- Who defined what `good enough` looks like?
- Who defined when escalation is permitted?

The answer is largely the learner, either directly or through the environment they provisioned.

The agent did not independently decide what the project's goal should be. It consumed the task, project state, instructions, workflow, quality criteria, tools, permissions, and transition rules and produced a credible-looking route through them.

If the easiest policy-compliant route bypasses difficult work, the workflow may reward bypassing it without the model having any human-like desire to shirk.

Useful line:

> **Agents do not need to be lazy for badly designed escape hatches to produce avoidance. If the shortest legal route satisfies the contract, the contract is what needs inspection.**

This reframes systematic failure away from personality and toward system design.

Ask:

> What did we make it reasonable for the agent to believe counted as success?

That question should become a reusable diagnostic habit.

## From loop to graph

After the learner has seen the non-converging loop and the new escape route, redraw the workflow:

```text
        ┌──────── repair ────────┐
        ↓                        │
review ───── pass ─────→ finish  │
  │                              │
  ├─ new resolvable defect ──────┘
  │
  └─ repeated/incompatible state
             ↓
          escalate
             ↓
           human
```

Then ask:

> Is this really just a loop anymore?

The learner has now earned the graph model: several possible states, several legal routes, and different exit conditions.

The deeper lesson is:

> **The learner is increasingly defining what progress, failure, success, and legitimate escape look like — not merely telling the agent what task to perform.**

## Evaluate the escape hatch, not just the happy path

This connects naturally to later TDD-inspired agent design and evaluation.

Define representative behavioural cases before changing the workflow skill:

```text
ordinary solvable defect
→ repair it; do not escalate

difficult but solvable defect
→ persist within bounded attempts

repeated non-converging defect
→ detect recurrence and stop

incompatible authoritative requirements
→ preserve evidence and escalate

missing authority
→ stop rather than invent policy
```

Then rerun the same cases whenever the stop/escape logic changes.

This demonstrates that an escape hatch is part of the agent's behavioural contract and can itself regress.

A good stop condition distinguishes:

> keep trying

from:

> more trying cannot resolve the underlying problem.

## Scaled glimpse — mature graph orchestration

After the learner has built the small conceptual version, briefly show a mature example.

Harley's iterative-review skill is a useful facilitator demonstration because it can show how the same idea scales to a much larger graph using:

- explicit nodes;
- a deterministic next-node script;
- durable logs;
- proof artifacts;
- expected outputs for each node;
- rejection of invalid routes when required artifacts do not exist on disk.

The purpose is not for the learner to understand the implementation.

Ask them to identify familiar concepts:

- Where is a review loop?
- What proves a node completed?
- How does the agent know what comes next?
- What stops it jumping to an invalid stage?
- Where are the legal escape/escalation routes?

Intended insight:

> **As workflow complexity grows, we can encode more of the route so the agent has to improvise less of the process.**

This is a glimpse of why a graph may be the right shape for sufficiently complex work, not a lesson in graph mechanics.

## Scaled glimpse — multi-skill orchestration

Also show a mature public example such as obra/superpowers, subject to verifying its current public shape when the lab is implemented.

The useful teaching point is that a larger workflow can be composed from distinct, harmonised skills rather than one monolithic skill.

The design → plan → execute → review lifecycle used in this module is inspired by this style of orchestration.

Use the comparison to show three possible shapes:

```text
one self-contained workflow skill

several skills orchestrated together

hybrid: orchestrator plus skills that contain their own loops/graphs
```

Do not ask the learner to implement or understand the framework internals.

The takeaway is:

> **Workflow shape is a design choice.**

## Do not introduce specialist sub-agents yet

If the mature skill set exposes an execution choice between single-agent execution and sub-agent-driven development, prefer single-agent execution for this module while visibly noting that another mode exists.

For example:

> Interesting. It is offering another execution mode here. We are not choosing that one yet.

The unresolved question should be allowed to sit:

> Our single agent can now discover requirements, design, plan, execute, and review the whole job. Is it actually a good idea for the same worker to perform every role?

That question is the natural precursor to the following module on specialist agent profiles and sub-agent-driven development.

## Principle

> **Teach the agent how work moves, not only how individual tasks are performed.**

And:

> **Do not spend human attention on defects or transitions the agent can cheaply handle itself. Keep humans at the gates where judgment, intent, authority, or consequential action matters.**

And:

> **A robust workflow defines not only how to continue, but how to recognise non-progress, how to stop, and which authority receives the unresolved decision.**

## Do not teach yet

Do not turn this module into:

- graph theory;
- workflow-engine implementation;
- node-schema semantics;
- a tutorial on Superpowers internals;
- specialist sub-agent orchestration;
- a claim that every task needs design → plan → execute;
- a claim that maximum autonomy is always desirable.

The learner should leave understanding why workflow orchestration exists and having seen a single provisioned agent perform a substantial human-in-the-loop lifecycle, including a loop that fails, a bounded escape from that failure, and the graph-shaped workflow that results.