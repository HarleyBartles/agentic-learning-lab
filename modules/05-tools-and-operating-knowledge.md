# Module 5 — Tools and operating knowledge

Approximate duration: 1 hour.

## Core idea

A capable model with the wrong tool is badly equipped, and giving it a rich tool does not automatically teach competent use of that tool.

Two things belong together:

1. provision the capability;
2. teach the agent how to use it well.

## Technical drawing example

Use the learner's earlier failure: asking ChatGPT to create a technical drawing and getting an image-generation workflow.

Discuss why image generation is the wrong lever for work that may require deterministic geometry, dimensions, repeatability, or exact vector/CAD output.

Possible appropriate tools might include:

- SVG/vector generation;
- OpenSCAD;
- CAD software;
- geometry libraries;
- PDF rendering;
- dimensional checks.

The lesson is:

> Intelligence and capability are separate things.

## Project-specific tooling

Different projects should expose different tools.

A technical drawing project may need geometry and rendering tools. A writing project may need document/PDF tools. A software project may need a compiler, tests, browser automation, and a database. A research project may need document extraction or indexing.

This is both a capability and an isolation question: an agent should not automatically receive every tool or credential available on the machine.

## Rich tools need operating doctrine

A large MCP such as GitHub can expose many overlapping operations. Tool descriptions tell the agent what actions exist, but not necessarily the best operating workflow.

A useful distinction:

- **Tool or MCP:** What can I do?
- **Skill:** How should I do this kind of work?
- **Project instructions:** What rules apply here?
- **Task:** What are we trying to accomplish now?

> Tools expose verbs. Skills teach workflows.

For example, a GitHub MCP may expose repository, branch, issue, PR, review, check, and publication operations. A corresponding skill can teach an agent to prefer the local checkout for deep inspection, use GitHub for remote state, verify before publishing, and treat remote evidence rather than a local claim as proof of publication.

## Suggested experiment

Give an agent a moderately rich tool without much procedural guidance and observe how it navigates the tool surface.

Then add concise workflow guidance or a skill and repeat a similar task.

Discuss what improved even though the underlying tool capability did not change.

## Principle

> Tool richness increases the need for operating knowledge.
