# Curriculum threads, breadcrumbs, and future cash-ins

This document tracks deliberate conceptual threads that begin in one lab or module and should be cashed later when the learner has enough experience for the deeper model to matter.

The curriculum is not required to keep today's module numbering or sequence. Ordering is fluid. Preserve conceptual dependencies and earned transitions rather than treating module numbers as fixed chronology.

The teaching pattern is:

> introduce a useful behaviour or mental model -> let the learner use it -> leave a breadcrumb -> later create pressure that exposes its limit -> cash the cheque with a richer model.

This document exists so those promises are not lost while individual labs are still being developed.

## Learner-owned fork as the curriculum workspace

Before Lab 1, the facilitator should help the learner fork the upstream curriculum repository into the learner's own GitHub account.

The learner does not need a Git lesson at this point. The practical explanation can be as simple as:

> This is your copy of the laboratory. You can break this one.

The roles are:

```text
upstream curriculum repository
facilitator-maintained teaching source
        ↓ fork
learner-owned repository
persistent laboratory for the learner's whole curriculum
        ↓ checkout / connectors
local and connected agent surfaces operate on learner-owned state
```

The learner's fork is the working project for the curriculum. The upstream repository remains the curriculum source.

This distinction should later become teaching material rather than day-one ceremony:

- local working state can differ from the learner's remote fork;
- the learner's fork can differ from upstream curriculum state;
- synchronization is a project-state question rather than `Git magic`;
- the learner's personal Git history records their path through the curriculum;
- the upstream history records the curriculum's own evolution.

Do not teach fork/remotes/upstream mechanics before the learner has a reason to care. Early synchronization can remain facilitator plumbing.

When mature labs are revised, hard-coded assumptions that cloud agents work directly against `HarleyBartles/agentic-learning-lab` should be replaced by the learner's fork where the experiment concerns learner project state.

## AGENTS.md starts as facilitator-owned experimental apparatus

In Labs 1–4, lab-scoped `AGENTS.md` files are facilitator controls over the agents invoked inside the exercises.

They survive the learner's fork and therefore arrive as part of the prepared experimental environment.

Their early purpose is not to teach `AGENTS.md`. Their purpose is to establish stable lab conditions without forcing the learner to reconstruct operating rules in every prompt.

Examples already present in mature labs include:

- limiting the local worker to the mission/project rather than teaching choreography;
- protecting local operational data from leaking onto remote surfaces;
- making discussion non-mutating;
- making ordinary changes stop for review before commit/push;
- defining what `discard that run` means.

The design rule for early lab instructions is:

> **Control the experiment, not the conclusion.**

Do not hide the file if the learner notices it. Explain briefly that it contains standing project instructions and that Lab 5 will explore that lever deliberately.

The intended progression is:

```text
Labs 1–4
facilitator provisions project instructions
learner experiences controlled behaviour
        ↓
Lab 5
learner opens AGENTS.md with the facilitator
learner hand-edits one bounded standing rule
fresh agent context demonstrates the changed instruction
instructions become a named layer of the system
        ↓
Labs 6–7 and later provisioning work
learner reasons about which knowledge belongs in which layer
        ↓
real project
learner owns the instruction surface
learner may delegate creation and maintenance of AGENTS.md
        ↓
later work
learner designs project doctrine and instruction scope deliberately
```

The Lab 5 reveal should feel like:

> You have been benefiting from this mechanism since the beginning. Now you have touched the lever yourself.

The later real-project transition is different:

> You understand this surface now. This is your project, so you decide what stable doctrine belongs here and what maintenance you want to delegate.

## From repeated guidance to selective provisioning

An early principle is:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

That model is useful but incomplete.

Later, deliberately break the accumulation interpretation:

> Moving every useful rule into the environment can itself make the agent worse.

The learner should eventually encounter an agent that is overwhelmed by a large collection of individually sensible but slightly drifted instructions, skills, profiles, tool guidance, quality criteria, permissions, and task rules.

The failure mode should be realistic rather than theatrical:

- excessive self-discussion;
- repeated policy reconciliation;
- hesitation before obvious actions;
- unnecessary clarification;
- over-analysis of what is allowed;
- tool/skill selection churn;
- weak commitment because several overlapping doctrines are all being litigated.

The diagnosis is:

> **The agent is not under-instructed. It is over-provisioned and poorly scoped.**

The richer principle is:

> **Provisioning is not accumulation. Give the agent the right knowledge, at the right scope, at the point where it is needed.**

Useful destination questions:

- Is this a stable project boundary?
- Is this task intent?
- Is this reusable workflow knowledge?
- Is this role-specific doctrine?
- Is this domain evidence/reference material?
- Is this a verification criterion?
- Does the current worker need this now at all?

This thread should cash into context engineering, instruction scope, retrieval, specialist profiles, and workflow design.

## Instruction surfaces, scope, and conflicts

The learner will eventually encounter several instruction-bearing surfaces:

- user/task prompt;
- project instructions such as `AGENTS.md`;
- global or harness instructions;
- skills;
- workflow/orchestration rules;
- agent profiles;
- managed policy/permissions;
- retrieved domain/context material that may itself contain instruction-like text.

The curriculum should eventually teach that `I told the agent X` does not imply that X is the only instruction in force.

Do not make Lab 5 a standards or precedence lecture. Its useful result is simply that the learner has seen project instructions as one real layer. The richer later mental model is scope:

> Which rule naturally owns this decision, for which worker, for how long, and under what authority?

The agent-overwhelming exercise is the natural place to make conflicting or duplicated scope visible.

## Model capability really can be the problem

Lab 5 correctly discourages reflexively blaming the model for every observed failure.

Its final diagnostic scenario deliberately preserves the opposite possibility: when context, tools, instructions, and opportunity to verify are held reasonably constant and one model still fails the same bounded reasoning step, model capability becomes a serious suspect.

The mature rule is:

> **Diagnosis before intervention. Sometimes the diagnosis really is model capability.**

This prevents the learner from replacing one simplistic belief (`the model is everything`) with another (`the environment can fix everything`).

## Specialist intent versus harness runtime state

Module 13 should let the learner describe a specialist conceptually before they learn any one product's dispatch schema.

That intended worker may include:

- role/instructions;
- model or capability expectation;
- reasoning-effort expectation;
- tools and permissions;
- context/isolation expectations;
- quality and verification contract.

Module 14 then deliberately breaks the assumption that another harness will realise those fields in the same way.

Different runtimes can ignore, rename, reject, inherit, or default different parts of the profile while still successfully launching a worker.

The durable distinction is:

> **The profile is configuration intent. The spawned worker is effective runtime state.**

Keep `runtime state` separate from the curriculum's semantic/source-of-truth language. This thread concerns what worker configuration actually exists, not which project artifact has authority.

The learner should verify observable effective configuration where the harness permits it rather than treating a successful task result as proof that the requested specialist contract was honoured.

## Agent economics are part of engineering correctness

The curriculum should eventually make resource allocation visible rather than treating cost as an implementation footnote.

The central pressure case is intentionally perverse:

```text
1 strong orchestrator
+
20 tiny mechanical jobs
```

If the harness silently inherits/defaults the strong orchestrator model for all twenty workers, the workflow may still produce an excellent answer while consuming dramatically more inference than the task justified.

Earn:

> **A system can be behaviourally correct and operationally wrong.**

And:

> **Capability, context, and inference are resources. Spend them in proportion to the job.**

Do not turn this into `always use the cheapest model`. Quality, risk, latency, independence, and confidence can all justify additional spend.

Likewise, do not fossilise current model-selection/reasoning knobs. They are human control surfaces today; future harnesses/models may increasingly allocate them automatically. Teach the resource-allocation problem underneath the current interface.

## Knowledge has a destination

Whenever a repeated correction or useful discovery occurs, ask not merely `should we save this?` but:

> What kind of knowledge is this, and therefore where should it live?

Useful mapping:

- project fact -> durable project state;
- stable project rule -> project instructions;
- reusable procedure -> skill/workflow;
- domain source/standard -> reference material;
- quality expectation -> verification/evaluation criterion;
- role-specific operating doctrine -> specialist profile;
- task-specific decision -> current task/conversation unless it becomes durable project state.

This becomes increasingly important once the learner has many available levers.

## Access, observation, and absence

Two deliberately related threads now land at different stages:

- Lab 8: something can exist now and still fail to be discovered through the current retrieval/navigation route;
- Module 18: something can be absent from current state and still exist in recorded historical state.

Together they support the more general principle:

> **Your observation method constrains what conclusions absence can support.**

Useful formulations:

```text
not found in current search
!=
does not exist now

not present now
!=
never existed
```

Lab 9 deliberately does **not** cash the historical half of this thread. It uses scoped current-state verification instead, and defers `is it tracked?` → `was it ever tracked?` until repository archaeology, provenance, and compressed evidence surfaces are the actual subject in Module 18.

## Source of truth and verification are distinct questions

Lab 3 deliberately leaves the learner with a contradiction between durable artifacts and the unresolved question:

> When the project disagrees with itself, how does an agent know what to trust?

Lab 9 explicitly reopens that same Repair Café contradiction rather than introducing authority as a disconnected concept.

Distinguish:

- **verification:** did the work satisfy the requirement?
- **authority:** which artifact/source defines the requirement or current truth?

A worker can verify perfectly against the wrong authority.

## Human gates are already present before autonomy is named

Lab 3 already uses a small human-in-the-loop lifecycle:

```text
agent changes state
→ stops for review
→ learner inspects
→ learner accepts or discards
→ explicit authorization
→ commit/push
```

Do not call this workflow orchestration in Lab 3.

When autonomous workflow is taught later, explicitly cash the breadcrumb:

> You have been using approval gates for several labs. Until now, you were manually pushing the worker from one stage to the next.

`Discard that run` is also an early return/retry edge. The learner should experience loops before naming them.

## One worker, one main line is an intentional interim model

The source-control lab deliberately assumes:

> one repository, one main line of history, one agent changing it at a time.

Make that assumption visible enough to remember, but do not teach branches/worktrees yet.

Later specialist work can deliberately break it:

> What happens when two implementation workers need to modify the project at the same time?

That earns isolation, separate workspaces/branches/worktrees, reconciliation, and merge review.

The Module 14A **20-Agent Bonfire** must not accidentally cash this thread early. Keep the Bonfire workers read-only, serialised, or on separate output paths if necessary. Its lesson is economics/context transport; the shared-mutable-state collision belongs to the later concurrency module.

## Context is finite and selective

The learner should not finish the curriculum with only the shorthand `context is temporary; state is persistent`.

Later teach that:

- context capacity is finite;
- long sessions may be compacted, summarised, truncated, or otherwise transformed;
- compacted context can preserve conclusions while losing qualification, provenance, rejected alternatives, or reasoning detail;
- irrelevant context can make agent decisions slower or worse;
- more context is not automatically better context;
- different workers may need different slices of the project;
- retrieval is one mechanism for selecting which project knowledge enters the current working context.

Use the existing `tears in the rain` line as the precursor:

> Context is tears in the rain. Persist what matters before the weather changes.

Then deepen it:

> **Persist what must survive; retrieve what is relevant; do not make every worker carry everything.**

## Context transport and materialisation

Once specialist workers exist, the curriculum should distinguish durable information from information currently materialised in one worker's context.

A handoff that pastes a large brief/value directly into a sub-agent causes that material to occupy the worker's context immediately.

A handoff that passes a durable file/artifact reference lets the recipient decide when and whether to resolve the contents.

Likewise, a worker that returns a giant report in its final message pushes that material into the orchestrator's context immediately. If the real deliverable is a file, it can write the file directly and return a short receipt/pointer instead.

Earn:

> **Pass references when you can. Pass contents when you must.**

And:

> **Do not make an agent narrate an artifact to another agent when it can create the artifact directly.**

This is not a claim that files make context free. It is control over **where, when, and whether** information is materialised.

Keep verification explicit: a short receipt does not establish content correctness. The worker/stage that owns correctness still has to inspect or deterministically verify the artifact.

## Lazy loading, eager loading, and agentic N+1

Use familiar systems/programming shapes as analogies without turning the curriculum into a coding/database course.

Lazy-loading question:

> I know the artifact exists. Does this worker need to read it now, read all of it, or follow all of its related doctrine/evidence?

Eager-loading question:

> If this worker predictably needs a coherent bundle of related material, should we supply/retrieve that bundle together instead of forcing serial rediscovery?

Agentic N+1 pressure:

```text
20 workers
→ each opens the same project instructions
→ each discovers the same skill
→ each follows the same architecture reference
→ each reloads substantially the same doctrine
```

Every read may be individually sensible while the system is globally wasteful.

Earn:

> **Many locally rational context loads can still form a globally inefficient system.**

This should cash into Module 15 selective provisioning/context.

## The system can know more than the orchestrator has loaded

Durable project state and specialist artifacts mean the overall agentic system can contain more useful knowledge than any one current worker has in context.

An orchestrator may only need a verdict and artifact pointer in order to route work; another stage may consume the underlying report directly.

Useful principle:

> **The agentic system can know more than any individual agent currently has in context.**

This changes the orchestrator's role from `agent that must ingest everything` to `agent that coordinates where knowledge and work need to flow`.

Again, routing is not verification. If the orchestrator does not inspect an artifact, some other responsible stage must establish whatever content-level property the workflow relies on.

## Retrieval and RAG should be earned from scale

Lab 1 begins with a human manually choosing and transporting context.

Later labs let agents retrieve or explore project state directly.

At larger scale, break the model again:

> An agent cannot necessarily load or inspect an entire large knowledge base every time. Something must decide what enters working context.

The learner only needs the architecture-level model initially:

```text
large body of durable knowledge
        ↓
retrieval/search
        ↓
relevant subset
        ↓
agent working context
```

RAG should be taught as mediated context selection, not as vector-database mathematics.

Connect it to the existing retrieval-versus-exploration distinction, the agent-overwhelming lesson, and the context-materialisation thread.

## Untrusted content is evidence, not authority

Connected/autonomous agents will read email, web pages, issues, documents, repositories, and other external content.

The learner should understand before high-autonomy external work that source content can contain instruction-like or malicious text.

The durable principle is:

> **Data from outside the trusted instruction boundary is evidence, not authority.**

An email, web page, issue, source document, or retrieved passage does not become project policy merely because it tells the agent what to do.

This should be taught as a continuation of Lab 3's semantic-authority lesson, not as an isolated cybersecurity warning.

Pair it with permissions and blast-radius controls: instructions describe intended behaviour; harness/permissions constrain what is possible.

## Evaluation should grow out of verification

The curriculum already repeatedly runs controlled before/after experiments:

- full versus missing context;
- different access surfaces;
- domain provision before/after;
- moving-house workflow runs;
- configuration changes.

Later name the general engineering habit:

> **When you change the agent, test the agent, not only the task that motivated the change.**

Use lightweight representative scenarios rather than benchmark culture.

A simple pattern:

```text
define observable desired behaviour
        ↓
run representative scenarios
        ↓
change the agent environment
        ↓
rerun the same scenarios
        ↓
compare evidence
```

This becomes especially important when editing skills, instructions, profiles, retrieval, and orchestration.

## TDD-inspired agent design

Test-Driven Development can be introduced as a general problem-solving discipline rather than a coding lesson.

Acknowledge its software origin briefly, then extract the transferable structure:

> **Define observable success before changing the system that is supposed to produce it.**

The agent-overwhelming scenario is a strong non-code example.

First define a behavioural contract such as:

- identify the relevant operating boundary quickly;
- make the strong obvious decision without prolonged policy litigation;
- use only relevant capabilities;
- preserve source material;
- verify the result;
- stop at the required human gate;
- avoid unnecessary clarification/self-discussion.

Run the overloaded environment and observe failure against the contract: the equivalent of `red`.

Then make the smallest useful environmental/scoping change and rerun: `green`.

Then simplify/reorganise the environment while repeatedly proving the contract still holds: `refactor`.

No code is required.

The transferable loop is:

```text
specify desired observable behaviour
        ↓
observe failure
        ↓
make the smallest system/environment change
        ↓
observe success
        ↓
simplify/refactor
        ↓
prove behaviour still holds
```

Use `TDD-inspired agent design` unless the exact exercise genuinely satisfies a strict TDD contract and calling it TDD adds clarity rather than confusion.

## Autonomy needs stopping conditions

The autonomous-workflow lesson should teach not only when the agent may continue, but when it must stop.

Possible stopping/escalation conditions include:

- bounded retry limit reached;
- confidence/verification threshold not met;
- repeated loop with no new evidence;
- plan/design assumption proven false;
- required authority unavailable;
- cost/time/risk exceeds the delegated budget;
- consequential external action requires human approval.

Useful principle:

> **Autonomy needs stopping conditions as much as continuation rules.**

The agent should know what it can carry forward itself, what it must verify, and when continued self-action is no longer justified.

## Provenance and observability across workflows

As workflows gain stages and multiple workers, the learner should be able to ask:

- Who/what produced this artifact?
- From which inputs and approved decisions?
- Which workflow stage produced it?
- What verification passed?
- What remains inference rather than evidence?

Do not require distributed-tracing terminology.

The practical principle is:

> **When work crosses stages or workers, leave enough evidence that another worker or human can reconstruct why the current state exists.**

This connects durable state, verification, handoff contracts, logs, graph proof artifacts, and specialist delegation.

## Specialist agents also reduce context and policy load

Specialization should not be justified only by role expertise or independent review.

A specialist can also be valuable because it receives a narrower operating envelope:

```text
general worker
every tool + every rule + every domain + every permission

specialist worker
relevant tools + relevant rules + relevant context + bounded permission
```

This is one way to cash the agent-overwhelming lesson.

Delegation remains a design choice. Narrowing a worker's context/policy can improve focus, but handoff and orchestration introduce their own costs.

## Concurrent specialists earn isolation

After the learner understands sequential specialist delegation, introduce concurrency only when there is a task where parallel work is genuinely useful.

Create the pressure:

> Two competent implementers can each make locally correct changes and still interfere when they share one mutable workspace.

Then earn:

- isolated workspaces/branches/worktrees or equivalent;
- explicit ownership of work slices;
- merge/reconciliation;
- conflict inspection;
- re-verification after integration.

Do not teach branching mechanics as ceremony before this problem appears.

## Module 10 is a synthesis checkpoint, not graduation

The current `build a real agentic project` material should not imply that the curriculum is over once the learner can establish a real project home, tools, instructions, and a first skill.

By Module 10, project instructions are no longer a reveal: Lab 5 already exposed and manipulated that layer. The new step is ownership in a real project and deliberate delegation of instruction maintenance where useful.

Its mature role is a synthesis checkpoint:

> You now know enough to build a genuine agentic project. From here, real project work and bounded teaching fixtures can both be used to introduce more advanced operating patterns.

Later self-introspection, autonomy, specialist delegation, harness portability/effective-worker verification, economics, selective provisioning, context transport/materialisation, retrieval/context, evaluation, security, and isolation remain core learning rather than optional epilogue material.

## Epilogue should compare two histories

Once the learner has used a fork throughout the curriculum, the final retrospective can compare:

- upstream curriculum history: how the course itself evolved;
- learner fork history: how this learner actually moved through it.

Both are evidence, but they answer different questions.

This reinforces that history is durable project evidence rather than complete memory of conversations or motives.
