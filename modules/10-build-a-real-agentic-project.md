# Module 10 — Build a real agentic project

Approximate duration: 60–75 minutes.

Status: structured planning. Treat this as a synthesis checkpoint, not as graduation from the curriculum.

## Core idea

Build something real enough that the learner can direct, inspect, refine, and verify an agent rather than merely discuss agentic concepts.

The default project is a small GitHub Pages site. It may be a personal page, an about-me page, a mini-portfolio, a showcase of interests or projects, or another small site that fits comfortably within GitHub Pages.

If the learner already has a small project they genuinely want to build, use that instead when it can support the same visible iteration loop and verification surface.

The learner does not need design skills or strong content ideas. Asking the agent to suggest structure, content, copy, and presentation is part of the exercise.

The central working loop is:

> **learner prompts -> agent proposes -> learner refines -> agent builds -> learner verifies**

The point is not that the agent gets the site right first time. The point is that the learner becomes comfortable shaping work through iterative judgment rather than manually implementing every detail.

## Why GitHub Pages is the default

A small website gives the learner:

- their first real repository that is independent of the forked learning-lab repository;
- a genuine project home they own;
- a visible artifact that is easy to inspect;
- concrete changes that can be compared across commits;
- a browser-verifiable result;
- a natural deployment boundary;
- a project that can continue to absorb later curriculum lessons.

The project should remain deliberately small. The learner is not being taught front-end development. The website is a controlled surface for learning how to direct an agentic workflow.

## Suggested session shape

### 0–10 minutes — Choose the project and create its home

First ask whether the learner already has a small project they genuinely want to build.

If yes, use it when it can support a clear propose/refine/build/verify loop.

If not, use the GitHub Pages default.

Help the learner choose a simple site purpose without requiring them to arrive with finished ideas. Useful prompts include:

- What would you be comfortable putting on a small public page?
- What would you like the page to communicate about you, your interests, or your work?
- What could the page showcase, even if the content is partly suggested by the agent?

The learner may also choose fictional or non-personal content if they do not want to publish personal information.

Once the project is chosen, create a new repository for it rather than another fork of the learning lab.

Pause there before asking the agent to fill it with work.

### 10–20 minutes — This repository is yours: decide what that means

This is the learner's first repository in the curriculum that exists because they chose to create it for their own project.

Use that moment to separate three ideas that are easy to collapse:

```text
visibility
who can see the repository

ownership
whose work this is

licence
what permission other people have to reuse it
```

Earn the distinction:

> **A public repository is not the same thing as public-domain work.**

Making work visible does not by itself express a broad permission for other people to copy, transform, redistribute, or commercialise it. A licence is the deliberate grant that answers those questions.

Do not turn this into a survey of licence families or legal trivia. Start from the learner's intent:

- Do you want other people merely to be able to see this work?
- Should they be able to copy it?
- Modify or transform it?
- Redistribute it?
- Use it commercially?
- Must they credit you?
- Does the repository contain different kinds of work that may deserve different terms?

The durable principle is:

> **Keep your work yours — or give it away, but do so deliberately.**

If the learner wants to retain the normal default rights and grant no broad reuse permission, they do not need to add an open licence merely because the repository exists.

If they do want to grant reuse rights, choose a licence because it expresses that intent.

Use simple examples rather than prescribing a universal answer:

- software may use a permissive software licence such as MIT when that matches the owner's intent;
- creative or educational material may use a content licence such as CC BY 4.0 when broad reuse with attribution is intended;
- a mixed repository can state different licences for different classes of material when that boundary is made clear.

The learning-lab repository itself is the worked example. Inspect its `LICENSE.md` and ask:

> What did the owner decide to let other people do with this repository?

Its curriculum and educational content use CC BY 4.0, while standalone software tooling uses MIT. The point is not that this is the correct answer for every repository. The point is that the rights were chosen deliberately and recorded where future humans and agents can find them.

Preserve the human authority boundary:

> **An agent can explain licence options and prepare the files. The owner decides what rights to grant.**

Record the learner's decision in the project. If the decision is `no broad reuse licence yet`, that can also be an explicit, deliberate outcome rather than an omission nobody thought about.

### 20–30 minutes — Learner prompts, agent proposes

Have the learner explain what they roughly want.

The first agent task is not immediately to build. Ask it to propose:

- the page structure;
- likely sections;
- draft content ideas;
- a visual direction;
- any assumptions it is making.

The learner should then refine the proposal in conversation.

This earns the first half of the loop:

> learner prompts -> agent proposes -> learner refines

The learner should feel free to say things such as:

- that sounds too formal;
- I do not want that section;
- make this more playful;
- I have nothing useful to say there, suggest something else;
- give me three alternatives;
- keep that idea but change the tone.

The learner is exercising judgment, not supplying implementation detail.

### 30–45 minutes — Baseline build

Once the learner is happy enough with the proposal, let the agent build the first pass.

Use a capable software-engineering model without adding specialist design guidance for the baseline.

The first pass is evidence, not failure or success.

Open the result in the browser and inspect it together.

Ask for concrete observations rather than only whether the learner likes it:

- Is the hierarchy clear?
- Is the typography appropriate?
- Is spacing consistent?
- Does the page feel balanced or cramped?
- Does the visual treatment fit the intended tone?
- Does the content scan well?
- Does it work at different viewport sizes?
- Does the page actually communicate what the learner intended?

The learner should capture what is specifically weak, strong, or merely acceptable.

## Separate software-engineering capability from design taste

Use the first pass to earn an important distinction:

> **Being very good at implementing a website is not the same thing as having strong visual taste.**

A model can be an excellent software engineer and still produce visually mediocre work.

Do not frame this as a defect in one named model. Model quality and relative strengths change over time.

The durable lesson is:

> **Different capable models can have different strengths, and domain guidance can materially change the quality of the same model's output.**

### 45–60 minutes — Add design guidance and iterate

Now hold the project and intent stable and change the worker environment.

Give the same model access to an appropriate design skill, design-system guidance, or other approved design expertise, then ask it to improve the existing site.

Keep the comparison controlled:

- same project;
- same learner intent;
- same implementation surface;
- same model where practical;
- improved design provision.

Then inspect the second result beside the first.

Ask:

- What changed in typography?
- What changed in spacing?
- What changed in hierarchy?
- What changed in layout or grouping?
- What changed in responsive behaviour?
- What changed in visual consistency?
- Which improvements can we point to concretely rather than describing as merely `better`?

This should make the effect of domain provision visible rather than mystical.

The learner should be able to say:

> We did not simply ask harder. We changed what expertise the worker had available.

### Optional — Compare models

If time and available model access make it useful, repeat a bounded design or review task with another capable model while keeping the brief and design guidance as stable as possible.

The purpose is not to crown a permanent winner.

The learner should notice that model choice itself is another engineering variable.

A useful discussion is:

- Which model was stronger at implementation?
- Which produced better visual judgment?
- Which was better at proposing content or structure?
- Did either need more steering?
- Did the design guidance narrow the gap between them?

Current facilitator examples may name contemporary models, but the curriculum should not depend on those names remaining true.

Module 10 only needs to earn the observation that model strengths differ. Later modules will examine worker profiles, harness portability, effective runtime configuration, observability, and economics in more depth.

### 60–75 minutes — Verify and decide whether to publish

The learner should now verify the result rather than accept the agent's declaration that it is done.

At minimum:

- inspect the page in the browser;
- check the major links and interactions;
- view it at more than one viewport size;
- compare the result against the learner's stated intent;
- inspect the repository diff or recent commits so the learner can see what changed.

Then decide whether to publish through GitHub Pages.

Publication is a deliberate human decision, especially if the page contains personal information.

Do not silently turn `build me a site` into `put this on the public internet`.

Now reconnect the licensing pause. These are separate decisions:

> **Should other people be able to see this?**

and:

> **If they can see it, what have I deliberately allowed them to do with it?**

A public deployment, a public repository, and a licence grant answer different questions.

The learner should recognise a natural approval boundary:

> The agent can prepare the work. The learner decides whether this result should cross the public boundary and what reuse rights, if any, accompany it.

## The real project becomes a later curriculum surface

The important outcome is not the website itself.

By the end of the module, the learner has a real repository in which they have already experienced:

- ownership of a project home independent of the learning-lab fork;
- an explicit visibility and licensing decision;
- project intent becoming durable source;
- iterative prompting and refinement;
- an agent proposing rather than merely executing;
- implementation by an on-disk worker;
- human inspection and verification;
- domain expertise changing worker output;
- model choice as an engineering variable;
- source-control evidence of successive iterations;
- a deliberate external publication boundary.

That project can now be reused when later modules introduce deeper operating patterns.

## Persistent instructions and skills should emerge from need

Lab 5 already revealed project instructions as one of the layers shaping agent behaviour.

Do not force Module 10 to create an `AGENTS.md` rule or reusable skill merely because those mechanisms exist.

If the learner repeatedly gives the same stable project guidance, ask:

> Where should this live so we stop rebuilding it in every prompt?

If a repeated instruction is genuinely stable project doctrine, it may belong in project instructions.

If a repeated activity becomes a reusable way of working, it may later belong in a skill.

Keep the existing distinction visible:

- tool/MCP = what can I do?
- skill = how should I do this kind of work?
- project instructions = what rules apply here?
- reference/domain material = what does competent work mean here?
- verification = how will we know the result is good enough?
- task = what are we doing now?

The durable rule remains:

> **Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.**

But do not accumulate guidance merely because it might be useful. Later modules will pressure-test over-provisioning and instruction scope.

## Reflect on the full system

By this point, discuss:

**model + harness + instructions + context + tools + persistent state + feedback**

Ask:

- What changed because of the learner's prompt?
- What changed because of iteration?
- What changed because of domain provision?
- What changed because of model choice?
- What evidence let the learner judge whether the change was actually better?
- Which decisions belonged to the agent, and which remained human decisions?
- Which repeated guidance deserves to become durable project knowledge?
- Which capabilities or context did this worker not need?
- Who can see this project, and what reuse rights have actually been granted?

## Signs the learning plan has worked so far

The learner does not need to know every technical term.

More useful signs are that they naturally ask:

- Can the agent propose options before it builds?
- What exactly do I dislike about this result?
- Is this an implementation problem, a design problem, a model-strength problem, or a provisioning problem?
- What changed between these two versions?
- Can I verify that rather than taking the agent's word for it?
- Should this repeated instruction become project guidance?
- Do I want other people to reuse this work, and under what terms?
- Is this ready to publish, or merely ready for me to review?

## This is a synthesis checkpoint, not the end

Do not frame this module as `you now know agentic AI`.

The learner now knows enough to direct a genuine project through a full human-agent iteration loop. That gives later curriculum somewhere real to land.

From this point onward, use both:

- bounded teaching fixtures when a controlled comparison matters;
- the learner's real project when the new operating pattern naturally belongs there.

Important later concepts still remain to be earned, including:

- agent self-introspection, local review, behavioural prediction, and test-first probes;
- autonomous human-in-the-loop lifecycle orchestration;
- specialist agent profiles and delegation;
- harness portability, effective-worker verification, observability, and current model/reasoning control surfaces;
- agent-system economics: capability, context, and inference should earn their cost;
- selective provisioning and agent overwhelm;
- context transport/materialisation, lazy/eager loading, and N+1-style repeated context work;
- finite context and retrieval/RAG;
- lightweight evaluation and TDD-inspired agent design;
- untrusted-content and capability boundaries;
- concurrent agents, isolation, integration, and re-verification.

The learning lab can increasingly become reference material without ceasing to be the source of deliberate conceptual pressure tests.
