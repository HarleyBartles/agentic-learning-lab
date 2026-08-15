# Module 4 — Model, harness, context, tools, and behaviour

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
