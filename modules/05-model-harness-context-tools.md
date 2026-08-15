# Module 5 — Model, harness, context, tools, and behaviour

Approximate duration: 1 hour.

## Core idea

What a user experiences as `the AI` is the result of several interacting layers.

A useful model is:

**model + harness + instructions/settings + context + tools + environment + feedback = observed behaviour**

The learner should leave less inclined to say `model X is better` when the observed difference may come from configuration or tooling.

## Suggested session shape

### 0–15 minutes — Start from the Claude/ChatGPT preference

Use the learner's real observation that Claude often felt less verbose.

Treat that preference as valid, then ask what it actually proves.

Discuss the difference between:

- `I prefer the product as currently configured`;
- `this model is inherently better at the metric I care about`.

### 15–30 minutes — Change behaviour without changing the job

Take one prompt and run it with two different behavioural configurations.

For example, configure one response to be concise, conversational, low-heading, and non-repetitive. Compare it with the default behaviour.

Ask what changed without changing the underlying task.

The lesson is not that models are identical. It is:

> Do not attribute something to the model until you have considered whether it came from configuration or environment.

### 30–45 minutes — Debug a few failures by layer

Use examples and ask the learner to classify them:

- The answer is too long: model, harness, or instruction problem?
- The agent cannot see a local file: context/access problem?
- One product can search Gmail: model capability or tool capability?
- The agent produced a plausible but dimensionally wrong drawing: reasoning problem, tool problem, or missing feedback?
- The agent keeps ignoring a project convention: one-off prompt problem or persistent instruction problem?

A recurring question:

> Is this a model problem, context problem, harness problem, tool problem, state problem, or feedback problem?

### 45–60 minutes — Fair comparison

Discuss what a fair model or agent comparison would try to hold constant:

- same task;
- comparable context;
- comparable tools and permissions;
- similar instructions;
- similar opportunity to verify work.

If useful, run the same small repo task in two harnesses. Codex can be the teaching baseline; another agentic IDE such as Devin Desktop can later be used as a comparator.

Do not force a winner. Compare steering, visibility of actions, diff/review experience, defaults, and tool use separately from raw model behaviour.

## Future callback — context compaction, degradation, and "tears in the rain"

This module is the natural home for a later lesson about what happens to long-running conversational context as an agent session grows.

The lesson should explicitly call back to Lab 3's formulation:

> Decisions that exist only in conversation are tears in the rain.

Lab 3 teaches the simple failure mode: if an important decision exists only in a conversation and that conversation disappears, the decision disappears with it unless it was persisted into project state.

A later context-focused exercise should deepen that lesson. Conversational context can become fragile even before a conversation is literally lost. Long-running agent sessions have finite context budgets. When a harness reaches or approaches those limits, it may compact, summarise, truncate, or otherwise transform earlier context so work can continue.

The exact mechanism varies by harness and should be verified against the products used when this lesson is implemented. The invariant is more important than any one product's current implementation:

> Context that still appears to be "in the conversation" may no longer exist in its original form.

Complex reasoning is especially vulnerable. A compacted representation may preserve a conclusion or short summary while losing qualifications, intermediate reasoning, rejected alternatives, provenance, or the path that made the conclusion trustworthy.

A useful mental model is:

```text
rich original context
        ↓
continued conversation
        ↓
context pressure
        ↓
compaction / summarisation / truncation
        ↓
lossier representation of what came before
```

The intended learner insight is not that compaction is bad. Compaction is often necessary for long-running work. The lesson is that conversation context is not a durable project record.

A useful formulation to earn later is:

> As soon as complex reasoning produces something worth keeping, it has started fading unless the important result and enough of its supporting evidence are persisted somewhere durable.

Or, more memorably:

> Context is tears in the rain. Persist what matters before the weather changes.

This later exercise should distinguish at least three things:

- a result or conclusion;
- the reasoning or evidence that supports it;
- the durable project state that future agents can inspect.

It should also demonstrate that merely retaining a compacted conclusion is not always equivalent to preserving the reasoning artifact that produced it.

Do not force this lesson into the initial Module 5 lab if that makes the session too dense. It can become a later dedicated lab or advanced exercise once the learner has enough experience with longer-running agent sessions for context pressure to feel real rather than theoretical. Its exact curriculum position is intentionally unpinned for now.

## Tools to experiment with

- ChatGPT personality/verbosity/instruction settings where available;
- Codex local agent configuration;
- a second agentic harness later for comparison;
- the same repository and same prompt as a controlled test fixture.

## Discussion prompts

- What would count as evidence that one model is genuinely better for a task?
- Which preferences are really harness preferences?
- Which parts of the system can we change without changing model?
- When is a default valuable even if it is technically configurable?

## Principle

> Separate capability from configuration.

## Do not teach yet

Avoid turning this into benchmark methodology or model leaderboard discussion. The practical goal is simply to diagnose the layer that needs changing before swapping models reflexively.
