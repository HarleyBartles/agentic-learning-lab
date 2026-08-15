# Module 1 — From chatbot to worker

Approximate duration: 1 hour.

## Core idea

There is a difference between asking an AI for an answer and giving an agent a place to work.

## Start from existing experience

Use ordinary ChatGPT first. Pick a modest multi-step task: write a short document from supplied material, organise some notes, or revise an earlier output.

Notice the friction rather than lecturing about it:

- copying output somewhere else;
- uploading source files;
- explaining what changed;
- finding the current version;
- reminding the model about previous decisions;
- manually carrying state between the AI and the real project.

The lesson is not that cloud chat is bad. It is that a conversation and a working environment solve different problems.

## Demonstration

Ask a cloud agent to create a document, then manually download or copy it.

Then ask an on-disk agent inside a disposable project to create `output/report.md` directly.

Discuss what changed about the human's role.

## Useful distinction

> A chat is somewhere you talk to an AI.
>
> A working environment is somewhere an AI can do work.

## Discussion prompts

- Which parts of the first workflow were useful?
- Which parts were administrative friction?
- Who was maintaining the project state: the AI or the human?
- When is a chat still exactly the right tool?

## Do not teach yet

Avoid Git internals, MCP, skills, branches, RAG, or multi-agent systems unless the conversation naturally demands them.
