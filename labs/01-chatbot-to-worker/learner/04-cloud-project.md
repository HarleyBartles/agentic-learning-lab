# Lab 1 — Exercise 4: Cloud project workspace

You have now completed the same mission in ordinary cloud conversations and with an on-disk worker.

For this run, give cloud ChatGPT a persistent working environment of its own.

## Create the cloud project

Create a new ChatGPT Project for the mission.

Add these project files:

- `mission/README.md`;
- every file in `mission/source/`.

Do not add the finished `mission-brief.md` from an earlier exercise.

## Run A — first project chat

Start a new chat inside that ChatGPT Project.

Ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context.

Inspect the answer against the same mission requirements used in the earlier exercises.

Do not copy the answer back into the local mission folder.

## Run B — a completely separate project chat

Leave the project files exactly as they are.

Start another new chat inside the same ChatGPT Project. Do not upload or paste any source material into this new chat.

Ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context. The west-route footbridge is confirmed unaffected by flooding.

Inspect this second answer against the same mission requirements, taking the new bridge information into account.

The wording may differ from Run A. The important question is whether the fresh chat can reconstruct the mission from the same project files and correctly incorporate the new information supplied in this prompt.

## Reflect

Talk through:

- Did the second chat know the mission sources even though you did not upload or paste them into that conversation?
- What information did Run B have that was not stored in the project files?
- Could you start a third or tenth chat in this Project and give it the same project context without re-uploading the sources each time?
- What changed compared with the ordinary cloud conversations in Exercises 1 and 2?
- Who put the project material into this cloud workspace in the first place?
- If one of the local source files changed tomorrow, would this cloud Project automatically contain that new version in the setup you just created?
- Who would be responsible for deciding that the cloud copy needed refreshing?
- Where do the two finished briefs exist right now?
- If a finished brief belongs in the local project, who would still have to move it there?

The important observations are:

> A cloud agent can have a persistent working environment too.

> Once project files are present in that environment, separate cloud chats can use the same project context without the human re-uploading it every time.

That persistent context can also be combined with new information supplied for the current task. In this setup, however, the human still creates and maintains the cloud representation of the project and decides when it needs to be refreshed from elsewhere.
