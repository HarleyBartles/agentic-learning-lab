# Lab 2 — Exercise 1: Which state are you looking at?

Both agents can now reach the project.

Use the same question in each run:

> What time is the supplier arriving at Riverside Hall?

## Run A

Ask cloud ChatGPT using the repository connector.

Then ask the prepared on-disk agent working in the Lab 2 project.

Compare the answers.

## Run B

Choose a different supplier arrival time. Do not write your chosen time into the repository or tell cloud ChatGPT.

Tell the on-disk agent to change the supplier arrival time to the time you chose, then stop for review without committing or publishing the change.

Ask both agents the same question again in fresh conversations.

Compare the answers.

## Run C

Leave the local change from Run B exactly where it is.

Choose another supplier arrival time, different from the one you chose for Run B.

Ask cloud ChatGPT to change the supplier arrival time directly in the repository to this new time using its repository access.

Do not refresh, reset, or otherwise synchronise the local working copy yet.

Ask both agents the same question again.

Compare the answers.

Now return to the on-disk agent and say:

> I changed my mind. Abandon my local change to the supplier file and restore that file to the saved local version. Then tell me the supplier arrival time again.

Compare that answer with the current repository answer from cloud ChatGPT.

## Reflect

Talk through:

- Did both agents have access to the project in all three runs?
- Were they always looking at the same current state?
- In Run C, how many different plausible project states existed at once?
- What did the cloud agent see?
- What did the local worker see before the local change was abandoned?
- What did the local worker see after restoring its saved local version?
- Why was that restored local value still different from the newer repository value?

Do not worry about the mechanics of synchronising, committing, or discarding changes yet. The observation for now is that `has access to the project` does not automatically mean `is looking at the same project state`.
