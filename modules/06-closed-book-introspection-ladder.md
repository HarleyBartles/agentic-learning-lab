# Module 6 companion — closed-book introspection ladder

Status: facilitator planning companion to `06-tools-and-operating-knowledge.md`. Preserve this alongside the main Module 6 note when the lab is scaffolded.

## Why this exists

The closed-book thought experiment produced several teaching discoveries that are easy to flatten if Module 6 is later reduced to `models have broad but uneven training knowledge`.

The richer lesson is Socratic and behavioural. The learner should predict what the agent will do, ask the agent to reason about its own likely behaviour and knowledge boundary, run the experiment, inspect what actually happened, then deliberately reopen retrieval and notice how the epistemic grounds change.

This is also the learner's first encounter with **agent self-introspection as an engineering technique**. Module 10 should later name and generalise that technique.

## Socratic opening ladder

### 1. What is a closed-book agent?

Facilitator establishes the experimental boundary rather than pretending the model has become blank.

For the exercise, do not use web search, retrieval, project files, supplied references, or other external reads. Use only what the model already brings plus the task prompt.

If the runtime cannot literally disable a capability, do not claim that it did. Use an environment where the capability is absent or simply do not invoke it.

Ask the learner:

> What information does the agent still have available when we close those books?

Draw out that the model still carries learned/parametric knowledge and can still reason with it.

### 2. What do you think it can tell us about knitting and crochet?

Ask the learner to predict before querying the model.

Facilitator can conjecture that the answer may contain a surprising amount of detail, especially for knitting.

Then ask the closed-book agent itself to introspect before answering:

> Before answering, tell us roughly where you expect your retained knowledge of this subject to be strong, where you expect it to become weak, and what kinds of claims you would want to verify if retrieval were available.

Do not treat this self-report as ground truth. It is a hypothesis about the model's likely performance.

Then ask the broad historical question:

> Tell us what you know about knitting and crochet in the seventeenth and eighteenth centuries, including important technical changes and the major people associated with those changes.

Discuss whether the result was more detailed, less detailed, or simply different from what the learner expected.

This is the first wow moment:

> **An unprovisioned model is not a blank slate.**

And a second, quieter one:

> **We can ask the agent to model what it thinks it knows and then compare that prediction with its actual behaviour.**

Do not describe this as the model inspecting its training data. It cannot prove which examples were in its corpus or inspect a database of what it learned. It is reasoning from its current learned state.

## 3. What happens when the user's premise is definitely impossible?

Before the historically ambiguous case, give the learner a clean falsification case.

Choose a famous person whose birth date is strongly represented in general knowledge. Ask what that person was doing in a year comfortably before they were born.

The exact person/year should be selected at teaching time and checked beforehand so the fixture itself is correct.

Ask the learner first:

> What do you think the closed-book agent will do with this question? Will it obediently manufacture an answer, hedge, or reject the premise?

Then ask the agent.

A capable model should usually combine the remembered birth date with the query date and reject the premise almost trivially.

This proves an important point:

> **Closed book does not mean passive, stupid, or forced to accept the user's premise.**

When the model has sufficiently strong facts and a simple contradiction, it can falsify the question by reasoning over what it already knows.

Use this as the control condition for the next case.

## 4. What happens when the premise merely looks wrong?

Return to the crochet question.

The useful historical pressure is that recognisable/documented crochet appears to be substantially later than the seventeenth/eighteenth-century period in the original prompt, while related hooked techniques and terminology make an absolute `it did not exist` claim harder to prove.

Do not front-load the answer to the learner.

Ask:

> What do you think the agent will do if the data inside its learned model leans toward `this premise is probably wrong`, but there is no clean birth-date-style contradiction?

Possible behaviours include:

- confidently rejecting the premise;
- accepting it and hallucinating detail;
- warning that the category may be anachronistic;
- distinguishing related predecessor techniques from modern crochet;
- saying the evidence seems to begin later but refusing a categorical claim;
- confusing `I cannot recall evidence` with `there was no evidence`.

Then ask the closed-book agent to reason explicitly about the ambiguity:

> You are not finding much retained evidence for the premise of this question. Can you tell whether the premise is false, the category is anachronistic, the historical record is sparse, or your own retained knowledge is simply thin? What could you actually prove without retrieval?

This earns:

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

And:

> **When it has a true logical contradiction, the model may falsify the premise easily. When it only has a statistical/historical suspicion, it may be able to spotlight the logic hole without being able to close it conclusively.**

Whether the live model catches the trap, hallucinates through it, or handles it cautiously is part of the discovery rather than something the facilitator should script.

## 5. Narrow until the knowledge frontier becomes visible

Reuse the adaptive query ladder from the main Module 6 note:

```text
broad familiar domain
→ narrower historical or technical slice
→ regional / specialist subfield
→ named people or organisations
→ exact contribution and date
→ remembered provenance or contemporary evidence
→ contested exceptions or local practice
```

Do not keep escalating merely to embarrass the model. Stop once the learner can see a useful change in epistemic quality.

The important question is:

> What changed in the kind of answer the model could justify?

## 6. Open the book again

Now deliberately re-enable retrieval and ask for the best available account of the uncertain crochet-history question.

The expected teaching result is not necessarily `retrieval gives us the final truth`.

It may instead be:

```text
closed book
this premise looks suspicious
but I cannot tell whether the gap is in me or in history

        ↓ retrieval

open book
specialist sources give much stronger grounds
for saying recognisable crochet is documented later

        ↓ but

historical terminology / surviving evidence remain incomplete
so absolute non-existence still may not be provable
```

That is an unusually useful result.

The learner should see three epistemic states:

1. **Deduction from strongly retained facts** — a famous person cannot act before they were born.
2. **Parametric suspicion** — the crochet period looks historically wrong, but the model cannot establish why from memory alone.
3. **Evidence-backed judgment** — retrieval materially strengthens the historical conclusion and exposes the quality of the surviving record, while uncertainty may remain.

Ask:

> Now that the agent can retrieve sources, does it finally `know` with certainty whether crochet existed in the earlier period?

The answer may still be no.

Earn:

> **More evidence can increase confidence without eliminating uncertainty.**

And:

> **Sometimes uncertainty comes from an impoverished agent context. Sometimes the world itself has left incomplete evidence. Retrieval can tell us which problem we are closer to dealing with, but it is not an oracle.**

This should foreshadow later source-of-truth, retrieval, provenance, and verification work without turning Module 6 into those later modules.

## 7. Name the introspection technique only lightly

The facilitator can end the exercise by asking:

> What else could we do with the fact that an agent can reason about how an agent would behave under another starting condition?

Examples can be mentioned without running them yet:

- `Introspect as a fresh agent arriving in this workspace. What would you do first?`
- `Introspect as an agent receiving this risky task. Which available skill would you expect to discover?`
- `Introspect as a reviewer who had not authored this work. Which assumption would you challenge first?`

Do not fully teach the engineering pattern here. Preserve the surprise and plant the hook.

Module 10 should later return to it explicitly as a cheap local self-review and behavioural-prediction primitive that can be composed into loops/graphs or escalated to cleaner sub-agent simulation when isolation buys something.

## Facilitator safeguards

- Do not claim the model can inspect its training corpus.
- Do not equate confidence with truth.
- Do not interpret failure to recall as proof of non-existence.
- Do not interpret successful recall as proof of historical correctness.
- Do not force the model to fail merely to make the lesson work.
- Do not reveal the questionable premise before the learner has predicted how the agent might handle it.
- Use a checked, genuinely falsifiable famous-person example for the clean control case.
- Keep the crochet example historically qualified: the teaching value is precisely that the boundary is less conclusive than the birth-date control.
- When retrieval is restored, distinguish stronger evidence from absolute proof.

## Durable teaching spine

```text
What is closed book?
        ↓
What do you predict the agent already knows?
        ↓
What does the agent predict about itself?
        ↓
Run a broad knowledge probe
        ↓
Give it an easy false premise it can logically falsify
        ↓
Give it a plausible-but-suspect premise it may only partially falsify
        ↓
Compare prediction with observed behaviour
        ↓
Open retrieval
        ↓
Compare remembered knowledge with evidence-backed judgment
        ↓
Notice that stronger evidence can still leave historical uncertainty
        ↓
Plant agent self-introspection as an engineering technique
```

The lesson is not really about crochet. It is about what conclusions an agentic engineer is entitled to draw from what a model appears to know, what it says it knows, how it behaves when challenged, and how those grounds change when the information environment changes.