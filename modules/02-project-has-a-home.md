# Module 2 — The project has a home

Approximate duration: 1 hour.

## Core idea

Persistent project state should live somewhere explicit, inspectable, and easy for an agent to enter.

## Example structure

```text
project/
    README.md
    source/
    notes/
    working/
    output/
```

Let the agent explore the project rather than spoon-feeding individual files.

Try prompts such as:

- Read the project and tell me what it is about.
- Find the important decisions already captured here.
- Update the output based on everything in `source/`.
- Tell me what is authoritative and what is disposable.

## Cloud memory and project files

Cloud memory is useful for lightweight continuity, but it is a poor project-state mechanism when the work needs to be authoritative, inspectable, versioned, or precisely controlled.

Cloud project files are useful too, but the human can become responsible for keeping the cloud copy synchronised with the real project.

Use this to introduce:

> Memory is context. Files are state.

and:

> Do not make the human act as the agent's filesystem.

## Suggested non-code example

A small family-history, research, writing, or household-project folder works well. The point is to show that repositories and project directories are not inherently software concepts.

## Discussion prompts

- What information belongs in chat history?
- What information should be durable project state?
- If two sources disagree, where should the authoritative answer live?
- How does the agent know what has changed since yesterday?

## Do not teach yet

Do not over-engineer folder structure or introduce a huge project instruction file. Keep the project simple enough to understand at a glance.
