# Module 1 — From chatbot to worker

Approximate duration: 1 hour.

## Purpose

The first session should change the learner's mental model of AI before teaching much machinery.

The starting model is likely to be:

> I have a question or task, I open ChatGPT, I explain it, it gives me something, and I take the result away.

The model we want to introduce is:

> I have a project with a real working environment. An agent can enter that environment, inspect its current state, do work there, use tools, and leave the project changed.

Do not frame this as cloud AI versus local AI, or good versus bad. Ordinary ChatGPT is often exactly the right tool. The lesson is that **a conversation and a workplace are different things**.

## Desired outcome

By the end of the hour, the learner should have personally experienced the difference between:

- asking an AI to produce an answer or artifact which the human then carries away; and
- asking an agent inside a project to inspect the project and change it directly.

If the learner leaves with only one sentence, it should be:

> A chat is somewhere I talk to an AI. A working environment is somewhere an AI can do work.

Do not worry yet about whether they know the words repository, harness, MCP, skill, context window, worktree, or RAG.

## Before the session

Prepare the environment so setup does not consume the hour.

Recommended minimum:

- the learner has access to ChatGPT;
- Git is installed, but does not need to be taught yet;
- this repository is cloned locally;
- an on-disk agent can work in the clone — Codex is the primary teaching agent for this lab;
- the learner can see the folder tree and open files in the IDE;
- no important personal or work data is present;
- no broad external credentials are required;
- do not add a large `AGENTS.md`, skills, or MCP collection yet.

The lack of sophisticated project instructions is intentional. Later modules should solve problems the learner has actually felt.

Use `labs/01-cloud-vs-local/` for the main exercise.

## Suggested shape of the hour

This is not a script. Follow interesting questions when they arise.

### 0–10 minutes — Start with what already feels normal

Ask how the learner currently uses ChatGPT or Claude.

Useful prompts for the conversation:

- What kinds of things do you already ask AI to do?
- When it writes something useful, what do you do with the result?
- Have you ever downloaded a generated file and then edited it elsewhere?
- Have you ever had to upload a revised version again?
- Have you ever had to remind a chat about something you thought it already knew?
- What happened with the technical drawing you tried to make?

Do not correct their workflow yet. The point is to establish that cloud chat is already useful and familiar.

If useful, explicitly acknowledge that one-off questions, discussion, brainstorming, web research, and many personal tasks may never need an on-disk agent.

### 10–25 minutes — Do a small project through cloud chat

Open `labs/01-cloud-vs-local/` locally, but use ordinary cloud ChatGPT for the task.

The lab contains a few small source files and asks for a short briefing document.

To make ChatGPT capable of doing the task, the human must expose the relevant material to it. Let the learner decide how: upload the files, copy and paste them, or otherwise provide the context.

A suitable task is:

> Read the supplied source material and produce a concise briefing that captures the objective, constraints, decisions, and open questions.

When the answer is good enough, ask:

> Where does the result live now?

If it exists only in the chat, have the learner get it into the real project. They might copy it into a file or download an artifact and move it into place.

Do not artificially make this painful. Let the normal workflow reveal its own friction.

Things to notice together:

- the human selected what to upload;
- the human carried files across the boundary;
- the model saw the representation supplied to it, not automatically the whole local project;
- the generated result initially lived in the conversation rather than in the project;
- the human had to decide where the result belonged;
- if the local source changes later, the cloud copy does not magically become the current project state.

The point is not that any one of these is terrible. The point is that **the human is doing integration work between the conversation and the project**.

### 25–45 minutes — Give the same job to an on-disk agent

Now open the local clone in the IDE with the on-disk agent operating in the repository.

Use a deliberately ordinary prompt. Avoid an elaborate engineered prompt because the environment itself is the demonstration.

For example:

> Read `labs/01-cloud-vs-local/`, work out what the exercise is asking for, and create the finished briefing in its `output/` directory. Do not change the source material.

Then let the agent work.

Watch what it actually does. Depending on the harness, it may inspect the directory, read the README and source files, decide where the output belongs, and create the file directly.

Open the resulting file from the project tree.

Discuss what changed about the human's job:

- nobody uploaded the source files one by one;
- nobody copied the answer out of the conversation;
- the agent could inspect the project structure itself;
- the output appeared where the work lives;
- the next agent entering the project can inspect the result as project state;
- the human can still review, edit, reject, or replace the work.

A useful phrase here is:

> If I am asking an AI to make something that ultimately needs to live on my computer, why am I always volunteering to be the courier?

Do not turn that into a universal rule. Sometimes the cloud artifact workflow is more convenient. The point is to reveal another option.

### 45–55 minutes — Compare the two environments

Talk through the difference without declaring a winner.

A simple comparison:

| Cloud conversation | On-disk working environment |
| --- | --- |
| Excellent for discussion and one-off tasks | Excellent for sustained project work |
| Human supplies or connects context | Agent can inspect local project state |
| Output naturally begins in the conversation | Output can be written directly into the project |
| Memory and project features can provide continuity | Filesystem and repo provide explicit persistent state |
| Connectors bridge external systems | Local tools can operate directly on project files |

Ask:

- Which parts of the cloud workflow were useful?
- Which parts were just movement of information?
- Who was maintaining the relationship between the AI's view and the real project?
- What kinds of jobs would not benefit from a local environment at all?
- What kinds of jobs become more attractive when the agent can work directly where the project lives?

Good non-code examples to throw into the discussion:

- researching and maintaining a family history archive;
- planning a house renovation with quotes, measurements, decisions, and drawings;
- maintaining a tabletop campaign or game design project;
- writing a long document with source material and revisions;
- organising a collection;
- preparing recurring reports from a folder of source material;
- producing technical drawings or other generated artifacts with the correct local tools.

The repository is not being introduced as a place for code. It is being introduced as a **bounded project home**.

### 55–60 minutes — Leave one useful itch unresolved

Finish by looking at the files the local agent changed.

The learner may naturally ask questions such as:

- What if the agent changes the wrong thing?
- How do I know what it changed?
- What if I want the old version back?
- How does it remember project rules next time?
- What happens when the project gets much larger?

Do not solve all of them now.

Those questions are the curriculum generating itself.

If fear of breakage comes up, reassure the learner only within the actual lab boundary: this repository is deliberately disposable and recoverable. It is safe to experiment here. Source control and recovery are covered properly in Module 3.

## The actual lab

Use:

`labs/01-cloud-vs-local/`

The source material is intentionally mundane. The intellectual difficulty of the task should be low so the learner can pay attention to the operating environment rather than the subject matter.

Run it twice:

1. cloud-first, with the human moving the relevant information and result;
2. local-agent-second, with the agent working directly in the repository.

If the learner notices that ChatGPT can also work with connected files or repositories, agree. That is useful. Do not defend a simplistic local-versus-cloud position. Say that later modules will distinguish direct project access, memory, uploaded project files, synced sources, and connectors.

## Tools to experiment with

Primary tools for this module:

- ChatGPT as an ordinary cloud conversation;
- the IDE's file tree/editor;
- Codex operating locally in the repository;
- the operating-system filesystem.

Tools deliberately **not** required yet:

- Git commands beyond whatever was needed to clone the lab;
- GitHub MCP or connector workflows;
- custom skills;
- `AGENTS.md`;
- branches/worktrees;
- multiple agents;
- RAG/vector databases.

The simplicity matters. We want the learner to attribute the difference to **where the work is happening**, not to a giant preconfigured agent stack.

## Things worth saying explicitly

### The conversation is not the project

A conversation can discuss a project, remember parts of it, receive files from it, or connect to services around it. That does not automatically make the conversation itself the authoritative project state.

### An agent can inspect reality instead of relying only on your description

If the project is on disk and the agent has appropriate access, it can inspect files, folders, outputs, and later history and tools directly. That reduces the amount of project topology the human has to narrate.

### Direct access changes what tasks are worth delegating

A request that feels silly in chat — because copying the result out would take as long as doing the work — can become useful when the agent can make the change directly.

For example:

> Update these twelve project notes to use the new terminology.

In a chat-only workflow, the movement of twelve files may dominate the task. In a local working environment, the agent can potentially inspect and modify them in place.

### Cloud tools remain useful

Do not create the impression that the goal is to abandon ChatGPT cloud. Later the learner should be comfortable choosing among conversation, local agent work, connectors, and combinations of them.

The engineering question is:

> Which environment puts the agent closest to the state and tools needed for this job?

## Watch for these misconceptions

### "Repos are for programmers"

Counter with the contents of this lab itself: Markdown, research notes, briefs, drawings, generated documents, source material, and project instructions all benefit from a durable project home and history.

### "The local agent is smarter"

Not necessarily. The model may be the same or comparable. What changed is the environment, available context, tools, and ability to act on state directly.

### "ChatGPT memory means the project is persistent anyway"

Do not fully unpack this until Module 2. For now, distinguish remembering something about the work from possessing and inspecting the current project state.

### "The agent might break my computer"

Keep the answer scoped. This lab is intentionally bounded and contains nothing precious. The learner will soon learn source control and recovery rather than being told to trust blindly.

## Optional extension if there is time

Make one small change to a source file after both briefings have been produced.

Ask:

> Which version of the project does each AI currently know about?

Do not go deep into memory or synchronisation yet. Just let the question hang as preparation for Module 2.

## Do not teach yet

Avoid turning the first hour into a survey of agentic AI terminology.

Unless the learner pulls hard on one of these topics, postpone:

- Git internals;
- branches and merge strategies;
- MCP architecture;
- skills;
- RAG;
- hooks;
- CI/CD;
- multi-agent orchestration;
- elaborate prompting frameworks.

Teach the invariant first:

> A persistent working environment lets an agent participate in a project instead of only talking about it.
