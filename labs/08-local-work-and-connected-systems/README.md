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

The lab should earn these distinctions through direct observation:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

> **When absence matters, understand how the agent looked before trusting the conclusion.**

It then adds one maintenance principle:

> **Do not hand-maintain derived navigation when the project can regenerate it deterministically.**

And one lifecycle principle:

> **If freshness matters at commit time, encode that expectation into the commit path instead of relying on memory.**

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

The learner should not collapse these into one generic idea of `files the agent can see`.

## Shape

```text
labs/08-local-work-and-connected-systems/
    README.md
    facilitator/
        README.md
        tooling/
            README.md
            generate_index_mesh.py
            pre-commit-index-mesh
            test_generate_index_mesh.py
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

Use a fresh local Codex session rooted at `working/environment/` for the scoped-instruction and navigation exercises. That location deliberately has both a parent `working/AGENTS.md` and a more-local `environment/AGENTS.md` so the learner can inspect which instruction sources are in force.

The `forgotten/` folder is deliberately omitted from the initial hand-authored index mesh. Do not reveal that omission before the blind-spot exercise. Likewise, do not copy the facilitator's index generator or hook tooling into the working environment until the learner has experienced the drift problem.

## Exercise 1 — Name the worker and inspect its effective instructions

Start from Lab 7's unanswered question.

Ask the learner to reconstruct what was assembled:

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

Then start a fresh Codex worker in `working/environment/` and ask:

> **What project instruction sources are currently in force for you, and where did they come from?**

Open the corresponding `AGENTS.md` files with the learner.

The point is not to memorize a filename. The learner should see a concrete example of a harness recognising project-scoped instructions and materialising the applicable ones into worker context.

Earn:

> **The environment can contain more than the worker has in context. Harness conventions decide that some project material is supplied automatically.**

Do not teach that every agent harness uses `AGENTS.md` or identical scope rules.

## Exercise 2 — Follow the navigational mesh

Open `working/environment/INDEX.md` with the learner.

Explain that this repository has chosen a different mechanism for navigation: a project-authored mesh of index files.

Ask the worker:

> **Using only the INDEX.md navigation mesh, tell me what this environment contains and where the documented operating material lives. Do not perform a broad filesystem search.**

The worker should follow the root index into the indexed child areas and build a reasonable map.

The learner should first experience why this is useful: a worker can orient itself without recursively ingesting or scanning everything.

Use the distinction:

```text
AGENTS.md
what operating guidance applies here?

INDEX.md
where should I look next?
```

The first is harness-recognised in this worked environment. The second is a project navigation convention.

## Exercise 3 — Prove the blind spot

Now ask a question whose answer lives in the deliberately unindexed folder:

> **Using only the INDEX.md navigation mesh, what is the escalation keyword for the field exercise? Do not perform a broad filesystem search.**

A compliant worker should reach the edge of the declared mesh and report that it cannot establish the answer.

Do not frame this as stupidity or failure to obey. Under the observation method it was given, the worker has insufficient evidence.

Then change only the observation route:

> **List the contents of `forgotten/`, then read the relevant file and answer the same question.**

The learner can now establish:

```text
the folder existed
+
the worker had filesystem access to it
+
the worker could list and read it when directly addressed
+
the index mesh did not lead there
=
accessible but undiscovered through the chosen route
```

Ask:

- Did the worker lack filesystem access?
- Did it lack the capability to read the file?
- Was the file absent?
- Did the index mesh contain a path to it?
- What exactly did the first `I cannot find it` claim prove?

The conceptual ladder is:

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

This is not an argument against index meshes. It is a lesson in interpreting evidence produced through a particular observation method.

## Exercise 4 — Keep the mesh trustworthy

Now ask the engineering question the blind spot creates:

> **If we are going to use this mesh to navigate the project, how do we keep it trustworthy?**

Reject `remember to update the indexes` as the final design.

At this point the facilitator supplies the prepared tooling.

Copy `generate_index_mesh.py` into `working/environment/tools/`, stage it if it is to enter the learner's next commit, and run it against the environment.

The generator derives navigation from Git's staged/tracked view rather than from arbitrary unstaged files in the raw working tree. That makes the generated mesh describe the project state that is actually heading toward a commit.

Inspect the result:

- `forgotten/` should now appear in the root mesh;
- a local `forgotten/INDEX.md` should be generated;
- running the generator again without changing staged/tracked structure should produce the same index content.

Earn:

```text
deterministic
same staged/tracked project state -> same generated mesh

idempotent
running it again does not keep changing the result
```

Then ask:

> **Who remembers to run it before every commit?**

Introduce Git hooks lightly. A hook is an action Git runs at a lifecycle point. This lab needs only one example: `pre-commit`.

Install the facilitator-provided hook in the learner fork. Its job is intentionally narrow:

```text
before commit
→ regenerate the index mesh from Git's staged/tracked state
→ stage only the generated INDEX.md files
→ continue the commit
```

Make and stage one harmless structural change inside the exercise environment, commit it, and inspect that the relevant index freshness update travelled in the same commit.

The lesson is not `always use pre-commit`. The lesson is:

> **When important derived project state must stay synchronized, make the maintenance mechanism reproducible and attach it to the lifecycle point where freshness matters.**

Do not overclaim what this proves. The generated mesh is now a trustworthy representation of the tracked structure it is designed to describe. It is not therefore an authority on every truth that may exist inside or outside the project.

## Exercise 5 — Cross the local boundary

Once the learner understands navigation inside an accessible project, widen the environment.

Use the repository's GitHub state as the worked example.

Ask the local worker to inspect the repository-integrity workflow and explain what the checked-in files establish about what **should** happen when the workflow runs.

Then use a GitHub-connected worker to establish a piece of live remote state, preferably:

> **Did the latest repository-integrity workflow run for the relevant remote commit actually complete successfully?**

The learner should separate:

```text
local source
what is configured or intended to run

connected remote state
what GitHub records as actually having happened remotely
```

If workflow-run access is unavailable, use another harmless remote-state fact such as the current remote branch head, whether a PR exists, or whether a known commit is present remotely.

Do not teach `local = exploration` and `connector = retrieval`. Either access surface can support focused retrieval or broader exploration.

The durable question is:

> **What surface am I observing, through what route, and what does that observation actually establish?**

## Handoff to Lab 9

Finish by putting several reachable statements in front of the learner:

- the local working copy can say one thing;
- the GitHub remote can record another state;
- a project note can express an intended requirement;
- a worker can confidently summarize all three.

Then ask:

> **The worker can reach all of these. Which one should it trust?**

And:

> **What would actually prove that the required work is correct?**

Do not answer those questions fully here.

Lab 8 has taught observation, discovery, and maintenance of one navigational representation. Lab 9 owns authority and verification.

## What this lab is not

Do not turn `AGENTS.md` into an OpenAI-product trivia lecture.

Do not teach `INDEX.md` as a universal standard or harness feature.

Do not teach generated indexes as inherently complete descriptions of reality. They are reproducible representations of the state they are designed to index.

Do not turn Git hooks into a deep Git-internals lesson. The learner needs the lifecycle concept, not hook plumbing mastery.

Do not imply that index meshes should replace broad search, or that broad recursive search should replace deliberate navigation.

Do not confuse an accessible object with an object already in model context.

Do not teach `local = agent` or `cloud = not agent`.

Do not teach connectors as inherently read-only, retrieval-only, or superior to direct project access.

Do not move into specialist sub-agent profiles or orchestration yet.

Do not resolve the final source-of-truth question. The next lab needs that pressure.