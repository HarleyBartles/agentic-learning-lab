# Module 13 companion / 13A practicum — The 20-Agent Bonfire and context transport

Status: facilitator planning companion to `13-harnesses-portability-and-agent-observability.md`, with a deliberate bridge into Module 14 selective provisioning/context. Preserve this alongside the main module when the practical lab is scaffolded. It may run as a separate 13A practicum rather than being forced into the core Module 13 hour.

## Why this exists

The harness-portability discussion exposed two related lessons that deserve a concrete practical exercise rather than a paragraph of theory:

1. agent systems have economics as well as behaviour;
2. context transport is itself an engineering decision.

A workflow can produce a correct result and still be badly engineered because it spent far more model capability, context, coordination, and usage than the result justified.

The exercise should make that visible first, then ask the learner to diagnose where the waste actually came from.

The deliberately memorable name is:

> **The 20-Agent Bonfire**

Do not tone the name down. This curriculum is for a specific facilitator/learner pair, not a generic corporate training product. Quirky names, jokes, and pop-culture references are allowed when they make the lesson easier to remember.

## Sequencing guard — do not accidentally teach Module 16 here

The Bonfire is about **resource economics, worker resolution, and context transport**.

It is not the curriculum's concurrency/isolation lesson.

If the chosen twenty-worker task would cause several workers to mutate the same workspace concurrently, constrain the fixture so the workers are read-only, run serially, or write to deliberately separate output paths. You may still discuss whether concurrency could affect latency, but do not let shared-workspace collisions become the dominant failure mode.

Module 16 later earns this distinct lesson:

> Concurrent mutable work needs isolation, explicit ownership, reconciliation, and re-verification.

Keep that powder dry.

## Practical exercise — The 20-Agent Bonfire

Choose one substantial but bounded task that can plausibly be completed more than one way.

Use the same harness, same project starting state, and same task for both facilitator and learner.

### Learner run

Give the learner the task and ask them to complete it using what they currently think is sensible agentic engineering.

Do not prescribe a worker count or model-routing strategy.

A suitable instruction is approximately:

> Complete this task in the way you think is most effective and efficient. Use agents/sub-agents where they genuinely help.

The learner may use one capable agent, a small number of specialists, a larger orchestrated workflow, or something else. Let their current engineering judgment determine the shape.

### Facilitator run

Run the same task from the same starting state, but intentionally engineer it badly.

A suitable instruction is approximately:

> Complete this task using as many sub-agents as possible. Slice the work into very small tasks and dispatch at least 20 sub-agents. Do not specify a sub-agent model. Prefer delegation even where the task could reasonably be done inline.

The exact current dispatch tool/schema must be verified at teaching time.

The point is not to prove that 20 workers are inherently bad. The point is to manufacture an obviously over-delegated system whose resource behaviour can be inspected.

## Record the resource state before and after

Before each run, record whatever current resource/usage surface the harness exposes.

After each run, record it again.

Depending on the product at teaching time this might be:

- an allowance bar;
- token/inference accounting;
- request/unit consumption;
- cost information;
- model-specific usage;
- another resource proxy.

Do not pretend that a visible allowance delta is necessarily precise per-worker accounting. Treat it as the best observable resource proxy the current harness exposes and explain its limitations.

The desired Socratic reveal can use made-up explanatory numbers such as:

> You used about 3% of your allowance. I used about 30% of mine. Why do you think that is?

Then:

> Is my result an order of magnitude better than yours?

And if it is not:

> Why did I pay roughly an order of magnitude more economically for a result that was not roughly an order of magnitude better?

The numbers are deliberately illustrative. Use the real observed values when the exercise is run.

## Compare three dimensions, not one

Do not reduce the debrief to `sub-agents are expensive`.

Compare:

```text
quality
Did the result satisfy the task well?

latency
Did concurrency or delegation materially reduce useful elapsed time?

resource efficiency
How much model/context/orchestration capacity did we spend to obtain it?
```

These dimensions can move independently.

Twenty workers might genuinely improve latency on separable work while using much more inference.

Twenty tiny workers might be both slower and more expensive because coordination dominates useful work.

A more expensive workflow may still be justified when the extra quality, confidence, independence, or speed is actually worth the spend.

Earn:

> **Parallelism and delegation consume resources. Spend them where separation or concurrency buys something.**

And:

> **A system can be behaviourally correct and operationally wrong.**

## The sting in the tail — what workers did we actually buy?

After the learner notices that the facilitator created many workers, ask a second question:

> Why were those workers as expensive as they were?

The facilitator deliberately did not specify the child model.

Now inspect the effective runtime workers where the harness permits it.

Questions include:

- did the sub-agent inherit the orchestrator model?
- did a harness default apply?
- was the requested/profile model unsupported or ignored?
- what reasoning-effort/default setting applied?
- did the worker receive broader tools than needed?
- did each worker receive more context than its narrow task justified?

This directly reinforces the parent Module 13 rule:

> **The profile is configuration intent. The spawned worker is effective runtime state.**

A workflow can appear to work perfectly while twenty narrow mechanical jobs quietly run on heavyweight orchestrator-class inference.

That is an economics failure even if no answer is visibly wrong.

## The engineering question is not `how many agents can I use?`

Ask:

> Where can you see efficiency opportunities?

Then:

> How can we spend less usage without sacrificing required quality?

Possible learner discoveries include:

- use fewer workers where separation buys nothing;
- slice work at meaningful ownership boundaries instead of microscopic operations;
- use a cheaper/faster worker where the task contract permits it;
- tune reasoning effort when the harness exposes that control;
- avoid repeatedly exploring the same project state;
- avoid repeatedly loading the same large context into many workers;
- use local self-review before buying a fresh independent context when independence is not required;
- stop retrying when the success condition is already established;
- parallelise genuinely independent work rather than parallelising for theatre;
- verify the effective runtime worker rather than assuming the intended profile was honoured.

The conclusion is not `always use fewer sub-agents`.

It is:

> **Use enough agent capacity to satisfy the job. Additional inference needs to earn its keep.**

And:

> **Competent agentic engineering is not maximising how much AI you can throw at a problem. It is spending the minimum capability required to achieve the required quality, confidence, and speed.**

## Second reveal — worker count is only one source of waste

Once the obvious 20-worker bonfire is diagnosed, ask:

> Suppose all twenty workers really were justified. Where else could we still be wasting context and inference?

This opens the context-transport lesson.

Possible sources of waste:

- giant dispatch prompts copied into every worker;
- every worker independently rereading the same doctrine;
- every worker independently rediscovering the same project facts;
- huge final handoff messages dumped back into the orchestrator;
- the orchestrator reading artifacts it only needs to route;
- the orchestrator manually transcribing a worker response into the file that should have been the worker's direct deliverable;
- an integration worker receiving prose summaries instead of the authoritative artifacts it is supposed to integrate.

## Context transport is an engineering decision

A useful principle is:

> **Pass references when you can. Pass contents when you must.**

This does **not** mean files make information free.

If a worker eventually reads the whole file, that content still enters the worker's context.

The advantage is control over **when**, **where**, and **whether** the information is materialised into a particular worker's context.

Compare:

```text
eager prompt transport
orchestrator pastes a 6,000-token brief into the dispatch
→ worker is born carrying all 6,000 tokens

reference transport
orchestrator says:
"Read tasks/reviewer-brief.md and execute the task contained within."
→ worker starts with a tiny handoff
→ worker resolves the durable brief when needed
```

The same idea matters on the return path.

```text
verbose return
worker writes a 5,000-token report into its final handoff
→ orchestrator immediately carries the whole report in context

artifact return
worker writes reports/review.md
→ final handoff says:
"Completed. Report written to reports/review.md."
→ orchestrator can decide whether it needs to read the report at all
```

Earn:

> **Route artifacts between agents; do not route their entire contents through the orchestrator unless the orchestrator actually needs them.**

## Do not make the orchestrator transcribe the worker

Call out this wasteful pattern explicitly:

```text
sub-agent discovers result
        ↓
sub-agent writes giant result into final response
        ↓
orchestrator reads giant response
        ↓
orchestrator transcribes response into desired file
```

If the desired output was a file, prefer:

```text
sub-agent
        ↓
writes authoritative result directly to file
        ↓
returns tiny receipt
        ↓
orchestrator routes/verifies the artifact
```

Useful principle:

> **Do not make an agent narrate an artifact to another agent when it can create the artifact directly.**

And the intentionally quirky facilitator line:

> **Do not make the orchestrator eat every document just because it owns the filing cabinet.**

## Artifact routing does not remove verification responsibility

Do not let `the orchestrator does not need to read it` mutate into `nobody needs to verify it`.

A tiny receipt can prove that a worker claims to have written an artifact and may establish its location. It does not by itself prove the artifact satisfies its contract.

If content-level correctness matters, assign that responsibility somewhere explicit:

- the producing worker may run deterministic checks before handoff;
- a reviewer/integration worker may inspect the artifact directly;
- a deterministic validator may establish the required property;
- the orchestrator may read it when orchestration itself requires semantic judgment.

The efficient pattern is not `skip inspection`. It is:

> **Make the worker or stage that actually needs the contents perform the inspection; do not force every coordinator in the route to materialise them.**

This preserves Module 8's evidence rule while avoiding unnecessary context transport.

## Superpowers-style SDD as a concrete facilitator example

A useful facilitator anecdote is the Superpowers subagent-driven-development style of handoff: deeply discourage large prompt payloads and large worker return payloads when a durable file can carry the brief/result instead.

The exact current skill wording should be verified before teaching it as a live product example.

The pattern to spotlight is simple:

```text
handoff to worker
"Read this file and execute the task contained within."

worker result
"Completed. Report written to some_file.txt."
```

The important part is not those exact strings.

It is the architecture:

- the brief exists as durable state;
- the worker discovers/reads it;
- the worker writes its deliverable directly to durable state;
- the return message is a receipt/pointer rather than a duplicate artifact;
- the orchestrator only materialises the artifact if its own job actually requires understanding it;
- verification responsibility remains explicit even when the orchestrator does not read the artifact.

## Bridge to Module 14 — this is old engineering in a new medium

Use this moment for a deliberate callback to software/programming first principles.

Do **not** claim pass-by-reference/value originated in object-oriented programming.

A more accurate facilitator line is:

> **Software engineers have been managing this shape of problem for decades: move references to large things when you can, and move the thing itself when the recipient genuinely needs it.**

Reference/value semantics are broader programming concepts. Object-oriented systems make the intuition particularly visible because programs commonly pass references to objects rather than copy whole object graphs everywhere.

This curriculum is not teaching coding, but many agentic-engineering problems rhyme with software and systems engineering because the underlying concerns are familiar:

- locality;
- loading/materialisation;
- interfaces;
- contracts;
- ownership;
- authority;
- isolation;
- state;
- cost;
- verification.

## Lazy loading, eager loading, and agentic N+1

Carry this explicitly into Module 14 selective provisioning/context.

### Lazy loading intuition

```text
I know this artifact exists
        ↓
do I need its contents?
        ↓
do I need all of its contents?
        ↓
do I need linked doctrine/policies/evidence too?
        ↓
materialise only the useful information graph
```

For an agent, `I know I have a thing` and `I have read, inspected, understood, and incorporated the thing plus its related doctrine` are very different context states.

### Eager loading intuition

If a worker is known to require a coherent cluster of related information, it may be cheaper/cleaner to provision or retrieve that cluster deliberately rather than force serial rediscovery.

The lesson is not `lazy is always good`.

It is to choose the loading strategy deliberately.

### Agentic N+1

Careless lazy loading can create the classic N+1 shape.

Manufacture the analogy:

```text
20 workers
        ↓
each reads task
        ↓
each opens same project instructions
        ↓
each discovers same governing skill
        ↓
each follows same architecture reference
        ↓
each loads same supporting material
```

No individual read is irrational.

Collectively the system may be paying to materialise substantially the same information graph twenty times.

Ask:

> Why are we repeatedly materialising the same expensive information?

Possible legitimate answers differ by task:

- independence really matters, so duplicated context is worth it;
- workers need only a smaller prepared brief;
- one specialist should resolve the source material and persist an authoritative derived artifact;
- a coherent related bundle should be loaded together;
- only one integration/review stage actually needs the full graph.

This is advanced context management, not a simplistic ban on repeated reads.

## The system can know more than the orchestrator has read

A particularly important conceptual jump:

> **The agentic system can know more than any individual agent currently has in context.**

Durable files, source material, specialist outputs, and project state can collectively contain more knowledge than the orchestrator has personally materialised.

For example:

```text
review worker
Completed.
Verdict: PASS
Evidence: reports/review.md
```

The orchestrator may not need to read `reports/review.md`.

It may only need to route it to the next stage, attach it, move it, or verify that the artifact exists.

Another specialist can consume the artifact directly.

This turns the orchestrator from `the agent that must know everything` into `the agent that coordinates where knowledge and work need to flow`.

That is a systems-engineering mindset rather than a prompt-engineering mindset.

## Programming/systems principles worth naming without teaching coding

Use these as brief analogies, not a software lecture:

- **references / indirection** — pass a durable location when the recipient can resolve it;
- **lazy loading** — do not materialise information before the worker needs it;
- **eager loading** — load a known-required coherent bundle deliberately rather than serially rediscovering it;
- **N+1 awareness** — many locally reasonable reads can become globally wasteful repetition;
- **locality** — keep expensive context near the worker that actually uses it;
- **interfaces/contracts** — workers exchange defined artifacts/results rather than unrestricted internal state;
- **separation of concerns** — orchestrators coordinate; specialists perform specialist work; do not force every layer to ingest everything;
- **materialisation cost** — knowing a thing exists is cheaper than loading and reasoning over the thing and all its dependencies.

Useful facilitator line:

> **If some of this feels suspiciously like software engineering, that is because it is. We are solving many of the same problems — locality, loading, interfaces, authority, isolation, cost, and state — but the things moving through the system are now instructions, evidence, artifacts, and agent work rather than only objects and function calls.**

## Avoid cargo cult optimisation

Do not turn this into `always use files` or `never put substantial information in a handoff`.

Sometimes the recipient genuinely needs the value immediately.

Sometimes opening a durable artifact costs more complexity than simply providing a short self-contained brief.

Sometimes independent workers deliberately need the same complete source context to prevent one worker's interpretation becoming everyone else's hidden premise.

The engineering question is always:

> What does this worker need to know, when does it need to know it, and is this information being materialised in places that never use it?

## Durable principles versus today's knobs

Today's competent agentic engineer may need to think explicitly about:

- child model selection;
- reasoning effort;
- sub-agent count;
- tool permissions;
- context provisioning;
- dispatch payload size;
- return payload size;
- artifact routing;
- retrieval/materialisation patterns.

Tomorrow's frontier models/harnesses may absorb some of those choices automatically.

Do not cargo-cult today's controls after the model/harness no longer needs them.

Preserve the durable concern underneath them:

> **Capability, context, and inference are resources. Spend and materialise them in proportion to the job.**

Then finish where the parent module finishes:

> **Reminder: it's the wild west. Could all change tomorrow.**