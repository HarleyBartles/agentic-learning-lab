# Module 7 — Local work and connected systems

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

## Future callback — access is not discoverability

This module is also the natural home for a deeper lesson about local-agent blindness.

Labs 2 and 4 establish two simpler facts first:

- project state can exist locally without being represented in the repository;
- Git only gives a recovery path for content that entered Git history.

Later, deepen that into a distinct discovery problem:

> A thing can exist, be accessible to the agent, and still be operationally invisible.

Use a project whose normal navigation is mediated by an index mesh or similar declared structure. For example, each directory can contain an `INDEX.md` that names the files and subdirectories considered part of the project's navigable structure.

Then place an ignored or otherwise undeclared local tree physically inside the project workspace but outside that navigation contract.

A competent on-disk agent may follow the index mesh perfectly, reach the edge of what is declared, and report that it found nothing relevant even though the desired object is sitting on disk nearby.

The intended model is:

```text
thing exists
≠
thing is represented in Git
≠
thing is represented in the project's navigation scheme
≠
agent will discover it
```

This should explicitly distinguish **retrieval** from **exploration**.

An index mesh is retrieval-oriented:

> The project tells me where things are.

A filesystem glob, broad search, or directory walk is exploratory:

> I am going to discover what actually exists.

Neither method is universally better. The failure occurs when the agent treats a declared navigation structure as proof that nothing exists outside it.

Useful lines to earn:

> Existence is not the same as discoverability.

> Access does not guarantee discovery.

> A navigation structure describes what it knows about. It does not prove that nothing exists outside it.

> When expected evidence is missing, widen the discovery method before concluding the thing does not exist.

This is a good place to reinforce that putting an agent "close to the project" improves its opportunities to inspect state, but does not magically guarantee that it will search every relevant surface or infer every hidden path.

Do not force this into the first version of the Module 7 lab if it makes the session too dense. It can be a dedicated exercise or later callback once the learner has enough experience to appreciate the difference between having filesystem access and actually discovering something through that filesystem.

## Tools to experiment with

- GitHub connector/MCP;
- local repository inspection via Codex;
- Git CLI/history locally;
- filesystem search/glob/grep when demonstrating exploration;
- optionally one external non-GitHub connector if there is a clear harmless example.

## Discussion prompts

- When is focused retrieval enough?
- When does an agent need freedom to explore broadly?
- What does direct filesystem access reveal that a search result may not?
- Can something be accessible but still fail to be discovered?
- Which external systems should this project be allowed to touch?
- Where should authoritative project state live?

## Principle

> Put the agent close to the source of truth it needs to work on, and give it appropriate bridges to everything else.

## Do not teach yet

Do not turn MCP into a protocol lecture. At this stage it is enough to understand it as a way to expose external context and actions to the agent. Protocol internals can wait until there is a reason to care.
