# Lab 10 — Build a real agentic project

Status: **Mature and ready to run.**

Approximate duration: 60–75 minutes.

No coding knowledge is assumed. No coding is required.

Lab 10 is the Course 1 synthesis project and course boundary.

## Core thesis

The learner should finish Course 1 able to take a real goal they own from vague intent to an accepted, evidence-backed result without becoming the manual implementation layer.

The central loop is:

> **learner prompts → agent proposes → learner refines → agent builds → learner verifies**

The result does not need to be technically ambitious. The learning is in owning the project, shaping the worker, judging successive results, verifying the final state, and deciding deliberately whether the result should cross a public boundary.

## Default project

The default is a small GitHub Pages site in a new repository owned by the learner.

It can be:

- a personal page;
- a mini-portfolio;
- a showcase of interests or projects;
- a fictional/non-personal page if the learner does not want to publish personal information;
- another small project the learner genuinely wants, provided it supports the same propose → refine → build → verify loop.

The website is a controlled surface, not a front-end-development lesson. The learner may ask the agent to suggest structure, copy, content, and presentation.

## Shape

```text
labs/10-build-a-real-agentic-project/
    README.md
    facilitator/
        README.md
    learner/
        01-this-project-is-mine.md
        02-shape-the-intent.md
        03-build-and-inspect.md
        04-make-one-thing-better.md
        05-prove-and-decide.md
```

There is deliberately no prepared `working/` fixture.

The working environment is the learner's new real repository. Root the worker there, not in the teaching lab.

Reveal learner cards one at a time.

## Stage 1 — This project is mine

Choose the project and create a new repository independent of the learner's fork of this curriculum.

Before the worker fills it with content, make three human decisions explicit:

```text
What are we making?
Who should be able to see it?
What reuse rights, if any, do I want to grant?
```

Keep these concepts separate:

```text
visibility
who can see the repository or published artifact

ownership
whose work this is

licence
what permission other people have to reuse it
```

Earn:

> **A public repository is not the same thing as public-domain work.**

> **Keep your work yours — or give it away, but do so deliberately.**

The agent may explain options and prepare files. The owner decides what rights to grant.

`No broad reuse licence yet` is a valid deliberate answer.

Publication is also separate from repository visibility and licensing. Do not publish personal material merely because the project is ready to build.

## Stage 2 — Shape the intent before implementation

Give the worker a rough description of what the learner wants.

Do not ask it to build immediately.

Ask for a proposal containing enough of the following to make assumptions visible:

- purpose and audience;
- page/project structure;
- likely sections or features;
- draft content ideas;
- visual or interaction direction where relevant;
- assumptions and unanswered questions.

Then refine the proposal conversationally.

The learner can say things like:

- that is too formal;
- remove that section;
- give me three alternatives;
- keep that idea but change the tone;
- I do not have content for that, suggest something else;
- this part matters more than that one.

Earn:

> **The learner supplies intent and judgment. The agent supplies implementation capability.**

The learner is not required to translate their judgment into code or implementation instructions.

## Stage 3 — Build once, then inspect

Once the direction is good enough, authorize the worker to build the first version.

The worker should review its own result before handoff.

Then inspect the artifact as a human user would. For the default website, open it in a browser.

Ask concrete questions:

- Does the result communicate what the learner intended?
- What is clearly strong?
- What is clearly weak?
- What feels merely acceptable?
- Is information easy to scan?
- Do important links/interactions work?
- Does it behave sensibly at more than one viewport size?

Do not require the learner to diagnose implementation details. Their job is to make useful observations about the result.

Earn:

> **A first implementation is evidence to judge, not a verdict.**

## Stage 4 — Make one meaningful thing better

Choose one real weakness from the learner's inspection and improve it through a controlled iteration.

If visual quality is the obvious weakness, adding appropriate design guidance or a design skill is a useful callback to Lab 7:

```text
same project
same intent
same model where practical
+
better domain provision
```

Then compare before and after concretely.

Ask what changed in the thing the learner actually wanted improved: hierarchy, spacing, tone, clarity, responsive behaviour, interaction, copy, or another relevant quality.

Earn, where domain provision was used:

> **We did not simply ask harder. We changed what expertise the worker had available.**

Do not force a design skill if the chosen project has a different natural weakness. The capstone is synthesis, not another provisioning experiment.

Do not require a model comparison. Model-strength comparisons, worker profiles, effective runtime configuration, and economics belong later.

## Stage 5 — Prove it and decide

Before accepting the work, cash Lab 9 explicitly.

Ask:

> **What source defines correct here?**

For this real project, that source will usually be the learner's approved intent, durable project decisions, and any requirements they chose to record.

Then ask:

> **What evidence would make me willing to accept this work?**

For the default site, useful evidence includes:

- browser inspection;
- important links/interactions;
- more than one viewport size;
- comparison against the approved intent;
- repository diff/history showing what changed;
- any project-specific checks the worker used.

The worker should self-check before handoff.

The learner still decides whether the evidence is sufficient.

Keep three boundaries separate:

```text
work is built
!=
work is accepted

work is accepted
!=
work is public

work is public
!=
others have broad reuse rights
```

If the learner chooses to publish, publication is an explicit human decision.

If they choose not to publish, the capstone can still be complete.

## Reflection — what system did you just operate?

Finish by asking the learner to reconstruct the major contributors to the result:

- What did the model contribute?
- What did the harness make possible?
- What project state carried forward between turns?
- What did the learner's prompts and refinement change?
- What did domain provision change, if anything?
- What evidence established success?
- Which decisions remained human decisions?
- Which repeated guidance, if any, now deserves a durable home?

Do not turn this into a terminology exam.

The Course 1 outcome is practical:

> **I can take an ambiguous real goal, give it a durable project home, shape a worker around it, direct and refine the work, verify the result against explicit authority, recover from reversible mistakes, and decide when the result is good enough to accept or publish.**

## Persistent guidance should emerge from need

Lab 5 already exposed project instructions. Lab 7 exposed skills/domain provision. Lab 8 exposed navigation and discovery.

Do not force the learner to add `AGENTS.md`, a skill, or another persistent mechanism merely to prove they know it exists.

If the learner repeats stable project guidance, ask:

> **Have you told the agent this more than once?**

Then ask where that knowledge naturally belongs.

Preserve:

> **Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.**

But do not turn that into `persist everything`. Later courses will pressure-test over-provisioning, scope, lifecycle automation, and context selection.

## Course boundary

Lab 10 is a coherent stopping point.

A learner who stops here should have a sound foundation for competent agentic engineering. They can direct, understand, provision, navigate, recover, verify, and safely accept useful agent work without needing to implement the work manually.

Course 2 starts from that competence and changes the question from:

> **How do I operate a useful agent competently?**

to:

> **How do I deliberately engineer the agent's behaviour, workflow, context, delegation, evaluation, and autonomy?**

## Do not teach yet

Do not turn Lab 10 into:

- autonomous workflow orchestration;
- lifecycle hooks or automatic gates;
- specialist-agent architecture;
- formal worker profiles;
- model-economics analysis;
- broad model benchmarking;
- selective-context/RAG engineering;
- formal evaluation or TDD-inspired agent design;
- connected-system trust/security;
- multi-agent concurrency or isolation.

Those are later-course topics. Lab 10 should demonstrate that the learner can now use the Course 1 system as a whole on something real.
