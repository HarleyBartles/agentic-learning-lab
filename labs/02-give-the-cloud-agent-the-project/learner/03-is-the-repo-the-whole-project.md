# Lab 2 — Exercise 3: Is the repository the whole project?

The Riverside Hall project needs a small operational attendee database.

## Create the local state

Choose five fictional attendees. Give each person:

- a name;
- whether they are confirmed;
- a meal choice of `standard`, `vegetarian`, or `vegan`.

Give those records only to the prepared on-disk agent. Do not put the record values into a tracked project file or into cloud ChatGPT.

Ask the on-disk agent:

> Set up the attendee database for this project using the records I have given you. Create the reusable database schema as part of the project, keep the operational database in the project's normal local location, and push the appropriate source-controlled project work when you are finished.

Let the worker complete the task and publish whatever project changes properly belong in the repository.

## Ask the connected cloud agent

Start a fresh cloud ChatGPT conversation with access to this repository.

Tell it:

> The on-disk worker has just created the attendee database and pushed the appropriate project work to this repository. Using only the repository, list the attendees it captured, whether each is confirmed, and each person's meal choice.

Let the cloud agent inspect the repository as thoroughly as it wants.

Then start a fresh on-disk-agent conversation rooted at the same local project and ask for the same information.

## Reflect

Talk through:

- Did the on-disk worker successfully push project work to the repository?
- What database-related material became visible on GitHub?
- Where did the actual attendee records end up?
- Could the cloud agent retrieve information that never crossed onto the GitHub surface?
- Could the fresh on-disk agent still query that state directly?

The database is not excluded just to make this exercise work. Operational database contents are commonly kept out of source control while reusable schema, migrations, setup code, and other source material may be versioned normally.

The important observation is:

> Publishing the source-controlled work does not necessarily publish every piece of state in the project's working environment.
