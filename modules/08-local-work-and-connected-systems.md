# Module 8 — What did we just create? Local work and connected systems

Approximate duration: 60–75 minutes.

Status: structured planning. The design is mature enough to promote into a lab after the current side quest; do not scaffold the lab yet.

## Core idea

Lab 5 decomposes the system around a model. Lab 6 asks what the model already knows and what changes when supplied/retrieved evidence is removed or restored. Lab 7 turns that into practical domain provisioning across three authority arrangements.

Module 8 should begin immediately after Lab 7 and ask:

> In Lab 7 you combined model knowledge, capabilities, instructions, operating/domain knowledge, project state and ways to judge the work. What exactly did you create?

It is useful for the learner to answer `an agent` or `a worker for this job`, but Course 1 must not leave them carrying an unqualified equation such as `agent = model + everything in the environment`.

By the end of this lab, the learner should hold a more complete working model:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

That is still a deliberately practical definition rather than a final ontology, but it is not knowingly false. Later specialist/sub-agent material may refine how several differently provisioned workers share an environment without requiring Course 1 learners to unlearn a stale misconception.

A useful decomposition to recall is:

```text
model
reasoning capability and broad uneven prior knowledge

+ harness
how the model is run and which conventions are recognised

+ effective instructions
what operating guidance actually reaches this worker

+ tools/capabilities
what it can observe and do

+ skills/workflows and domain material
how recurring work should be done and what good looks like

+ project state
what durable state exists for this job

+ permissions
what it may read/change/reach

+ access and discovery mechanisms
how available state is selected, navigated, retrieved or explored

+ verification/feedback
how work is judged

= a provisioned worker operating against an environment
```

The missing qualification is central:

> **The environment can contain more than the model currently has in context or has successfully discovered.**

Having filesystem or connector access does not pour every reachable object into model context.

## Agent perception: environment, context and navigation

This lab should make visible how an agent comes to know about its working world.

Use three distinct project surfaces:

```text
AGENTS.md
harness-recognised scoped operating instructions

INDEX.md
project-authored navigation convention

filesystem / connector / search tools
mechanisms for observing what actually exists on an accessible surface
```

The learner should not collapse these into one generic concept of `files the agent can see`.

## Scoped AGENTS.md as automatically supplied project context

Lab 5 has already revealed `AGENTS.md` as a project-instruction surface. Module 8 is the right place to deepen the learner's understanding of how its scope affects a worker.

For Codex, make the product-specific fact explicit and bounded: Codex discovers applicable `AGENTS.md` / override instruction files according to project/directory scope and supplies those instructions to the worker. This is a Codex harness convention, not a universal law of agents.

A useful experiment is to start a fresh local worker in a directory with both repository-level and more-local instructions and ask:

> What project instruction sources are currently in force for you, and where did they come from?

Then open the actual files with the learner and map the effective scope.

Earn the durable concept underneath the implementation detail:

> **A harness can automatically materialise scoped project instructions into a worker's context.**

The learner should understand that the file existing somewhere in the repository is not the whole mechanism; the harness recognises it and supplies the applicable instructions.

## INDEX.md and the navigational mesh

Now introduce a contrasting mechanism.

`INDEX.md` is not assumed to be harness magic. It is a project convention: a deliberately authored map an agent can follow to navigate a larger body of project material without recursively scanning everything.

Open the index files with the learner rather than hiding the mechanism behind agent behaviour.

A simple mesh might look like:

```text
INDEX.md
├── curriculum -> curriculum/INDEX.md
├── examples   -> examples/INDEX.md
└── references -> references/INDEX.md
```

Each child index describes its own neighbourhood and points onward where appropriate.

The useful distinction is:

```text
AGENTS.md
what operating guidance applies here?
(harness-recognised and automatically supplied in the Codex example)

INDEX.md
where should I look next?
(project navigation convention deliberately followed by the worker)
```

The index mesh is valuable because large project environments should not require every worker to ingest or recursively scan everything merely to discover where relevant knowledge lives.

## Core pressure exercise — the blind spot in the mesh

The mature Lab 8 should deliberately make the index mesh incomplete.

Prepare a bounded project surface such as:

```text
workspace/
    INDEX.md
    curriculum/
        INDEX.md
        ...
    references/
        INDEX.md
        ...
    forgotten/
        answer.md
```

`forgotten/` physically exists inside the worker's accessible workspace but is not referenced by the root index or any reachable child index.

First instruct the worker:

> **Use only the INDEX.md navigation mesh to find the information about X. Do not perform a broad filesystem search.**

A competent worker may correctly follow the declared route to its edge and report that it cannot find the requested information.

Do not frame this as the agent becoming stupid or failing to obey. Under the observation method it was given, the conclusion can be reasonable.

Then change only the observation route. Ask directly:

> **List the contents of `forgotten/`.**

The worker should now expose the previously missed file.

The learner can establish:

```text
the folder existed
+
the worker had filesystem access to it
+
the worker could list/read it when directly addressed
+
the index mesh did not lead there
=
accessible but undiscovered through the chosen navigation route
```

Ask explicitly:

- Did the worker lack filesystem access? No.
- Did it lack capability to read the file? No.
- Was the file absent? No.
- What failed? The navigation/discovery route was incomplete for the question being asked.

Earn:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

> **When absence matters, understand how the agent looked before trusting the conclusion.**

A useful conceptual ladder is:

```text
thing exists
!=
thing is represented in Git
!=
thing is represented in the project's navigation scheme
!=
thing has entered the worker's current context
!=
worker will discover it
```

This is not an argument against index meshes. It teaches their boundary. Efficient guided navigation and broad exploration solve different problems.

## Retrieval and exploration are strategies, not local/cloud identities

Preserve the distinction without teaching a false mapping such as `connector = retrieval` and `local = exploration`.

Retrieval asks through some known route for relevant information. Exploration broadens the observation method to discover what is actually present.

An index mesh is retrieval-oriented:

> The project tells me where things are.

A filesystem walk or broad search is exploratory:

> I am going to discover what actually exists on this accessible surface.

A connector can support focused retrieval or broad traversal depending on its interface. A local worker can perform exact retrieval or exploratory search. The strategy and the access surface are separate engineering choices.

## Widen the environment: local source and connected remote state

After the learner understands navigation inside the local environment, widen the question:

> What about relevant state that does not live on this filesystem at all?

Direct project access and connectors solve different problems and should be composed rather than treated as substitutes.

Do not teach `local = agent` or `cloud = not agent`. Local, cloud, connected and mixed arrangements are deployment/access choices for a worker.

The repository's real GitHub Actions workflow is a useful representative example:

- the local checkout can expose the workflow definition, checker and tests — what source says should run;
- GitHub remote state can establish whether a workflow actually ran and what conclusion the remote system recorded.

Use the same factual question across both surfaces where practical so the learner can attribute differences to the evidence surface rather than to a changed task.

Earn:

> **Source can describe intended remote behaviour without proving the remote event happened.**

This should prepare Module 9 without cashing its authority/verification lesson prematurely.

## Compose the worker's environment

Ask the learner to sketch a realistic worker environment:

```text
                     email / calendar
                          |
issue tracker ---- worker / harness ---- GitHub remote
                          |
                    project repo
                    local tools
                    instructions
                    navigation mesh
```

Ask:

- what belongs directly in the project workplace?
- which outside systems need connectors?
- what should be read-only?
- what does this worker not need at all?
- which surfaces are automatically supplied, deliberately navigated, directly explored or externally retrieved?

This prepares later least-capability and specialist-worker material without teaching it early.

## Course-1-safe agent model

Do not end this lab by saying the learner has a knowingly incomplete misconception that will be corrected after the course break.

Reconcile explicitly:

> **The agent is not merely the model, and it is not the entire environment. It is a model operating through a harness with an effective set of instructions and capabilities, observing and acting on an environment through particular access and discovery mechanisms.**

Later modules can refine this model — for example, one broad environment may support several differently configured specialist workers — but a learner who stops after Course 1 should already have a defensible mental model.

## Handoff to Module 9

Lab 8 should finish by giving the worker several accessible observations that disagree or answer different parts of a question.

For example:

```text
local project state says X
GitHub remote state says Y
another durable project source says Z
```

Then ask:

> **The worker can reach all three. Which one should it trust?**

And:

> **What would actually prove that the work is correct?**

Stop there.

Lab 8 establishes how a worker gets to observe things. Lab 9 owns authority and verification:

> **Access tells us what evidence the worker can reach. It does not tell us which source is authoritative or whether the work is correct.**

## Tools to experiment with

- Codex/local repository inspection;
- scoped `AGENTS.md` / `AGENTS.override.md` behaviour;
- project-authored `INDEX.md` navigation mesh;
- filesystem list/search/glob for the discovery comparison;
- GitHub connector/MCP for remote state;
- Git CLI/history only where it supports the observation lesson.

## Discussion prompts

- What did we actually create when we provisioned the worker?
- What part of the environment has actually entered the model's working context?
- Which instructions were automatically supplied by the harness?
- Which knowledge did the worker have to navigate or retrieve deliberately?
- What does an index prove, and what does it not prove?
- Can something be accessible but still fail to be discovered?
- When should a worker widen its discovery method?
- What can local source establish about a remote system, and what requires observing that remote system?
- Which external systems should this worker be able to reach?
- When several accessible sources disagree, what question must we ask next?

## Principles

> **Access is not context.**

> **Access does not guarantee discovery.**

> **When absence matters, understand how the agent looked before trusting the conclusion.**

> **Put the worker close to the state it needs to act on, and give it appropriate bridges to the rest — while remaining explicit about how evidence actually reaches its context.**

## Do not teach yet

Do not turn MCP into a protocol lecture. At this stage it is enough to understand connectors/MCP as mechanisms that expose external context or actions to a worker.

Do not introduce specialist/sub-agent orchestration merely to make the agent definition more elaborate. The Course-1 model should be correct enough to stand on its own while leaving room for later refinement.

Do not treat `INDEX.md` as a universal harness standard. It is the worked project-navigation convention used to expose the durable distinction between environment access and discovery.