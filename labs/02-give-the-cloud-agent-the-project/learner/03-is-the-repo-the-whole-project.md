# Lab 2 — Exercise 3: Is the repository the whole project?

The Riverside Hall project keeps current attendee requirements in a local operational database.

Ask cloud ChatGPT, using only its repository access:

> How many confirmed vegetarian meals are currently required?

Then ask the prepared on-disk agent the same question from the local Lab 2 project.

## Reflect

Talk through:

- Could the cloud agent discover that the project uses a local attendee database?
- Could it inspect the current records in that database through the repository connector?
- Could the on-disk agent find and query the database in its working environment?
- Does the repository necessarily contain every piece of state used by the project?

The database is not excluded just to make this exercise work. Operational database contents are commonly kept out of source control while schema, setup, migrations, test data, and code around the database may be versioned normally.

The important observation is:

> The source-controlled repository and the project's working environment can overlap without being identical.
