# Lab 7 facilitator guide

Status: **Mature and ready to run.**

## Learning goal

The learner should leave understanding that agent quality can change materially when domain expertise is deliberately provisioned into the worker's environment, even when the base model already knows a great deal.

The lab must preserve three different authority arrangements:

```text
Phase 1 — facilitator-grounded
software engineering

Phase 2 — shared non-authoritative
choose a domain both people can judge usefully

Phase 3 — learner-grounded
choose a domain the learner knows substantially better
```

The learner should be able to explain:

> **Knowledge is not capability. Capability is not domain provision. Apparent competence is not verification.**

> **Expertise should be provisioned, not repeatedly performed.**

> **Provisioning can improve the worker. Verification still belongs to the human.**

And, after Phase 2:

> **Neither of us needed to be an expert. Neither of us became an expert. We made the agent an expert anyway.**

Treat `expert` here as the learner's useful working shorthand for a worker equipped with externally sourced domain guidance. Do not imply that a skill makes the model infallible or transfers human acceptance authority to it.

## Contract

No coding knowledge is assumed. No coding is required.

Software engineering is a teaching domain, not an entry requirement.

Do not ask the learner to write code, read source code, debug syntax, or judge implementation details they do not understand. Use plain-English design, review, architecture, risk, verification, and delivery decisions.

If the learner is an experienced software engineer, do not simplify them into a novice. Use their expertise as additional evidence.

## Setup

Use one capable agent that can work in the lab's `working/` folder.

Keep facilitator and learner choreography outside the agent's working context. Point the live worker at `working/` rather than the whole lab where practical.

Before the learner arrives:

1. Confirm the agent can create plain-text artifacts in `working/`.
2. Decide on a small software-engineering task for Phase 1 that can be discussed without code.
3. Prepare the Phase 2 worked route or a portable alternative.
4. If using the writing worked example, make `writing-with-clarity` available from the agent-asset marketplace or another trusted installation route.
5. Have at least one fallback shared domain for Phase 2.
6. Do **not** preselect the learner's Phase 3 expert domain unless you already know a suitable one. The discovery conversation is part of the lab.

The preferred external skill source for the writing worked example is:

`HarleyBartles/agent-asset-marketplace`

`codex-marketplace/plugins/repo-worker-pack/skills/writing-with-clarity`

The skill operationalises writing guidance into bounded references. Its authority record traces historical source material to William Strunk Jr.'s 1918 *The Elements of Style* while treating that source as provenance rather than unquestionable modern style authority.

Do not require the learner to inspect the skill internals unless curiosity makes that useful. The important observation is that externally authored expertise was transformed into reusable operational guidance for an agent.

## Opening — reconnect to Lab 6

Start with the unresolved Lab 6 question:

> If the model already seems to know a lot about software engineering, what does a real software-engineering expert still add?

Do not answer immediately.

Explain the experiment:

> We are going to run essentially the same engineering move three times, but we will change where reliable domain judgment comes from.

## Phase 1 — facilitator-grounded software engineering

### Calibrate the learner first

Do not assume `non-coder`.

Ask briefly:

- Have you worked in software engineering before?
- If yes, what kind of work and roughly how much?
- Are there areas where you already have strong opinions about what good engineering looks like?

Route accordingly.

### If the learner has little or no software-engineering experience

Use the facilitator's expertise visibly but explain it in plain English.

A good task is:

> Design the architecture and delivery approach for a small shared household task application. Explain the major components, data storage, failure handling, testing approach, deployment assumptions, and important trade-offs. Do not write code.

Other small applications are fine. Keep the task understandable without programming knowledge.

Let the agent produce a baseline.

Then inspect it aloud. Focus on a few concrete expert concerns, for example:

- Is it solving the actual problem or overengineering it?
- Are important failure cases missing?
- Is testing treated as an afterthought?
- Are security/privacy assumptions unexplained?
- Does the architecture introduce complexity with no benefit?
- Are deployment and recovery assumptions realistic?
- Does it look complete while leaving important operational work unspecified?

The learner does not need to know the answers in advance. They are watching an expert distinguish plausible from competent.

Ask:

> If I have to repeat these same classes of correction every time, where should that knowledge live?

Turn a small number of recurring concerns into suitable operating knowledge: a brief standards note, project guidance, verification criteria, or another appropriate surface.

Ask the agent to inspect that provision before rerunning a comparable design task.

Compare the result.

### If the learner is an experienced software engineer

Use the same task, but let both people judge it.

Ask:

- Which assumptions would you challenge?
- Which standards are currently implicit in your head?
- Which choices are preference versus project requirement?
- What would you want the worker to know before it begins the next task?

Disagreement is useful. The point is not to establish the facilitator as supreme authority. The facilitator's competence is guaranteed enough to run the exercise; learner competence is variable and may be equal or stronger in specific areas.

This version should earn:

> **Traditional software-engineering expertise is not the same thing as expertise in engineering an agentic working environment.**

The agentic-engineering move is converting useful expert judgment into durable worker provision rather than manually re-performing it on every task.

### Do not teach code

If the agent offers code, ask it to keep the comparison at architecture/review level or explain its reasoning in plain English.

The learner should participate in judgment without becoming a manual implementation layer.

## Phase 2 — shared judgment, expertise outside the room

### Find a suitable shared domain

The invariant is:

> Both people can make useful quality judgments, but neither should be treated as the final domain authority.

Novel writing is the preferred worked example when both people read fiction and can discuss prose quality.

If that does not fit, ask:

- What do we both know reasonably well?
- What could we both critique even though neither of us could teach it professionally?
- Where do we share enough vocabulary to say *why* something feels weak or strong?
- What output could we compare before and after importing external guidance?

Possible alternatives include cooking plans, photography critique, film analysis, music, gardening, tabletop games, travel planning, home design, sports analysis, or another shared-interest domain.

Avoid domains where one person is secretly the clear authority; save that arrangement for Phase 3.

### Worked example — original prose and writing-with-clarity

Use an original prose task so copyright is not part of the exercise.

Example:

> Write a 400-word scene in which two old friends meet after several years apart. One of them wants to ask for help but is reluctant to admit it. Keep the scene grounded in action and dialogue rather than explaining the characters' emotions directly.

Save the baseline.

Ask both people:

- What feels padded?
- Where is the prose too abstract or vague?
- Which sentences carry weight and which merely take up space?
- Is anything repetitive?
- Does word choice fit the scene?
- Are important moments getting enough emphasis?
- Is the writing clear without becoming flat?

Do not pretend these observations make either human a professional novelist.

Now introduce the external expertise.

Use wording close to:

> Neither of us wrote this expertise. The skill author did not need to memorise or personally master *The Elements of Style*. They operationalised externally authored knowledge into guidance an agent can use, and checked enough of the source to verify that the transformation was faithful enough to trust as a working tool.

Then invoke `writing-with-clarity` and ask for a comparable revision or second passage under the same intent.

Compare concrete changes:

- sentence economy;
- unnecessary modifiers;
- directness;
- concrete versus abstract phrasing;
- word choice;
- sentence rhythm;
- paragraph flow;
- placement of emphasis;
- whether any useful texture was lost.

The `ah` moment is:

> **Neither of us needed to be an expert. Neither of us became an expert. We made the agent an expert anyway.**

Immediately ask:

> Does that mean the second version is automatically the version we want?

The answer must remain no.

A style skill can improve clarity while harming character voice, deliberate rhythm, ornament, humour, audience fit, or artistic intent.

Earn:

> **The agent does not get to mark its own homework. Human acceptance remains the final verification boundary.**

### Generalise the engineering move

Make the chain visible:

```text
external domain knowledge
→ agentic engineer sources it
→ operationalises it for agent use
→ validates the transformation enough to trust it
→ provisions it to the worker
→ agent applies it
→ human judges whether the result is fit for purpose
```

This is a tool in the agentic engineer's kitbag.

The engineer does not need to personally become expert in every domain the worker can be equipped to handle.

## Phase 3 — learner-grounded expert domain

### Discover the domain

The invariant is:

> The learner can independently catch plausible mistakes or weak quality that the facilitator might accept.

Use questions that get there quickly:

- What subject could I confidently say something wrong about and you would catch me immediately?
- What have you spent years doing, reading, watching, collecting, building, practising, or arguing about?
- What subject do people come to you for answers about?
- What could an AI produce or explain where you would know whether it was genuinely good rather than merely plausible?
- What weird convention, edge case, exception, or local practice would a generally competent AI be likely to miss?

The domain does not need to be professional.

Deep Harry Potter lore is valid if the learner can reliably identify canon errors, chronology problems, source-boundary mistakes, or plausible inventions the facilitator would miss.

Other examples include technical drawing, vehicle repair, football tactics, Warhammer, knitting, aviation, music production, a trade, a profession, a game, or a hobby with deep accumulated knowledge.

### Selection test

Choose a domain where:

- the learner can independently judge quality;
- the facilitator does not need to become the authority;
- a bounded task can be attempted twice;
- the base model can plausibly produce a reasonable first attempt;
- there is specialist knowledge, convention, workflow, or capability worth provisioning.

If the learner can only say `I like this topic` but cannot explain what competent work looks like, keep searching.

### Run the baseline

Ask the learner to define a bounded task.

Examples:

- technical drawing: produce a small drawing or drawing plan using an appropriate deterministic capability;
- lore: reconcile a chronology or explain a canon-sensitive issue with explicit source boundaries;
- vehicle repair: propose a diagnostic sequence for a bounded symptom;
- sport: analyse a tactical situation under specific constraints.

Let the agent try with general knowledge and currently available capability.

The learner evaluates.

Ask them to classify failures:

- missing general knowledge?
- missing specialist/local knowledge?
- missing tool/capability?
- missing workflow?
- wrong assumptions?
- weak verification?

### Provision before the second pass

Capture recurring knowledge rather than patching the artifact line by line.

Possible destinations:

- reference material;
- project instructions;
- examples;
- a small skill/workflow;
- tool guidance;
- quality criteria;
- verification rules.

Before the second attempt, ask the agent to report its working understanding at a useful level:

> Inspect the provisioned material. Tell us what conventions, constraints, quality criteria, and workflow you think apply. Do not perform the task yet.

The learner corrects misunderstandings.

Then rerun a comparable task.

The learner judges the result.

The facilitator should explicitly defer:

> You know this domain better than I do. What changed, and is it actually better?

### Technical drawing worked example

Technical drawing is useful when available because it cleanly separates:

```text
model knows what a technical drawing is
!=
worker has an appropriate drawing capability
!=
worker knows this learner's niche industry conventions
```

Do not force that distinction into every Phase 3 domain. If the chosen domain has no meaningful tool gap, use specialist knowledge and verification instead.

## Exercise 4 — compare the three authority arrangements

Use the final learner card to reconstruct what happened.

Ask:

- Where did domain judgment live in Phase 1?
- Where did the expertise come from in Phase 2?
- Who could independently verify Phase 3?
- Which things changed because of tools?
- Which changed because of knowledge provision?
- Which changed because of workflow?
- Which decisions could the agent make?
- Which acceptance decisions remained human?

Then show the assembled worker shape:

```text
model
+ harness
+ tools
+ instructions
+ skills/workflows
+ domain material
+ project state
+ quality criteria
+ human verification
```

Ask:

> **What exactly did we just create?**

Do not fully define agent architecture yet. Module 8 owns the immediate answer and the next question: where should this worker operate and what systems should it connect to?

## If a live comparison does not behave as expected

The lab must survive model variance.

If Phase 1 baseline is already excellent:

- say so;
- ask what expert provision would still make assumptions explicit or repeatable;
- compare whether the second result is more aligned, not merely longer.

If the writing skill produces little visible change:

- choose a deliberately padded but still reasonable baseline passage for revision;
- verify the skill actually loaded;
- inspect a few concrete sentence-level changes rather than demanding a dramatic transformation.

If the writing skill makes the prose worse:

- that is useful evidence;
- ask whether the source guidance was mismatched to the artistic goal;
- reinforce that provision does not remove human verification.

If no shared Phase 2 domain appears quickly:

- use a facilitator-prepared neutral domain where both can discuss quality from examples;
- do not burn the session searching for the perfect hobby overlap.

If the learner struggles to identify an expert Phase 3 domain:

- ask about work, hobbies, fandoms, games, family roles, collections, practical skills, and subjects they have spent years around;
- lower the bar from `professional expert` to `I would catch mistakes you would miss`.

If the learner is expert in everything the facilitator proposes for Phase 2:

- choose something else;
- preserve Phase 2 as genuinely shared and non-authoritative.

## Do not teach yet

Do not turn this into skill-authoring training. It is enough to see skill authoring as one way an agentic engineer can operationalise external expertise.

Do not teach selective context loading in depth. The writing skill's bounded references may provide a breadcrumb, but later modules own context engineering.

Do not teach specialist sub-agent profiles or orchestration.

Do not imply `more expertise` always means `better result`.

Do not transfer acceptance authority from the human to a skill, source, model, or agent.