# Core principles

These are the ideas to reinforce throughout the lab. They are more important than any particular product, command, model, or framework.

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
