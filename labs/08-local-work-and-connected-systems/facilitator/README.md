# Lab 8 facilitator guide

Status: **Mature and ready to run.**

Approximate duration: 60–75 minutes.

## Learning goal

The learner should leave understanding that an agent does not perceive its whole environment automatically. A worker reasons over what its harness, instructions, tools and chosen observation routes actually bring into view.

Earn:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

Then deepen the navigation lesson:

> **Do not hand-maintain derived navigation when the project can regenerate it deterministically.**

> **If a representation is important enough for agents to rely on, make it reproducible.**

The Course-1-safe agent model is:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

## Contract

No coding knowledge is assumed. No coding is required.

The learner does not need to understand Python, shell syntax, Git internals, workflow YAML, or hook implementation. The facilitator supplies and operates mechanics when needed. The learner participates in the judgment loop.

## Setup

Before the learner arrives:

1. Start from the shipped Lab 8 fixture before any generator has been copied into `working/environment/`.
2. Confirm a local Codex session can be rooted at `working/environment/`.
3. Confirm the worker can report, or at least demonstrably obey, the applicable `AGENTS.md` instruction sources.
4. Confirm the hand-authored root `INDEX.md` reaches `curriculum/` and `references/` but not `forgotten/`.
5. Keep `facilitator/assets/mesh-tooling/` outside the worker root until Exercise 4.
6. Run `python labs/08-local-work-and-connected-systems/facilitator/assets/mesh-tooling/test_generate_index_mesh.py` and confirm it passes.
7. Confirm at least one harmless GitHub remote-state query is available. Workflow-run status is preferred; branch/commit/PR presence is a valid fallback.
8. Keep facilitator and learner choreography outside the worker root.

Reveal learner cards one at a time.

## Exercise 1 — Name the worker and inspect instruction scope

Start from Lab 7:

> **What exactly did we just create?**

Let the learner answer naturally, then reconstruct:

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

Start Codex in `working/environment/` and ask:

> What project instruction sources are currently in force for you, and where did they come from?

Open `working/AGENTS.md` and `working/environment/AGENTS.md` with the learner.

For this Codex worked example, explain only the bounded product fact: applicable project instruction files are harness-recognised and supplied according to scope. Do not generalise `AGENTS.md` into a universal agent standard.

Earn:

> **A harness can automatically materialise scoped project instructions into a worker's context.**

## Exercise 2 — Follow the mesh

Open `working/environment/INDEX.md`.

Contrast:

```text
AGENTS.md
what operating guidance applies here?

INDEX.md
where should I look next?
```

The former is harness-recognised in this worked example. The latter is a project-authored navigation convention.

Ask:

> Using only the INDEX.md navigation mesh, tell me what this environment contains and where the documented operating material lives. Do not perform a broad filesystem search.

Let the worker successfully navigate the declared mesh first. The learner should see why guided navigation is useful before seeing its failure mode.

## Exercise 3 — Let the route fail honestly

Ask:

> Using only the INDEX.md navigation mesh, what is the escalation keyword for the field exercise? Do not perform a broad filesystem search.

The answer is in `forgotten/answer.md`, but that directory is absent from the mesh.

A compliant worker should say it cannot establish the answer from the permitted route. If it broad-searches anyway, repeat with the constraint explicit.

Then ask:

> List the contents of `forgotten/`, read the relevant file, and answer the same question.

Classify what changed:

- access did not change;
- file contents did not change;
- model capability did not change;
- observation route changed.

Earn:

```text
thing exists
!=
thing is represented in Git
!=
thing is represented in the navigation mesh
!=
thing is in current model context
!=
worker will discover it
```

and:

> **When absence matters, understand how the agent looked before trusting the conclusion.**

## Exercise 4 — Make the mesh reproducible

Ask:

> **If agents are going to rely on this mesh, how do we keep the mesh itself trustworthy?**

Let `remember to update it` surface naturally, then pressure it. A manually maintained derived representation will drift eventually.

Reveal `facilitator/assets/mesh-tooling/`.

Copy `generate_index_mesh.py` to `working/environment/tools/generate_index_mesh.py` and let the worker inspect its own usage/help surface rather than teaching the learner the implementation.

Ask the worker to regenerate the **entire** mesh from the Git project state the mesh is intended to represent.

Inspect the result:

- `forgotten/` becomes represented;
- a generated `forgotten/INDEX.md` exists;
- the same represented state produces the same mesh;
- regenerating again does not accumulate further changes;
- unrelated untracked drafts do not become part of generated project navigation.

Name the useful properties:

```text
deterministic
same represented project state -> same generated mesh

idempotent
regenerate again -> no accumulating change
```

The generator deliberately has a good CLI surface, including `--help`, non-mutating inspection and explicit mutation. Do not make those interface semantics the lesson here. Preserve them as a breadcrumb for later Course 2 work on agent-friendly tools.

Earn:

> **If a navigation surface is derived from project state, regenerate it from that state rather than hand-editing it.**

Then deliberately leave one problem unsolved.

Ask:

> **We now have a reliable generator. Does the existence of that tool guarantee the worker will run it whenever the mesh needs refreshing?**

The answer is no.

Do not install a hook, write standing workflow instructions, add CI enforcement, or otherwise solve the lifecycle problem in Lab 8.

The learner should later be allowed to encounter the natural failure:

```text
generator exists
+
worker can use it
+
project changes
+
no one remembers to ask for regeneration
=
mesh can still go stale
```

That later cashes a central curriculum rule:

> **Things you keep telling the agent need to become things you stop telling the agent.**

## Exercise 5 — Widen beyond the filesystem

Ask:

> What if the state we need is not on this disk at all?

Use the repository-integrity workflow as the preferred example.

With the local worker, inspect checked-in workflow/checker/test files and ask what they establish. The answer should be about configured/intended behaviour.

Then use the GitHub-connected worker to establish current remote state, preferably whether the relevant workflow run actually completed successfully.

Earn:

> **Local source can describe intended remote behaviour without proving that the remote event happened.**

Do not map retrieval/exploration onto local/connected:

> **Retrieval and exploration are strategies. Local and connected are access surfaces.**

## Finish on the Lab 9 problem

Bring together several reachable statements:

- local state;
- GitHub remote state;
- a durable project statement of what should be true.

Ask:

> **The worker can see all three. Which one should it trust?**

Then:

> **What would actually prove that the required work is correct?**

Stop. Lab 9 owns authority and verification.

## Failure handling

If the worker discovers `forgotten/` despite the mesh-only constraint, determine whether it used a broad filesystem route. Reset the prompt/turn rather than pretending the experiment worked.

If Codex cannot clearly name its instruction sources, open the files manually and demonstrate effective scope. Do not turn the lab into product debugging.

If the generator includes an unrelated untracked draft, treat that as a tooling defect and stop. The supplied tests exist specifically to prevent that false lesson.

If workflow-run state is unavailable, use another remote-only fact such as branch head, PR presence, or commit presence.

## Do not teach yet

Do not teach `INDEX.md` as a standard.

Do not teach generated indexes as universally authoritative. They are trustworthy only for the source state and transformation they model.

Do not teach broad recursive search as universally better than guided navigation.

Do not teach hooks, hook managers, CI gates, or lifecycle enforcement. The missing lifecycle behaviour is deliberate future curriculum pressure.

Do not turn the generator into a CLI design lesson. Preserve the good interface and cash its value later.

Do not introduce specialist sub-agent profiles or orchestration.

Do not solve Lab 9's authority question early.