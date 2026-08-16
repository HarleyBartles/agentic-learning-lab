# Module 12 — Selective provisioning, context, and evaluation

Status: structured planning. This module cashes several earlier breadcrumbs: persistent instructions, skill composition, context limits, retrieval, instruction scope, and the danger of over-provisioning.

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
- Module 6 asks where repeated domain knowledge should live;
- Module 10 shows multiple skills harmonising into a larger workflow;
- Module 11 shows specialist profiles carrying narrower role-specific operating conditions.

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
- global/harness instructions;
- skills;
- workflow/orchestration rules;
- specialist profiles;
- managed policy/permissions.

Do not teach a product-specific precedence table.

Teach the more durable question:

> Which rule naturally owns this decision, for which worker, for how long, and under what authority?

A useful project environment avoids forcing every worker to reconcile the whole policy universe on every task.

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

> **Good agent design is selective: provision what this worker needs, where it naturally belongs, when it is needed, and test that the resulting behaviour is actually better.**

## Do not teach yet

Do not turn this into:

- token-count optimisation;
- vector-database internals;
- product-specific instruction-precedence trivia;
- benchmark engineering;
- a blanket argument for tiny prompts;
- a claim that specialist agents are always superior.
