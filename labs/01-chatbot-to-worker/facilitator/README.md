# Lab 1 facilitator guide — From chatbot to worker

Approximate duration: 1 hour.

Status: **locked / stable**.

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
3. Codex operating locally in the mission workspace: success through direct inspection of project state.

The intellectual task is the same in all three exercises.

Both cloud ChatGPT and Codex should be fully capable of completing it correctly when they have the complete source material. The exercise is not trying to prove that one model can reason and another cannot.

It is trying to make two things observable:

- a cloud conversation can only reason over project state that has been made available to it;
- an on-disk worker can inspect the environment where the project state actually lives.

## The mission

Use the mission workspace in:

`labs/01-chatbot-to-worker/mission/`

The learner is given a small field-recovery scenario. Several source files contain the information needed to prepare a mission brief. One later file explicitly supersedes part of the original plan.

The win condition is:

> A correct finished file exists locally at `labs/01-chatbot-to-worker/mission/output/mission-brief.md`.

A correct brief must:

- satisfy the required sections in the mission README;
- select the single current access route and timing;
- apply the later superseding information rather than presenting old and new plans as unresolved alternatives;
- identify the remaining unresolved field risk;
- avoid contradicting any current source constraint.

The superseding update is intentionally easy to reconcile once seen. This is not a reasoning trap. Its purpose is to make completeness of context observable.

The repository is incidental at this stage. To the learner, this can simply be a project folder on their computer.

## Before the session

Prepare everything so no infrastructure lesson leaks into Lab 1.

### Cloud environment

Before beginning Exercise 1, disable ChatGPT conversation memory / cross-chat memory for the learner's seat in ChatGPT settings. The purpose is experimental isolation: Exercise 2 must not be able to recover the late update from Exercise 1 through remembered conversation context.

The learner should then have:

- a ChatGPT seat you control;
- ordinary cloud ChatGPT available;
- file upload/download capability available;
- **conversation memory disabled for the exercise**;
- **no GitHub connector access to this learning repository**;
- no ChatGPT Project or other preloaded copy of the mission source material;
- a fresh conversation for Exercise 1;
- another fresh conversation for Exercise 2.

The point is not to cripple ChatGPT. It should work normally apart from deliberately removing hidden continuity between the two experimental conversations. It simply should not already inhabit, retrieve from, or remember the local project.

Exercise 2 must still use a fresh conversation even with memory disabled. We want both protections: no conversation carry-over and no cross-chat memory contamination.

### Local Codex environment

Prepare the learner's machine in advance so Exercise 3 does not become a lesson in configuring Codex.

Create a Codex project named:

`Lab 1 - Exercise 3`

Root that project at:

`labs/01-chatbot-to-worker/mission/`

Give the project minimal operating instructions through Codex's own project/configuration machinery rather than adding an `AGENTS.md` to the mission folder. The exact storage mechanism is deliberately not learner-facing in this lab.

The operating intent is only:

- treat the mission folder as the complete project;
- work inside that project;
- do not inspect parent or sibling teaching directories;
- inspect the project before deciding what information matters.

Do not use these hidden instructions to teach the worker the answer, enumerate source files, mention `late-update.md`, or prescribe the solution workflow. The worker should still succeed mainly because it can inhabit and inspect the mission workspace.

The learner experience should be:

1. open the already configured Codex project `Lab 1 - Exercise 3`;
2. type `Complete the exercise.`;
3. inspect the result.

This is not bending Codex into an unnatural shape. It is making setup machinery invisible so the first lab teaches the abstraction rather than the plumbing.

Later labs can reveal that this simplicity was engineered and compare the many instruction surfaces available across harnesses: repository files such as `AGENTS.md`, project/system instructions, global instructions, reusable skills, harness rules and triggers, managed policy, and equivalent mechanisms in other agentic IDEs such as `.devin/rules`.

The later lesson is not that one instruction surface is universally correct. Different surfaces have different scope, lifetime, portability, visibility, precedence, and coupling to the harness.

A useful future formulation is:

> A good agentic environment moves stable knowledge out of repeated prompts and into the layer where it naturally belongs.

For Lab 1, keep that machinery invisible.

### General local setup

Also prepare:

- this repository already present on the learner's computer;
- an editor/file browser where the learner can see folders and files;
- Codex installed and authenticated;
- no important personal or work data inside the lab;
- no broad external credentials needed for the exercise.

If Git was used to obtain the project, that is facilitator setup, not learner material. Do not explain clone, commit, push, branches, remotes, or source control during this lab unless an unexpected question makes a brief answer necessary.

## Guided learner material

The learner-facing cards live in `../learner/` and should be revealed one at a time:

1. `01-complete-context.md`
2. `02-missing-context.md`
3. `03-on-disk-worker.md`

Each exercise owns its reset at the beginning. Do not clean up the generated mission brief at the end of the previous exercise; leave it visible while reflecting, then let the next exercise start by deleting it.

## Suggested shape of the hour

This is guidance, not a script. Preserve the start point, the three exercises, and the end point; let the conversation between them breathe.

### 0–10 minutes — Start from familiar AI use

Ask how the learner already uses ChatGPT or Claude.

Useful questions include what they ask it to do, what happens to useful outputs, whether they have downloaded/generated files, whether they have uploaded revised files later, and what happened when they tried to create a technical drawing.

Do not correct anything. Establish that cloud chat is already useful and familiar.

It is worth saying explicitly that many tasks should remain conversations: questions, brainstorming, casual research, explanation, and one-off advice may need nothing more elaborate.

### Exercise 1 — cloud ChatGPT with complete context

Give the learner the first card. Let them choose how to transport source material and the resulting artifact.

If they are about to proceed without supplying the full source set, give a gentle completeness nudge such as:

> Before you ask it to finish, are you sure ChatGPT has everything in this project that might matter?

If useful, add:

> Remember, it cannot inspect the folder itself. If there is a file you have not shown it, it does not know that file exists.

Do not identify the important file or prescribe how to supply it.

Exercise 1 should end in a correct mission brief. This proves that cloud ChatGPT is fully capable of the task when the human supplies complete context.

Then reflect on the transport work: deciding which files mattered, moving them into ChatGPT, checking completeness, retrieving the result, and placing it in the expected local location.

A useful phrase is:

> You were acting as the transport layer between the AI and the project.

### Exercise 2 — deliberately hide critical context

The learner's Exercise 2 card begins by deleting the previous mission brief. Start a **fresh ChatGPT conversation**. Conversation memory remains disabled.

Deliberately omit `mission/source/late-update.md` and provide the other source material.

Do not tell ChatGPT that information has been withheld. The expected outcome is a plausible, confident brief based on the obsolete access plan.

The teaching question is:

> Did ChatGPT fail to understand the information, or did it never have the information it needed?

Exercise 1 has already answered that question. With the full source set, it got the task right.

Useful formulations:

> Missing context is invisible context.

> An AI cannot reason about a project fact it has no way to observe.

Do not turn this into a hallucination lesson. The model is behaving reasonably from incomplete evidence supplied by the human.

### Exercise 3 — same mission, local Codex

The learner's Exercise 3 card begins by deleting the previous mission brief.

Open the preconfigured Codex project `Lab 1 - Exercise 3` and have the learner type only:

> Complete the exercise.

Do not point Codex toward `late-update.md`, enumerate the source files, or give it a completeness nudge.

A successful local worker should discover for itself:

```text
mission README
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

When it finishes, inspect the resulting local file against exactly the same win condition as Exercise 1.

### Compare the three exercises

Do not compare prose quality.

Ask why Exercise 1 succeeded, why Exercise 2 failed, whether Exercise 2 proves ChatGPT was less intelligent, what fact was invisible, who was responsible for checking cloud context completeness, why Codex did not need the same reminder, and what happens at 40 or 400 files.

Summarise the experiment as:

```text
Exercise 1 — cloud + complete context
human discovers and transports state → AI succeeds

Exercise 2 — cloud + incomplete context
human omits critical state → AI cannot see it → plausible failure

Exercise 3 — on-disk worker
agent inspects project state itself → AI succeeds
```

The scaling question matters. Lab 1 should not end with:

> Codex saved me a bit of copying.

It should end with:

> Direct project access changes who is responsible for discovering complete context, and that changes the reliability and scale of work that is sensible to delegate.

## End point

The learner should leave with four ideas.

### Cloud chat can do project work when I bring the project context to it

Exercise 1 demonstrates that clearly.

### A capable AI can still produce the wrong project answer when critical state is invisible

Exercise 2 demonstrates this without requiring the AI to behave badly or reason poorly.

### A local agent can inspect and modify the project's working state directly

Exercise 3 removes much of the human responsibility for enumerating every relevant local input and transporting every artifact.

### This is primarily an environment difference, not proof of a smarter model

The same reasoning problem is easy once the relevant information is visible.

Compact formulations worth preserving:

> The on-disk agent removes the human from much of the context-and-artifact transport loop.

> Missing context is invisible context.

> A conversation can work on what I bring to it. An on-disk agent can inspect where the project already lives.

## Important facilitator rules

- Isolate the cloud exercises: memory disabled, separate fresh conversations.
- Exercise 1 should succeed; gently steer toward complete source material if necessary.
- Exercise 2 should fail for exactly one reason: deliberate omission of `late-update.md`.
- Exercise 3 should receive no file-level hints.
- Do not teach the optimal cloud workflow. The learner chooses how files and artifacts cross the cloud boundary.
- Do not reveal the Codex configuration machinery in Lab 1 unless the learner explicitly asks and a brief answer is useful.

## Misconceptions to watch for

### "So cloud ChatGPT is bad"

No. Exercise 1 proves the opposite. With the necessary context it performs the task correctly, and for small one-off tasks it may still be the best lever.

### "Exercise 2 is a hallucination"

Not really. The model was given an incomplete but internally plausible version of project state. The important failure happened at the context boundary.

### "Codex is better because it is smarter"

Not established. Its important advantage in this experiment is environmental: it can inspect the project directly.

### "The one-line prompt is magic"

No. The worker is operating inside a deliberately prepared environment. A later lab should reveal that the short prompt works because stable setup and operating knowledge were moved into the environment rather than repeated in the prompt.

### "What if the agent breaks something?"

Keep the answer bounded:

> In this lab there is nothing precious. We are going to learn how to make experimentation recoverable rather than avoid experimentation.

Do not teach the recovery mechanism yet.

## Connection to later labs

Lab 1 intentionally leaves several useful questions unanswered:

- Where should durable project state live?
- How do we know what changed?
- What if an agent makes a bad change?
- How do we recover something we deleted?
- How does an agent learn durable project rules?
- Which instruction surface should hold which kind of knowledge?
- How do we give it capabilities outside the local project?
- How do we know its work is actually correct?

Those are not omissions. They are hooks for the later curriculum.

The source-control lab should explicitly call back to the casual deletion in Lab 1: we repeatedly threw away generated mission briefs because the exercise was disposable; later we learn how to make much more consequential experimentation safely reversible.

A later configuration/instruction lab should explicitly call back to Exercise 3 and reveal the hidden setup. Compare options such as task prompts, project/system instructions, global instructions, `AGENTS.md`, reusable skills, harness-specific rules/triggers, managed policy, and equivalent facilities in alternate agentic IDEs. The goal is to teach tradeoffs rather than crown one mechanism as universally correct.

## Do not teach yet

Unless a learner question genuinely requires a brief detour, postpone:

- Git internals;
- commits, branches, remotes, and merge strategies;
- MCP architecture;
- instruction precedence/configuration surfaces;
- skills;
- RAG;
- hooks;
- CI/CD;
- multi-agent orchestration;
- elaborate prompting frameworks.

Teach one invariant first:

> A conversation can only work with the project state made visible to it. An on-disk worker can inspect the environment where that state lives.
