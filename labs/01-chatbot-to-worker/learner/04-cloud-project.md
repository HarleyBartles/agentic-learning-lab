# Lab 1 — Exercise 4: Persistent workspaces

You have now seen an on-disk worker inspect the mission directly.

For this exercise, compare what survives between completely fresh agents when the useful information lives in different places.

Neither side is using memory from an earlier conversation. Memory is not what this exercise is testing.

## Prepare the cloud workspace

Open the prepared ChatGPT Project for Lab 1.

Add these project files:

- `mission/README.md`;
- every file in `mission/source/`.

Do not add the finished `mission-brief.md` from an earlier exercise.

You only need to add the source set once.

## Run A — cloud project plus new information

Start a fresh chat inside the prepared ChatGPT Project.

Ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context. The west-route footbridge is confirmed unaffected by flooding.

Inspect the answer against the mission requirements.

The finished brief should combine the stored project files with the new bridge information supplied in this prompt.

Do not copy the answer into the local mission folder or change the cloud project files.

## Run B — fresh cloud chat, unchanged project files

Start another completely fresh chat inside the same ChatGPT Project.

Do not upload or paste any source material. Do not repeat the bridge confirmation.

Ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context.

Inspect the answer again.

The new chat still has the complete baseline mission context from the project files, but the west-route footbridge confirmation from Run A was never added to those shared files.

## Run C — local workspace plus the same new information

Return to the prepared local Codex project rooted at the mission folder.

Delete `mission/output/mission-brief.md` if it exists so this run starts with no finished brief.

Start a fresh local-agent conversation and ask:

> Complete the exercise. The west-route footbridge is confirmed unaffected by flooding.

Inspect `mission/output/mission-brief.md` when the worker finishes.

The finished file should incorporate the same bridge confirmation used in cloud Run A.

## Run D — fresh local agent, same workspace

Start another completely fresh local-agent conversation rooted at the same mission folder.

Do not repeat the bridge confirmation.

Ask:

> What's the current plan expressed in the mission folder?

Inspect the answer.

The fresh worker can discover the bridge confirmation because Run C left a finished mission brief containing it in the workspace.

## Reflect

Talk through:

- Which information was shared automatically between cloud Runs A and B?
- Which information existed only in the prompt for cloud Run A?
- Why did cloud Run B lose the bridge confirmation even though it still had all the project files?
- Did the fresh local worker in Run D remember Run C's conversation?
- Where did Run D actually discover the bridge confirmation?
- What would have happened if local Run C had only replied in chat and had not written `mission/output/mission-brief.md`?
- Could another fresh cloud chat still use all the uploaded baseline sources without you uploading them again?
- Who is responsible for keeping the cloud Project's uploaded representation fresh if the local source files change later?

The important observations are:

> Neither agent remembered a previous conversation. Memory is not the point.

> Project files can provide persistent baseline context to many fresh cloud chats, while the current prompt can add extra context for one task.

> Information survives into a fresh agent when it has been persisted somewhere that agent can inspect.

In this exercise, cloud Run A used the bridge confirmation but left it only in its conversation output. Local Run C wrote the confirmation into a project artifact, so local Run D could discover it from the workspace.
