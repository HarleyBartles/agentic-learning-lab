# Module 6 — Local work and connected systems

Approximate duration: 1 hour.

## Core idea

Direct project access and connectors solve different problems. They should be composed rather than treated as substitutes.

The repository is the workplace. Connectors let the agent reach outside that workplace.

## Suggested session shape

### 0–15 minutes — Compare access modes

Ask the learner what an on-disk agent can inspect without anyone pre-selecting files for it.

Examples:

- walk directories;
- read many files;
- grep/search broadly;
- inspect Git history;
- run project scripts;
- render outputs;
- compare generated artifacts;
- discover things nobody knew to retrieve explicitly.

Then ask what a connector is especially good at: reaching systems that are not part of the local project environment.

### 15–35 minutes — Run the same repo through two routes

Use this learning-lab repository itself.

Through the GitHub connector, ask a focused remote-state question such as:

- Which module discusses safe breakage?
- What files currently exist under `modules/`?
- What is the latest remote commit touching a chosen file?

Then use the local agent to inspect the repository broadly:

> Explore this repository and explain how the learning plan, labs, and project examples fit together. Follow any references you think matter.

Discuss how the connector retrieved useful remote information while the local agent could freely traverse the working copy and build its own map.

### 35–50 minutes — Retrieval versus exploration

Use the distinction:

> Retrieval asks for something. Exploration discovers what is there.

A connector may be exactly right for `find the issue where we decided X` or `read the email Bob just sent`.

A local agent is better positioned for `deeply understand this project, inspect whatever is relevant, and modify it safely`.

Neither is universally better.

### 50–60 minutes — Compose them

Sketch a realistic environment:

```text
                     email / calendar
                          |
issue tracker ---- local agent ---- GitHub remote
                          |
                    project repo
                    local tools
                    instructions
```

Ask which systems the project should be able to touch, which should be read-only, and which do not belong in this environment at all.

This prepares later conversations about least privilege and deliberate capability boundaries.

## Tools to experiment with

- GitHub connector/MCP;
- local repository inspection via Codex;
- Git CLI/history locally;
- optionally one external non-GitHub connector if there is a clear harmless example.

## Discussion prompts

- When is focused retrieval enough?
- When does an agent need freedom to explore broadly?
- What does direct filesystem access reveal that a search result may not?
- Which external systems should this project be allowed to touch?
- Where should authoritative project state live?

## Principle

> Put the agent close to the source of truth it needs to work on, and give it appropriate bridges to everything else.

## Do not teach yet

Do not turn MCP into a protocol lecture. At this stage it is enough to understand it as a way to expose external context and actions to the agent. Protocol internals can wait until there is a reason to care.
