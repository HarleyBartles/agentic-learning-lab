# Lab 8 — What did we just create? Local work and connected systems

Status: **Mature and ready to run.**

Approximate duration: 75–90 minutes.

No coding knowledge is assumed. No coding is required.

Lab 7 ended by asking:

> **What exactly did we just create?**

Lab 8 answers that question, then makes the worker's relationship with its environment visible.

By the end of the lab, the learner should hold this practical Course 1 model:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

Later courses may deepen that model, but Course 1 should not leave the learner carrying a knowingly false idea such as `the agent is everything in its environment` or `if the agent can access something then it already knows about it`.

## Core lessons

The lab earns:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

> **When absence matters, understand how the agent looked before trusting the conclusion.**

It then asks a second-order engineering question:

> **If agents are going to rely on a navigation mesh, how do we keep it trustworthy?**

That earns:

> **Do not hand-maintain derived navigation when the project can regenerate it deterministically.**

> **Inspect by default. Mutate explicitly.**

> **If freshness matters at a lifecycle boundary, encode the check there instead of relying on memory.**

## Three different project surfaces

```text
AGENTS.md
harness-recognised scoped operating instructions

INDEX.md
project-authored navigation convention

filesystem / search / connector tools
ways to observe accessible state
```

For the Codex worked example, applicable `AGENTS.md` instructions are supplied by the harness according to scope. `INDEX.md` has no such magic: it is a project convention the worker follows because the project or user tells it to.

## Shape

```text
labs/08-local-work-and-connected-systems/
    README.md
    facilitator/
        README.md
        assets/
            mesh-tooling/
                README.md
                generate_index_mesh.py
                test_generate_index_mesh.py
                pre-commit-check
                pre-commit-apply
    learner/
        01-name-the-worker.md
        02-follow-the-mesh.md
        03-prove-the-blind-spot.md
        04-keep-the-mesh-trustworthy.md
        05-cross-the-boundary.md
    working/
        AGENTS.md
        README.md
        environment/
            AGENTS.md
            INDEX.md
            curriculum/
                INDEX.md
                overview.md
            references/
                INDEX.md
                operations.md
            forgotten/
                answer.md
```

Reveal learner cards one at a time.

The facilitator assets deliberately stay outside the worker root until Exercise 4. The initial hand-authored mesh must remain incomplete long enough for the learner to experience the blind spot before seeing how generated navigation can prevent that class of drift.

## Exercise 1 — Name the worker and inspect effective instructions

Start from Lab 7's unanswered question and reconstruct:

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

Start a fresh Codex session in `working/environment/` and ask which project instruction sources are in force.

Open the applicable `AGENTS.md` files with the learner.

For Codex, make the product-specific fact explicit but bounded: applicable project instruction files are recognised by the harness and supplied according to scope. Do not teach that every agent harness works this way.

Earn:

> **A harness can automatically materialise scoped project instructions into worker context.**

## Exercise 2 — Follow a project-authored navigation mesh

Open `working/environment/INDEX.md`.

Contrast:

```text
AGENTS.md
what operating guidance applies here?

INDEX.md
where should I look next?
```

Ask the worker to use only reachable `INDEX.md` links to map the environment. The mesh should work well across the surface it actually describes.

## Exercise 3 — Prove the blind spot

Ask the mesh-only worker for the field-exercise escalation keyword.

The answer lives in `forgotten/answer.md`, but `forgotten/` is absent from the mesh.

The worker should be unable to establish the answer through the permitted route.

Then ask it directly to list `forgotten/` and read the relevant file.

The learner can now establish:

```text
the folder existed
+
the worker had filesystem access
+
the worker could read it when directly addressed
+
the mesh did not lead there
=
accessible but undiscovered through the chosen route
```

Use the ladder:

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

## Exercise 4 — Keep the mesh trustworthy

Now ask:

> **If this navigation structure can drift, why should an agent trust it tomorrow?**

Reveal the facilitator-supplied generator.

The generator has two explicit modes:

```text
--check
non-mutating inspection
report whether generated indexes match tracked/staged project state

--apply
explicit mutation
regenerate the owned INDEX.md files
```

Run `--check` first and observe stale state without mutation. Then run `--apply`, inspect the regenerated mesh, and run `--check` again.

The supplied tests establish the intended tool contract:

- stale state is detected;
- regeneration discovers tracked structure omitted by the hand-authored mesh;
- repeated `--apply` is byte-idempotent;
- untracked local drafts do not leak into the generated commit mesh.

Name the properties:

```text
deterministic
same tracked/staged state -> same output

idempotent
repeat --apply -> no accumulating change
```

Then ask who remembers to run the check before every commit.

Introduce `pre-commit` only as a lifecycle mechanism and compare two policies:

```text
check-and-block
pre-commit -> --check -> stale? block -> explicit --apply -> inspect/stage -> retry

apply-and-stage
pre-commit -> --apply -> stage only generator-owned INDEX.md paths -> continue
```

Neither is universally correct. The important engineering move is to choose the policy deliberately.

A local hook only governs commits made through that configured checkout. Shared provisioning or CI can repeat the same non-mutating check when a project needs a wider guarantee.

## Exercise 5 — Cross the local boundary

Once the learner understands observation inside the project, widen the environment.

Use the repository's GitHub state as the preferred worked example.

The local checkout can show what the repository-integrity workflow is configured to do. A GitHub-connected worker can establish what GitHub actually records as having happened remotely.

Earn:

> **Local source can describe intended remote behaviour without proving the remote event happened.**

Keep this distinction:

> **Retrieval and exploration are strategies. Local and connected are access surfaces.**

## Handoff to Lab 9

Finish with several reachable statements that can disagree or answer different questions:

- local working state;
- GitHub remote state;
- a durable project statement of what should be true.

Ask:

> **The worker can reach all of these. Which one should it trust?**

Then:

> **What would actually prove that the required work is correct?**

Stop there.

Lab 8 owns observation, navigation, discovery, and maintenance of one navigational representation. Lab 9 owns authority and verification.

## What this lab is not

Do not teach `INDEX.md` as a universal standard.

Do not teach generated indexes as authoritative about more than the source state and transformation they model.

Do not teach `local = agent`, `cloud = not agent`, `connector = retrieval`, or `filesystem = exploration`.

Do not require the learner to write or debug the supplied scripts.

Do not turn hooks into a Git-internals or CI lecture.

Do not solve the Lab 9 source-of-truth problem early.