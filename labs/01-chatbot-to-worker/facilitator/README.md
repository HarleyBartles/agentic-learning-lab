# Lab 1 facilitator guide — From chatbot to worker

Approximate duration: 1 hour.

Status: **locked / stable**.

## Learning goal

The first session should change one mental model and do little else.

The learner probably begins here:

> I have a task, I open ChatGPT, I explain it, it gives me something, and I take the result away.

By the end of the session, they should have experienced this alternative:

> I have a project. An agent can work inside an environment which carries project context and state, rather than every interaction beginning from an empty conversation.

The important distinction is not cloud bad, local good. It is:

> A conversation is not the same thing as a workspace.

The exercise should make that distinction visible through experience rather than explanation.

## The core experiment

Run **the same mission four times** under different environmental constraints.

1. Ordinary cloud ChatGPT with the complete source set supplied into the conversation: success.
2. Ordinary cloud ChatGPT with one critical source file deliberately omitted: plausible failure.
3. Codex operating directly inside the local mission workspace: success through direct inspection of project state.
4. Cloud ChatGPT inside a persistent ChatGPT Project whose project files were populated by the learner: success from a reusable cloud context environment.

The intellectual task is the same in all four exercises.

The experiment is not trying to prove that one model is smarter than another or that one environment is universally better. It is trying to expose how much the environment changes who is responsible for supplying, discovering, maintaining, and transporting project context and artifacts.

The four runs should make these distinctions observable:

- an ordinary cloud conversation can only reason over project state that has been made available to that conversation;
- missing context is invisible context;
- an on-disk worker can inspect the environment where the local project state already lives;
- a cloud agent can also be given a persistent working environment, but when that environment contains a separately uploaded representation of the project, the human still owns synchronization between the local project and the cloud copy.

## The mission

Use the mission workspace in:

`labs/01-chatbot-to-worker/mission/`

The learner is given a small field-recovery scenario. Several source files contain the information needed to prepare a mission brief. One later file explicitly supersedes part of the original plan.

For Exercises 1–3, the win condition is:

> A correct finished file exists locally at `labs/01-chatbot-to-worker/mission/output/mission-brief.md`.

For Exercise 4, the same intellectual result is required, but the learner asks for the finished brief in the cloud reply and deliberately does not copy it back to the local project yet. This makes the remaining artifact-transport boundary visible.

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
- ChatGPT Projects available for Exercise 4;
- **conversation memory disabled for the exercise**;
- **no GitHub connector access to this learning repository**;
- no pre-existing ChatGPT Project containing the mission source material before Exercise 4;
- a fresh conversation for Exercise 1;
- another fresh conversation for Exercise 2.

The point is not to cripple ChatGPT. It should work normally apart from deliberately removing hidden continuity between the first two experimental conversations. It simply should not already inhabit, retrieve from, or remember the local project.

Exercise 2 must still use a fresh conversation even with memory disabled. We want both protections: no conversation carry-over and no cross-chat memory contamination.

For Exercise 4, the learner deliberately creates a ChatGPT Project and uploads the mission README plus the complete source set as project files. Do not connect that Project to GitHub or any other external system of record. It is intentionally a separately maintained cloud representation of the mission.

### Local Codex environment

Prepare the learner's machine in advance so Exercise 3 does not become a lesson in configuring Codex.

Create a Codex project named:

`Lab 1 - Exercise 3`

Root that project at:

`labs/01-chatbot-to-worker/mission/`

The mission folder contains `AGENTS.md` with the standing operating instructions for the local worker.

Those instructions should stay minimal:

- treat the mission folder as the complete project;
- work inside that project;
- do not inspect parent or sibling teaching directories;
- inspect the project before deciding what information matters;
- follow the mission README;
- preserve source material unless the task explicitly requires otherwise;
- place finished work where the project requires it;
- check the result against the stated requirements before stopping.

Do not use `AGENTS.md` to teach the worker the answer, enumerate source files, mention `late-update.md`, or prescribe the solution workflow. The worker should still succeed mainly because it can inhabit and inspect the mission workspace.

The learner experience should be:

1. open the already configured Codex project `Lab 1 - Exercise 3`;
2. type `Complete the exercise.`;
3. inspect the result.

`AGENTS.md` does not need to be hidden. If the learner notices it or asks what it is, explain briefly that it contains standing instructions for how the local agent should work in this project, that it is part of the exercise plumbing, and that a later lab will examine this mechanism properly.

This is not bending Codex into an unnatural shape. It is moving stable operating knowledge out of the task prompt and into the project where it can persist.

Later labs can compare the many instruction surfaces available across harnesses: repository files such as `AGENTS.md`, project/system instructions, global instructions, reusable skills, harness rules and triggers, managed policy, and equivalent mechanisms in other agentic IDEs such as `.devin/rules`.

The later lesson is not that one instruction surface is universally correct. Different surfaces have different scope, lifetime, portability, visibility, precedence, and coupling to the harness.

A useful future formulation is:

> A good agentic environment moves stable knowledge out of repeated prompts and into the layer where it naturally belongs.

For Lab 1, use `AGENTS.md` as plumbing without turning it into the subject of the lesson.

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
4. `04-cloud-project.md`

Exercises 1–3 own their local output reset at the beginning. Leave the Exercise 3 mission brief in place while reflecting; Exercise 4 uses the same source material but produces its result in the cloud reply rather than replacing the local output.

## Suggested shape of the hour

This is guidance, not a script. Preserve the start point, the four exercises, and the end point; let the conversation between them breathe.

### 0–10 minutes — Start from familiar AI use

Ask how the learner already uses ChatGPT or Claude.

Useful questions include what they ask it to do, what happens to useful outputs, whether they have downloaded/generated files, whether they have uploaded revised files later, and what happened when they tried to create a technical drawing.

Do not correct anything. Establish that cloud chat is already useful and familiar.

It is worth saying explicitly that many tasks should remain conversations: questions, brainstorming, casual research, explanation, and one-off advice may need nothing more elaborate.

### Exercise 1 — ordinary cloud ChatGPT with complete context

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

### Exercise 2 — ordinary cloud ChatGPT with missing context

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

### Exercise 3 — direct local workspace

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

### Exercise 4 — persistent cloud workspace

Now let the learner deliberately give cloud ChatGPT an environment of its own rather than returning to an empty standalone conversation.

Have the learner create a fresh ChatGPT Project for the mission and add:

- `mission/README.md`;
- every file in `mission/source/`.

Do not upload the finished mission brief from Exercise 3.

Start a new chat inside the Project and ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context.

The result should satisfy the same mission requirements.

This run is a first-class part of the experiment. It demonstrates that a cloud agent can also operate with a persistent project environment and does not need the human to re-upload the same source material into every conversation inside that Project.

Then inspect what responsibility remains with the human:

- the learner created the cloud Project;
- the learner chose and uploaded the source material;
- if the local source changes later, the cloud Project does not become fresh merely because the local project changed;
- in this setup the learner remains responsible for refreshing that cloud representation;
- the finished brief currently exists in the cloud reply rather than the local project's output location.

Useful formulation:

> We stopped carrying the files into every conversation. We have not stopped carrying them between project environments.

Do not turn this into a source-control or source-of-truth lesson yet. Treat the local mission workspace and the ChatGPT Project as two independent project environments for now.

### Compare the four exercises

Do not compare prose quality.

Ask:

- Why did Exercise 1 succeed?
- Why did Exercise 2 fail?
- Did Exercise 2 prove the cloud model was less intelligent?
- Who was responsible for discovering and transporting context in Exercises 1 and 2?
- Why did Exercise 3 not need the same completeness reminder?
- What did Exercise 4 improve compared with ordinary standalone cloud conversations?
- Who created and maintains the cloud Project's representation of the mission?
- If a local source changes next week, which environment automatically knows about it?
- Where did each exercise leave its finished artifact?
- What happens to these responsibilities at 40 or 400 files?

Summarise the four runs as:

```text
Exercise 1 — ordinary cloud + complete context
human discovers and transports state → AI succeeds

Exercise 2 — ordinary cloud + incomplete context
human omits critical state → AI cannot see it → plausible failure

Exercise 3 — direct local workspace
agent inspects project state where it already lives → AI succeeds

Exercise 4 — persistent cloud workspace
human transports project state into a reusable cloud environment → AI succeeds across conversations without repeated uploads
```

The scaling question matters. Lab 1 should not end with:

> Local is better than cloud.

It should end with something closer to:

> The environment changes who is responsible for discovering, carrying, maintaining, and returning project state.

## End point

The learner should leave with five ideas.

### Ordinary cloud chat can do project work when I bring the project context to it

Exercise 1 demonstrates that clearly.

### A capable AI can still produce the wrong project answer when critical state is invisible

Exercise 2 demonstrates this without requiring the AI to behave badly or reason poorly.

### A local agent can inspect and modify the project's working state directly

Exercise 3 removes much of the human responsibility for enumerating every relevant local input and transporting every artifact.

### A cloud agent can also have a persistent project environment

Exercise 4 shows that project-style cloud context can remove repeated uploads between conversations and provide a useful persistent workspace.

### Persistent cloud context does not automatically synchronize separate project environments

In Exercise 4, the human is still the transport layer between the local mission workspace and the separately populated cloud Project, and remains the arbiter of whether that cloud representation is fresh.

Compact formulations worth preserving:

> A conversation is not the same thing as a workspace.

> Missing context is invisible context.

> The on-disk agent removes the human from much of the context-and-artifact transport loop.

> A cloud agent can have a working environment too.

> We stopped carrying the files into every conversation. We have not stopped carrying them between project environments.

## Important facilitator rules

- Isolate Exercises 1 and 2: memory disabled, separate fresh conversations.
- Exercise 1 should succeed; gently steer toward complete source material if necessary.
- Exercise 2 should fail for exactly one reason: deliberate omission of `late-update.md`.
- Exercise 3 should receive no file-level hints.
- Exercise 4 should use a newly created ChatGPT Project populated manually by the learner with the complete mission source set.
- Do not connect Exercise 4's cloud Project to GitHub or another source system. Lab 2 earns that step.
- Do not teach source control or declare either workspace authoritative yet.
- `mission/AGENTS.md` is visible plumbing. If the learner asks, explain it briefly and defer the deeper instruction-surface lesson.

## Misconceptions to watch for

### "So cloud ChatGPT is bad"

No. Exercises 1 and 4 prove the opposite. With appropriate context and environment it performs the task correctly. The question is how that environment obtains and maintains the project state it needs.

### "Exercise 2 is a hallucination"

Not really. The model was given an incomplete but internally plausible version of project state. The important failure happened at the context boundary.

### "Codex is better because it is smarter"

Not established. Its important difference in this experiment is environmental: it can inspect the local project directly.

### "The cloud Project solves the transport problem completely"

No. It solves repeated context transport between conversations inside the cloud Project. In this exercise, the human still populated the cloud workspace from the local project and would still need to refresh it when the underlying local source changes.

### "The one-line prompt is magic"

No. The local worker is operating inside a deliberately prepared environment. `AGENTS.md` carries standing project instructions so they do not have to be repeated in the task prompt. A later lab should unpack that mechanism and compare it with other instruction surfaces.

### "What if the agent breaks something?"

Keep the answer bounded:

> In this lab there is nothing precious. We are going to learn how to make experimentation recoverable rather than avoid experimentation.

Do not teach the recovery mechanism yet.

## Connection to later labs

Exercise 4 creates the natural handoff into Lab 2.

At the end of Lab 1, the learner has seen both a direct local workspace and a useful persistent cloud workspace. The cloud workspace, however, still contains a human-maintained representation of the project.

Lab 2 can therefore ask:

> What changes if, instead of maintaining a separate copy of project context inside ChatGPT, we give the cloud agent a route to the project itself?

That introduces connector-mediated repository access without implying that the cloud environment was previously incapable of persistent project work.

Lab 1 also intentionally leaves several later questions unanswered:

- Where should durable project state live?
- How do we know what changed?
- What if an agent makes a bad change?
- How do we recover something we deleted?
- How does an agent learn durable project rules?
- Which instruction surface should hold which kind of knowledge?
- How do we give it capabilities outside its current workspace?
- How do we know its work is actually correct?

Those are not omissions. They are hooks for the later curriculum.

The source-control lab should explicitly call back to the casual deletion in Lab 1: we repeatedly threw away generated mission briefs because the exercise was disposable; later we learn how to make much more consequential experimentation safely reversible.

A later configuration/instruction lab should explicitly call back to `mission/AGENTS.md`: the learner has already seen a project-local standing instruction file in use, even though Lab 1 did not stop to teach it. Compare that mechanism with task prompts, project/system instructions, global instructions, reusable skills, harness-specific rules/triggers, managed policy, and equivalent facilities in alternate agentic IDEs. The goal is to teach tradeoffs rather than crown one mechanism as universally correct.

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

> A conversation is not the same thing as a workspace. Different environments change how project state reaches the agent and how completed work gets back to the project.
