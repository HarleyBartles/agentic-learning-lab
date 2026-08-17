# Module 8 — What did we just create? Local work and connected systems

Approximate duration: 1 hour.

## Core idea

Lab 5 decomposes the system around a model. Module 6 then asks what the model already knows and what changes when external evidence is removed or restored. Module 7 turns that into practical domain provisioning across software engineering, novel writing, and technical drawing, transferring domain authority from facilitator to shared proficiency to learner.

This module should begin immediately after that three-domain progression and briefly let the learner name the assembled thing before asking where it should operate.

A useful opening question is:

> In Module 7 you took models that already knew some things, gave them suitable capabilities, supplied operating/domain knowledge that could not safely be assumed, and added ways to judge the work. What exactly did you create?

At this stage, it is fair and useful for the learner to answer:

> We created an Agent for this job.

Do not immediately over-correct that model.

The useful interim conception is:

> **An agent is the model-in-environment, equipped and instructed to do a job.**

Operationally, the learner has created a worker.

The deeper distinction between a broad environment and specific custom agent profiles/sub-agents should be deliberately deferred until a later module has created a reason for that refinement.

This follows the curriculum-wide pattern of giving the learner a useful mental model, letting it become operational knowledge, and only breaking it when a later requirement exposes its limits.

A rough decomposition to recall is:

```text
model
reasoning capability and broad uneven prior knowledge

+ harness
where/how it operates

+ tools
what it can do

+ instructions
how it should behave

+ skills/workflows
how it should perform recurring work

+ domain material
what good looks like here

+ project state
what it knows about this job

+ permissions
what it is allowed to touch

+ verification/feedback
how its work is judged

= a provisioned worker for a job
```

The question for this module then becomes:

> We built a worker. Where should that worker work, and what other systems should it be connected to?

## Local work and connected systems

Direct project access and connectors solve different problems. They should be composed rather than treated as substitutes.

The repository is the workplace. Connectors let the agent reach outside that workplace.

Do not teach `local = agent` or `cloud = not agent`.

Local, cloud, connected, and mixed arrangements are deployment and access choices for a worker. They are not the definition of agency.

The learning-lab repository itself is useful evidence: substantial curriculum development has been performed by a cloud ChatGPT worker operating through a GitHub connector rather than by an on-disk agent.

## Suggested session shape

### 0–10 minutes — Name the worker

Ask:

> Across the Module 7 exercises you combined model knowledge, tools, instructions, references, domain provision and quality checks. What exactly did you just create?

Let the learner reason toward `an Agent` or `a worker for this job`.

Use the interim model rather than immediately introducing specialist profiles.

Then ask:

> If that is our worker, where should it actually work?

This opens the access/deployment question.

### 10–25 minutes — Compare access modes

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

### 25–40 minutes — Run the same repo through two routes

Use this learning-lab repository itself.

Through the GitHub connector, ask a focused remote-state question such as:

- Which lab discusses safe breakage?
- What files currently exist under `modules/`?
- What is the latest remote commit touching a chosen file?

Then use the local agent to inspect the repository broadly:

> Explore this repository and explain how the learning plan, labs, and project examples fit together. Follow any references you think matter.

Discuss how the connector retrieved useful remote information while the local agent could freely traverse the working copy and build its own map.

### 40–50 minutes — Retrieval versus exploration

Use the distinction:

> Retrieval asks for something. Exploration discovers what is there.

A connector may be exactly right for `find the issue where we decided X` or `read the email Bob just sent`.

A local agent is better positioned for `deeply understand this project, inspect whatever is relevant, and modify it safely`.

Neither is universally better.

### 50–60 minutes — Compose the worker's environment

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

Ask which systems the worker should be able to touch, which should be read-only, and which do not belong in this environment at all.

This prepares later conversations about least privilege, deliberate capability boundaries, and eventually specialist workers with different access profiles.

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

Do not force this into the first version of the Module 8 lab if it makes the session too dense. It can be a dedicated exercise or later callback once the learner has enough experience to appreciate the difference between having filesystem access and actually discovering something through that filesystem.

## Future deliberate model break — one environment, several workers

Preserve the learner's useful Module 8 conception for now:

> We provisioned the environment and created an Agent for this job.

A later specialist/sub-agent module should deliberately reopen it:

> What if the same project needs several workers that should not all think, act, or access things in the same way?

That is where the learner can discover that a broad environment can support multiple distinct agent profiles and that an invoked profile can become a specialist worker within that environment.

Do not explain that machinery here. The later contradiction is pedagogically useful.

## Tools to experiment with

- GitHub connector/MCP;
- local repository inspection via Codex;
- Git CLI/history locally;
- filesystem search/glob/grep when demonstrating exploration;
- optionally one external non-GitHub connector if there is a clear harmless example.

## Discussion prompts

- What did we actually create when we provisioned the worker?
- Which parts belong to the model and which belong to its operating environment?
- When is focused retrieval enough?
- When does an agent need freedom to explore broadly?
- What does direct filesystem access reveal that a search result may not?
- Can something be accessible but still fail to be discovered?
- Which external systems should this worker be allowed to touch?
- Where should authoritative project state live?

## Principle

> Put the agent close to the source of truth it needs to work on, and give it appropriate bridges to everything else.

And, for this stage of the curriculum:

> **The agent is the model-in-environment, equipped and instructed to do a job.**

Treat that as a useful working model, not the final word.

## Do not teach yet

Do not turn MCP into a protocol lecture. At this stage it is enough to understand it as a way to expose external context and actions to the agent. Protocol internals can wait until there is a reason to care.

Do not introduce custom agent profiles or sub-agent orchestration merely to make the definition more technically complete. Let the learner first use the simpler worker model until later work creates a concrete reason to break it.