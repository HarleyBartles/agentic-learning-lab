# Lab 8 facilitator guide

Status: **Mature and ready to run.**

## Learning goal

The learner should leave understanding that an agent does not perceive its whole environment automatically. A worker only reasons over what its harness, instructions, tools and chosen discovery routes actually bring into view.

They should be able to explain:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

They should also see that a useful navigation structure becomes dangerous if everyone assumes it is fresh while nobody owns how freshness is maintained.

Earn:

> **Do not hand-maintain derived navigation when the project can regenerate it deterministically.**

> **If freshness matters at commit time, encode that expectation into the commit path instead of relying on memory.**

And leave with a Course-1-safe model:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

## Contract

No coding knowledge is assumed. No coding is required.

Do not require the learner to understand Python, shell syntax, Git internals, workflow YAML, or hook implementation details. Those surfaces are facilitator-provided infrastructure and evidence for the lesson, not prerequisites.

The learner must be able to participate in the judgment loop without manually implementing anything.

## Setup

Before the learner arrives:

1. Use a fresh branch/fork state where `labs/08-local-work-and-connected-systems/working/environment/` exists exactly as shipped.
2. Confirm a local Codex session can be rooted at `working/environment/`.
3. Confirm the worker can report the project instruction sources currently in force.
4. Confirm the root `INDEX.md` reaches `curriculum/` and `references/` but not `forgotten/`.
5. Do not reveal the `forgotten/` omission before Exercise 3.
6. Keep `facilitator/tooling/` outside the worker's root and do not copy its generator or hook into the working environment before Exercise 4.
7. Run `python -m unittest facilitator/tooling/test_generate_index_mesh.py -v` from the lab directory or an equivalent path and confirm all tests pass.
8. Confirm Git hooks can run in the learner's local Git environment. Git for Windows, macOS and Linux are all acceptable; handle executable-bit/platform plumbing for the learner rather than turning it into their task.
9. Confirm the learner's GitHub-connected surface can answer at least one harmless remote-state question. Prefer workflow-run state if available; otherwise use branch head, PR presence or commit presence.
10. Keep learner and facilitator choreography outside the local worker's working root.

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

Add the qualification:

> The environment can contain more than the worker currently has in context or has discovered.

Do not leave the learner with `model + everything in the environment = agent`.

### Deepen AGENTS.md

Lab 5 already exposed `AGENTS.md` as a standing-instruction surface. Here, teach why it can affect a worker before the worker manually opens the file.

Start Codex in `working/environment/` and ask:

> What project instruction sources are currently in force for you, and where did they come from?

Open:

- `working/AGENTS.md`
- `working/environment/AGENTS.md`

Map which instruction applies broadly and which applies locally.

Explain the product-specific fact carefully:

- in Codex, applicable `AGENTS.md` / override files are a harness-recognised project-instruction mechanism;
- they are supplied according to project/directory scope;
- this is not a universal law of all agent harnesses.

The durable concept is:

> **A harness can automatically materialise scoped project instructions into a worker's context.**

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

The answer is physically present in `forgotten/answer.md`, but `forgotten/` is not represented in the hand-authored mesh.

A compliant worker should say it cannot establish the answer from the allowed navigation route.

If it performs a broad search anyway, rerun in a fresh turn with the constraint made explicit. The experiment depends on holding the observation method constant.

Do not mock the worker. Under its allowed evidence route, uncertainty is the correct posture.

Then ask:

> List the contents of `forgotten/`, read the relevant file, and answer the same question.

Ask the learner to classify what changed:

- filesystem access did not change;
- file contents did not change;
- model capability did not change;
- the observation route changed.

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

## Exercise 4 — Keep the mesh trustworthy

Do not jump straight from `the mesh drifted` to `remember to edit it better`.

Ask:

> **If we expect agents to rely on this navigation mesh, what would make it trustworthy enough to rely on?**

If the learner suggests hand-edit discipline, accept it as a first answer and then pressure it:

> Who remembers? What happens after six months? What if three people add folders differently? What tells us the mesh matches the commit we are about to ship?

Now reveal `facilitator/tooling/`.

Copy `generate_index_mesh.py` into:

`working/environment/tools/generate_index_mesh.py`

Stage the copied tool if it is intended to enter the next learner commit.

Explain only the observable contract of the generator:

- it derives the mesh from Git's staged/tracked view;
- the same staged/tracked structure produces the same output;
- repeated generation without a structural change produces no additional change;
- unstaged local files do not leak into the commit mesh.

The learner does not need to inspect the Python unless they want to.

Run it and inspect the result. `forgotten/` should become represented and receive its own generated `INDEX.md`.

Run it again. There should be no further index-content change.

Name the properties:

```text
deterministic
same staged/tracked state -> same mesh

idempotent
run it again -> no accumulating change
```

Then ask:

> We fixed the generator. Who remembers to run it before every commit?

Introduce hooks only as a lifecycle mechanism:

> A Git hook is a command Git can run automatically at a particular point in its workflow.

This lab uses `pre-commit` because the invariant matters exactly when project state is about to become durable history.

Copy/install the supplied `pre-commit-index-mesh` hook into the learner fork's `.git/hooks/pre-commit` location. Handle platform-specific executable setup yourself.

Its intended behavior is deliberately narrow:

```text
before commit
→ regenerate mesh from staged/tracked Git state
→ stage only generated INDEX.md files
→ continue commit
```

Do not let it broadly `git add` the repository. The hook must not sweep unrelated learner changes into a commit.

Have the learner make and stage one harmless structural change under the exercise environment, then commit it.

Inspect the resulting commit/diff together:

- did the structural change land?
- did the matching index update land?
- did unrelated unstaged work stay out?
- would another checkout of that commit receive the same navigation representation?

The durable principle is broader than Git:

> **If important derived state must stay synchronized with source state, make regeneration reproducible and attach it to the lifecycle point where freshness matters.**

Keep the boundary explicit: a generated mesh can be trustworthy about the tracked structure it models without becoming authoritative about every truth in the environment.

## Exercise 5 — Widen beyond the local environment

Now ask:

> What if the state we need is not on this disk at all?

Use the repository-integrity workflow as the preferred real example.

With the local worker, inspect the checked-in workflow/checker/test files and ask what they establish.

The learner should be able to say:

> These files show what is configured or intended to happen.

Then use a GitHub-connected worker and ask for current remote evidence, preferably whether the relevant repository-integrity workflow run actually completed successfully.

The learner should be able to say:

> GitHub remote state can establish what GitHub recorded as actually happening remotely.

If workflow-run inspection is unavailable, choose another remote-state distinction:

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

If the harness itself surfaces a full directory listing automatically, use a nested fixture location that is not exposed by that listing or change the question so the answer still requires following the mesh.

### Worker cannot report AGENTS.md sources clearly

Do not turn the session into harness debugging. Open the applicable files manually and explain the scoped-instruction mechanism.

### Generator appears to include an unrelated local draft

That is a tooling defect, not a learner lesson. Stop and verify that the facilitator-supplied generator is the staged/tracked-state version and that its tests pass. Do not normalize a misleading commit mesh.

### Hook does not execute on the learner's platform

Treat hook installation as facilitator plumbing. Repair permissions/shebang/path handling without making the learner debug shell mechanics. The learning objective is the lifecycle invariant.

### GitHub workflow runs are unavailable

Use another current remote-state fact. The invariant is:

> local source can describe intended/configured state; a connected remote surface can establish remote state that the local checkout alone cannot prove.

### Learner asks whether INDEX.md is a standard

Answer no. It is a project convention used here to teach a durable navigation idea. Other repositories may use READMEs, docs sites, manifests, generated indexes, search, databases or other navigation structures.

## What not to teach yet

Do not introduce specialist sub-agent profiles merely to make the agent definition more elaborate.

Do not teach trust boundaries in depth; Course 3 owns that wider system problem.

Do not teach retrieval/RAG mechanics in depth; later context-engineering material owns them.

Do not turn hooks into a survey of Git internals or hook managers.

Do not teach that generated indexes are authoritative because they are generated. They are reliable only for the source state and transformation they actually model.

Do not let the learner conclude that broad recursive search is always safer or better than indexes. Efficient guided navigation and exploration have different costs and failure modes.

Do not solve Lab 9's authority problem early.