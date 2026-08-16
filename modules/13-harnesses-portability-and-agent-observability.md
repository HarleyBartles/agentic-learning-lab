# Module 13 — Harnesses, portability, and agent observability

Status: structured planning. This module follows specialist sub-agents deliberately: the learner first understands the conceptual specialist profile, then discovers that the mechanism for creating that worker is harness-specific and still changing quickly.

Approximate duration: 1 hour.

## Core idea

A model, profile, skill, or workflow does not run in the abstract. A harness decides how instructions enter context, which tools exist, how sub-agents are dispatched, which profile fields are understood, which model and reasoning controls are available, what defaults apply, what activity is visible, and how the resulting worker is presented to the human.

The durable principle is:

> **Agent concepts can travel between harnesses. Their implementations often cannot.**

And the deliberately memorable warning is:

> **It is the wild west. Every harness has its own standard. They often agree, but not always.**

Do not teach today's product interfaces as permanent laws. Exact tool names, schemas, model constraints, inheritance rules, defaults, and UI behaviours must be re-verified when this lab is implemented or run.

## Why this comes immediately after specialist sub-agents

Module 12 teaches a conceptual specialist profile as some combination of:

- role;
- instructions;
- model/capability level;
- tools;
- permissions;
- context expectations;
- domain material;
- quality criteria;
- operating boundaries.

That abstraction is useful. Now break the learner's likely next assumption:

> If I define a `reviewer` profile, every agent harness must know what I mean by `reviewer` and dispatch it the same way.

It does not.

Different harnesses may expose entirely different sub-agent tools, parameters, allowed values, inheritance rules, profile formats, built-in worker types, model-selection controls, tool restrictions, context-isolation semantics, and result handoffs.

The concept `delegate this bounded review to an independent specialist` may be portable while the concrete invocation is not.

## Main comparison — port one conceptual specialist

Use one specialist whose intent is already understood from Module 12. A reviewer is a good default.

Conceptually:

```text
reviewer
- independently review completed work
- receive fresh context where practical
- inspect against explicit acceptance criteria
- read project state
- run verification
- do not publish
- use only as much model capability / reasoning effort as the work requires
```

Ask the learner to express what this worker *means* before discussing either harness.

Then run or inspect the closest equivalent in at least two current harnesses.

Build a comparison around questions rather than a permanent compatibility table:

```text
conceptual requirement          harness A              harness B
fresh context                   how?                   how?
profile instructions            where?                 where?
model selection                 supported?             supported?
reasoning effort                supported?             supported?
tool allowance                  inherited/scoped?      inherited/scoped?
permissions                     how enforced?          how enforced?
dispatch tool                   what surface?          what surface?
allowed parameters              which values?          which values?
worker identity                 how represented?       how represented?
result / handoff                how returned?          how returned?
visible activity                what can we inspect?   what can we inspect?
```

The learner should feel the difference rather than merely hear that products differ.

## Facilitator observations to preserve, but verify at teaching time

Current discussion produced useful concrete examples from Codex and Devin/Cognition. Preserve them as candidate fixtures, not evergreen documentation.

Observed/recalled shape for Devin/Cognition:

- a `run_subagent`-style tool can dispatch configured sub-agent profiles;
- a custom profile can carry choices such as model, tool allowance, and custom instructions;
- when no custom profiles exist, built-in profiles may provide a general fresh-context worker and a more constrained exploration/read-only worker;
- exact names, built-in model assignments, available fields, and inheritance rules are product details that may change.

Observed/recalled shape for Codex:

- sub-agent tool shape can vary with the parent model/runtime;
- different dispatch tool versions may expose different model-selection or routing controls;
- some parent/runtime combinations may constrain child model choices while others expose more choice or inheritance;
- exact v1/v2 names, model families, constraints, and allowed values must be checked against the current runtime rather than taught from memory.

The teaching point does not depend on any one of these details remaining true.

> **Equivalent-looking agent concepts can be backed by different runtime contracts.**

## The profile you intended is not necessarily the worker you received

This is one of the most important lessons in the module.

A profile is configuration intent. The spawned worker is runtime truth.

Suppose a profile created for one harness says, conceptually:

```text
mechanical-checker
- narrow role
- cheap/fast model
- low reasoning effort
- read-only tools
- fresh context
- deterministic verification instructions
```

A second harness may:

- understand every field;
- express the same concept under different keys;
- ignore an unknown field;
- reject the profile;
- partially load it and fill unsupported fields with runtime defaults.

Partial success is particularly dangerous because the worker still launches.

The resulting worker might actually be:

```text
role instructions:     honoured
fresh context:         honoured
model selection:       ignored / unsupported
reasoning effort:      defaulted
read-only restriction: different semantics or not enforced
actual model:          inherited/default orchestrator model
actual tools:          harness defaults
```

Nothing necessarily crashes.

The task may even complete correctly.

Earn:

> **The profile is configuration intent. The spawned worker is runtime truth.**

And:

> **Do not assume the specialist you requested is the worker that was instantiated.**

## Verify the effective worker

Teach a small runtime verification habit after dispatch:

```text
1. define the intended specialist
2. translate/invoke it in the current harness
3. predict what the harness will instantiate
4. dispatch it
5. inspect what can actually be established about the effective worker
6. compare intended profile with resolved runtime worker
7. only then evaluate the work
```

Where the harness makes them observable, inspect:

- effective role/instructions;
- model or model class;
- reasoning effort;
- available tools;
- permission/capability boundary;
- context freshness/isolation;
- inherited project/runtime inputs;
- result/handoff channel;
- cost/usage evidence.

Where a field is not observable, say so. Do not turn an assumption into proof.

Useful callback to source-of-truth teaching:

> **What you asked the harness to instantiate is a claim. What the runtime actually instantiated is state.**

## A successful result does not prove a successful port

Give the learner a case where the task succeeds but the effective configuration is wrong.

For example, the orchestrator is deliberately a strong/high-cost model because it must understand the whole problem, resolve ambiguity, route work, and supervise specialists.

The workflow then dispatches many narrow mechanical workers:

```text
find these references
compare these values
check these filenames
run this deterministic verification
summarise this bounded artifact
```

The intended economics may be:

```text
1 strong orchestrator
+
20 inexpensive bounded workers
```

If the harness does not honour the requested child model and instead inherits/defaults to the orchestrator's strong model, the workflow may still produce excellent answers:

```text
1 strong orchestrator
+
20 strong inherited workers
```

The behavioural result can be correct while the system is economically badly engineered.

Earn:

> **A system can be behaviourally correct and operationally wrong.**

Cost, latency, capability allocation, and permission scope are part of agent-system correctness once work is repeated or scaled.

## Model choice and reasoning effort are current engineering control surfaces

At present, a competent agentic engineer may need to decide deliberately:

- which jobs deserve a frontier/high-capability model;
- which jobs can use a cheaper/faster model;
- where high reasoning effort is worth the cost/latency;
- where a narrow mechanical task does not justify heavyweight inference;
- whether child workers should inherit or override the orchestrator's configuration.

A useful question is:

> **What level of capability does this job require, and what is the least expensive worker configuration that satisfies the contract reliably?**

Do not reduce this to penny-pinching. It is resource allocation under quality and risk constraints.

But do not teach today's manual controls as permanent either.

Frontier models and harnesses are already absorbing behaviours that previously had to be explicitly scaffolded. A future orchestrator may increasingly choose model, effort, context, and tool allocation itself from a higher-level budget/quality policy.

Separate the durable concept from the current implementation:

```text
DURABLE CONCEPT
Different jobs require different amounts of capability,
context, inference, independence, and authority.
Use enough to satisfy the job reliably without wasting resources.

CURRENT CONTROL SURFACES
select model
select reasoning effort
configure profile fields
invoke harness-specific dispatch tool
inspect inheritance/defaults

POSSIBLE FUTURE CONTROL SURFACE
"Perform this delegation efficiently within these
quality, risk, latency, and cost constraints."
```

Earn:

> **Learn today's controls seriously, but remember what they are trying to control.**

## Portability exercise — predict before moving

Use Module 10's introspection technique.

Before moving the specialist/workflow to another harness, ask the current agent to inspect its setup and classify likely portability:

```text
portable intent
- task goal
- domain references
- quality criteria
- conceptual specialist role
- workflow logic

likely harness adapter
- profile schema
- sub-agent dispatch call
- model-selection key
- reasoning-effort control
- tool inheritance/restriction semantics
- instruction injection
- approval mechanics
- context creation
- activity reporting
```

Then actually move the small workflow/profile and compare prediction with behaviour.

Use:

> **introspect → predict → port → observe → repair**

Do not judge the port solely by whether the final task succeeded. Verify the effective worker and operating contract.

## Harness observability — use the telemetry you have

Different harnesses expose different amounts and forms of agent activity.

At teaching time, compare current surfaces such as:

- occasional progress/activity updates;
- collapsible per-turn reasoning/activity views;
- prominent tool-call traces;
- long-running visible thought/activity streams;
- plans and status messages;
- logs and intermediate observations.

Current product examples are deliberately volatile. ChatGPT, Codex, Devin/Cognition, and other tools may expose substantially different amounts of visible activity even when related model families are used.

Do not make `which product prints the most thoughts` the lesson.

Earn:

> **The harness determines what observability surface exists around the worker. Learn to use the telemetry you have.**

## Scan-reading a fast activity stream

When a harness exposes a high-volume activity stream, teach the learner not to read every token as prose.

Scan for trajectory.

Useful warning patterns include:

- the same hypothesis appearing repeatedly;
- the same files or sources being reread without new evidence;
- repeated tool failures;
- the same repair being undone and reapplied;
- oscillation between two states;
- long policy/instruction debate without task progress;
- repeated restatement of the plan;
- no new evidence entering the process;
- objective drift;
- premature commitment despite unresolved evidence.

This becomes an agentic-engineering supervision skill:

```text
visible activity
        ↓
scan trajectory rather than every word
        ↓
progress / new evidence / useful action?
        ↓
if not: detect churn, loop, drift, or dead end
        ↓
steer while intervention is still cheap
```

Module 11 taught the structure of non-converging loops. Here the learner can watch one developing from outside the worker.

Useful line:

> **Watch the agent's observable activity for trajectory, not prose quality.**

## Open the hood only a little

The learner should see that apparently magical harness behaviours can be assembled from mechanisms they already understand.

Conceptually, a visible activity stream might be implemented as simply as:

```text
system / harness instruction
"regularly report your current progress, reasoning,
uncertainty and next action through the activity tool"

        +

tool schema
activity_update(text)

        +

UI
render those calls as a collapsible activity stream
```

The exact implementation of any real product should not be asserted without current evidence. The point is architectural:

```text
model
+
system/developer instructions
+
tool schemas
+
context construction
+
runtime/default rules
+
UI
=
observable agent experience
```

This cashes Module 5's system decomposition.

Do not say the UI necessarily exposes the model's complete private internal reasoning.

> **Observable reasoning/activity is a harness-produced signal, not guaranteed privileged access to everything happening inside the model.**

It can be highly useful telemetry without being a perfect transcript.

## The harness can change behaviour without changing the model

Use this question:

> If we keep the same model but change its system instructions, tools, defaults, context construction, permissions, and UI feedback loops, have we kept the same agent system?

No.

This is why moving a crafted agent to a new harness can change behaviour even when the nominal model stays the same.

The model may transfer more easily than the agent.

Useful principle:

> **A model is portable more easily than an agent. An agent is partly the contract its harness creates around the model.**

## Avoid cargo-cult agent scaffolding

Close the technical material by challenging another assumption.

Some agentic workflows contain explicit instructions such as:

```text
do work
→ check your work
→ repair mistakes
→ report
```

Those instructions may have been valuable compensation for an earlier model/runtime that did not reliably self-review.

As frontier model behaviour improves, some explicit scaffolding may become redundant or counterproductive ceremony.

The durable engineering rule is:

> **Add structure where the agent needs structure, not because yesterday's agent needed it.**

The same applies to explicit model routing, reasoning-effort selection, review prompts, sub-agent profiles, and other current control surfaces.

When a stronger model or harness absorbs one of those responsibilities reliably, reevaluate the workflow rather than preserving the old ceremony forever.

## Principles

> **Agent concepts can travel between harnesses. Their implementations often cannot.**

> **The profile is configuration intent. The spawned worker is runtime truth.**

> **Do not assume the specialist you requested is the worker that was instantiated.**

> **A system can be behaviourally correct and operationally wrong.**

> **Learn today's control surfaces seriously, but remember the underlying quality, risk, capability, latency, and cost decisions they represent.**

> **Use visible activity as telemetry; scan for trajectory, churn, loops, and drift.**

> **A model is portable more easily than an agent.**

## Facilitator freshness rule

This module is unusually vulnerable to product drift.

Before teaching it, verify current behaviour for every named harness used in the comparison:

- exact sub-agent tool names;
- available tool versions;
- profile format;
- built-in profiles;
- model-selection constraints;
- reasoning-effort controls;
- inheritance/default behaviour;
- permission/tool scoping;
- context isolation;
- visible activity/reasoning surfaces;
- cost/usage reporting where relevant.

If the products have converged since this module was written, teach that convergence as evidence. If they have diverged further, teach the divergence.

Do not preserve an obsolete discrepancy just because the lesson originally used it.

## Do not teach

Do not turn this module into:

- a permanent Codex-versus-Devin feature matrix;
- memorising tool schemas;
- product tribalism or `which harness is best`;
- a claim that visible activity is a complete internal thought transcript;
- mandatory use of the cheapest possible model;
- a claim that more expensive models are wasteful by definition;
- a prediction that manual model routing definitely will disappear;
- a universal portability standard that does not yet exist.

The learner should leave able to separate portable agent intent from harness-specific adapters, verify the effective runtime worker after dispatch, reason about model/effort economics, use available observability while work is in flight, and expect the interfaces to evolve.

End with the explicit reminder:

> **Reminder: it's the wild west. Could all change tomorrow.**
