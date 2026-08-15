# Labs

A lab is the complete learning experience for a curriculum topic.

A lab may contain three distinct surfaces:

```text
facilitator/
    rationale, setup, teaching guidance, observations, and things to defer

learner/
    learner-facing exercise cards or reference material, revealed as needed

mission/ or another working folder
    the bounded project environment where the task itself lives
```

These are not separate root-level systems. They belong together because they describe and run the same learning experience.

The working environment should be scoped deliberately. If an agent only needs the mission workspace, point the agent at that workspace rather than the whole teaching lab. This keeps facilitator and learner choreography out of the agent's project context and creates a clean boundary between teaching material and project state.

Some setup may be performed in advance by the facilitator so early labs can teach an abstraction without first teaching all of its machinery. That setup should use normal capabilities of the harness rather than artificial tricks. Later labs can reveal the hidden configuration and explore its alternatives and tradeoffs.

## Current stable lab

- `01-chatbot-to-worker/` — compare complete cloud context, deliberately incomplete cloud context, and an on-disk worker operating directly in the mission workspace.

## Safety

Nothing in these labs should be precious. The learner should be free to make bad changes, delete generated outputs, inspect surprising results, and later learn how to recover more consequential state safely.
