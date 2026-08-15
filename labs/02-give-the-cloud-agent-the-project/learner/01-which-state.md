# Lab 2 — Exercise 1: Which state are you looking at?

Both agents can now reach the project.

Use the same question in each run:

> What time is the supplier arriving at Riverside Hall?

## Run A

Ask cloud ChatGPT using the repository connector.

Then ask the prepared on-disk agent working in the Lab 2 project.

Compare the answers.

## Run B

The facilitator will change the local project without changing the repository copy visible to cloud ChatGPT.

Ask both agents the same question again in fresh conversations.

Compare the answers.

## Run C

The facilitator will reset the project, then cloud ChatGPT will be asked to change the supplier time through its repository access.

Do not refresh the local working copy yet.

Ask both agents the same question again.

Compare the answers.

## Reflect

Talk through:

- Did both agents have access to the project in all three runs?
- Were they always looking at the same current state?
- In which run was the local worker ahead?
- In which run was the connected cloud agent ahead?

Do not worry about the mechanics of synchronising the copies yet. The observation for now is that `has access to the project` does not automatically mean `is looking at the same project state`.
