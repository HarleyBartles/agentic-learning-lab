# Module 6 — Local work and connected systems

Approximate duration: 1 hour.

## Core idea

Direct project access and connectors solve different problems. They should be composed rather than treated as substitutes.

## Local access

An on-disk agent in a repository can inspect the project directly:

- walk directories;
- read many files;
- grep/search broadly;
- inspect Git history;
- run project scripts;
- render outputs;
- compare generated artifacts;
- discover things nobody knew to retrieve explicitly.

This makes it well suited to deep project exploration and modification.

## Connectors

Connectors are excellent when the agent needs to reach systems outside the project environment:

- GitHub remote state;
- email;
- calendars;
- issue trackers;
- cloud storage;
- databases;
- external APIs.

A connector is a bridge, not a replacement for direct access to the project when deep local inspection is the real task.

## Useful distinction

> Retrieval asks for something. Exploration discovers what is there.

A connector often works by retrieving the relevant object or result. A local agent can build its own understanding by traversing the project and following evidence wherever it leads.

## Suggested demonstration

Use the same repository through two routes.

First, ask a cloud-connected agent a focused question through the GitHub connector, such as locating a file or checking a remote issue.

Then ask a local agent to understand the repository structure and explain how the project fits together.

Discuss why both are useful and why they are not interchangeable.

## Project isolation

Use this module to reinforce that different agent environments should expose only the capabilities they need.

A project may have:

```text
local repo
  + local tools
  + project instructions
  + Git history
  + selected MCPs/connectors
```

The repository is the workplace. Connectors let the agent reach outside that workplace.

## Discussion prompts

- When is retrieval enough?
- When does the agent need direct access to inspect broadly?
- Which external systems should this project be allowed to touch?
- What information belongs locally versus behind a connector?
