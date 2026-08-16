# Module 14 — Selective provisioning, context, and evaluation

Status: structured planning. This module cashes several earlier breadcrumbs: persistent instructions, skill composition, context limits, retrieval, instruction scope, inspectable reasoning, and the danger of over-provisioning.

Approximate duration: 1 hour.

## Core idea

Earlier modules correctly teach the learner to move repeated guidance into the environment. This module deliberately breaks the simplistic accumulation model.

> **Provisioning is not accumulation. Give the agent the right knowledge, at the right scope, at the point where it is needed.**

A heavily provisioned agent can become slower, more hesitant, and less decisive when it must continually reconcile overlapping tools, skills, instructions, profiles, permissions, and slightly drifted versions of the same doctrine.

The goal is not to teach `fewer instructions are always better`. The goal is selective, scoped provisioning.

## Breadcrumbs to cash

Earlier labs have already modelled narrow operating doctrine:

- Lab 1 uses minimal `AGENTS.md` instructions to bound the mission without teaching the answer;
- Lab 2 uses a focused rule to prevent local operational data leaking to remote surfaces;
- Lab 3 moves repeated review/discussion behaviour into standing project doctrine while leaving semantic authority with the human;
- Module 5 separates model behaviour from harness/configuration/context;
- Module 6 asks where repeated domain knowledge should live;
- Module 10 introduces agent self-introspection, local self-review, behavioural prediction, and test-first thinking as cheap local engineering primitives;
- Module 11 shows multiple skills harmonising into a larger workflow;
- Module 12 shows specialist profiles carrying narrower role-specific operating conditions;
- Module 13 shows that harnesses differ in how those profiles, tools, models, defaults, and observability surfaces are actually realised at runtime.

Open by asking:

> We have spent several labs learning how to give agents more. Can giving them more ever make them worse?

## Main pressure exercise — overwhelm the agent

Use one bounded task whose correct operating doctrine is simple and already understood.

Create an intentionally over-provisioned environment in which several surfaces contain individually reasonable but slightly drifted versions of the same underlying doctrine.

For example:

```text
global/harness instruction
prefer conservative changes and ask before consequential actions

project AGENTS.md
make minimal changes; preserve source; stop before publish

skill
complete the workflow autonomously but request approval for significant decisions

agent profile
be proactive and avoid unnecessary user interruption

task prompt
finish this efficiently

quality criteria
ensure every affected artifact is consistent before completion

tool guidance
prefer making all related updates in one operation
```

None should be absurd in isolation.

The intended failure is policy and context churn rather than stupidity:

- repeated self-checking;
- debating whether an approval is required;
- uncertainty over `minimal` versus `all related` changes;
- unnecessary clarification;
- excessive caveats;
- tool/skill selection hesitation;
- repeated restatement of allowed scope;
- slower commitment to strong obvious decisions.

Ask:

> Is this agent missing guidance, or is it carrying too much overlapping guidance?

Earn:

> **The agent is not under-instructed. It is over-provisioned and poorly scoped.**

## Refactor the operating environment

Do not randomly delete instructions.

Classify the knowledge by natural destination:

- stable project boundary -> project instructions;
- actual desired outcome -> task prompt;
- reusable procedure -> skill;
- role-specific operating doctrine -> agent profile;
- domain evidence/standards -> reference material;
- quality expectation -> verification/evaluation contract;
- irrelevant-to-this-worker material -> do not load it now.

Run the same task again.

The improved worker should reach strong decisions faster with less visible policy litigation while still preserving the safety and quality invariants.

Useful line:

> **Things the agent does not currently need should not become things it must continuously reason about.**

## Instruction surfaces and scope

The learner now has enough experience to see that several instruction-bearing surfaces can coexist:

- task/user prompt;
- project instructions such as `AGENTS.md`;
- user/home-level instructions;
- global/harness/system instructions;
- skills;
- workflow/orchestration rules;
- specialist profiles;
- managed policy/permissions;
- retrieved material that may itself contain instruction-like text.

Do not reduce this to one product-specific precedence table.

Teach the more durable questions:

> Which rule naturally owns this decision, for which worker, for how long, and under what authority?

And:

> If two rules conflict, what does this runtime say about precedence?

A useful project environment avoids forcing every worker to reconcile the whole policy universe on every task.

## Instruction hierarchy whodunnit

Use short cases where the learner predicts which instruction should win or where a surprising instruction came from.

The cases should include three categories:

1. the answer is specified and deterministic;
2. the answer depends on how the harness/runtime injects the instruction;
3. the apparent conflict is not inside the project at all.

### Case — nested AGENTS.md scope

For Codex/OpenAI-style `AGENTS.md` semantics, a deeper `AGENTS.md` applies to its subtree and takes precedence over a conflicting instruction from a higher directory for files in that subtree.

Example:

```text
/AGENTS.md
use British English

/docs/AGENTS.md
customer-facing documentation uses US English

/docs/help.md
```

Ask:

> Which rule applies when the agent edits `docs/help.md`?

Answer: the nearer/deeper scoped instruction for that file.

Treat this as a product/runtime rule that should be verified against current documentation when the lab is implemented, not as a universal law of all agent harnesses.

### Case — direct prompt versus project instruction

For Codex's documented hierarchy, direct system/developer/user instructions outrank `AGENTS.md` instructions.

Example:

```text
root AGENTS.md
run the full validation suite before finishing

user task
for this investigation, do not run validation; only inspect and report
```

Ask which instruction has authority in this runtime.

Again, teach the general habit: know whether the answer comes from a published runtime contract rather than intuition.

### Case — project instruction versus invoked skill

Pose the question deliberately without pretending there is one universal answer:

```text
root AGENTS.md
contains rule A

invoked skill
contains contradictory rule B
```

Ask:

> Which wins?

The answer may depend on how that harness presents the skill to the model and what instruction role/authority it receives.

This is valuable precisely because `it depends` is sometimes the correct engineering answer.

Do not guess. Inspect the runtime documentation, active prompt construction, or run a controlled behavioural test.

Useful principle:

> **Instruction hierarchy is partly a model contract and partly a harness implementation detail. Know which one you are reasoning about.**

### Case — the poison is outside the project

Example:

> The root `AGENTS.md` clearly says X. There is no contradictory project instruction anywhere, but the agent repeatedly behaves as though `not X` is a standing rule. Where do you look?

Answer: outward.

Possible sources include:

- home/user-level `AGENTS.md` or equivalent;
- ancestor/workspace instructions;
- harness configuration;
- developer/system prompts;
- workspace policy;
- active skills;
- tool instructions;
- retrieved context;
- runtime-injected operational policy.

Earn:

> **The project can be the authoritative state of the work without being the complete instruction environment of the agent.**

## Hierarchy does not solve composition

Include a case where no instruction directly contradicts another, yet their combination produces bad behaviour.

For example:

```text
root instruction
be proactive

local instruction
never modify source material

review skill
resolve detected inconsistencies before finishing

user task
summarise this deliberately inconsistent fixture
```

The agent may become tempted to repair or over-handle the inconsistency even though no single instruction explicitly said `modify this fixture`.

The point:

> **Instruction hierarchy tells you which rule has authority when rules conflict. It does not guarantee that the combined instruction set produces good behaviour.**

This connects directly back to agent overwhelming and selective provisioning.

## Inspectable agents — not magic black boxes

Module 13 has already taught visible activity as a harness-specific observability surface and the practical skill of scan-reading it for churn, loops, drift, and lack of new evidence.

This module cashes that capability diagnostically rather than reteaching the harness comparison.

Many agent harnesses expose some combination of:

- visible reasoning/activity summaries;
- plans;
- tool calls;
- intermediate observations;
- self-review notes;
- status messages;
- logs.

The amount and fidelity varies by model, harness, and settings.

The learner should not assume that because the final answer looks plausible, the route to it was sound.

Useful principle:

> **When the harness exposes the agent's working trace, inspect it. Do not assume the model reasoned well merely because the output looks credible.**

But immediately add the qualification:

> **Visible reasoning is evidence about the agent's process, not a guaranteed complete transcript of everything that influenced it.**

A runtime may summarise, hide, transform, or omit parts of the model's internal reasoning. The learner should use visible traces diagnostically without treating them as perfect ground truth.

## The thought stream can reveal injected concepts without explaining their provenance

Use a demo where the agent repeatedly refers to a concept the learner never supplied.

The learner now knows from Module 13 that a harness can produce and surface activity channels in different ways. Here the question is not how the stream is rendered, but what an unexpected concept in that stream tells us about the worker's instruction environment.

A suitable live-demo candidate, subject to verification at teaching time, is a verbose agent/model configuration that repeatedly mentions an internally injected operating mode or policy while reasoning about an otherwise ordinary task.

The wow moment is not `we extracted a secret`.

It is:

> **You typed one prompt, but that was not necessarily the first instruction the model received.**

The agent may talk about an injected concept as though it were completely natural because, from the model's point of view, it is simply part of the current context.

The thought stream may therefore tell you *that* a rule is influencing behaviour without telling you *where that rule came from*.

When surprised, ask the agent:

> Why did you think that?

Then:

> Where did that instruction or assumption enter your context?

And when necessary:

> Which instruction surface supplied it, and what authority does that surface have?

Use a diagnostic ladder:

```text
what did the agent do?
        ↓
what did the visible reasoning/activity say?
        ↓
what rule or premise was it following?
        ↓
where did that rule enter the context?
        ↓
what authority did that instruction surface have?
```

This is `diagnosis before intervention` applied to instruction provenance.

## Hidden/system prompts are operating inputs, not secure vaults

A later reveal may show the learner that the harness supplies system/developer instructions before or alongside anything they typed.

Do not frame this as `hacking the secret prompt`.

The useful model is:

```text
system / harness instructions
        ↓
developer or managed policy
        ↓
project / user-scoped instructions
        ↓
skills / workflow injections
        ↓
retrieved context
        ↓
user task
        ↓
agent reasoning and action
```

The exact stack and precedence vary by runtime.

Teach two security consequences:

1. model-readable hidden instructions should not be treated as a safe place for secrets merely because the UI does not normally display them;
2. critical behavioural boundaries should not rely solely on hidden natural-language instructions when sandboxing, permissions, capability scoping, or other mechanical enforcement can make the forbidden action impossible.

Connect back to the trust-boundary principle:

> **An instruction can influence behaviour without being a trustworthy security boundary.**

Do not make system-prompt extraction itself the learning objective. The objective is to understand that the learner-visible project is only one layer of the worker's operating environment.

## Context is finite and selective

Now deepen the earlier shorthand `context is temporary; state is persistent`.

Teach that:

- working context has finite capacity;
- long sessions may be compacted, summarised, truncated, or otherwise transformed by the harness;
- compaction can preserve conclusions while losing qualifications, provenance, rejected alternatives, or reasoning detail;
- irrelevant context can make decisions noisier or slower;
- more context is not automatically better context;
- different workers may need different slices of the same durable project state.

Call back to Lab 3:

> Context is tears in the rain. Persist what matters before the weather changes.

Then refine it:

> **Persist what must survive; retrieve what is relevant; do not make every worker carry everything.**

## Retrieval and RAG — architecture before machinery

Cash the progression from Lab 1 and Module 7.

Lab 1 begins with the human manually selecting and transporting context.

Module 7 distinguishes retrieval from exploration.

At scale, introduce the next problem:

> What if the durable knowledge base is too large to load or inspect wholesale for every task?

Use the simple model:

```text
large body of durable knowledge
        ↓
retrieval/search
        ↓
relevant subset
        ↓
agent working context
```

RAG is introduced as mediated context selection, not vector-database mathematics.

The learner should understand that an agent often does not `know the whole project` at once. Some process selects what evidence reaches the current context.

Connect back to the absence lesson:

> Not retrieved does not prove nonexistent.

Retrieval quality therefore affects what conclusions an agent can safely draw.

## Evaluation grows out of verification

The curriculum has already performed controlled before/after experiments repeatedly. Name the general habit now.

> **When you change the agent, test the agent, not only the task that motivated the change.**

Use a small set of representative scenarios and observable success criteria.

For example:

```text
representative tasks
+ known behavioural expectations
        ↓
run current agent configuration
        ↓
change instructions/skills/context/tool scope
        ↓
rerun the same scenarios
        ↓
compare evidence
```

Do not introduce benchmark culture. These are local regression/evaluation cases for the behaviour this environment is meant to preserve.

Instruction-hierarchy and provenance scenarios are useful regression cases too:

```text
nested scoped instruction
→ correct local rule wins

user override where runtime permits it
→ correct direct instruction wins

runtime-injected rule
→ agent can identify/provenance the rule when challenged

no direct conflict but poor composition
→ evaluation detects undesirable emergent behaviour
```

## TDD-inspired agent design

Acknowledge Test-Driven Development's software origin briefly, then extract the transferable discipline:

> **Define observable success before changing the system that is supposed to produce it.**

Use the overwhelmed-agent scenario itself.

Before refactoring, define a behavioural contract such as:

- identify the relevant operating boundary quickly;
- make the strong obvious decision without prolonged policy litigation;
- use only capabilities relevant to the task;
- preserve source material;
- verify the result;
- stop at the required human gate;
- avoid unnecessary clarification/self-discussion.

Run the overloaded environment. It violates the contract: `red`.

Make the smallest useful scoping/environment change. Rerun until the contract passes: `green`.

Then simplify/reorganise without losing the proven behaviour: `refactor`.

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

This lets the learner feel TDD's value independently of coding.

## Model capability can still be the limiting layer

Close the provisioning story carefully.

After teaching how much environment design can change behaviour, include a controlled comparison where tools, context, instructions, task, and verification opportunity are held reasonably constant and one model still performs materially better on a bounded requirement.

Earn:

> **Diagnosis before intervention. Sometimes the diagnosis really is model capability.**

Do not replace `the model is everything` with `the environment can fix everything`.

## Principle

> **Good agent design is selective: provision what this worker needs, where it naturally belongs, when it is needed, inspect how the worker is reasoning from those inputs, trace surprising beliefs back to their source, and test that the resulting behaviour is actually better.**

Useful closing diagnostic:

> **When an agent surprises you, do not only ask what it did. Ask what it believed, why it believed it, where that belief entered the system, and which instruction surface had authority.**

## Do not teach yet

Do not turn this into:

- formal XAI theory;
- chain-of-thought epistemology;
- token-count optimisation;
- vector-database internals;
- memorising one product's entire precedence table;
- system-prompt extraction as a party trick;
- benchmark engineering;
- a blanket argument for tiny prompts;
- a claim that specialist agents are always superior.
