# Core principles

These are the ideas to reinforce throughout the lab. They are more important than any particular product, command, model, or framework.

## The learner directs work rather than manually reproducing it

This curriculum is not a coding course and does not require the learner to become the manual implementation layer for an agent.

The core learning loop is:

> **Learner instruct -> Agent do -> Learner inspect, verify and question -> Agent explain -> Learner instruct again.**

The learner should become increasingly good at deciding what outcome they want, placing the agent in an appropriate environment, inspecting what actually happened, questioning unfamiliar machinery, and using the explanation to steer the next iteration.

The central methodology is:

> **The learner knows how to use agents to accomplish things before they fully understand the implementation, while using the work itself to progressively build that understanding.**

Do not hide code, Git operations, configuration, scripts, SQL, or other technical artifacts merely because the learner cannot yet produce them manually. Let the agent do useful work, then use the work itself as material for inspection and learning.

This method should generalise beyond the curriculum. If the learner later wants to learn programming or another unfamiliar technical craft, the same loop applies.

See [Learning methodology and origin](learning-methodology.md) for the fuller curriculum-wide statement and the repository's own origin story.

## When the learner knows the domain, provision that expertise

The earlier learning loop often starts from learner uncertainty: the agent does work, the learner inspects it, and the agent explains unfamiliar implementation.

Once the learner is proficient in a domain, the normal direction changes.

The learner should make enough of their domain expertise available to the agent before expecting specialist work.

> **Expertise should be provisioned, not repeatedly performed.**

The learner's expertise is not only for correcting bad work after the fact. It belongs in the agent's operating environment through appropriate combinations of:

- project instructions;
- source and reference material;
- examples of good and bad work;
- standards and conventions;
- tools;
- reusable skills/workflows;
- quality criteria and verification checks.

A repeated correction should trigger a question:

> Is this a one-off mistake, or did we just reveal something the agent's environment should know from now on?

If nobody in the loop knows what good looks like, plausible output can masquerade as good work.

Domain knowledge can also be distributed. One expert is not always required; useful working knowledge may be assembled from partial human expertise, source material, standards, examples, tools, and feedback.

Module 6 should teach this through a deliberate three-domain progression: coding with facilitator domain authority, novel writing with shared/partial authority, and technical drawing with learner domain authority.

## The conversation is not the project

A chat is a useful interface for thinking and asking questions. A project needs durable state that can be inspected, changed, versioned, and revisited independently of one conversation.

## Context is not the same as state

Memory and retrieved context can help continuity, but authoritative project state should live somewhere explicit and inspectable.

A useful shorthand:

> Memory is context. Files are state.

## Do not make the human act as the filesystem

If the real project already exists on disk, repeatedly uploading files, downloading outputs, copying changes back, and explaining which version is current creates unnecessary human synchronisation work.

Where appropriate, let the agent work where the project actually lives.

## Separate model capability from configuration

Observed behaviour comes from more than the model:

**model + harness + instructions/settings + context + tools + environment + feedback**

A preference for shorter responses, different formatting, or a particular workflow may be a harness or configuration preference rather than evidence that one underlying model is categorically better.

When something works badly, ask:

> Is this a model problem, a context problem, a harness problem, a tool problem, or a feedback problem?

## Give the agent the right tools

A capable model with the wrong tool is still badly equipped.

Image generation is not a technical drawing system. A technical drawing may need deterministic vector, CAD, geometry, rendering, or measurement tools.

Project environments should expose capabilities appropriate to the work being done.

## Tools and operating knowledge belong together

Provisioning a rich tool does not teach competent use of that tool.

A useful distinction:

- **Tool or MCP:** What can I do?
- **Skill:** How should I do this kind of work?
- **Project instructions:** What rules apply in this project?
- **Task:** What are we trying to accomplish now?

Rich tool surfaces create a larger decision space. They become more useful when paired with procedural guidance that teaches the agent when to use a capability, how to combine operations, what counts as success, and when a different route is better.

> Tools expose verbs. Skills teach workflows.

## Local access and connectors are complementary

A connector is excellent when the agent needs to reach an external system such as GitHub, email, a calendar, an issue tracker, or a database.

Direct project access is better suited to deep exploration of a local project: walking directories, reading many files, grepping, inspecting history, running scripts, rendering output, and discovering things nobody knew to retrieve explicitly.

> Retrieval asks for something. Exploration discovers what is there.

Neither replaces the other.

Do not teach `on-disk good, cloud bad`. Different surfaces expose different state, capabilities, permissions, and safety boundaries. Select the environment that fits the task.

The learning-lab repository itself is a useful proof point: substantial curriculum development was carried out through cloud ChatGPT using a GitHub connector after only minimal manual setup.

## Prefer evidence over agent claims

An agent saying it changed something is not proof that it changed it correctly.

Verification may mean inspecting a diff, reading the file, rendering a document, running a check, searching for an old value, testing dimensions, or checking remote publication state.

> Do not trust that work happened when you can inspect whether it happened.

## Safe breakage is part of learning

The goal is not to avoid mistakes. The goal is to make mistakes cheap and recoverable.

Replace:

> I should not try this because I might break something.

with:

> What is the blast radius, and do I have a recovery path?

Source control, disposable examples, narrow permissions, and clear project boundaries make experimentation safer.

Be fearless with reversible state. Be deliberate with external side effects such as sending messages, deleting remote records, publishing, spending money, or changing real permissions.

## Teach invariants; let techniques emerge

Teach ideas such as source of truth, recovery, verification, isolation, bounded authority, and persistent state directly.

Let advanced techniques such as elaborate Git workflows, RAG, multi-agent orchestration, CI/CD, complex MCP setups, and sophisticated automation arrive when the learner encounters the problem they solve.
