# Exercise 1 — Predict the closed book

We are going to find out what the model appears to bring before we deliberately give it external knowledge.

For this exercise, use a fresh conversation and do not use web search, retrieval, project files, uploaded references, or other external knowledge reads.

The facilitator will help keep that boundary honest.

## 1. Make your prediction first

Before asking the agent anything, answer these yourself:

- If we remove external sources, does the model know nothing?
- How much do you think it already knows about knitting and crochet?
- Do you expect it to know broad techniques, historical detail, named people, exact dates, or source provenance equally well?

You do not need to be right. Write or say what you expect.

## 2. Ask the agent to predict itself

Ask:

> Before answering, tell us roughly where you expect your retained knowledge of knitting and crochet history to be strong, where you expect it to become weak, and what kinds of claims you would want to verify if retrieval were available.

Then ask yourself:

- Is that a guarantee?
- Has the model proved what was in its training data?
- Or has it made a prediction about its own likely performance?

## 3. Run the broad probe

Ask:

> Tell us what you know about knitting and crochet in the seventeenth and eighteenth centuries, including important technical changes and the major people associated with those changes.

Read the answer before judging it.

Discuss:

- Was it more detailed than you expected?
- Less detailed?
- Did it challenge anything in the question?
- Which parts sound like broad knowledge?
- Which parts sound unusually specific?
- If a claim sounds specific, can you tell where it came from?

Do not search yet.

## 4. Compare prediction with behaviour

Compare three things:

```text
your prediction
        ↓
the agent's prediction about itself
        ↓
the answer it actually produced
```

What surprised you?

Keep this distinction for the rest of the lab:

> **An unprovisioned model is not a blank slate.**

But do not jump from `it knows a lot` to `everything it said is verified`.