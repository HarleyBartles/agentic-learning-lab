# Module 1 — From chatbot to worker

Approximate duration: 1 hour.

Status: **tightening / intended to become stable**.

## Learning goal

The first session should change one mental model and do little else.

The learner probably begins here:

> I have a task, I open ChatGPT, I explain it, it gives me something, and I take the result away.

By the end of the session, they should have experienced this alternative:

> I have a project. An agent can work inside the project's environment, inspect the project's actual state, and leave useful work there.

The important distinction is not cloud bad, local good. It is:

> A chat is somewhere I talk to an AI. A working environment is somewhere an AI can do work.

The exercise should make that distinction visible through experience rather than explanation.

## The core experiment

Run **the same mission twice**.

Attempt A uses ordinary cloud ChatGPT with no access to the local project.

Attempt B uses Codex operating locally inside the project.

The intellectual task and success condition are identical. The thing that changes is where the agent is working.

The learner should discover that the cloud workflow requires the human to transport project context into the AI's environment and then transport the resulting artifact back out. In the local workflow, that transport work largely disappears.

## The mission

Use:

`labs/01-cloud-vs-local/`

The learner is given a small field-recovery scenario. Several source files contain the information needed to prepare a mission brief, including a late update that supersedes part of the original plan.

The only win condition is:

> A correct finished file exists locally at `labs/01-cloud-vs-local/output/mission-brief.md`.

The brief must satisfy the requirements stated in the lab README and correctly reconcile the source material.

The repository is incidental at this stage. To the learner, this can simply be a project folder on their computer.

## Before the session

Prepare everything so no infrastructure lesson leaks into Module 1.

### Cloud environment

The learner should have:

- a ChatGPT seat you control;
- ordinary cloud ChatGPT available;
- file upload/download capability available;
- **no GitHub connector access to this learning repository**;
- no ChatGPT Project or other preloaded copy of the lab source material;
- a fresh conversation for Attempt A.

The point is not to cripple ChatGPT. It should work normally. It simply should not already inhabit or retrieve from the local project.

### Local environment

Prepare in advance:

- this project already present on the learner's computer;
- an IDE/editor where the learner can see folders and files;
- Codex installed and authenticated;
- Codex able to work locally in the project folder;
- no important personal or work data inside the project;
- no broad external credentials needed for the exercise.

If Git was used to obtain the project, that is facilitator setup, not learner material. Do not explain clone, commit, push, branches, remotes, or source control during this module unless an unexpected question makes a brief answer necessary.

Do not pre-install a large `AGENTS.md`, skills, MCP collection, or other sophisticated project machinery. The local agent should win mainly because it can inhabit the project.

## Suggested shape of the hour

This is guidance, not a script. Preserve the start point, the two attempts, and the end point; let the conversation between them breathe.

### 0–10 minutes — Start from familiar AI use

Ask how the learner already uses ChatGPT or Claude.

Useful questions:

- What kinds of things do you ask it to do?
- When it produces something useful, what happens next?
- Have you downloaded a generated file before?
- Have you copied an answer into a document or another application?
- Have you uploaded revised files back into a later chat?
- What happened when you tried to create a technical drawing?

Do not correct anything. Establish that cloud chat is already useful and familiar.

It is worth saying explicitly that many tasks should remain conversations: questions, brainstorming, casual research, explanation, and one-off advice may need nothing more elaborate.

### 10–25 minutes — Attempt A: complete the mission with cloud ChatGPT

Show the learner the local folder:

`labs/01-cloud-vs-local/`

Give them the goal, not the workflow:

> Complete this mission using ChatGPT. You have succeeded when the correct `mission-brief.md` exists in the local `output` folder. ChatGPT cannot see this project. Use it however you want.

Then stop directing the mechanics.

If they ask:

> Should I upload the source files or paste them?

A good answer is:

> Either works. Choose how you want to get the job done.

The learner may:

- upload the source files;
- paste some or all of their contents;
- ask ChatGPT to create a downloadable Markdown file;
- copy the final answer into a new local file;
- download an artifact and move it into the output folder;
- use some other reasonable combination.

All of those count.

Do not manufacture extra friction. The exercise succeeds even if the learner finds an efficient cloud workflow.

What matters is that **they decide how information crosses both boundaries**:

```text
local project
    ↓ human transports project context
cloud ChatGPT
    ↓ human transports finished artifact
local project
```

The learner has won Attempt A when the file exists locally in the correct place and is good enough.

### 25–30 minutes — Notice what happened

Before explaining anything, ask:

> What work did you have to do purely because ChatGPT could not see or write to this project?

Possible observations:

- deciding which files ChatGPT needed;
- opening or selecting them;
- uploading or pasting them;
- explaining relationships between them if necessary;
- retrieving the generated result;
- deciding how to turn the result into the required local file;
- moving or pasting it into the expected output location.

The point is not that this was difficult. With a handful of small files it may have been trivial.

A useful phrase is:

> You were acting as the transport layer between the AI and the project.

Do not yet discuss source control, connectors, persistent project instructions, or elaborate agent architecture.

### 30–35 minutes — Discard the result

Delete the completed `output/mission-brief.md` and return the exercise to its starting state.

Do this casually.

There is no commit and no push. There is no need to explain recovery semantics yet. The lab is disposable and the artifact is about to be regenerated.

This deliberate discard is useful later: the source-control module can reveal why we can become even more comfortable making and undoing changes in project environments.

### 35–50 minutes — Attempt B: same mission, local Codex

Now allow Codex to operate locally in the project.

The learner's prompt should be intentionally small:

> Complete the exercise in `labs/01-cloud-vs-local`.

That should be enough.

Do not secretly encode the navigation plan into the prompt. We want the environment to carry that information.

A successful local agent should be able to discover for itself:

```text
lab README
    ↓
mission and output requirement
    ↓
source directory
    ↓
relevant source files
    ↓
late/superseding information
    ↓
output/mission-brief.md
```

Watch what Codex actually inspects and changes.

When it finishes, open the resulting file from the local project tree and compare it with the required outcome.

### 50–60 minutes — Compare the work, not the prose

The key comparison is not which mission brief was better written.

Ask:

- What did you have to move manually in Attempt A?
- What did you have to move manually in Attempt B?
- Did Codex need you to tell it which source files existed?
- Did you need to copy its finished answer anywhere?
- Was the local agent necessarily smarter, or did it have a different working environment?
- Would the cloud workflow still be perfectly reasonable for four tiny files?
- What changes if there are 40 files? 400?
- What if the task is to update six existing documents rather than create one new document?
- What if neither you nor the agent initially knows which files contain the relevant information?
- What if this job happens repeatedly as the project changes?

The scaling question is important. Module 1 should not end with:

> Codex saved me thirty seconds of copying.

It should end with something closer to:

> Direct project access changes the kinds and scale of work that are sensible to delegate.

## End point

The learner should leave with three ideas.

### Cloud chat can do project work when I bring the project context to it

That can be completely appropriate for small or occasional tasks.

### A local agent can inspect and modify the project's working state directly

The human does not always need to select every input, upload it, retrieve every output, and put it back where it belongs.

### This is primarily an environment difference, not proof of a smarter model

The local agent may have comparable intelligence. What changed was its proximity to the source of truth and its ability to act on the project directly.

A compact formulation:

> The on-disk agent removes the human from much of the context-and-artifact transport loop.

## Why the mission includes a late update

The source material deliberately contains a superseding fact.

This gives the artifact a small correctness criterion beyond merely producing plausible prose. The learner or agent has to inspect enough of the source set to notice that the original plan is no longer fully current.

Do not turn this into the verification lesson yet. It simply makes the mission real enough to have a right and wrong result.

## Tools in this module

Use only what is needed to make the environmental contrast visible:

- ordinary cloud ChatGPT;
- file upload/download or copy/paste, at the learner's discretion;
- the local filesystem and IDE file tree;
- Codex operating locally in the project.

Deliberately avoid making these part of the lesson:

- Git commands;
- GitHub pushes or pull requests;
- GitHub connector/MCP access;
- custom skills;
- `AGENTS.md`;
- branches or worktrees;
- multi-agent systems;
- RAG/vector databases.

## Important facilitator rule

**Do not teach the learner the optimal cloud workflow before Attempt A.**

Their chosen method of getting context into ChatGPT and the artifact back into the project is part of the observation.

Help if they are genuinely blocked, but do not solve the transport problem for them merely because you know a quicker route.

## Misconceptions to watch for

### "So cloud ChatGPT is bad"

No. For a small one-off task, Attempt A may be the simpler choice. The lesson is to recognise when the integration burden begins to dominate the useful work.

### "Codex is better because it is smarter"

Not established. It had direct project access and permission to change local state. Module 4 will later separate model, harness, context, tools, and feedback more carefully.

### "Repositories are for programmers"

Do not even need to use the word repository heavily yet. This is a project folder containing Markdown source material and an output artifact. Later modules can reveal what source control adds.

### "What if the agent breaks something?"

Keep the answer bounded:

> In this lab there is nothing precious. We are going to learn how to make experimentation recoverable rather than avoid experimentation.

Do not teach the mechanism yet.

## Connection to later modules

Module 1 intentionally leaves several useful questions unanswered:

- Where should durable project state live?
- How do we know what changed?
- What if an agent makes a bad change?
- How do we recover something we deleted?
- How does an agent learn durable project rules?
- How do we give it capabilities outside the local project?
- How do we know its work is actually correct?

Those are not omissions. They are hooks for the later curriculum.

The source-control module should explicitly call back to the casual deletion in Module 1: we threw away the first mission brief because the exercise was disposable; now we learn how to make much more consequential experimentation safely reversible.

## Do not teach yet

Unless a learner question genuinely requires a brief detour, postpone:

- Git internals;
- commits, branches, remotes, and merge strategies;
- MCP architecture;
- skills;
- RAG;
- hooks;
- CI/CD;
- multi-agent orchestration;
- elaborate prompting frameworks.

Teach one invariant first:

> A conversation can work on what I bring to it. An on-disk agent can work where the project already lives.
