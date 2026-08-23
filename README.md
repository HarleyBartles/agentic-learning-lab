# Agentic Learning Lab

A conversational, practical learning environment for understanding agentic AI by using it.

The curriculum is organized as three progressive courses. No coding knowledge is assumed and no coding is required. The aim is to build useful mental models through discussion, examples, experiments, mistakes, recovery, and eventually a real project of the learner's own.

The three-course structure is:

1. **Agentic Engineering 101: Zero to Hero** — Labs 1–10. Learn to direct and understand agents competently, ending with a real agentic project.
2. **Advanced Agentic Engineering: Mastering Agents** — its own course-local Lab 1 onward sequence. Learn to deliberately engineer agent behaviour, workflow, context, delegation, verification, evaluation, autonomy, trust boundaries, concurrency, isolation, integration, and the evidence produced by those systems.
3. **Beyond the Agent: Engineering Agent Systems** — its own course-local Lab 1 onward sequence. Course 3 begins after the Course 2 mastery arc and will be planned as a genuinely new system-level course rather than inheriting topics merely because they once had higher global module numbers.

**Lab numbers reset at each course boundary.** Course 2 does not begin at Lab 11, and Course 3 will not inherit Course 2's final number. The number of labs in Courses 2 and 3 remains an editorial decision while their planning modules are expanded into mature labs. Ten labs per course is a useful target where the material naturally supports it, not a quota that should force artificial splitting.

Each course should form a coherent stopping point. In particular, Course 1 should leave the learner with a sound, self-contained foundation for competent agentic engineering rather than a known stale misconception that only a later course repairs.

## Learning philosophy

The lab is built around a few ideas:

- Start from friction the learner has already experienced.
- Teach the problem before the mechanism that solves it.
- Prefer real demonstrations over abstract explanation.
- Keep early environments simple; add tools only when their value is visible.
- Break things deliberately in a safe environment.
- Make reversible experimentation feel normal.
- Treat source control as a recovery mechanism, not as programmer ceremony.
- Distinguish the model from the harness, context, tools, state, and feedback around it.
- Give agents both the tools they need and the operating knowledge to use those tools well.
- Treat local project access and connectors as complementary capabilities.
- Prefer evidence of completed work over confident agent claims.
- Teach the learner to direct, inspect, verify, question, and iteratively steer agent work rather than becoming the agent's manual implementation layer.
- Give the learner useful interim mental models, then deliberately break and refine them when later examples expose their limits.
- Do not knowingly carry a materially false mental model across a course boundary.
- Teach agents how work moves through a lifecycle, not only how to perform isolated tasks.
- Treat delegation to specialist agents as a design choice rather than an automatic sign of maturity.
- Treat harness interfaces as implementation contracts rather than universal agent standards; verify the effective worker instead of assuming the requested profile was honoured.
- Treat capability, context, and inference as resources whose use should be proportionate to the job.
- Treat provisioning as selective design rather than accumulation: the right knowledge, at the right scope, when the worker needs it.
- Define observable success for agent behaviour and re-test it when instructions, skills, tools, profiles, or context change.

## Learner workspace from day one

Before Lab 1, the facilitator should help the learner fork this repository into the learner's own GitHub account.

The learner does not need to understand forks, remotes, upstreams, or synchronization yet. The practical explanation can simply be:

> This is your copy of the laboratory. You can break this one.

The intended roles are:

```text
upstream curriculum repository
facilitator-maintained teaching source
        ↓ fork
learner-owned repository
persistent laboratory for the whole curriculum
        ↓
local checkout / connectors / agent workspaces
```

Early synchronization can remain facilitator plumbing. Later modules can deliberately reveal the difference between local working state, the learner's remote fork, and upstream curriculum state.

Lab-scoped `AGENTS.md` files survive the fork. In Labs 1–4 they are facilitator-owned experimental controls: they establish stable agent behaviour and safety boundaries without making instruction architecture the subject of those labs. Lab 5 explicitly reveals this lever: the learner reads the project instructions with the facilitator, hand-edits one bounded standing rule, and starts a fresh agent to observe the resulting behaviour. Lab 8 deepens that mechanism by inspecting scoped effective instructions and contrasting harness-supplied context with project-authored navigation. Later, when the learner creates a real project, they own that instruction surface and can deliberately delegate its maintenance to an agent.

## Labs

A lab is the complete learning experience for one topic. Where useful, a lab contains separate surfaces for the learner, facilitator, and working mission/project environment.

Lab 1 is the stable reference structure:

```text
labs/01-chatbot-to-worker/
    README.md
    facilitator/
        README.md
    learner/
        01-complete-context.md
        02-missing-context.md
        03-on-disk-worker.md
        04-cloud-project.md
    mission/
        README.md
        source/
        output/
```

The responsibilities are intentionally local to the lab:

```text
lab
    the complete learning experience

facilitator/
    why and how to run it

learner/
    what the learner should do next

mission/ or project/
    the bounded environment the AI actually works in, when the lab needs one
```

Not every lab needs a mission. Labs should use whatever small set of exercises best demonstrates the lesson.

If a file only makes sense because a particular lab exists, it should usually live inside that lab. Cross-cutting doctrine belongs in `docs/`.

For Lab 1, learner cards should be revealed one at a time. The local Codex worker is scoped to the `mission/` folder rather than the whole lab so it does not see the teaching choreography.

## Curriculum

The numbering below is course-local. Each course starts again at Lab 1. The three course boundaries are deliberate; individual later module details may still evolve while drafts become mature labs.

### Course 1 — Agentic Engineering 101: Zero to Hero

1. [From chatbot to worker](labs/01-chatbot-to-worker/)
2. [Give the cloud agent the project](labs/02-give-the-cloud-agent-the-project/)
3. [The project has a home](labs/03-project-has-a-home/)
4. [Repositories, save points, and safe breakage](labs/04-repositories-save-points-and-safe-breakage/)
5. [Model, harness, context, tools, and behaviour](labs/05-model-harness-context-tools-and-behaviour/)
6. [What does the model know?](labs/06-what-does-the-model-know/)
7. [Tools, operating knowledge, and domain provisioning](labs/07-tools-operating-knowledge-and-domain-provisioning/)
8. [What did we just create? Local work and connected systems](labs/08-local-work-and-connected-systems/)
9. [Source of truth and verification](labs/09-source-of-truth-and-verification/)
10. [Build a real agentic project](labs/10-build-a-real-agentic-project/)

Labs 1–10 are mature and ready to run. Together they form **Course 1 — Agentic Engineering 101: Zero to Hero**. Lab 10 is the synthesis project and a coherent course boundary.

### Course 2 — Advanced Agentic Engineering: Mastering Agents

Current planning sequence, using **Course 2-local linear numbering**:

1. Agent self-introspection and local review
2. Autonomous human-in-the-loop workflows
3. Specialist sub-agents and orchestration
4. Harnesses, portability, and agent observability
5. The 20-Agent Bonfire and context transport
6. Selective provisioning, context, and evaluation
7. Trust boundaries and connected autonomy
8. Concurrent agents and isolation
9. Epilogue: show how this was built

The former `14A` is now simply Course 2 Module 5. The new taxonomy has no lettered exception.

These are planning modules, not a commitment that Course 2 will contain exactly nine mature labs. As each area is expanded, it may remain one lab or split where the learning pressure genuinely warrants it. The existing nine-module spine gives us natural room to land at ten mature labs without manufacturing filler.

See [`modules/course-2/README.md`](modules/course-2/README.md) for the authoritative Course 2 planning index and the mapping from older draft filenames.

### Course 3 — Beyond the Agent: Engineering Agent Systems

Course 3 will restart at **Lab 1** after the Course 2 mastery arc. Its detailed planning sequence is intentionally not pinned down by the old global 16–18 numbering; those topics now belong to Course 2.

Lab 2 is the direct continuation of Lab 1. Lab 1 showed that an agent which cannot see the project surface cannot know what project state is missing. Lab 2 changes that access condition by giving cloud ChatGPT a bridge to the learner's repository, then compares connector-mediated access with direct local workspace access.

Lab 3 stops treating cloud versus local as the organizing question and focuses on durable project state, deliberate promotion of conversational material into durable state, and conflicting durable artifacts.

Lab 4 makes the source-control machinery visible after the learner has already benefited from it: working state, recorded history, diffs and restore, commit versus push, historical recovery, and the repository boundary around external side effects.

The middle of Course 1 deliberately compounds earlier ideas rather than replacing them. Lab 5 decomposes observed agent behaviour into model, harness, instructions, context, tools, environment, state, and feedback. Lab 6 then deliberately withholds supplied/retrieved knowledge to expose what the model still brings from training, where its retained grounds become uncertain, and how retrieval changes the evidential basis without becoming an oracle. Lab 7 turns from observing model knowledge to engineering domain provision through three real authority configurations: facilitator-grounded software engineering, shared non-authoritative provision from external expertise, and a learner-grounded expert domain. Lab 8 then asks how that worker perceives and navigates its environment and connected systems. Lab 9 makes authority, verification, evidence, and human acceptance explicit. Lab 10 turns the accumulated Course 1 understanding into a learner-owned real project and closes the first course with a full intent → proposal → build → inspection → verification loop.

Course 2 progressively turns competent agent collaboration into deliberate engineering of agent behaviour and agent operation. Course 2 Module 1 makes agent self-introspection, behavioural prediction, local self-review, and test-first probes explicit as cheap local primitives. Module 2 composes those primitives into autonomous human-in-the-loop workflows, loops, gates, stopping conditions, and legal routes. Module 3 puts pressure on the `one worker does every stage` model and introduces specialist profiles, delegation, and orchestrator trade-offs. Module 4 pressure-tests the portability of that specialist abstraction by comparing harness-specific worker contracts, effective runtime configuration, current model/reasoning control surfaces, economics, and observability. Module 5 stress-tests context transport and orchestration through **The 20-Agent Bonfire**. Module 6 breaks the accumulation model of provisioning and introduces selective scope, finite context, context transport/materialisation, retrieval/RAG as context selection, lightweight evaluation, and TDD-inspired agent design. Module 7 extends the engineered worker into connected systems where authority, permissions, provenance, and consequential actions matter. Module 8 makes concurrent mutable work force the need for isolation, reconciliation, integration, and integrated-state verification. Module 9 then turns the curriculum repository itself into the mastery capstone: the learner investigates how the whole thing was built, what its history proves, and what they would change.

Course 3 begins from that stronger endpoint and will widen the design boundary again. Its exact lab spine should be planned deliberately rather than inferred from legacy numbering.

Existing files in `modules/` are working facilitator drafts for later curriculum material that has not yet been promoted into a mature lab. Legacy numeric prefixes on older planning files are source-history identifiers only; the course-local planning indexes are authoritative for curriculum numbering.

See also [Curriculum shape](docs/curriculum-shape.md), [Core principles](docs/core-principles.md), [Learning methodology and origin](docs/learning-methodology.md), and [Curriculum threads, breadcrumbs, and future cash-ins](docs/curriculum-threads.md).

## Repository areas

- `labs/` contains complete learning experiences, including learner guidance, facilitator notes, and bounded working environments where appropriate.
- `docs/` contains cross-cutting principles and curriculum-wide guidance.
- `modules/` contains draft planning material for later labs that have not yet been fully promoted. Course-specific planning indexes define the local numbering while older source filenames may retain historical prefixes until those drafts are next rewritten or promoted.

There is deliberately no separate root-level `guided/`, `projects/`, or stable facilitator hierarchy. Learner and facilitator material, fixtures, and project environments that belong to a lab live with that lab.

## Expected progression

The broad conceptual progression currently includes:

**chat without project access -> on-disk workspace -> connected cloud access -> persistent project state -> recoverable history -> model/harness/context/tools -> closed-book model knowledge and retrieval-backed evidence -> domain provisioning under changing human authority -> agent environment/navigation/access/discovery -> authority and verification -> learner-owned real project -> self-introspection and local review -> autonomous human-in-the-loop workflow -> specialist delegation -> harness portability/effective-worker verification/observability -> context-transport stress -> selective context transport/provisioning/retrieval and evaluation -> trust boundaries -> concurrent isolation/branch-PR integration -> retrospective on how the whole framework was built**

The exact detail inside later modules can move while labs are expanded and tested. Preserve the three course boundaries and the causal links between concepts.

## Important safety model

This repository is a laboratory. The learner's fork should contain nothing precious.

The learner is expected to make bad changes, delete things, ask agents to do overly broad work, inspect the result, and recover it. The goal is to replace fear of breakage with the engineering question:

> What is the blast radius, and do I have a recovery path?

Be fearless with reversible project state. Be deliberate with irreversible or external side effects.
