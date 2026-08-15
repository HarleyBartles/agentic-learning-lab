# Module 4 — Model, harness, context, tools, and behaviour

Approximate duration: 1 hour.

## Core idea

What a user experiences as `the AI` is the result of several interacting layers.

A useful model is:

**model + harness + instructions/settings + context + tools + environment + feedback = observed behaviour**

## Use the existing Claude/ChatGPT preference

The learner preferred Claude's responses because they tended to be less verbose. Treat that as a valid product preference, but distinguish it from a model capability claim.

Configure ChatGPT or the agent to respond more concisely and compare again.

Discuss which behaviour came from:

- the model;
- the product harness;
- explicit instructions;
- response settings;
- available tools;
- current context.

The lesson is not that models are identical. It is:

> Do not attribute something to the model until you have considered whether it came from configuration or environment.

## Useful debugging question

Whenever something works badly, ask:

> Is this a model problem, a context problem, a harness problem, a tool problem, or a feedback problem?

## Examples

- Shorter answers may be an instruction or verbosity setting.
- Access to Gmail is a tool capability, not evidence of greater reasoning ability.
- A model that has not inspected the repository may lack context rather than intelligence.
- A model that cannot verify a result may be missing feedback rather than reasoning capacity.

## Discussion prompts

- What would constitute a fair model comparison?
- Which preferences are product preferences rather than model preferences?
- What parts of an agent system can we change without changing the underlying model?

## Optional comparison

Later, repeat the same task in two different agentic IDEs with comparable repository access. Use the experience to separate model differences from harness differences.
