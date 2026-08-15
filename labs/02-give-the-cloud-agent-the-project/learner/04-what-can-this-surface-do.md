# Lab 2 — Exercise 4: What can this surface do?

Everything in `project/scratch/` is deliberately disposable.

## Run A

Ask the prepared on-disk agent:

> Delete everything in `scratch/`, but do not commit or publish the deletion. Stop for review when the files are gone locally.

Inspect what happened.

Then tell the same on-disk agent:

> I changed my mind. Abandon those local changes and restore the scratch files.

Inspect the folder again.

Do not worry about the source-control mechanics yet. Just notice that a local destructive change which has not been published can be cheap to reverse when the project has a saved version underneath it.

## Run B

Ask cloud ChatGPT, through its repository access, to perform the equivalent deletion against `project/scratch/`.

Follow any confirmation or approval flow that appears normally.

Inspect what happened.

## Reflect

Talk through:

- Could both agents see the scratch area?
- Could both agents change it in the same way?
- What happened when you changed your mind about the local deletion?
- Did either environment require an extra approval or impose a restriction?
- Is that difference a property of the underlying model, or of the access surface, project state, and permissions around it?

The point is not that one environment is inherently safer than the other. Different environments can be configured with different permissions and guardrails.

The important observation is:

> Project access includes not only what an agent can see, but what it is allowed to do through that route.
