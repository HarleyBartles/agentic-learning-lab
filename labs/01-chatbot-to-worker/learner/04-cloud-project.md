# Lab 1 — Exercise 4: Cloud project workspace

You have now completed the same mission in an ordinary cloud conversation and with an on-disk worker.

For this run, give cloud ChatGPT a more persistent working environment of its own.

## Create the cloud project

Create a new ChatGPT Project for the mission.

Add these project files:

- `mission/README.md`;
- every file in `mission/source/`.

Do not add the finished `mission-brief.md` from an earlier exercise.

## Run the mission

Start a new chat inside that ChatGPT Project.

Ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context.

Inspect the answer against the same mission requirements used in the earlier exercises.

Do not copy the answer back into the local mission folder yet.

## Reflect

Talk through:

- Did you have to upload the source files again when you started the chat inside the Project?
- Who put the project material into the cloud workspace in the first place?
- If one of the local source files changed tomorrow, would this cloud Project automatically contain that new version in the setup you just created?
- Who would be responsible for deciding that the cloud copy needed refreshing?
- Where does the finished brief exist right now?
- If the finished brief belongs in the local project, who would still have to move it there?

The important observation is:

> A cloud agent can have a persistent working environment too.

That environment reduces repeated context transport between cloud conversations, but in this setup the human still creates and maintains the cloud representation of the project.
