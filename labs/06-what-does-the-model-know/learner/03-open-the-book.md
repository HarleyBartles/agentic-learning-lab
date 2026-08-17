# Exercise 3 — Open the book

Until now we deliberately withheld external knowledge sources.

Now change that condition on purpose.

## 1. Say what is changing

Before retrieving anything, state the experiment:

```text
before
model knowledge + our prompts + reasoning

now add
retrieved external evidence
```

We are not swapping the historical question. We are changing what evidence the agent can inspect.

## 2. Investigate the uncertain question

Ask the agent to investigate the earlier crochet-history question using retrieval and to show the sources that support its account.

A useful prompt is:

> Investigate the historical status of crochet in the seventeenth and eighteenth centuries using external sources. Distinguish recognisable crochet from related predecessor techniques or changing terminology. Show which sources support the main claims and be explicit about uncertainty in the surviving record.

Let the agent retrieve.

Do not judge the answer from citations alone. Open or inspect enough of the sources to understand what they actually support.

## 3. Compare closed book with open book

Put the earlier answer beside the retrieved answer.

Ask:

- Which claims were confirmed?
- Which became more precise?
- Which were corrected?
- Which now have identifiable provenance?
- Did the agent become more cautious anywhere?
- Did any uncertainty remain after retrieval?

Try to classify the remaining uncertainty:

```text
agent-context gap
we simply had not supplied/retrieved useful evidence

terminology gap
different periods or sources use categories differently

source disagreement
good sources do not line up cleanly

historical-record gap
surviving evidence may not support an absolute answer
```

There may be more than one.

## 4. Ask what retrieval did *not* prove

Ask the agent:

> Which parts of your retrieved answer are now strongly evidenced, and which conclusions would still be too strong to claim as absolute historical fact?

Discuss:

- Did retrieval make the answer better grounded?
- Did it make every uncertainty disappear?
- Is `I found sources` the same as `the sources prove everything I said`?

Keep these lines:

> **More evidence can increase confidence without eliminating uncertainty.**

> **Sometimes the gap is in the agent's context. Sometimes the world has left an incomplete record. Retrieval helps us distinguish those situations; it is not an oracle.**

## 5. Look back at the experiment

You have now observed the same model under two knowledge conditions.

What changed?

What did not?

Was the closed-book model empty?

Was the open-book agent omniscient?

The next exercise asks whether some domains look unusually deep even before we deliberately provision them.