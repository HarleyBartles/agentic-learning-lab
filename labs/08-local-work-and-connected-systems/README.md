# Lab 8 — What did we just create? Local work and connected systems

Status: **Mature and ready to run.**

Approximate duration: 60–75 minutes.

No coding knowledge is assumed. No coding is required.

Lab 7 ended by asking:

> **What exactly did we just create?**

Lab 8 answers that question, but it does not stop at naming the thing. It makes the worker's relationship with its environment visible.

By the end of the lab, the learner should hold this practical Course 1 model:

> **An agent is a model operating through a harness, with effective instructions, capabilities and permissions, observing and acting on an environment through particular context, access and discovery mechanisms.**

This is deliberately practical rather than a final ontology. It is complete enough for the Course 1 boundary: later courses may deepen it, but they should not need to repair a knowingly false idea such as `the agent is everything in its environment` or `if the agent can access something then it already knows about it`.

## Core lessons

Lab 8 should earn these distinctions through direct observation:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

> **When absence matters, understand how the agent looked before trusting the conclusion.**

The lab also makes three project surfaces visibly different:

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
    learner/
        01-name-the-worker.md
        02-follow-the-mesh.md
        03-prove-the-blind-spot.md
        04-cross-the-boundary.md
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

The `forgotten/` folder is deliberately omitted from the index mesh. Do not reveal that omission before the blind-spot exercise.

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

Earn the distinction:

> **The environment can contain more than the worker has in context. Harness conventions decide that some project material is supplied automatically.**

Do not teach that every agent harness uses `AGENTS.md` or identical scope rules.

## Exercise 2 — Follow the navigational mesh

Open `working/environment/INDEX.md` with the learner.

Explain that this repository has chosen a different kind of mechanism for navigation: a project-authored mesh of index files.

Ask the worker:

> **Using only the INDEX.md navigation mesh, tell me what this environment contains and where the documented operating material lives. Do not perform a broad filesystem search.**

The worker should follow the root index into the indexed child areas and build a reasonable map.

The learner should notice that this is useful precisely because the worker does not need to recursively ingest or inspect everything merely to orient itself.

Use the distinction:

```text
AGENTS.md
what operating guidance applies here?

INDEX.md
where should I look next?
```

The first is harness-recognised in this worked environment. The second is a project navigation convention.

## Exercise 3 — Prove the blind spot

Now ask the worker a bounded question whose answer lives in the deliberately unindexed folder:

> **Using only the INDEX.md navigation mesh, what is the escalation keyword for the field exercise? Do not perform a broad filesystem search.**

A worker following the experiment correctly should reach the edge of the declared mesh and report that it cannot establish the answer.

Do not frame this as stupidity or disobedience. Under the observation method it was given, the worker has insufficient evidence.

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

## Exercise 4 — Cross the local boundary

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

If workflow-run access is unavailable in the learner environment, use another harmless remote-state fact such as the current remote branch head, whether a PR exists, or whether a known commit is present remotely. Preserve the distinction rather than forcing one specific GitHub feature.

Do not teach `local = exploration` and `connector = retrieval`. Either surface can support focused retrieval or broader exploration. The durable question is:

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

Lab 8 has taught observation and discovery. Lab 9 owns authority and verification.

## What this lab is not

Do not turn `AGENTS.md` into an OpenAI-product trivia lecture.

Do not teach `INDEX.md` as a universal standard or harness feature.

Do not imply that index meshes should replace broad search, or that broad recursive search should replace deliberate navigation.

Do not confuse an accessible object with an object already in model context.

Do not teach `local = agent` or `cloud = not agent`.

Do not teach connectors as inherently read-only, inherently retrieval-only, or inherently superior to direct project access.

Do not move into specialist sub-agent profiles or orchestration yet.

Do not resolve the final source-of-truth question. The next lab needs that pressure.