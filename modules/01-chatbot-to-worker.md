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

Run **the same mission three times**.

1. Cloud ChatGPT with the complete source set: success.
2. Cloud ChatGPT with one critical source file deliberately omitted: plausible failure.
3. Codex operating locally in the project: success through direct inspection of project state.

The intellectual task is the same in all three stages.

Both cloud ChatGPT and Codex should be fully capable of completing it correctly when they have the complete source material. The exercise is not trying to prove that one model can reason and another cannot.

It is trying to make two things observable:

- a cloud conversation can only reason over project state that has been made available to it;
- an on-disk worker can inspect the environment where the project state actually lives.

## The mission

Use:

`labs/01-cloud-vs-local/`

The learner is given a small field-recovery scenario. Several source files contain the information needed to prepare a mission brief. One later file explicitly supersedes part of the original plan.

The win condition is:

> A correct finished file exists locally at `labs/01-cloud-vs-local/output/mission-brief.md`.

A correct brief must:

- satisfy the required sections in the lab README;
- select the single current access route and timing;
- apply the later superseding information rather than presenting old and new plans as unresolved alternatives;
- identify the remaining unresolved field risk;
- avoid contradicting any current source constraint.

The superseding update is intentionally easy to reconcile once seen. This is not a reasoning trap. Its purpose is to make completeness of context observable.

The repository is incidental at this stage. To the learner, this can simply be a project folder on their computer.

## Before the session

Prepare everything so no infrastructure lesson leaks into Module 1.

### Cloud environment

Before beginning Stage 1, disable ChatGPT conversation memory / cross-chat memory for the learner's seat in ChatGPT settings. The purpose is experimental isolation: Stage 2 must not be able to recover the late update from Stage 1 through remembered conversation context.

The learner should then have:

- a ChatGPT seat you control;
- ordinary cloud ChatGPT available;
- file upload/download capability available;
- **conversation memory disabled for the exercise**;
- **no GitHub connector access to this learning repository**;
- no ChatGPT Project or other preloaded copy of the lab source material;
- a fresh conversation for Stage 1;
- another fresh conversation for Stage 2.

The point is not to cripple ChatGPT. It should work normally apart from deliberately removing hidden continuity between the two experimental conversations. It simply should not already inhabit, retrieve from, or remember the local project.

Stage 2 must still use a fresh conversation even with memory disabled. We want both protections: no conversation carry-over and no cross-chat memory contamination.

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

This is guidance, not a script. Preserve the start point, the three stages, and the end point; let the conversation between them breathe.

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

### 10–22 minutes — Stage 1: cloud ChatGPT with complete context

Show the learner the local folder:

`labs/01-cloud-vs-local/`

Give them the goal, not the workflow:

> Complete this mission using ChatGPT. Make sure ChatGPT has all of the information. You have succeeded when the correct `mission-brief.md` exists in the local `output` folder. ChatGPT cannot see this project. Use it however you want.

Then stop directing the mechanics.

If they ask:

> Should I upload the source files or paste them?

A good answer is:

> Either works. Choose how you want to get the job done.

The learner may upload files, paste contents, ask ChatGPT for a downloadable Markdown file, copy the answer into a local file, or use some other reasonable workflow.

All of those count.

Do not manufacture extra friction. The goal is not to make cloud ChatGPT look clumsy.

If the learner is about to proceed without supplying the full source set, give a gentle nudge:

> Before you ask it to finish, are you sure ChatGPT has everything in this project that might matter?

If useful, add:

> Remember, it cannot inspect the folder itself. If there is a file you have not shown it, it does not know that file exists.

Do not identify the important file or prescribe how to supply it.

Stage 1 should end in a correct mission brief. This proves that cloud ChatGPT is fully capable of the task when the human supplies complete context.

### 22–28 minutes — Notice the transport work

Ask:

> What work did you have to do purely because ChatGPT could not see or write to this project?

Possible observations:

- deciding which files ChatGPT needed;
- opening or selecting them;
- uploading or pasting them;
- checking that the source set was complete;
- retrieving the generated result;
- turning the result into the required local file;
- putting it into the expected output location.

A useful phrase is:

> You were acting as the transport layer between the AI and the project.

Then delete `output/mission-brief.md`.

Do this casually. There is no commit and no push. Source control is not part of this lesson.

### 28–38 minutes — Stage 2: deliberately hide critical context

Start a **fresh ChatGPT conversation**. Conversation memory should still be disabled.

Now repeat the same mission, but deliberately omit:

`source/late-update.md`

Give ChatGPT the other source files and ask it to prepare the mission brief.

Do not tell ChatGPT that information has been withheld. The model should simply work from the apparently complete evidence it was given.

Inspect the result together.

The expected outcome is a plausible, confident brief based on the original access plan. It should be wrong about the current route/timing because the superseding state was invisible.

The teaching question is:

> Did ChatGPT fail to understand the information, or did it never have the information it needed?

Stage 1 has already answered that question. With the full source set, it got the task right.

A useful formulation:

> Missing context is invisible context.

And another:

> An AI cannot reason about a project fact it has no way to observe.

Do not turn this into a discussion of hallucination. The model is behaving reasonably from incomplete evidence supplied by the human.

Delete any Stage 2 output before continuing.

### 38–52 minutes — Stage 3: same mission, local Codex

Now allow Codex to operate locally in the project.

The learner's prompt should be intentionally small:

> Complete the exercise in `labs/01-cloud-vs-local`.

That should be enough.

Do not point Codex toward `late-update.md`, enumerate the source files, or give it a completeness nudge.

A successful local worker should be able to discover for itself:

```text
lab README
    ↓
mission and pass conditions
    ↓
source directory
    ↓
complete source set
    ↓
original plan + late superseding update
    ↓
current reconciled mission state
    ↓
output/mission-brief.md
```

When it finishes, inspect the resulting local file against exactly the same win condition as Stage 1.

If it succeeds, the contrast is now much stronger than a simple cloud/local convenience comparison.

The learner has seen:

- a capable cloud AI succeed with complete context;
- the same kind of AI workflow fail when a critical project fact is omitted;
- an on-disk worker discover the relevant project state without relying on the human to enumerate every input.

### 52–60 minutes — Compare the three stages

Do not compare prose quality.

Ask:

- Why did Stage 1 succeed?
- Why did Stage 2 fail?
- Was Stage 2 evidence that ChatGPT was less intelligent?
- What fact was invisible in Stage 2?
- Who was responsible for deciding whether cloud ChatGPT had the complete source set?
- Why did Codex not need the same completeness reminder?
- What would happen with 40 files? 400?
- What if neither you nor the AI initially knew which file contained the critical update?
- What if several files had changed since the last time you ran the task?

The comparison can be summarised as:

```text
Stage 1 — cloud + complete context
human discovers and transports state → AI succeeds

Stage 2 — cloud + incomplete context
human omits critical state → AI cannot see it → plausible failure

Stage 3 — on-disk worker
agent inspects project state itself → AI succeeds
```

The scaling question matters. Module 1 should not end with:

> Codex saved me a bit of copying.

It should end with:

> Direct project access changes who is responsible for discovering complete context, and that changes the reliability and scale of work that is sensible to delegate.

## End point

The learner should leave with four ideas.

### Cloud chat can do project work when I bring the project context to it

Stage 1 demonstrates that clearly.

### A capable AI can still produce the wrong project answer when critical state is invisible

Stage 2 demonstrates this without requiring the AI to behave badly or reason poorly.

### A local agent can inspect and modify the project's working state directly

Stage 3 removes much of the human responsibility for enumerating every relevant local input and transporting every artifact.

### This is primarily an environment difference, not proof of a smarter model

The same reasoning problem is easy once the relevant information is visible.

Compact formulations worth preserving:

> The on-disk agent removes the human from much of the context-and-artifact transport loop.

> Missing context is invisible context.

> A conversation can work on what I bring to it. An on-disk agent can inspect where the project already lives.

## Why the mission includes superseded state

The source material deliberately contains an original plan and `late-update.md`, which explicitly supersedes part of it.

The correct interpretation is straightforward once both files are visible.

That is intentional. We are not testing whether the cloud or local agent can reason through a difficult ambiguity. We are testing whether the system has access to the complete project state needed to reach the correct answer.

This lightly foreshadows later lessons about source of truth, retrieval, verification, and persistent state without teaching those concepts yet.

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

## Important facilitator rules

### Isolate the cloud stages

Disable ChatGPT conversation memory before Stage 1 and keep it disabled throughout the exercise. Use separate fresh conversations for Stages 1 and 2.

The controlled Stage 2 failure is only meaningful if `late-update.md` is genuinely unavailable to that conversation.

### Stage 1 should succeed

Gently steer the learner toward supplying all source material if necessary. We want proof that cloud ChatGPT can solve the task.

### Stage 2 should fail for exactly one reason

Use a fresh conversation and deliberately omit only `source/late-update.md`. The resulting failure should be attributable to missing context, not confusing instructions or a difficult reasoning problem.

### Stage 3 should receive no file-level hints

Give Codex the one-line mission prompt and let it inspect the project. Its ability to discover the complete source set is part of the evidence.

### Do not teach the optimal cloud workflow

The learner chooses how files and artifacts cross the cloud boundary. That transport work is itself part of the lesson.

## Misconceptions to watch for

### "So cloud ChatGPT is bad"

No. Stage 1 proves the opposite. With the necessary context it performs the task correctly, and for small one-off tasks it may still be the best lever.

### "Stage 2 is a hallucination"

Not really. The model was given an incomplete but internally plausible version of the project state. The important failure happened at the context boundary.

### "Codex is better because it is smarter"

Not established. Its important advantage in this experiment is environmental: it can inspect the project directly.

### "Repositories are for programmers"

Do not even need to use the word repository heavily yet. This is a project folder containing source material and an output artifact. Later modules can reveal what source control adds.

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

The source-control module should explicitly call back to the casual deletion in Module 1: we repeatedly threw away generated mission briefs because the exercise was disposable; later we learn how to make much more consequential experimentation safely reversible.

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

> A conversation can only work with the project state made visible to it. An on-disk worker can inspect the environment where that state lives.
