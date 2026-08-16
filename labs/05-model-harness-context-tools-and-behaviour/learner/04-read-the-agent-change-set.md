# Exercise 4 — Read the agent change set

Before looking at any new scenarios, inspect the accumulated working-tree state from this lab:

`git status --short`

You should be able to find three deliberate interventions:

- a tracked change to standing project instructions;
- new untracked project evidence;
- a new untracked checking tool.

Inspect `git diff -- AGENTS.md` for the tracked instruction change, and open the two new files if you need to inspect their contents.

Ask:

> What did we actually change about the worker during this lab?

Try to map each change to a layer of the system before reading on.

A useful compact model is:

> **model + harness + instructions/settings + context + tools + environment/state + feedback = observed behaviour**

Now use that model on the scenarios below.

For each one, answer three questions:

1. Which layer or layers are plausible suspects?
2. What evidence would you inspect first?
3. What is the smallest justified intervention after that inspection?

There may be more than one plausible cause.

## Scenario A

The agent gives an 800-word answer when you wanted a short operational brief, even though the factual content is good.

## Scenario B

The agent says it cannot tell whether a proposed venue layout is allowed. You know the rule exists somewhere on your computer, but that file is outside the agent's current workspace.

## Scenario C

The agent can explain exactly how to query a database, but it cannot actually inspect the database in its current environment.

## Scenario D

Every new session violates the same project naming convention until you remind the agent again.

## Scenario E

The agent creates a plausible schedule and confidently says it works, but nobody and nothing checks the output against the scheduling constraints.

## Scenario F

Two products using what you believe is the same underlying model behave differently. One can search connected project systems and carries project instructions; the other only sees the prompt you typed.

## Scenario G

You hold the task, prompt, project context, tools, instructions, and verification opportunity reasonably constant. Across repeated bounded trials, Model A succeeds reliably and Model B repeatedly fails the same reasoning step.

For the final scenario, it is acceptable to say:

> Model capability is now a serious suspect.

The rule is not `never blame the model`.

Keep this line:

> **Diagnosis before intervention.**
