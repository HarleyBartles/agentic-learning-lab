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
4. Compare a prepared persistent cloud workspace with the local workspace using fresh agents, prompt-time information, and persisted project artifacts.

The intellectual task is the same across the lab.

The experiment is not trying to prove that one model is smarter than another or that one environment is universally better. It is trying to expose how much the environment changes who is responsible for supplying, discovering, maintaining, transporting, and persisting project context and artifacts.

The four exercises should make these distinctions observable:

- an ordinary cloud conversation can only reason over project state that has been made available to that conversation;
- missing context is invisible context;
- an on-disk worker can inspect the environment where the local project state already lives;
- a cloud agent can also be given a persistent working environment whose project files are reusable across independent conversations;
- prompt-time context can be combined with stored project context without becoming persistent project state automatically;
- a fresh agent can discover information left by another agent when that information was written into shared workspace state.

## The mission

Use the mission workspace in:

`labs/01-chatbot-to-worker/mission/`

The learner is given a small field-recovery scenario. Several source files contain the information needed to prepare a mission brief. One later file explicitly supersedes part of the original plan.

For Exercises 1–3, the win condition is:

> A correct finished file exists locally at `labs/01-chatbot-to-worker/mission/output/mission-brief.md`.

Exercise 4 deliberately varies where the finished state is left. The cloud runs return briefs only in chat. The local run writes the brief into the mission workspace, allowing a later fresh local agent to inspect that persisted artifact.

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

Before beginning Exercise 1, disable ChatGPT conversation memory / cross-chat memory for the learner's seat in ChatGPT settings. The purpose is experimental isolation: later fresh conversations must not recover information merely because another chat previously mentioned it.

The learner should then have:

- a ChatGPT seat you control;
- ordinary cloud ChatGPT available;
- file upload/download capability available;
- a prepared ChatGPT Project for Exercise 4;
- **conversation memory / cross-conversation memory disabled for the exercise**;
- **no GitHub connector access to this learning repository**;
- no mission source files preloaded into the prepared Lab 1 Project before the learner reaches Exercise 4;
- a fresh conversation for Exercise 1;
- another fresh conversation for Exercise 2.

The point is not to cripple ChatGPT. It should work normally apart from deliberately removing hidden continuity between experimental conversations. It simply should not already inhabit, retrieve from, or remember the local project.

Exercise 2 must still use a fresh conversation even with memory disabled. We want both protections: no conversation carry-over and no cross-chat memory contamination.

For Exercise 4, configure the ChatGPT Project in advance. Project-level cross-conversation memory should be disabled as an implementer concern. The learner does not need to create or configure the Project.

The learner's meaningful setup action is to open the prepared Lab 1 Project and upload:

- `mission/README.md`;
- every file in `mission/source/`.

Do not connect that Project to GitHub or any other external system of record. It is intentionally a separately maintained cloud representation of the mission.

The cloud runs in Exercise 4 must use completely fresh chats so any continuity comes from the shared project files, not remembered conversation state.

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

Exercises 1–3 own their local output reset at the beginning. Exercise 4 includes its own cloud and local runs and explicitly controls whether new information is left only in chat or written into the workspace.

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

Let Exercise 3 create a natural provisional conclusion. The learner may reasonably feel that direct local workspace access is clearly the answer to the repeated context problem. Do not correct that feeling before Exercise 4; let the next exercise complicate it.

### Exercise 4 — persistent workspaces and what survives

Exercise 4 deliberately compares fresh cloud and local agents. Neither side should use memory from a previous conversation. Memory is not the point.

The learner opens the prepared Lab 1 ChatGPT Project and uploads the mission README plus every file in `mission/source/`. They only do this once.

#### Run A — cloud project plus prompt-time information

Start a fresh chat in the Project and ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context. The west-route footbridge is confirmed unaffected by flooding.

The result should correctly combine:

- the persistent project files;
- the new bridge confirmation supplied in this prompt.

Do not copy the result into the local mission folder and do not modify the cloud project files.

This should quietly demonstrate that project documents can be a durable baseline while prompt-time context adds information for the current task.

#### Run B — fresh cloud chat, unchanged project files

Start another completely fresh chat inside the same Project.

Do not upload or paste the sources again. Do not repeat the bridge confirmation.

Ask:

> Complete the mission brief task. Give me the finished brief in your reply. Use the project files as your source of context.

The fresh cloud chat should still reconstruct the baseline mission from the shared project files without any repeated source transport. It should not know that the west-route footbridge was confirmed unaffected, because that information existed only in Run A's prompt and reply and was never added to the shared project files.

This is important: do not describe Run B as the cloud model "forgetting." Nothing is being remembered or forgotten here. The new agent is reading the unchanged persistent workspace available to it.

#### Run C — local workspace plus the same prompt-time information

Return to the prepared local Codex project. Delete `mission/output/mission-brief.md` if it exists so this run begins without a finished brief.

Start a fresh local-agent conversation and ask:

> Complete the exercise. The west-route footbridge is confirmed unaffected by flooding.

The local worker should combine the existing project sources with the prompt-time fact and write the resulting brief to `mission/output/mission-brief.md`.

#### Run D — fresh local agent, same workspace

Start another completely fresh local-agent conversation rooted at the same mission folder.

Do not repeat the bridge confirmation.

Ask:

> What's the current plan expressed in the mission folder?

The fresh worker should discover that the west-route footbridge is confirmed unaffected because Run C wrote that information into `mission/output/mission-brief.md`.

Push this distinction strongly:

> The local agent did not remember Run C.

and:

> Neither agent remembered anything. Memory is not what produced the difference.

Run D knows because the previous worker changed persistent workspace state that the new worker can inspect.

A useful formulation is:

> The agent didn't remember. The project carried the result forward.

Be precise when unpacking that line: the project is not cognitively remembering. The previous agent persisted information into project state, and the next agent read it.

The cloud environment is not incapable of this in principle. In this specific run, Cloud A was instructed to return the answer in chat and not update the shared project documents. The local worker was operating in a workspace where its normal task contract leaves the finished artifact in the project. The point is to observe the consequence of where the result was persisted.

Then inspect the remaining human responsibility around the cloud Project:

- the learner uploaded the project material into the prepared cloud workspace;
- those files can serve many fresh cloud chats without repeated uploads;
- if the local source changes later, the cloud Project does not become fresh merely because the local project changed;
- in this setup the learner remains responsible for refreshing that cloud representation.

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
- After Exercise 3, did direct local access feel like the obvious answer?
- What did the cloud half of Exercise 4 disprove about that conclusion?
- Why could a fresh cloud chat still use all the uploaded baseline sources without another upload?
- Why did the bridge confirmation disappear from the fresh cloud run?
- Why did the fresh local agent know the bridge confirmation?
- Did either fresh agent remember the earlier conversation?
- What would happen if the local agent had only replied in chat and never written the mission brief?
- Who created and maintains the cloud Project's representation of the mission?
- What happens to these responsibilities at 40 or 400 files?

Summarise the four exercises as:

```text
Exercise 1 — ordinary cloud + complete context
human discovers and transports state → AI succeeds

Exercise 2 — ordinary cloud + incomplete context
human omits critical state → AI cannot see it → plausible failure

Exercise 3 — direct local workspace
agent inspects project state where it already lives → AI succeeds

Exercise 4 — persistent workspaces
cloud project files persist across fresh chats
prompt-only information does not become shared project state automatically
local worker writes prompt-time information into the workspace
fresh local worker discovers that persisted result
```

The scaling question matters. Lab 1 should not end with:

> Local is better than cloud.

It should end with something closer to:

> The environment changes who is responsible for discovering, carrying, maintaining, persisting, and returning project state.

## End point

The learner should leave with six ideas.

### Ordinary cloud chat can do project work when I bring the project context to it

Exercise 1 demonstrates that clearly.

### A capable AI can still produce the wrong project answer when critical state is invisible

Exercise 2 demonstrates this without requiring the AI to behave badly or reason poorly.

### A local agent can inspect and modify the project's working state directly

Exercise 3 removes much of the human responsibility for enumerating every relevant local input and transporting every artifact.

### A cloud agent can also have a persistent project environment

Exercise 4 demonstrates that uploaded project files can provide reusable baseline context to fresh cloud chats without the human re-uploading or pasting those sources into every conversation.

### Stored project context and prompt-time context can be combined

Cloud Run A demonstrates this quietly: persistent project files provide the baseline while the prompt supplies the new bridge confirmation for the current task.

### Persistent state, not agent memory, carries information into a fresh worker

Cloud Run B and local Run D provide the contrast. Neither fresh agent remembers a previous conversation. Cloud Run B sees unchanged shared project files, so it does not know the prompt-only bridge confirmation. Local Run D sees a mission brief written by Run C, so it can discover the confirmation from the workspace.

Compact formulations worth preserving:

> A conversation is not the same thing as a workspace.

> Missing context is invisible context.

> The on-disk agent removes the human from much of the context-and-artifact transport loop.

> A cloud agent can have a working environment too.

> Neither agent remembered anything. Memory is not the point.

> The agent didn't remember. The project carried the result forward.

> We stopped carrying the files into every conversation. We have not stopped carrying them between project environments.

## Important facilitator rules

- Keep conversation memory / cross-conversation memory disabled for the experimental runs.
- Exercise 1 should succeed; gently steer toward complete source material if necessary.
- Exercise 2 should fail for exactly one reason: deliberate omission of `late-update.md`.
- Exercise 3 should receive no file-level hints.
- Let Exercise 3 create the provisional feeling that direct local access may be the obvious solution; do not prematurely explain Exercise 4.
- Exercise 4 should use a prepared ChatGPT Project. Project creation and cross-conversation-memory configuration are implementer concerns, not learner work.
- The learner should personally upload the mission README and complete source set into the prepared Project so they experience project files becoming shared cloud context.
- Cloud Runs A and B must be entirely separate chats, with no conversational continuity and no source re-upload between them.
- Cloud Run A must not update the shared cloud project files with the bridge confirmation.
- Local Runs C and D must be entirely separate agent conversations rooted at the same mission workspace.
- Local Run C must leave its finished brief in `mission/output/mission-brief.md` so Run D has persisted state to inspect.
- Push the point that neither Run B nor Run D depends on agent memory. The difference is inspectable environment state.
- Do not connect Exercise 4's cloud Project to GitHub or another source system. Lab 2 earns that step.
- Do not teach source control or declare either workspace authoritative yet.
- `mission/AGENTS.md` is visible plumbing. If the learner asks, explain it briefly and defer the deeper instruction-surface lesson.

## Misconceptions to watch for

### "So cloud ChatGPT is bad"

No. Exercises 1 and 4 prove the opposite. With appropriate context and environment it performs the task correctly. Exercise 4 specifically demonstrates that persistent cloud project files can be reused across independent conversations.

### "Exercise 2 is a hallucination"

Not really. The model was given an incomplete but internally plausible version of project state. The important failure happened at the context boundary.

### "Codex is better because it remembers the sources"

No. Memory is not responsible for the result. Exercise 4 shows that cloud ChatGPT can also be given persistent project context which multiple fresh chats use independently. The local fresh agent in Run D knows the bridge status because another worker wrote it into the shared workspace, not because Codex remembered the earlier conversation.

### "Cloud Run B forgot the bridge"

No. Run B is a fresh agent with the same unchanged project files. The bridge confirmation existed only in Run A's task context and reply. It never became shared project state.

### "The cloud Project solves the transport problem completely"

No. It solves repeated context transport between conversations inside the cloud Project. In this exercise, the human still populated the cloud workspace from the local project and would still need to refresh it when the underlying local source changes.

### "The one-line prompt is magic"

No. The local worker is operating inside a deliberately prepared environment. `AGENTS.md` carries standing project instructions so they do not have to be repeated in the task prompt. A later lab should unpack that mechanism and compare it with other instruction surfaces.

### "What if the agent breaks something?"

Keep the answer bounded:

> In this lab there is nothing precious. We are going to learn how to make experimentation recoverable rather than avoid experimentation.

Do not teach the recovery mechanism yet.

## Connection to later labs

Exercise 4 creates the natural handoff into Lab 2 and quietly plants a seed for Lab 3.

At the end of Lab 1, the learner has seen both a direct local workspace and a useful persistent cloud workspace. Multiple cloud chats can share the same uploaded project context, so persistent workspace affordances are clearly not unique to local agents. The cloud workspace, however, still contains a human-maintained representation of the project.

Lab 2 can therefore ask:

> What changes if, instead of maintaining a separate copy of project context inside ChatGPT, we give the cloud agent a route to the project itself?

Exercise 4 also gives the learner an experience which Lab 3 can later name more explicitly: information supplied in a conversation is temporary unless something persists it into project state.

Do not fully teach that abstraction in Lab 1. Let the learner experience it first.

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

> A conversation is not the same thing as a workspace. Different environments change how project state reaches the agent, what gets persisted, and how completed work gets back to the project.
