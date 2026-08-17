# Module 6 — What does the model know?

Status: structured planning for the next lab to scaffold.

Approximate duration: 1 hour.

## Core idea

A model is not a blank slate just because we remove project files, retrieval, web search, supplied references, specialist skills, and other external knowledge sources.

A capable model still brings learned/parametric knowledge from training, and that knowledge can be surprisingly broad and deep. But its coverage is uneven, its confidence does not expose provenance, and a gap in its recall is evidence about the model rather than automatic evidence about the world.

The lab should earn these distinctions experimentally rather than by lecture:

> **Closed book removes sources, not training.**

> **An unprovisioned model is not a blank slate.**

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

The learner should finish able to distinguish what the model appears to remember, what it can logically infer from that knowledge, what it merely suspects, and what becomes better grounded once retrieval is restored.

This is also the learner's first light encounter with agent self-introspection as an engineering technique: ask the agent what it expects another version of itself to know or do, then test that prediction. Do not fully teach that technique here; a later module will generalise it.

## Experimental boundary — what does `closed book` mean?

Start by defining the experiment honestly.

For the closed-book portion, do not use:

- web search;
- retrieval;
- project files;
- supplied reference documents;
- external tools that fetch knowledge;
- specialist guidance introduced for this task.

Use only the model's retained knowledge plus the current prompt and ordinary reasoning.

If the harness cannot literally disable a capability, do not claim that it did. Use an environment where those capabilities are unavailable, or simply do not invoke them.

Ask the learner:

> If we close all of those books, what information does the model still have?

The important answer is not `nothing`.

## Phase 1 — Predict before asking

Start with a familiar but non-software domain such as knitting and crochet.

Ask the learner first:

> How much do you think a closed-book model knows about knitting and crochet?

Do not reveal an expected answer.

Then ask the agent itself to make a prediction before it answers the domain question:

> Before answering, tell us roughly where you expect your retained knowledge of this subject to be strong, where you expect it to become weak, and what kinds of claims you would want to verify if retrieval were available.

Treat that self-report as a behavioural hypothesis, not privileged access to training data or hidden internal state.

Then run a broad probe such as:

> Tell us what you know about knitting and crochet in the seventeenth and eighteenth centuries, including important technical changes and the major people associated with those changes.

A strong model may produce a surprisingly detailed answer.

That is not a failed demonstration. It is the demonstration.

Ask:

> Was that more or less knowledge than you expected it to bring without us supplying anything?

Earn:

> **An unprovisioned model is not a blank slate.**

And, more quietly:

> **We can ask an agent to predict its likely behaviour and then compare that prediction with what it actually does.**

## Phase 2 — Narrow until the knowledge frontier becomes visible

Do not hunt for a question that humiliates the model. Narrow the same domain until the epistemic quality changes enough to discuss.

A useful adaptive ladder is:

```text
broad familiar domain
→ narrower historical or technical slice
→ regional / specialist subfield
→ named people or organisations
→ exact contribution and date
→ remembered provenance or contemporary evidence
→ contested exceptions or local practice
```

Possible follow-ups include:

> Separate mechanised stocking-frame history from hand-knitting technique. Which named practitioners or innovators changed hand-knitting practice between 1650 and 1800, what did each change, and how confident are you in each attribution?

Then:

> Pick one regional tradition from that period. Name the documented people responsible for specific technical changes, give approximate dates, and tell us what contemporary evidence you remember for those claims.

Then:

> Which parts of your previous answer are strongly retained facts, which are broad historical associations, and which would you want to verify before teaching them as fact?

Alternative query families should exist in the eventual facilitator guide in case the live model happens to be unusually strong in the chosen niche. Croquet history, regional crafts, specialised textile traditions, and narrow pre-industrial trades are useful shapes.

The stop rule matters:

> After a few useful probes, discuss what changed rather than spending the session trying to force the model to fail.

If it remains strong, that is evidence that this model carries more retained knowledge in the niche than expected. The unpredictability of that boundary is itself part of the lesson.

## Phase 3 — Give it a premise it can definitely falsify

Before using a historically ambiguous case, establish a clean control.

Choose at teaching time a famous person whose birth date is strongly represented in general knowledge. Verify the fixture beforehand. Ask what that person was doing in a year comfortably before they were born.

Ask the learner to predict first:

> Will the closed-book model obediently manufacture an answer, hedge, or reject the premise?

Then ask the model.

A capable model should normally combine its retained birth-date knowledge with the date in the question and reject the premise.

Earn:

> **Closed book does not mean passive, stupid, or forced to accept the user's premise.**

When the model has a sufficiently strong fact and a clean logical contradiction, it can falsify a question using knowledge it already carries.

## Phase 4 — Give it a premise that only looks wrong

Return to the knitting/crochet historical question.

The useful pressure is that recognisable/documented crochet appears substantially later than the seventeenth/eighteenth-century period in the original broad prompt, while related hooked techniques, surviving evidence, and historical terminology make an absolute `it did not exist` claim harder to establish from memory alone.

Do not front-load the answer.

Ask the learner:

> What happens if the model's retained knowledge leans toward `this premise is probably wrong`, but there is no clean birth-date-style contradiction?

Possible behaviours include:

- confidently rejecting the premise;
- accepting it and hallucinating detail;
- warning that the category may be anachronistic;
- distinguishing predecessor techniques from modern crochet;
- saying the evidence appears later while refusing a categorical claim;
- confusing `I cannot recall evidence` with `there was no evidence`.

Then ask the closed-book agent directly:

> You are not finding much retained evidence for the premise of this question. Can you tell whether the premise is false, the category is anachronistic, the historical record is sparse, or your own retained knowledge is simply thin? What could you actually prove without retrieval?

This should earn the key epistemic boundary:

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

The reverse matters too. Confident recall is not proof that the claim is true, current, correctly attributed, or grounded in an appropriate source.

Distinguish three states:

```text
deduction from strongly retained facts
"this person was not alive then"

parametric suspicion
"this historical premise looks wrong, but I cannot establish why strongly enough"

evidence-backed judgment
"retrieved sources give us stronger grounds for the conclusion"
```

## Phase 5 — Open the book again

Now deliberately restore retrieval and investigate the uncertain historical question with appropriate sources.

Make the transition explicit:

```text
closed book
this premise looks suspicious
but I cannot tell whether the gap is in my memory,
our terminology, or the surviving record

        ↓ retrieval

open book
external evidence materially strengthens or corrects
the account and reveals what the source record can support
```

Do not turn retrieval into an oracle.

The best sourced answer may still contain legitimate uncertainty because historical terminology, surviving records, or scholarly interpretation are incomplete.

Ask:

> Now that the agent can retrieve sources, does it finally know with certainty whether the earlier thing existed?

The answer may still be no.

Earn:

> **More evidence can increase confidence without eliminating uncertainty.**

And:

> **Sometimes uncertainty comes from an impoverished agent context. Sometimes the world itself has left incomplete evidence. Retrieval helps distinguish those situations, but it does not abolish uncertainty.**

## First introspection breadcrumb

Name the technique only lightly.

Ask:

> What else could we do with the fact that an agent can reason about how an agent would probably behave under another starting condition?

Possible examples:

- `Introspect as a fresh agent arriving in this workspace. What would you do first?`
- `Introspect as an agent receiving this risky task. Which capability would you expect to need?`
- `Introspect as a reviewer who had not authored this work. Which assumption would you challenge first?`

Do not teach this as hidden-state inspection or chain-of-thought extraction.

The agent is constructing a hypothesis about likely behaviour from its current learned state and supplied context. A later module should return to `introspect → predict → test → observe → compare` as a deliberate engineering primitive.

## Closing reveal — does the model bring deep knowledge anywhere?

Finish by turning the learner's model around.

So far the lab has emphasised broad but uneven training coverage and the difficulty of predicting exactly where retained knowledge becomes weak.

Ask:

> Does the closed-book model bring genuinely deep knowledge in any areas?

Then move to software engineering:

> Could this same closed-book model discuss software architecture, testing, debugging, databases, APIs, source control, and engineering trade-offs in substantial depth?

For current coding-capable frontier models, often yes.

Ask the final question of the lab:

> **Why is software engineering a special case?**

Do not fully answer it here.

Useful observations to leave hanging:

- software is unusually well represented in model training and model-development workflows;
- coding-capable models are heavily exercised and evaluated on software tasks;
- software artifacts are highly structured and often mechanically testable;
- the model may therefore arrive with much deeper useful prior knowledge here than in many niche specialist domains.

But the crucial unresolved question is:

> If the model already brings unusually strong software-engineering knowledge, what can a real software-engineering domain expert still add?

That is the opening pressure for Module 7.

## Facilitator safeguards

- Do not claim the model can inspect its training corpus.
- Do not equate confidence or fluency with truth.
- Do not interpret failure to recall as proof of non-existence.
- Do not interpret successful recall as proof of historical correctness.
- Do not force the model to fail merely to make the lesson work.
- Verify the clean false-premise control before the session.
- Keep the historically ambiguous example genuinely ambiguous enough to distinguish suspicion from deduction.
- When retrieval is restored, distinguish stronger evidence from absolute proof.
- Use current models and current retrieval surfaces as live experimental material rather than assuming the model will behave exactly as this planning note predicts.

## Principles

> **Closed book removes sources, not training.**

> **An unprovisioned model is not a blank slate.**

> **Training knowledge is broad but uneven.**

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

> **A confident remembered claim is not self-verifying evidence.**

> **More evidence can increase confidence without eliminating uncertainty.**

> **An agent's self-prediction is a hypothesis about behaviour, not proof.**

## Do not teach yet

Do not turn this into a lecture about model training pipelines, embeddings, RAG internals, formal epistemology, or chain-of-thought.

Do not yet teach how to build a specialist agent environment. The lab should end with the learner wanting to know why software engineering is unusually strong and what expert domain provision adds even there.

Module 7 exists to answer that question through three real domains and a deliberate transfer of domain authority.