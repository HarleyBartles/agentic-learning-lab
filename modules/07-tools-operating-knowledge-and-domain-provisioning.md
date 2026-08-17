# Module 7 — Tools, operating knowledge, and domain provisioning

Status: structured planning. This is the practical follow-on to Module 6 and should preserve the specific facilitator/learner domains chosen for this curriculum.

Approximate duration: 1 hour, with flexibility for the learner-authority phase if the technical-drawing exercise earns more time.

## Core idea

Module 6 ends by asking why software engineering is a special case: a closed-book coding-capable model may already bring unusually deep useful knowledge of software engineering.

This module asks the next question:

> If the model already knows a great deal about a domain, what does a real domain expert still add?

Then it deliberately changes who holds domain authority across three phases:

```text
Phase 1 — software engineering
facilitator is the domain expert

        ↓

Phase 2 — novel writing
facilitator and learner share partial proficiency
neither is the domain expert

        ↓

Phase 3 — technical drawing
learner is the domain expert
```

These are not generic interchangeable examples. They are the workable domains for this facilitator and this learner. Keep that honest.

The transferable structure underneath them is:

> **facilitator domain expert → shared domain proficiency → learner domain expert**

The learner should experience the same engineering principle under three different authority arrangements rather than merely hear that it generalises.

The durable distinctions to earn are:

> **Knowledge is not capability. Capability is not domain provision. Apparent competence is not verification.**

> **Expertise should be provisioned, not repeatedly performed.**

And:

> **If nobody in the loop knows what good looks like, plausible can masquerade as good.**

## Start from Module 6's unanswered question

Open directly on the software-engineering special case.

Recall that the closed-book model could often discuss substantial software architecture, testing, debugging, APIs, databases, source control, and engineering trade-offs without us supplying reference material.

Ask:

> If the model already knows that much, what can an experienced software engineer contribute if the AI is still the one actually writing the code?

Do not make this a coding lesson. The learner does not need to judge syntax or manually implement anything.

The question is about domain authority and the operating environment around the agent.

## Phase 1 — Software engineering: facilitator domain expert

The facilitator is a professional software engineer. The learner is not a coder.

Use this asymmetry deliberately.

A useful opening question is:

> If you and I both asked the same capable AI to build the same application, and neither of us manually wrote the code, do you think we would necessarily get the same quality of result?

The likely answer is no.

Follow with:

> If the model already knows a great deal about software engineering and neither of us is touching the keyboard, what am I contributing that you are not?

Draw out things such as:

- knowing what good architecture looks like;
- knowing which constraints matter;
- spotting brittle abstractions;
- recognising plausible nonsense;
- knowing what should be tested;
- understanding trade-offs;
- knowing when a result is incomplete despite looking finished;
- knowing which compromises are acceptable;
- knowing which project-specific standards cannot safely be assumed from training;
- knowing when the agent is solving the wrong problem elegantly.

Use this to distinguish simplistic `vibe coding` from competent agent-directed coding.

```text
vibe coding
ask for a result
→ accept plausible implementation
→ little understanding or verification of how it was achieved

agent-directed coding
state the goal
→ provision the environment
→ let the agent implement
→ inspect and verify against known standards
→ question and steer
→ improve the environment when repeated corrections reveal missing operating knowledge
```

The important distinction is not:

> AI wrote the code versus a person wrote the code.

It is:

> **Did anyone in the loop know what good looked like, and was the work evaluated against that standard?**

Do not claim an agent cannot write competent code without a domain expert present. A strong model may outperform a novice on many bounded tasks.

Software is useful precisely because it is the harder case: even where the base model already carries unusually strong domain knowledge, expert specification, architecture, project conventions, verification, and supervision can materially change the result.

Earn:

> **The agent's general capability is only part of the system. The quality of domain supervision changes the quality of the outcome.**

## What exactly are we changing around the agent?

Before moving to the next domain, name the available levers without yet turning this into the later selective-provisioning module.

A domain expert may improve the agent's working environment through combinations of:

- project instructions;
- source/reference material;
- examples of good and bad work;
- standards and conventions;
- appropriate tools;
- reusable skills/workflows;
- quality criteria;
- verification checks;
- task framing and constraints;
- persistent project state.

A repeated correction should trigger:

> Is this a one-off mistake, or did we just reveal something the agent's environment should know from now on?

The goal is not to accumulate everything forever. A later module will pressure-test over-provisioning and scope.

For now, earn the simpler progression:

> **Expertise should be provisioned, not repeatedly performed.**

## Phase 2 — Novel writing: shared domain proficiency

Move completely out of software so the learner cannot dismiss the principle as something peculiar to coding.

Novel writing is deliberately a shared, incomplete domain.

The facilitator is actively learning how to write novels and how to build environments that help agents work on novels, but is not a professional novelist.

The learner is also not a professional novelist, but is an experienced reader with useful judgment about what a book should or should not feel like.

Neither person has perfect authority.

That makes the question:

> Can we materially improve agent performance when useful domain knowledge is partial and distributed rather than held by one expert?

Use an actual novel-writing task rather than discussing this only in the abstract.

Start with a relatively ordinary agent and ask it to perform a bounded piece of real novel work: a scene, revision, character interaction, outline pressure-test, or comparable task where differences can be inspected.

Observe the baseline before changing the environment.

Then progressively introduce useful operating/domain material. Depending on the actual project, this may include:

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

Run comparable work again and discuss what changed.

The comparison is not `longer prompt = better prose`.

Ask instead:

- Which intervention changed the output usefully?
- Which knowledge belongs in durable project state?
- Which belongs in reference material?
- Which is really an instruction?
- Which is a reusable workflow?
- Which is a quality criterion?
- Which is merely task-specific?
- Did anything we added fail to help or create new friction?

That last question is an intentional breadcrumb toward later selective provisioning.

### Micromanagement versus provisioning

Use the contrast explicitly.

```text
micromanagement
Agent drafts
→ "less exposition"
→ Agent redrafts
→ "that character would not say that"
→ Agent redrafts
→ "the POV drifted again"
→ Agent redrafts
→ repeat the same classes of correction
```

versus:

```text
provisioned environment
identify recurring domain knowledge
→ encode it in the appropriate project surface
→ agent begins future work with that knowledge available
→ humans discuss the actual scene/plot problem
→ inspect and refine
```

Earn:

> **Useful domain provision does not require one omniscient expert.**

And:

> **An agent can approximate quality from general training. Domain knowledge and feedback turn approximation into directed quality.**

## Phase 3 — Technical drawing: learner domain expert

Now transfer domain authority to the learner.

Technical drawing is selected because it is a real domain in which the learner can independently judge whether the output is competent and has prior experience of concluding that `AI can't do technical drawings`.

The facilitator should not abstract this away into a generic `choose any learner domain` exercise. The transfer of authority is the principle; technical drawing is the actual domain for this learner.

Open by recalling Module 6:

> If we cut the model off from everything except its training knowledge, could it probably talk in depth about the requirements of technical drawings?

Likely yes.

Then ask:

> If it knows what a technical drawing should contain, why might it still fail when asked to make one?

This separates **knowledge** from **capability**.

A conversational model may know projection, dimensioning, tolerances, line conventions, sections, annotations, and general standards while still lacking a suitable deterministic drawing/CAD/vector capability.

Give the agent an appropriate capability such as SVG/vector generation, OpenSCAD, CAD tooling, geometry libraries, rendering, or dimensional checks.

Do not stop there.

Move to the learner's niche industry/domain knowledge:

> Would you trust an unprovisioned model to know the peculiar drawing conventions used in your industry if that industry deliberately does something differently from the wider standard?

This is the specialist-domain gap the exercise should expose.

### Pass 1 — general knowledge plus suitable capability

Give the agent the drawing capability but relatively little niche-specific provision.

Ask for a bounded technical-drawing task.

The learner inspects the result using their own expertise.

Ask:

> Which failures come from missing capability, which from missing general knowledge, and which from not knowing how your industry does this differently?

The facilitator must resist becoming the authority here. The learner owns the quality judgment.

Capture recurring missing knowledge rather than merely patching the artifact line by line.

### Provision before Pass 2

Have the learner decide which recurring knowledge should become part of the agent's environment.

Possible destinations include:

- project instructions;
- source/reference material;
- known-good examples;
- a concise skill or workflow;
- tool guidance;
- verification rules;
- explicit quality criteria.

Before asking for another drawing, ask the agent to inspect the material and explain its working understanding at a reportable level:

> Before you make another drawing, inspect the project material and examples. Tell me what conventions, quality criteria, and workflow you think this project expects. Do not draw anything yet.

The learner checks that understanding and corrects it where necessary.

### Pass 2 — work from the provisioned specialist environment

Give the agent a comparable technical-drawing task.

The learner evaluates the result independently.

The intended proof belongs to the learner:

> I know this domain. I saw that the model already knew some of it. I saw that knowing was not the same as being able to create the artifact. I gave it the capability. I found specialist knowledge it could not safely be assumed to know, provisioned that knowledge, and judged the improved work by standards I understand independently.

That completes the authority transfer.

## What the three phases prove together

Make the progression explicit at the end:

```text
software engineering
Facilitator knows what good looks like.
Learner derives the theory from that asymmetry.

novel writing
Neither person has complete authority.
Useful domain provision is assembled from shared knowledge,
examples, source material, feedback, and project state.

technical drawing
Learner knows what good looks like.
Learner proves the theory from their own expertise.
```

The broad principle is:

> **When the learner does not know the domain, the agent can help the learner build understanding. When the learner does know the domain, the learner should provision that expertise into the agent's environment before expecting specialist work.**

This is not permanent training of model weights.

`Agent, learn this before we start` means something like:

- inspect the relevant domain material;
- understand the local conventions;
- use supplied examples and standards;
- adopt the project's workflow;
- use the right tools;
- expose its working understanding for correction before acting.

## Tools, workflow, domain knowledge, and quality

Keep these layers distinct:

- **Model training / prior knowledge:** What does the model appear to know already?
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

Deepen the earlier curriculum principle:

> Things you repeatedly tell the agent should eventually stop being things you repeatedly tell the agent.

Repeated domain corrections are evidence that expertise may be trapped in a human's head and being manually performed during every task.

Ask:

> Where should this knowledge live so the next task begins with it already available?

Possible answers vary by knowledge type:

- project fact → project state;
- persistent rule → project instructions;
- reusable workflow → skill;
- source convention or standard → reference material;
- quality requirement → verification/check;
- task-specific choice → current task/conversation.

Again, do not turn this into unlimited accumulation. The later selective-provisioning module exists to break that simplistic interpretation once it has been useful.

## Transition — what did we just create?

End by looking back across all three phases.

The learner has now seen combinations of:

```text
model
+ tools/capabilities
+ instructions
+ workflow
+ domain material
+ project state
+ quality criteria
+ verification
```

produce a worker that is materially better suited to a particular job.

Ask:

> **What exactly did we just create?**

Do not answer completely here.

That is the opening question for Module 8.

## Principles

> **Knowledge is not capability. Capability is not domain provision. Apparent competence is not verification.**

> **Expertise should be provisioned, not repeatedly performed.**

> **If nobody in the loop knows what good looks like, plausible can masquerade as good.**

> **Useful domain provision does not require one omniscient expert.**

> **The quality of domain supervision changes the quality of the outcome even when the model already knows a great deal.**

> **Repeated correction is often evidence that durable operating knowledge is missing.**

## Do not teach yet

Do not turn the software phase into a programming lesson.

Do not turn the novel phase into a creative-writing course. Its role is to pressure-test provisioning under shared partial authority.

Do not let the facilitator reclaim authority during technical drawing. The learner must be the person who knows what competent work looks like.

Do not install a giant universal tool/skill stack. Use only capabilities and operating knowledge that the three exercises genuinely earn.

Do not teach that base-model knowledge is either absent or dependable by default. Module 6 already established the uncertainty of retained knowledge; this module is about engineering the environment around that reality.

Do not prematurely explain specialist profiles/sub-agents or selective-context machinery. The learner should first leave with the useful working intuition that they have provisioned a worker for a job.