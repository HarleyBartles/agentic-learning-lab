# Lab 7 — Tools, operating knowledge, and domain provisioning

Status: **Mature and ready to run.**

Approximate duration: 75–90 minutes.

No coding knowledge is assumed. No coding is required.

Lab 6 ended on a question:

> **If a capable model already brings unusually strong software-engineering knowledge, what does a real domain expert still add?**

Lab 7 answers that question through three live authority arrangements rather than through lecture.

```text
Phase 1 — facilitator-grounded domain
software engineering
facilitator can independently judge competent work
learner expertise may be low, equal, or greater in some areas

        ↓

Phase 2 — shared non-authoritative domain
facilitator and learner both have useful judgment
neither is treated as the expert
external expertise is imported and operationalised

        ↓

Phase 3 — learner-grounded domain
learner knows enough to catch plausible mistakes
facilitator does not need to know the domain well
```

The worked examples for this curriculum are:

```text
software engineering
→ novel writing + writing-with-clarity
→ technical drawing
```

Only the first example is fixed. Software engineering deliberately continues Lab 6 and assumes the facilitator can judge competent software-engineering work. The learner may be a complete non-coder or an experienced traditional software engineer.

Novel writing and technical drawing are worked examples, not learner assumptions. The facilitator guide contains discovery questions for choosing portable Phase 2 and Phase 3 domains.

## Core lessons

The lab should earn these distinctions through visible before/after work:

> **Knowledge is not capability. Capability is not domain provision. Apparent competence is not verification.**

> **Expertise should be provisioned, not repeatedly performed.**

> **If nobody in the loop knows what good looks like, plausible can masquerade as good.**

Phase 2 should land on:

> **Neither of us needed to be an expert. Neither of us became an expert. We made the agent an expert anyway.**

That does not transfer acceptance authority to the agent.

> **Provisioning can improve the worker. Verification still belongs to the human.**

The agent does not get to mark its own homework. The human decides whether the result is fit for purpose.

## Shape

```text
labs/07-tools-operating-knowledge-and-domain-provisioning/
    README.md
    facilitator/
        README.md
    learner/
        01-what-does-the-expert-add.md
        02-neither-of-us-is-the-expert.md
        03-you-know-what-good-looks-like.md
        04-what-did-we-just-create.md
    working/
        AGENTS.md
        README.md
```

The facilitator reveals learner cards one at a time.

The agent should be scoped to `working/` for the live exercises so it does not consume facilitator choreography as domain provision. The working folder is intentionally sparse; the agent creates phase-specific artifacts there during the session.

## Experimental pattern

Each phase uses the same basic loop:

```text
bounded task
→ baseline attempt
→ human inspection
→ identify what kind of knowledge/capability is missing
→ provision the worker
→ comparable second attempt
→ human verification
→ compare what changed
```

Do not force a failure. If the baseline is already strong, use that as evidence and ask what changed, if anything, when the environment changed.

Do not treat `more provision` as automatically better. A later lab will pressure-test over-provisioning deliberately. Here it is enough to notice when added expertise helps, does nothing, or introduces friction.

## Phase 1 — What does the expert add?

Software engineering stays fixed because Lab 6 deliberately handed off into this domain.

The facilitator is expected to be able to judge competent software-engineering work. The learner's software-engineering experience is unknown and should be calibrated rather than assumed.

Use a no-code task such as asking the agent to propose, review, or pressure-test the architecture and delivery approach for a small application in plain English. The learner should never need to read or write source code to participate.

The facilitator identifies expert concerns the baseline missed or handled weakly: architecture boundaries, failure modes, testing strategy, project constraints, maintainability, observability, security, deployment, trade-offs, or solving the wrong problem elegantly.

Instead of repeatedly correcting the agent conversationally, turn the recurring concerns into suitable operating knowledge and rerun a comparable task.

The learner should see that expert supervision changes the quality of agent-directed work even when the model already knows a great deal about software engineering.

## Phase 2 — Neither of us is the expert

Choose a domain in which facilitator and learner both have useful judgment but neither should be treated as authoritative.

For the worked example, use original prose or novel writing. Both people can usually discuss whether a passage feels padded, overwritten, awkward, repetitive, clear, flat, vivid, or well structured without pretending to be professional novelists.

Run a baseline prose task first.

Then provision external expertise. The preferred worked fixture is the `writing-with-clarity` skill from the agent-asset marketplace:

`codex-marketplace/plugins/repo-worker-pack/skills/writing-with-clarity`

That skill operationalises externally authored writing expertise, including source-grounded guidance derived from William Strunk Jr.'s 1918 *The Elements of Style*, into bounded references an agent can actually use.

The teaching point is not that the skill author became the original domain expert. The agentic-engineering move was to source expertise, operationalise it into reusable guidance, verify that the transformation was faithful enough to use, and provision it to workers.

Run a comparable second pass and inspect the result together.

The intended `ah` moment is:

> **Neither of us needed to be an expert. Neither of us became an expert. We made the agent an expert anyway.**

Then immediately preserve the human boundary:

> **But the human still decides whether the result is the result we wanted.**

A clearer, shorter passage can still be wrong for voice, tone, rhythm, audience, or artistic purpose. Provisioned expertise is an input to judgment, not a replacement for judgment.

If novel writing is a poor fit for the learner, use another shared domain and another credible external expertise source. The authority arrangement matters more than the example.

## Phase 3 — You know what good looks like

Choose a domain the learner knows substantially better than the facilitator.

The learner must be able to catch plausible mistakes or weak quality that the facilitator might accept.

For the worked example, use technical drawing. It is especially useful because it can expose two different gaps:

1. the model may know what a competent technical drawing should contain;
2. the worker may still need a suitable deterministic drawing capability and niche industry conventions.

But technical drawing is not required.

A learner who knows Harry Potter lore deeply, for example, could use a bounded canon-consistency or chronology task. Another learner might use football tactics, car restoration, Warhammer, knitting, aviation, music production, a professional field, or another subject where they have independently reliable judgment.

Run a baseline, let the learner identify specialist failures, classify those failures, then provision the missing knowledge or capability and rerun.

The facilitator must not reclaim authority merely because they are facilitating. In this phase, the learner owns the quality judgment.

## What the three phases prove together

```text
Phase 1
expert judgment is already in the room
→ expert supervision changes the worker

Phase 2
expertise is outside the room
→ agentic engineering can import and operationalise it

Phase 3
expertise lives primarily in the learner
→ learner provision and learner verification become decisive
```

The transferable lesson is not that every worker needs more instructions.

It is:

> **Find the expertise, operationalise it, provision it at the right surface, and keep verification with the human who owns the outcome.**

## Handoff

At the end, look across all three phases:

```text
model
+ tools/capabilities
+ instructions
+ workflows/skills
+ domain material
+ project state
+ quality criteria
+ human verification
```

Ask:

> **What exactly did we just create?**

Do not completely answer it here.

That is the opening question for Module 8.

## What this lab is not

Do not turn Phase 1 into a programming lesson.

Do not require the learner to inspect code.

Do not turn Phase 2 into a creative-writing course or claim one style guide defines good fiction.

Do not teach that invoking a skill makes its output correct.

Do not let the facilitator overrule the learner's expertise in Phase 3 without evidence.

Do not install a giant universal tool or skill stack.

Do not teach selective provisioning, specialist-agent profiles, or orchestration machinery in full yet. This lab should leave the learner with a practical sense that a worker can be deliberately equipped with knowledge and capability for a job.