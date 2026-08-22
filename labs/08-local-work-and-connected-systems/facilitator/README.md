# Lab 8 facilitator guide

Status: **Mature and ready to run.**

## Learning goal

The learner should leave understanding that an agent does not perceive its whole environment automatically. A worker only reasons over what its harness, instructions, tools and chosen discovery routes actually bring into view.

They should be able to explain:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

And they should leave with a Course-1-safe model:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

## Contract

No coding knowledge is assumed. No coding is required.

Do not require the learner to understand shell syntax, Git internals, workflow YAML, or implementation details. Those surfaces are evidence for the lesson, not prerequisites.

The learner must be able to participate in the judgment loop without manually implementing anything.

## Setup

Before the learner arrives:

1. Use a fresh branch/fork state where `labs/08-local-work-and-connected-systems/working/environment/` exists exactly as shipped.
2. Confirm a local Codex session can be rooted at `working/environment/`.
3. Confirm the worker can report the project instruction sources currently in force.
4. Confirm the root `INDEX.md` reaches `curriculum/` and `references/` but not `forgotten/`.
5. Do not reveal the `forgotten/` omission before Exercise 3.
6. Confirm the learner's GitHub-connected surface can answer at least one harmless remote-state question. Prefer workflow-run state if available; otherwise use branch head, PR presence or commit presence.
7. Keep learner and facilitator files outside the local worker's working root.

## Exercise 1 — Name the worker without leaving a false model

Start from Lab 7's final question:

> **What exactly did we just create?**

Let the learner answer naturally. `An agent`, `a worker`, or `a provisioned agent` are all useful.

Then reconstruct the parts together:

```text
model
+ harness
+ effective instructions
+ tools/capabilities
+ skills/workflows and domain material
+ project state
+ permissions
+ access/discovery mechanisms
+ verification/feedback
```

Now add the missing qualification:

> The environment can contain more than the worker currently has in context or has discovered.

That is the important Course 1 correction. Do not leave the learner with `model + everything in the environment = agent`.

### Deepen AGENTS.md

Lab 5 already exposed `AGENTS.md` as a standing-instruction surface. Here, teach why it can affect a worker before the worker manually opens the file.

Start Codex in `working/environment/` and ask:

> What project instruction sources are currently in force for you, and where did they come from?

Open:

- `working/AGENTS.md`
- `working/environment/AGENTS.md`

Map which instruction applies broadly and which applies locally.

Explain the product-specific fact carefully:

- in Codex, applicable `AGENTS.md`/override files are a harness-recognised project-instruction mechanism;
- they are supplied according to project/directory scope;
- this is not a universal law of all agent harnesses.

The durable concept is:

> **A harness can automatically materialise scoped project instructions into a worker's context.**

Do not overteach exact implementation internals. The learner needs the mechanism and boundary, not a protocol specification.

## Exercise 2 — Open the navigation mesh

Open `working/environment/INDEX.md` with the learner.

Ask what is different from `AGENTS.md`.

The intended distinction is:

```text
AGENTS.md
harness knows this convention
→ applicable instructions are supplied

INDEX.md
project knows this convention
→ worker follows the map deliberately
```

Then ask the worker:

> Using only the INDEX.md navigation mesh, tell me what this environment contains and where the documented operating material lives. Do not perform a broad filesystem search.

Let it follow the mesh.

The index is deliberately useful. It should orient the worker efficiently and correctly across the indexed surface.

Avoid teaching the blind spot too early. First let the learner appreciate why deliberate navigation is valuable.

## Exercise 3 — Let the route fail honestly

Ask:

> Using only the INDEX.md navigation mesh, what is the escalation keyword for the field exercise? Do not perform a broad filesystem search.

The answer is physically present in `forgotten/answer.md`, but `forgotten/` is not represented in the mesh.

A compliant worker should say it cannot establish the answer from the allowed navigation route.

If it performs a broad search anyway, stop and rerun in a fresh turn with the constraint made explicit. The experiment depends on holding the observation method constant.

Do not mock the worker for failing to find the answer. Under its allowed evidence route, the correct epistemic posture is uncertainty.

Then ask:

> List the contents of `forgotten/`, read the relevant file, and answer the same question.

The answer should now become visible.

Ask the learner to classify what changed:

- filesystem access did not change;
- file contents did not change;
- model capability did not change;
- the observation route changed.

This is the core reveal.

Use the ladder:

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

Then earn:

> **When absence matters, understand how the agent looked before trusting the conclusion.**

## Exercise 4 — Widen beyond the local environment

Now ask:

> What if the state we need is not on this disk at all?

Use the repository-integrity workflow as the preferred real example.

With the local worker, inspect the checked-in workflow/checker/test files and ask what they establish.

The learner should be able to say:

> These files show what is configured or intended to happen.

Then use a GitHub-connected worker and ask for current remote evidence, preferably whether the relevant repository-integrity workflow run actually completed successfully.

The learner should be able to say:

> GitHub remote state can establish what GitHub recorded as actually happening remotely.

If workflow-run inspection is unavailable, choose another remote-state distinction that is easy to understand:

- current remote branch head;
- whether a PR exists;
- whether a commit is present remotely;
- whether a branch exists remotely.

Do not create a false local/cloud dichotomy. Say explicitly:

> Retrieval and exploration are strategies. Local and connected are access surfaces.

A connector can support exploration. A local worker can perform precise retrieval. The lab is about what surface is being observed and what the resulting evidence establishes.

## Finish on the next problem

Bring together three possible statements:

- local working state says one thing;
- GitHub remote state says another;
- a project note states what should be true.

Ask:

> The worker can see all three. Which one should it trust?

Then:

> What would actually prove that the required work is correct?

Stop there.

Do not solve source-of-truth and verification in this lab. Lab 9 owns that distinction.

## If the live experiment varies

### Worker already mentions the unindexed folder

Check whether it used a broad filesystem command despite the constraint. If so, reset to a fresh turn and explicitly require navigation only through reachable `INDEX.md` links.

If the harness itself surfaces a full directory listing automatically, use a nested fixture location that is not exposed by that listing or change the question so the answer still requires following the mesh. Preserve the underlying contrast between accessible state and route-mediated discovery.

### Worker cannot report AGENTS.md sources clearly

Do not turn the session into harness debugging. Open the applicable files manually and explain the scoped-instruction mechanism. The observation is stronger when the worker can report it, but the lesson does not depend on a particular introspection phrase.

### GitHub workflow runs are unavailable

Use another current remote-state fact. The invariant is:

> local source can describe intended/configured state; a connected remote surface can establish remote state that the local checkout alone cannot prove.

### Learner asks whether INDEX.md is a standard

Answer no. It is a project convention used here to teach a durable navigation idea. Other repositories may use READMEs, docs sites, manifests, generated indexes, search, databases or other navigation structures.

## What not to teach yet

Do not introduce specialist sub-agent profiles merely to make the agent definition more elaborate.

Do not teach trust boundaries in depth; Course 3 owns that wider system problem.

Do not teach retrieval/RAG mechanics in depth; later context-engineering material owns them.

Do not let the learner conclude that broad recursive search is always safer or better than indexes. Efficient guided navigation and exploration have different costs and failure modes.

Do not solve Lab 9's authority problem early.