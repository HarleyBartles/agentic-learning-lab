# Module 6 — Tools and operating knowledge

Approximate duration: 1 hour, followed by a linked learner-domain mini-project.

## Core idea

A model arrives with broad but uneven knowledge from training. That knowledge is not the same as what an agent has been deliberately equipped to know for a particular job.

A capable model with the wrong tool is badly equipped, and giving it a rich tool does not automatically teach competent use of that tool.

Keep four things distinct:

1. what useful knowledge the model appears to bring from training;
2. what capabilities and tools the agent can actually use;
3. what domain and project knowledge must be provisioned deliberately;
4. how the resulting work will be verified.

A useful distinction to earn:

> **Knowledge is not capability. Capability is not domain provision. Apparent competence is not verification.**

This module should introduce the reverse of an earlier curriculum pattern.

Earlier, the learner often does not understand the domain or implementation yet, so the agent helps the learner build understanding.

Here, once the learner is proficient in a domain, the normal direction changes:

> The learner should make enough of their domain expertise available to the agent before substantial work begins.

The learner's expertise is not only there to correct bad output afterwards. It is part of the working environment.

A useful principle:

> **Expertise should be provisioned, not repeatedly performed.**

And:

> **If nobody in the loop knows what good looks like, `good enough` is whatever the agent can plausibly approximate.**

## Teaching shape — ask, pressure, then hand over authority

The main Lab 6 should remain mostly Socratic. Use open-ended questions and cross-domain comparisons to help the learner build a model of what is true, what is merely plausible, and what can actually be verified.

The lab itself uses two main domains:

```text
1. Software engineering
Facilitator expert
→ expose uneven model knowledge and derive the role of expert supervision

2. Novel writing
shared / partial expertise
→ pressure-test the same ideas where authority is distributed
```

Do not complete the learner-authority proof inside the same hour. The natural split point comes when domain authority passes from facilitator/shared discussion to the learner.

That learner-owned proof belongs in the linked **Lab 6A mini-project — provision an agent for your specialist domain**, described later in this planning note. Technical drawing is the current intended domain for that mini-project.

## Preamble — What does the model know?

Start before software engineering with a short conversational sequence.

Ask:

> If we cut a model off from retrieval, project files, supplied references, and specialist guidance, can it still tell us about knitting?

The likely answer is yes — often in surprising detail.

It may know terminology, techniques, materials, common patterns, mistakes, and broad practice because training exposed it to substantial material about the domain.

Then increase the specificity:

> Could that same isolated model give us a trustworthy, detailed account of a genuinely obscure niche — for example the history and major players in the advancement of croquet technique in the nineteenth century?

The answer becomes much less certain.

Ask why.

Draw out that:

- training coverage is broad but uneven;
- some subjects are represented by much more material than others;
- common knowledge and niche specialist knowledge are not equally covered;
- depth can vary dramatically even within one broad domain;
- a plausible answer does not reveal the provenance, completeness, or reliability of what the model learned.

Do not teach that a model knows nothing until the human uploads documents. That is visibly false.

Do not teach that because the model can discuss a domain, it should be trusted as an expert in every corner of that domain. That is also false.

### Facilitator note — use live no-retrieval queries, not a scripted failure

When this becomes a lab, preserve the live uncertainty of the exercise. The facilitator guide should contain a small bank of no-retrieval queries and a method for making them progressively harder, not one question whose expected answer is `the model does not know`.

The point is to observe the shape of the model's retained training knowledge on the day.

A useful setup prompt is:

> For this turn, do not use web search, retrieval, tools, project files, or other reads. Answer only from what you retain from training. Be explicit about where your recall becomes uncertain rather than filling gaps with invented precision.

If the product or harness cannot actually disable a capability, use an environment where those capabilities are unavailable or simply do not invoke them. Do not claim a stronger isolation than the setup really provides.

A good first demonstration is deliberately broad enough that the model may surprise the learner:

> Tell us what you know about knitting and crochet in the seventeenth and eighteenth centuries, including important technical changes and the major people associated with those changes.

A strong model may answer with substantial detail. That is not a failed demonstration. It proves that an unprovisioned model is not a blank slate.

Then narrow the same domain until the coverage becomes visibly less secure. For example:

> Now separate mechanised stocking-frame history from hand-knitting technique. Which named practitioners or innovators changed hand-knitting practice between 1650 and 1800, what did each change, and how confident are you in each attribution?

Then:

> Pick one regional tradition from that period. Name the documented people responsible for specific technical changes, give the approximate dates, and tell us what contemporary evidence you remember for those claims.

Then:

> Which parts of your previous answer are well-attested facts you strongly recall, which are broad historical associations, and which would you want to verify before teaching them as fact?

The same narrowing pattern can be reused in other domains:

```text
broad familiar domain
→ narrower historical or technical slice
→ regional / specialist subfield
→ named people or organisations
→ exact contribution and date
→ remembered provenance or contemporary evidence
→ contested exceptions or local practice
```

Useful alternative prompts should be available in the eventual facilitator guide in case one domain happens to be unusually well represented in the model used on the day. Candidate shapes include:

- `Tell us the history and major players in the development of nineteenth-century croquet technique. Which specific tactical or technical changes are associated with which people or manuals?`
- `Choose a specialised textile or decorative craft from early modern Britain. Explain how its techniques changed across a fifty-year period, then name the people who drove those changes and the contemporary sources that establish the attribution.`
- `Take a regional craft tradition rather than the whole craft. Explain which conventions were distinctive, when they appeared, who introduced them, and how certain you are that those named attributions are historical rather than later folklore.`
- `Describe a narrow pre-industrial trade or production technique in depth. Then identify the named practitioners, workshops, or publications responsible for three specific technical changes and distinguish remembered evidence from inference.`

These are prompt *shapes*, not claims that the named domain definitely contains neat canonical innovators. That uncertainty is useful. A model may correctly challenge a premise, reveal that the history is collective rather than person-led, or say that the evidence is sparse.

### Facilitator note — absence of recall is not proof of absence

Include at least one closed-book query whose premise may itself be historically or technically wrong, anachronistic, or based on a category that did not yet exist in the period being asked about.

The knitting-and-crochet example can naturally expose this. If the model has little or no retained evidence for crochet in the seventeenth or eighteenth century, it faces several different possibilities:

- crochet as the modern named craft did not yet exist;
- related techniques existed but were described under different names;
- the historical boundary is disputed or terminologically messy;
- relevant material existed but was weakly represented in training;
- the model encountered it during training but does not reliably retain it now.

A closed-book answer usually cannot prove which of those explanations is correct merely from its own lack of recall.

Ask the model explicitly:

> You are not finding much evidence in your retained knowledge for the premise of this question. Can you tell whether the premise is false, the category is anachronistic, or your training coverage is simply thin here? What could you prove without retrieval?

Then ask the learner:

> What is the difference between `the model cannot recall evidence for X` and `X did not exist`?

This should introduce a useful epistemic boundary:

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

The reverse also matters. A model confidently recalling a claim does not prove the claim is true, current, correctly attributed, or grounded in the right source.

The eventual facilitator guide should contain one or two query shapes that deliberately test this distinction. Prefer historically plausible but uncertain premises over silly trick questions. The learner should have to reason about whether the model has encountered a real knowledge boundary, a false premise, an anachronistic category, or merely weak recall.

Do not tell the learner in advance which explanation is correct. The value is in noticing that the closed-book model cannot necessarily settle the question from inside its own parametric knowledge.

If one query produces a surprisingly detailed answer, do not argue with the model or keep escalating merely to force an embarrassing failure. Ask the learner what the result itself tells us: this model appears to carry more training knowledge in that niche than we expected. Then move one step narrower, ask for provenance, or switch to another niche.

If the model remains strong across several attempts, that is still a valid outcome. The lesson becomes that the boundary of parametric knowledge is difficult to predict from the outside. That unpredictability is itself a reason not to build project guarantees on an assumption about what the model probably knows.

The facilitator should not quietly verify answers during the no-retrieval demonstration and then feed corrections back as though they came from the model. Keep the experiment clean. Later, if useful, retrieval can be turned back on explicitly to compare remembered knowledge with authoritative sources. That comparison belongs to the verification/provenance thread, not to pretending the closed-book answer was sourced.

The facilitator guide for Lab 6 should therefore carry:

- one broad opening query likely to demonstrate surprising retained knowledge;
- at least three progressively narrower follow-ups in the same domain;
- at least two alternative niche-domain query families;
- at least one premise-challenge query where `I cannot recall evidence` must be distinguished from `the premise is false`;
- a reminder that unexpected success is evidence, not a demo failure;
- a stop rule: after a few useful probes, discuss what was observed rather than spending the session hunting for a question the model cannot answer;
- an explicit ban on judging truth from confidence or fluency alone.

Useful line to earn:

> **What the model may know from training is not the same as what this agent has been deliberately equipped to know for this job.**

Then pivot deliberately to software engineering:

> If broad model knowledge is uneven, could this same isolated model discuss deep software architecture with us?

Probably yes, often at substantial depth.

Ask:

> Why can it talk so deeply about software engineering when we were much less confident about the obscure specialist domain?

Use software as the important counterexample. Modern coding-capable models have unusually strong software knowledge relative to many specialist domains. The learner should not generalise from software and assume every field receives the same depth of base-model competence.

This makes software engineering the natural starter position for the rest of the module rather than an exception to it.

## Phase 1 — Theorize in software engineering

The facilitator is a professional software engineer and has deep domain expertise in coding. The learner is not a coder.

Do not ask the learner to judge source code they cannot yet evaluate independently. Use software to derive the principle conversationally.

A useful opening question is:

> If you and I both asked the same capable AI to build the same application, and neither of us manually wrote the code, do you think we would get the same quality of result?

The expected learner-led discovery is that the answer is probably no.

Follow with:

> If the model already knows a great deal about software engineering and neither of us is touching the keyboard, what am I contributing that you are not?

Possible answers to draw out:

- knowing what good architecture looks like;
- knowing which constraints matter;
- spotting brittle abstractions;
- recognising plausible nonsense;
- knowing what should be tested;
- understanding tradeoffs;
- knowing when a result is incomplete despite looking finished;
- knowing which compromises are acceptable;
- knowing which project-specific rules or standards cannot safely be assumed from training.

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

Do not claim that an agent cannot write competent code without a domain expert present. A strong agent may outperform a novice on many bounded tasks. Software is deliberately useful here because it shows the harder case: even where the base model already brings substantial domain knowledge, expert specification, supervision, verification, architecture, and project-specific provision can materially change the outcome.

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

## Lab 6A mini-project — provision an agent for your specialist domain

This is conceptually part of Lab 6 but should not be crammed into the same one-hour discussion lab or cause Module 7 to be renumbered.

Treat it as an intermediate mini-project or practicum between Lab 6 and Module 7.

The purpose is to turn domain authority over to the learner and ask them to prove the Lab 6 ideas in a field where they can independently judge quality.

Technical drawing is the current intended domain because the learner has real experience of asking an AI for a technical drawing and concluding that "AI can't do technical drawings."

The mini-project should interrogate that belief through the Lab 6 lens rather than accepting it at face value.

Start by asking:

> If we cut the model off from everything except its training data, could it talk to us in depth about the requirements of technical drawings?

Probably yes, in surprising depth.

That establishes:

> The model may understand a great deal about the domain while still being unable to produce the required artifact with its current capabilities.

Then ask:

> If it knows what a technical drawing should contain, why did it fail when you asked it to make one?

Use this to separate **knowledge** from **capability**. A conversational model may know projection, dimensioning, tolerances, line conventions, sections, annotation, and other general principles while still lacking an appropriate deterministic drawing/CAD/vector capability.

Give the agent an appropriate capability such as SVG/vector generation, OpenSCAD, CAD tooling, geometry libraries, rendering, or dimensional checks.

Do not stop there.

Move to the learner's niche-industry knowledge:

> Would you trust an unprovisioned model to know the peculiar diagram conventions used in your industry if that industry deliberately does something differently from the wider standard?

Probably not without evidence.

This is the specialist-domain gap the mini-project should expose.

Use a two-pass comparison.

### Pass 1 — general knowledge plus capability

Give the agent the suitable drawing capability but relatively little niche-specific provision.

Ask for a bounded drawing task.

The learner inspects the result using their own expertise.

Ask:

> Which failures come from missing capability, which come from missing general knowledge, and which come from not knowing how your industry does this differently?

Capture the missing recurring knowledge.

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

### Pass 2 — work from the provisioned specialist model

Give the agent a comparable technical-drawing task.

The learner evaluates the result.

The intended proof is learner-owned:

> I know this domain. I saw that the model already knew some of it. I saw that knowing was not the same as being able to create the artifact. I gave it the capability. I then found specialist knowledge it could not safely be assumed to know, provisioned that knowledge, and judged the improved work by standards I understand independently.

That is the practical conclusion of Lab 6.

## What Lab 6 and 6A prove together

The authority relationship changes deliberately:

```text
Software engineering
Facilitator knows what good looks like.
Learner derives the theory from that asymmetry.

Novel writing
Neither person has complete authority.
The theory survives through shared, partial knowledge.

Lab 6A specialist-domain mini-project
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

For the main Lab 6 discussion, keep tooling light. The lesson is primarily conceptual and comparative.

For Lab 6A, use:

- one deterministic technical-drawing tool;
- examples/reference artifacts in the technical-drawing domain;
- local shell/tool execution through the agent;
- project instructions or a very small skill when repeated guidance earns one;
- verification appropriate to the domain.

## Discussion prompts

- What does an isolated model appear to know already, and how confident are we about the depth of that knowledge?
- If the model cannot recall evidence for something, what would justify concluding that the thing did not exist rather than that the model simply lacks the relevant knowledge?
- How can the model distinguish a false premise from thin training coverage without external evidence?
- Why might software engineering be unusually strong relative to a niche specialist domain?
- If two people use the same model to build the same thing, why might the results differ?
- What is the domain expert contributing when they never manually perform the implementation?
- How can an agent know what `good` means for this project?
- Which repeated corrections should become persistent environment knowledge?
- What knowledge belongs in instructions, references, skills, tools, or checks?
- Can incomplete expertise from several sources still produce a substantially better environment?
- What can the model reason about but not actually do with its current tools?
- Which capabilities should this project *not* have?

## Principles

> A model arrives with broad but uneven knowledge from training.

> A model's missing memory is evidence about the model, not automatically evidence about the world.

> What the model may know is not the same as what the agent has been deliberately equipped to know for this job.

> Tool richness increases the need for operating knowledge.

> Give the worker the right tools — and teach it how to use them.

> Expertise should be provisioned, not repeatedly performed.

> If nobody in the loop knows what good looks like, plausible can masquerade as good.

## Do not teach yet

Do not install a giant universal MCP collection or a library of skills. One obvious capability plus one obvious workflow plus clearly motivated domain provision is more educational than an impressive stack the learner cannot explain.

Do not turn the coding discussion into a coding lesson or an argument about programming language syntax.

Do not turn the novel phase into a creative-writing course. Its role is to pressure-test the domain-provisioning principle in a shared, imperfect domain.

Do not turn technical drawing into a lecture from the facilitator. In Lab 6A the learner must hold domain authority.

Do not teach the learner that base-model knowledge is either absent or dependable by default. The point is to reason about what can be assumed, what must be supplied, and what needs verification.
