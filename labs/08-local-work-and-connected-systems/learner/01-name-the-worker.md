# 01 — Name the worker

Lab 7 ended with a question:

> **What exactly did we just create?**

Start with your own answer.

You took a model and deliberately added things around it:

```text
instructions
capabilities
skills and workflows
domain knowledge
project state
permissions
ways to judge the work
```

What would you call the resulting thing?

## Look at the worker that is running now

Ask the local agent:

> **What project instruction sources are currently in force for you, and where did they come from?**

Then open the instruction files with the facilitator.

Notice that the agent did not need you to paste every applicable instruction into the prompt manually.

Ask:

- Which instructions apply broadly?
- Which apply specifically to this working location?
- Did every file in the environment automatically become part of the model's context?

Keep this working model:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

The important qualification is:

> **The environment can contain more than the worker currently has in context or has discovered.**

Keep that in mind for the next card.