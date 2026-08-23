# Lab 10 facilitator guide

Status: **Mature and ready to run.**

Approximate duration: 60–75 minutes.

## Learning goal

Lab 10 is the Course 1 synthesis project.

The learner should demonstrate that they can take a real goal they own from rough intent to an accepted, evidence-backed result by directing an agent, inspecting what it produces, refining it, and verifying the outcome.

The learner is not being tested on coding ability.

The durable participation rule remains:

> **The learner must be able to participate in the judgment loop without being required to implement the work manually.**

The central loop is:

> **learner prompts → agent proposes → learner refines → agent builds → learner verifies**

## Default project and fallback

Prefer a small GitHub Pages site in a new repository owned by the learner.

Why it works well:

- it is a genuine project independent of the curriculum fork;
- it produces a visible artifact;
- browser inspection gives immediate feedback;
- source control records iterations;
- publication is optional but meaningful;
- the project can be reused later in Course 2.

If the learner already has another genuinely small project they want, use it when it still supports proposal, implementation, inspection, iteration, and verification within the session.

Do not turn project choice into a lengthy product-design exercise.

## Before the session

Confirm the learner has:

- access to create a repository in their own GitHub account;
- a local worker/harness capable of editing that repository;
- a browser or other suitable artifact-inspection surface;
- a safe path to preview locally before any public deployment;
- no expectation that they must publish personal information.

The learner may use fictional or non-personal content.

Do not create the project in advance. Creating the project home is part of the capstone.

## Stage 1 — This project is mine

Reveal `learner/01-this-project-is-mine.md`.

Help the learner choose a small project, then create a new repository separate from the curriculum fork.

Pause before implementation.

Ask the learner to decide:

1. What are we making?
2. Who should be able to see the repository or result?
3. What reuse rights, if any, should other people receive?

Keep visibility, ownership, and licensing separate.

The learner does not need a licence taxonomy.

Useful outcomes include:

- private repository, no publication;
- public repository, no broad reuse licence;
- public repository with a deliberately chosen licence;
- private during construction with a later publication decision.

The key lines are:

> **A public repository is not the same thing as public-domain work.**

> **Keep your work yours — or give it away, but do so deliberately.**

If licensing needs explanation, the agent can explain options or inspect this curriculum repository's licensing structure as an example. The human owner makes the rights decision.

Do not silently treat repository creation as consent to public deployment.

## Stage 2 — Shape intent before implementation

Reveal `learner/02-shape-the-intent.md`.

Root the worker in the learner's new project repository.

Have the learner describe the project naturally and ask the worker to propose before building.

A useful prompt shape is:

> I want to make [rough project idea]. Do not build it yet. Propose a small first version: purpose, structure, content/features, visual or interaction direction where relevant, assumptions you are making, and anything you think I should decide before implementation.

Let the learner refine freely.

Do not rescue them by translating every reaction into implementation language.

If they say `that feels too corporate`, `I hate that section`, or `give me three alternatives`, let the worker interpret the judgment and propose changes.

The learner should experience that useful direction does not require knowing how to code the requested change.

Earn:

> **The learner supplies intent and judgment. The agent supplies implementation capability.**

## Stage 3 — Build and inspect

Reveal `learner/03-build-and-inspect.md`.

Once the direction is good enough, authorize implementation.

The worker should review its own result before handoff.

For the default website, preview locally and open it in a browser.

Ask the learner for concrete observations rather than a single `good/bad` verdict.

Useful probes:

- What is the page trying to communicate?
- Does that come across quickly?
- What is strongest?
- What is weakest?
- What feels generic or awkward?
- Are important things easy to find?
- Do links/interactions work?
- Does the layout survive a narrower viewport?

Do not require design vocabulary.

`The text feels squashed` or `I don't know where to look first` is perfectly useful evidence.

The worker's first result may already be good. Do not manufacture a failure. The stage succeeds when the learner can inspect and make a defensible judgment.

Earn:

> **A first implementation is evidence to judge, not a verdict.**

## Stage 4 — Improve one real weakness

Reveal `learner/04-make-one-thing-better.md`.

Choose one weakness the learner actually noticed.

Run one controlled improvement cycle.

If visual quality is the natural weakness, domain-provision the same worker with suitable design guidance or a design skill and keep the other major variables stable where practical.

This is a callback to Lab 7, not a new provisioning lesson.

Ask the learner to compare the before/after state concretely.

Good comparisons include:

- hierarchy;
- spacing;
- clarity;
- tone;
- layout;
- interaction;
- responsive behaviour;
- content structure.

If another project/domain has a more natural quality weakness, provision or refine for that instead.

Do not force a design skill merely because the default project is a website.

If domain provision was the intervention, earn:

> **We did not simply ask harder. We changed what expertise the worker had available.**

Do not add a second model just to create a comparison. Model selection, worker profiles, runtime state, and economics belong later.

## Stage 5 — Prove it and decide

Reveal `learner/05-prove-and-decide.md`.

Explicitly cash Lab 9.

Ask first:

> **What source defines correct here?**

The answer should be grounded in the learner's approved intent and any durable project decisions/requirements, not simply whatever the worker most recently produced.

Then ask:

> **What evidence would make me willing to accept this work?**

For the default website, verify at least:

- browser rendering;
- important links/interactions;
- more than one viewport size;
- content against the learner's approved intent;
- repository diff/history or current changed-file state;
- relevant worker self-checks.

Do not accept `done` because the worker says it confidently.

Do not reject self-verification either. It is useful evidence that should improve the handoff.

Preserve:

> **The agent should check its own work. The agent does not get to mark its own homework.**

Then ask whether the learner wants the result published.

Publication is optional.

Keep these distinctions visible:

```text
built != accepted
accepted != public
public != broadly reusable
```

If the learner chooses publication, confirm they are comfortable with the content crossing that boundary before enabling GitHub Pages or another public route.

## Reflection and Course 1 close

Do not administer a terminology quiz.

Ask the learner to explain their project in system terms using whatever vocabulary they naturally remember.

Prompts:

- What did the model contribute?
- What did the harness make possible?
- What state persisted independently of the conversation?
- What changed because you refined the proposal?
- What changed because of extra domain provision, if used?
- What evidence made you accept the result?
- Which decisions were the agent allowed to make?
- Which decisions stayed yours?
- Did you repeat any stable instruction enough that it may deserve a durable home?

A strong learner outcome sounds approximately like:

> I can give an agent a real project, make the important state durable, give it useful capabilities and expertise, steer it through results rather than writing the implementation myself, check what it actually did, and decide whether I accept or publish it.

The learner need not reproduce the exact course vocabulary.

## Persistent instructions and skills

Do not require an `AGENTS.md` or custom skill in this lab.

If repeated stable guidance naturally appears, ask whether it should become durable project guidance.

If not, leave it alone.

Course 2 will later pressure-test scope, over-provisioning, reusable procedures, workflows, and context selection.

The Course 1 rule is only:

> **Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.**

not:

> persist every useful sentence forever.

## Keep the course boundary honest

Lab 10 is a credible stopping point, not graduation from every advanced agent-system concept.

A learner stopping after Course 1 should have a substantially correct model of ordinary agentic engineering and should not require Course 2 to repair a known foundational misconception.

Course 2 can deepen and pressure-test the model through:

- agent self-introspection and local review;
- autonomous human-in-the-loop workflows;
- specialist agents and orchestration;
- harness/runtime portability and observability;
- economics;
- selective provisioning/context;
- evaluation.

Course 3 widens further into trust boundaries, concurrency, integration, and provenance.

Do not preview those as a long lecture. A short `this is where we go next` is enough.

## Do not teach yet

Do not turn Lab 10 into:

- a GitHub Pages configuration lecture;
- front-end-development training;
- a licence-family survey;
- mandatory skill creation;
- autonomous orchestration;
- lifecycle hook design;
- multi-agent delegation;
- model benchmarking;
- worker-profile design;
- RAG/context engineering;
- formal evaluation/TDD;
- prompt-injection/security training;
- concurrency/isolation.
