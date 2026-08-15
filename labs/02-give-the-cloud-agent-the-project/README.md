# Lab 2 — Give the cloud agent the project

Status: **locked / stable**.

Lab 2 is the direct continuation of Lab 1.

Lab 1 showed that an agent which cannot see the project surface cannot know what project state is missing from the context the human supplied. Lab 2 changes that condition: cloud ChatGPT is given access to this repository through the GitHub connector.

The aim is not to decide that cloud or local agents are better. It is to make `has access to the project` feel like an incomplete description.

The lab uses four exercises:

1. `learner/01-which-state.md` — both agents can reach the project, but they can observe different current states;
2. `learner/02-can-you-see-it.md` — a file can exist on an accessible project surface without the connector exposing the representation needed for the task;
3. `learner/03-is-the-repo-the-whole-project.md` — a source-controlled repository is not necessarily the whole working environment;
4. `learner/04-what-can-this-surface-do.md` — access surfaces can expose different mutation permissions and safety boundaries.

The shared exercise fixture lives in `project/` inside this same teaching repository. The cloud agent reaches it through the GitHub connector. The on-disk agent reaches the learner's local working copy.

Connector implementation details remain facilitator setup in this lab. The learner should experience the differences before being asked to understand how the connector is implemented.
