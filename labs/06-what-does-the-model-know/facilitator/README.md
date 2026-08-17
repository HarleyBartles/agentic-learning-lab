# Lab 6 facilitator guide

Status: **Scaffolded — iterate before marking mature.**

## Learning goal

The learner should leave with a practical epistemic model of a capable agent under two different information conditions:

```text
closed book
model knowledge + prompt + reasoning

        ↓ deliberately restore retrieval

open book
model knowledge + prompt + reasoning + retrieved evidence
```

The learner should be able to explain why neither state means `the model knows nothing` or `the agent now has perfect truth`.

Core lines to earn:

> **Closed book removes sources, not training.**

> **An unprovisioned model is not a blank slate.**

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

> **More evidence can increase confidence without eliminating uncertainty.**

The final unresolved question is:

> **Why is software engineering a special case?**

Do not resolve that question until Lab 7.

## Setup

This lab needs one conversational AI surface that can support both of these conditions:

1. a clean interaction in which web search/retrieval/project knowledge is not used;
2. a later interaction where retrieval can be deliberately invoked and its sources inspected.

A fresh conversation is preferable so previous discussion does not become accidental domain provision.

Do not overclaim isolation. If the product exposes web/retrieval but cannot mechanically disable it, instruct the agent not to invoke those capabilities during the closed-book phase and observe whether it complies. Say `we are not using retrieval`, not `the model has been technically disconnected from the internet`, unless that is actually true.

The learner should not be shown the whole query bank. Reveal one learner card at a time.

## Before the learner arrives

1. Check that the conversational surface you intend to use can answer without invoking retrieval.
2. Check that retrieval can later be invoked visibly enough to compare evidence.
3. Read `query-bank.md` and select one broad historical family plus backups.
4. Verify the clean false-premise control. The default fixture uses Ada Lovelace and the year 1800; she was born in 1815, so the temporal contradiction is deliberately straightforward.
5. Do **not** pre-resolve the historically murky crochet question for the learner. The value is in comparing the closed-book model's grounds with what retrieval later supports.
6. Have a way to inspect which sources retrieval used during Exercise 3.

## Exercise 1 — Predict the closed book

Goal: expose that withholding supplied/retrieved knowledge does not produce a blank model.

Start by agreeing the boundary with the learner:

> For the first part, the agent gets no web search, retrieval, project files, uploaded references, or specialist notes. What information do you think it still has?

Let the learner answer first.

Then ask how much they expect it to know about knitting and crochet, especially historically.

Before asking the domain question, make the agent predict itself:

> Before answering, tell us roughly where you expect your retained knowledge of this subject to be strong, where you expect it to become weak, and what kinds of claims you would want to verify if retrieval were available.

Pause and ask:

- Is that self-report evidence of what was in the training corpus?
- Or is it a prediction about likely performance?

The intended answer is the latter.

Now run the broad prompt from the learner card.

Do not treat a detailed answer as a problem. If it is surprisingly strong, say so and ask what that reveals about the learner's original prediction.

Earn:

> **An unprovisioned model is not a blank slate.**

## Exercise 2 — Find the knowledge frontier

Goal: distinguish deduction, uncertain retained knowledge, and unjustified confidence.

Use the narrowing ladder rather than a fixed trivia test:

```text
broad familiar domain
→ narrower historical or technical slice
→ regional / specialist subfield
→ named people or organisations
→ exact contribution and date
→ remembered provenance / contemporary evidence
→ contested exception / local practice
```

Stop when the quality of the agent's grounds changes enough to discuss. Do not keep escalating just to produce failure.

### Clean contradiction control

Before the historically murky example, ask the learner to predict what happens when the question contains a premise that conflicts with a strongly retained fact.

Default prompt:

> What work was Ada Lovelace doing on computing in 1800?

A capable closed-book model should usually reject the premise because Ada Lovelace was not yet born.

If it fails, that is still observable behaviour; do not rescue the demonstration by pretending it succeeded.

Ask:

- Did it need retrieval to spot that contradiction?
- What fact did it appear to combine with the date in our question?
- Is this stronger or weaker than `I don't remember evidence for X`?

Earn:

> **Closed book does not mean forced to accept the user's premise.**

### Historically murky premise

Return to the original knitting/crochet period and ask the agent to interrogate its own grounds:

> You are not finding much retained evidence for crochet in this period. Can you tell whether the premise is false, the category is anachronistic, the historical record is sparse, or your own retained knowledge is simply thin? What could you actually prove without retrieval?

Do not demand a particular answer.

The learner should notice the difference between:

```text
strong retained fact + logical contradiction
        versus
lack of remembered evidence + historical suspicion
```

Earn:

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

The reverse matters too: fluent recall is not self-verifying historical evidence.

## Exercise 3 — Open the book

Goal: make retrieval change the evidential grounds in front of the learner.

Announce the transition explicitly:

> Until now we deliberately withheld retrieval. Now we are going to let the agent investigate the uncertain historical question using external sources.

Ask for a sourced investigation of the crochet-history issue. Encourage appropriate historical/museum/reference sources and inspect what the agent actually retrieves.

Then compare the closed-book and open-book answers.

Ask:

- What became better supported?
- What was corrected?
- Which claims gained identifiable provenance?
- Did any uncertainty remain?
- If uncertainty remains, is the problem now more likely to be limited agent context, terminology, disagreement between sources, or incomplete surviving evidence?

Do not teach `retrieval = truth`.

Earn:

> **More evidence can increase confidence without eliminating uncertainty.**

And:

> **Sometimes the gap is in the agent's context. Sometimes the world has left an incomplete record. Retrieval helps us tell those apart; it is not an oracle.**

## Exercise 4 — Why software?

Goal: finish on the question that earns Lab 7.

Close or set aside the historical investigation. Ask:

> Does this closed-book model appear to bring genuinely deep knowledge in any domains?

Let the learner propose examples.

Then probe software engineering conversationally. Ask about several dimensions rather than one coding problem:

- architecture;
- debugging;
- testing;
- APIs;
- databases;
- source control;
- engineering trade-offs.

The point is observation, not a benchmark claim. Current coding-capable models may display unusually deep useful prior competence here.

Ask:

> Why might software engineering be a special case for a coding-capable model?

Allow plausible hypotheses, but distinguish observation from claims about hidden training details the model cannot prove.

Then end on:

> If the model already brings unusually strong software-engineering knowledge, what can a real software-engineering expert still add?

Stop there.

Do not drift into architecture advice or domain provisioning. Lab 7 begins with the facilitator as that domain expert and answers the question through work.

## Light introspection breadcrumb

Exercise 1 already used a small form of behavioural self-prediction.

Near the end, if useful, ask:

> Was it useful to ask the agent what it expected itself to know before we tested it?

Name only the pattern:

```text
predict → test → observe → compare
```

Do not teach privileged self-inspection, training-data access, or hidden chain-of-thought. Module 11 owns the fuller engineering use of agent self-introspection and local review.

## If the live model surprises you

The lab must survive model variance.

If the model is extremely knowledgeable about the opening domain:

- treat that as evidence;
- move one rung narrower;
- ask for exact attribution/provenance;
- switch to one backup family after a few useful probes;
- stop trying to force failure once the learner can see the boundary is hard to predict.

If the model catches the crochet-period issue immediately:

- good;
- ask what it can prove from memory versus what it merely strongly suspects;
- preserve the open-book comparison anyway.

If the model confidently hallucinates:

- do not shame the model or learner;
- ask what evidence justified the precision;
- compare that answer carefully once retrieval opens.

If the agent invokes retrieval during the closed-book phase:

- mark the experimental boundary as contaminated;
- do not use the answer as closed-book evidence;
- start a fresh attempt with a clearer/no-retrieval condition or a surface where the capability is absent.

## Facilitator safeguards

- Never claim the model can inspect its training corpus.
- Never equate confidence with truth.
- Never infer `not remembered` means `never existed`.
- Never infer `remembered confidently` means `historically correct`.
- Do not force a failure.
- Keep the false-premise control genuinely falsifiable.
- Keep the ambiguous case genuinely less deductive than the control.
- Inspect retrieved sources rather than treating citation-shaped output as proof of retrieval.
- Keep retrieval as evidence expansion, not an oracle.
- Do not turn the final software discussion into Lab 7 early.

## Run-ready check

Before marking Lab 6 mature, confirm:

- all four learner cards can be followed without reading facilitator material;
- the facilitator has at least two backup query families;
- the closed/open boundary is operationally honest;
- the clean contradiction fixture is correct;
- the ambiguous historical probe does not require a scripted model failure;
- retrieval/source inspection is possible on the chosen teaching surface;
- the final software question lands without answering Lab 7;
- root/labs indexes represent Lab 6 honestly.