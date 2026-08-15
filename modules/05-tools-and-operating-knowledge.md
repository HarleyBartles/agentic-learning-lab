# Module 5 — Tools and operating knowledge

Approximate duration: 1 hour.

## Core idea

A capable model with the wrong tool is badly equipped, and giving it a rich tool does not automatically teach competent use of that tool.

Two things belong together:

1. provision the capability;
2. teach the agent how to use it well.

## Suggested session shape

### 0–15 minutes — Revisit the technical drawing failure

Use the learner's real example: asking ChatGPT for a technical drawing and getting an image-generation workflow.

Discuss why image generation is a poor lever when the job needs deterministic geometry, dimensions, repeatability, exact vectors, or machine-checkable output.

Possible better tools include:

- SVG/vector generation;
- OpenSCAD;
- CAD software;
- geometry libraries;
- PDF rendering;
- dimensional checks.

The lesson is:

> Intelligence and capability are separate things.

### 15–35 minutes — Give one project a purpose-built tool

Use `projects/technical-drawing/` or another simple fixture.

Install or expose one deterministic tool, ideally something understandable such as SVG generation or OpenSCAD.

Ask the agent to create a simple dimensioned object, then modify one measurement and regenerate it.

Compare that workflow with image generation. Focus on controllability, reproducibility, editability, and verification rather than visual prettiness.

### 35–50 minutes — Rich tools need operating doctrine

Introduce a richer surface such as the GitHub MCP/connector.

Distinguish:

- **Tool or MCP:** What can I do?
- **Skill:** How should I do this kind of work?
- **Project instructions:** What rules apply here?
- **Task:** What are we trying to accomplish now?

> Tools expose verbs. Skills teach workflows.

A large GitHub tool surface may expose repo reads, branches, issues, PRs, comments, checks, and publication operations. That does not by itself teach the agent when local Git is better, when remote proof matters, or what order constitutes a safe publication workflow.

Run a small experiment if practical:

1. expose a moderately rich tool and give only the task;
2. observe how the agent navigates the tool surface;
3. provide concise procedural guidance or a simple skill;
4. repeat a similar task;
5. discuss what improved without changing the underlying capability.

### 50–60 minutes — Project-specific capability

Compare toolsets for different project types:

```text
technical drawing -> geometry + renderer + checks
writing           -> document/PDF tooling
software          -> compiler + tests + browser + database
research          -> extraction + search + provenance tools
```

Discuss why not every project should expose every credential or capability.

## Tools to experiment with

- one deterministic technical-drawing tool;
- local shell/tool execution through the agent;
- one rich MCP such as GitHub;
- later, one tiny skill that teaches a specific workflow.

## Discussion prompts

- What can the model reason about but not actually do with its current tools?
- Which tool is the right lever for this artifact?
- How would the agent know the preferred workflow for a large tool surface?
- Is this guidance project-specific or reusable across projects?
- Which capabilities should this project *not* have?

## Principle

> Tool richness increases the need for operating knowledge.

and:

> Give the worker the right tools — and teach it how to use them.

## Do not teach yet

Do not install a giant universal MCP collection or a library of skills. One obvious capability plus one obvious workflow is more educational than an impressive stack the learner cannot explain.
