# Module 6 — Tools and operating knowledge

Approximate duration: 1 hour.

## Core idea

A capable model with the wrong tool is badly equipped, and giving it a rich tool does not automatically teach competent use of that tool.

Three things belong together:

1. provision the capability;
2. teach the agent how to use it well;
3. provision enough domain knowledge and quality criteria for the agent to know what good work means here.

This module should introduce the reverse of an earlier curriculum pattern.

Earlier, the learner often does not understand the domain or implementation yet, so the agent helps the learner build understanding.

Here, once the learner is proficient in a domain, the normal direction changes:

> The learner should make enough of their domain expertise available to the agent before substantial work begins.

The learner's expertise is not only there to correct bad output afterwards. It is part of the working environment.

A useful principle:

> **Expertise should be provisioned, not repeatedly performed.**

And:

> **If nobody in the loop knows what good looks like, `good enough` is whatever the agent can plausibly approximate.**

## Teaching shape — theorize, pressure, prove

Use three deliberately ordered domains whose authority relationship changes each time:

```text
1. Coding
Facilitator expert
→ theorize

2. Novel writing
shared / partial expertise
→ pressure

3. Technical drawing
Learner expert
→ prove
```

The order matters.

Do not replace the domains casually when this module is scaffolded. The authority shift is part of the teaching mechanism.

## Phase 1 — Theorize in coding

The facilitator is a professional software engineer and has deep domain expertise in coding. The learner is not a coder.

Do not ask the learner to judge source code they cannot yet evaluate independently. Use coding to derive the principle conversationally.

A useful opening question is:

> If you and I both asked an AI to build the same application, and neither of us manually wrote the code, do you think we would get the same quality of result?

The expected learner-led discovery is that the answer is probably no.

Follow with:

> If neither of us is touching the keyboard, what am I contributing that you are not?

Possible answers to draw out:

- knowing what good architecture looks like;
- knowing which constraints matter;
- spotting brittle abstractions;
- recognising plausible nonsense;
- knowing what should be tested;
- understanding tradeoffs;
- knowing when a result is incomplete despite looking finished;
- knowing which compromises are acceptable.

Use this to distinguish simplistic `vibe coding` from competent agent-directed coding.

For this curriculum, the useful contrast is:

```text
vibe coding
ask for a result
→ accept plausible implementation
→ little understanding or verification of how it was achieved

agent-directed coding
state the goal
→ provision the environment
→ let the agent implement
→ inspect and verify the work against known standards
→ question and steer
→ improve the environment when repeated corrections reveal missing operating knowledge
```

The important distinction is not:

> AI wrote the code versus a person wrote the code.

It is:

> Did anyone in the loop know what good looked like, and was the work evaluated against that standard?

Do not claim that an agent cannot write competent code without a domain expert present. A strong agent may outperform a novice on many bounded tasks. The teaching point is that domain expertise substantially improves specification, supervision, verification, architecture, and the ability to detect plausible-but-wrong work.

The theory to carry forward is:

> The agent's general capability is only part of the system. The quality of domain supervision changes the quality of the outcome.

## Phase 2 — Pressure in novel writing

Move completely out of software so the learner cannot dismiss the theory as something peculiar to coding.

Novel writing is intentionally a shared, incomplete domain rather than an expert-led one.

The facilitator is actively learning how to write novels and how to build environments that help agents work on novels, but is not a professional novelist. The learner is also not a professional novelist, but is an experienced reader and has useful judgment about what a good book should or should not feel like.

That makes this a good pressure test:

> Can we materially improve agent performance when the domain knowledge is incomplete and distributed between us?

Start with the observation that an unprovisioned model can generate novel-shaped prose. That is not the same as reliably producing the novel this project wants.

Discuss what useful domain provision might include:

- voice and prose principles;
- point-of-view rules;
- character models;
- world/canon material;
- structure conventions;
- plot state;
- pacing expectations;
- examples of acceptable prose;
- examples of recurring failure modes;
- revision workflow;
- checks for drift, repetition, exposition, weak scene purpose, or broken character logic.

The key contrast is between micromanagement and provisioning.

### Micromanagement

```text
Agent drafts
→ "less exposition"
→ Agent redrafts
→ "that character would not say that"
→ Agent redrafts
→ "the POV drifted again"
→ Agent redrafts
→ repeat the same classes of correction
```

### Provisioned environment

```text
identify recurring domain knowledge
→ encode it in project instructions, references, examples, skills, checks, or durable project state
→ Agent begins future work with that knowledge available
→ discuss the actual plot or scene problem
→ inspect and refine the result
```

A useful learner question whenever the same correction appears twice is:

> Is this a one-off mistake, or did we just reveal something the agent's environment should know from now on?

This phase should demonstrate that domain knowledge does not have to live in one perfect expert. It can be assembled from partial expertise, examples, standards, source material, tools, feedback, and shared judgment.

Useful line to earn:

> **An agent can approximate quality from general training. Domain knowledge and feedback turn approximation into directed quality.**

## Phase 3 — Prove in technical drawing

Now give the learner domain authority.

The learner understands technical drawings. The facilitator does not.

This is where the theory becomes something the learner can prove from their own judgment rather than borrowing the facilitator's authority.

Use the learner's real previous failure mode: asking ChatGPT for a technical drawing and getting an image-generation workflow.

The exercise should not merely be:

> give the agent a better drawing tool.

The stronger question is:

> What does this agent need to understand about technical drawings before you would trust it to do this work competently?

Use a two-pass comparison.

### Pass 1 — capability without enough domain provision

Give the agent an appropriate deterministic drawing capability, such as SVG/vector generation, OpenSCAD, CAD tooling, geometry libraries, rendering, or dimensional checks.

Ask for a bounded drawing task with relatively little domain-specific instruction.

The learner inspects the result using their own expertise.

Ask:

> What does this agent not understand about technical drawings that is obvious to you?

Capture the missing knowledge.

This may include conventions, required information, representation choices, dimensioning expectations, tolerances, layout, readability, verification, or workflow.

### Provision before the second attempt

Do not merely patch the first artifact with a sequence of corrections.

Have the learner decide which recurring knowledge should become part of the agent's environment.

Possible destinations include:

- project instructions;
- source/reference material;
- known-good examples;
- a concise skill or workflow;
- tool guidance;
- verification rules;
- explicit quality criteria.

Then ask the agent to inspect that material and explain its working model before making the second drawing.

A useful prompt direction is:

> Before you make another drawing, inspect the project material and examples. Tell me what conventions, quality criteria, and workflow you think this project expects. Do not draw anything yet.

The learner checks that understanding and corrects it where necessary.

### Pass 2 — work from the provisioned domain model

Give the agent a comparable technical-drawing task.

The learner evaluates the result.

The intended proof is learner-owned:

> I know this domain. I saw the agent misunderstand it. I changed what the agent knew and how it was equipped before it worked. The resulting work was materially better by standards I can independently judge.

That is the conclusion of the three-domain progression.

## What the three phases prove together

The authority relationship changes deliberately:

```text
Coding
Facilitator knows what good looks like.
Learner derives the theory from that asymmetry.

Novel writing
Neither person has complete authority.
The theory survives through shared, partial knowledge.

Technical drawing
Learner knows what good looks like.
Learner proves the theory from their own expertise.
```

The broad principle is:

> **When the learner does not know the domain, the agent can help the learner build understanding. When the learner does know the domain, the learner should provision that expertise into the agent's environment before expecting specialist work.**

This should not be framed as permanently training the model's weights. `Agent, learn this before we start` means:

- inspect the relevant domain material;
- understand the local conventions;
- use the supplied examples and standards;
- adopt the project's workflow;
- use the right tools;
- expose its working understanding for correction before acting.

## Tools, workflow, domain knowledge, and quality

Keep these layers distinct:

- **Tool or MCP:** What can I do?
- **Skill:** How should I do this kind of work?
- **Project instructions:** What rules apply here?
- **Domain material:** What does competent work mean in this domain and project?
- **Verification:** How will we know whether the work is actually good enough?
- **Task:** What are we trying to accomplish now?

A tool gives the agent leverage.

A skill gives it a workflow.

Domain provision gives it a local model of competent work.

Verification tests whether that model produced the right result.

## Connection to persistent instructions

This module should deepen an earlier curriculum principle:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

Here the principle is not merely about prompt convenience.

Repeated domain corrections are evidence that expertise is trapped in the learner's head and being performed manually during every task.

The agentic response is to ask:

> Where should this knowledge live so the next task begins with it already available?

Possible answers vary by knowledge type:

- project fact -> project state;
- persistent rule -> project instructions;
- reusable workflow -> skill;
- source convention or standard -> reference material;
- quality requirement -> verification/check;
- task-specific choice -> current conversation.

The goal is to move from continuous expert micromanagement toward a competent working environment.

## Tools to experiment with

- one deterministic technical-drawing tool;
- examples/reference artifacts in the technical-drawing domain;
- local shell/tool execution through the agent;
- project instructions or a very small skill when repeated guidance earns one;
- verification appropriate to the domain;
- optionally one rich MCP such as GitHub later in the module if it still serves the lesson.

## Discussion prompts

- If two people use the same model to build the same thing, why might the results differ?
- What is the domain expert contributing when they never manually perform the implementation?
- How can an agent know what `good` means for this project?
- Which repeated corrections should become persistent environment knowledge?
- What knowledge belongs in instructions, references, skills, tools, or checks?
- Can incomplete expertise from several sources still produce a substantially better environment?
- What can the model reason about but not actually do with its current tools?
- Which tool is the right lever for this artifact?
- Which capabilities should this project *not* have?

## Principles

> Tool richness increases the need for operating knowledge.

> Give the worker the right tools — and teach it how to use them.

> Expertise should be provisioned, not repeatedly performed.

> If nobody in the loop knows what good looks like, plausible can masquerade as good.

## Do not teach yet

Do not install a giant universal MCP collection or a library of skills. One obvious capability plus one obvious workflow plus clearly motivated domain provision is more educational than an impressive stack the learner cannot explain.

Do not turn the coding discussion into a coding lesson or an argument about programming language syntax.

Do not turn the novel phase into a creative-writing course. Its role is to pressure-test the domain-provisioning principle in a shared, imperfect domain.

Do not turn technical drawing into a lecture from the facilitator. The learner must hold domain authority in the proof phase.
