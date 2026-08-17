# Lab 6 — What does the model know?

Status: **Mature and ready to run.**

Approximate duration: 60–75 minutes.

Lab 5 taught the learner to stop treating observed agent behaviour as `the model` in isolation. Lab 6 now removes most deliberately supplied knowledge and asks a narrower question:

> **What does a capable model still bring when we close the books?**

The learner uses one conversational agent as a live experimental subject. They predict what it will know, ask the agent to predict its own likely knowledge boundary, probe broad and increasingly narrow historical questions, compare a clean logical contradiction with a historically murky premise, then deliberately restore retrieval and inspect how the evidential basis changes.

The lab should earn these distinctions through observation:

> **Closed book removes sources, not training.**

> **An unprovisioned model is not a blank slate.**

> **A model's missing memory is evidence about the model, not automatically evidence about the world.**

> **More evidence can increase confidence without eliminating uncertainty.**

The final reveal asks whether the same closed-book model appears to bring unusually deep knowledge in any domain, lands on software engineering, and ends on the unresolved question:

> **Why is software engineering a special case?**

That question is the handoff into Lab 7.

## Shape

```text
labs/06-what-does-the-model-know/
    README.md
    facilitator/
        README.md
        query-bank.md
    learner/
        01-predict-the-closed-book.md
        02-test-the-knowledge-boundary.md
        03-open-the-book.md
        04-why-software.md
```

There is deliberately no `project/` or `mission/` folder. This lab is about the model's retained knowledge and the change in epistemic grounds when retrieval becomes available; adding a project workspace would introduce a knowledge source the first half is deliberately withholding.

## Experimental boundary

For the closed-book portion, use a fresh conversational context and do not use:

- web search;
- connected retrieval;
- project files;
- uploaded references;
- specialist skills or supplied domain notes;
- other external knowledge reads.

Use only what the model already brings, the conversation prompts, and ordinary reasoning.

If the chosen harness cannot literally disable a capability, do not claim that it did. The facilitator should either use a surface where retrieval can be withheld or explicitly instruct the agent not to invoke those capabilities during the closed-book phase and verify from the interaction that it did not.

When Exercise 3 begins, deliberately reopen retrieval. The transition must be visible to the learner.

## Exercises

1. `learner/01-predict-the-closed-book.md` — define the closed-book boundary, have the learner predict the model's knowledge, have the agent predict its own likely strengths and weaknesses, then run a broad historical probe.
2. `learner/02-test-the-knowledge-boundary.md` — narrow the same domain, compare a premise the model can falsify from strongly retained facts with a historically plausible-but-suspect premise, and distinguish missing recall from proof of absence.
3. `learner/03-open-the-book.md` — restore retrieval, investigate the uncertain historical question using external evidence, then compare what became better supported, what changed, and what uncertainty remains.
4. `learner/04-why-software.md` — ask whether the closed-book model brings genuinely deep knowledge anywhere, use software engineering as the observable special case, and end on what a real domain expert can still add.

The facilitator should reveal learner cards one at a time.

## What this lab is not

Do not turn the session into:

- a competition to find something the model does not know;
- a hallucination gotcha;
- a lecture about training pipelines;
- a claim that the model can inspect its training corpus;
- a historical crochet lesson;
- a benchmark of model intelligence;
- a full lesson on retrieval/RAG;
- a full lesson on agent self-introspection.

Unexpectedly strong closed-book answers are valid evidence. The learner is studying the shape and limits of the model's available grounds, not trying to embarrass it.

## Handoff

The intended final sequence is:

```text
broad but uneven retained knowledge
        ↓
closed-book uncertainty becomes visible
        ↓
retrieval changes the evidential basis
        ↓
some domains still look unusually deep without provisioning
        ↓
software engineering
        ↓
why is this a special case?
        ↓
if the model already knows a lot, what does a real expert add?
        ↓
Lab 7
```

Do not answer the final domain-provisioning question in this lab. Lab 7 should earn it through facilitator expertise, shared proficiency, and learner expertise.