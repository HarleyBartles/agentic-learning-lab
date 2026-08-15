# Module 2 — The project has a home

Approximate duration: 1 hour.

## Core idea

Persistent project state should live somewhere explicit, inspectable, and easy for an agent to enter.

The key distinction is:

> Memory is context. Files are state.

and:

> Do not make the human act as the agent's filesystem.

## Suggested session shape

### 0–15 minutes — Revisit Module 1 friction

Open the local project from the previous session and ask what the agent can know by inspecting the folder versus what a cloud chat may merely remember from conversation.

Discuss examples of information that feels different when written into the project:

- current objectives;
- authoritative decisions;
- source documents;
- generated outputs;
- unresolved questions;
- notes that may later become stale.

### 15–35 minutes — Build a small project home

Use or create a simple structure such as:

```text
project/
    README.md
    source/
    notes/
    working/
    output/
```

Let the learner decide what belongs where. Avoid presenting the structure as sacred.

Ask the local agent:

- Read the project and tell me what it is about.
- Find the important decisions already captured here.
- Tell me which files look authoritative and which look disposable.
- Update the output based on everything in `source/`.

The important observation is that the agent can discover project state rather than being told every fact in the prompt.

### 35–50 minutes — Compare memory, project files, and actual project state

Discuss cloud memory fairly. It is useful for lightweight continuity and personal preferences. Its natural limitations for authoritative project state include selective recall, opacity, lack of normal versioning, and difficulty precisely inspecting what is currently considered true.

Discuss cloud project files fairly too. They are useful, but when the real project also exists elsewhere the human may become responsible for synchronising two representations of the work.

A useful diagram:

```text
real project on disk
        <->
cloud representation maintained by the human
```

Ask what happens when a local source file changes after it was uploaded.

### 50–60 minutes — Source of truth itch

Create a harmless disagreement between two notes: one says a decision is A, another says B.

Ask the agent what it believes and why.

Do not fully solve governance yet. The aim is to surface the need for explicit authority and prepare Module 7.

## Tools to experiment with

- filesystem and IDE tree;
- local agent repository inspection;
- ordinary ChatGPT memory/project features if useful for comparison;
- simple text files as explicit durable state.

## Non-code examples

Good project homes include family history, a house renovation, tabletop game design, research, writing, event planning, a collection, or technical design work.

## Discussion prompts

- What belongs in chat history versus project state?
- Which information should survive a new conversation?
- Which information should be easy to inspect and version?
- What should happen when two files disagree?
- How much structure helps before structure becomes bureaucracy?

## Do not teach yet

Do not introduce a huge project instruction file, knowledge graph, database, RAG pipeline, or elaborate taxonomy. Keep the project understandable at a glance.
