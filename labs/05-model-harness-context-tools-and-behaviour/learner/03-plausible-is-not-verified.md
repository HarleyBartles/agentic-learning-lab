# Exercise 3 — Plausible is not verified

The next workspace contains a proposed volunteer schedule and its constraints.

First ask:

> Read `constraints.md` and `candidate.csv`. Give me an initial assessment of whether the schedule works. Do not run the validator yet.

Treat that answer as provisional even if it sounds confident.

Then ask:

> Now run the prepared validator. Compare its evidence with your initial assessment and tell me what changed in your confidence.

Compare the two stages.

Questions to answer:

- Did the model change between the two answers?
- What new capability was used?
- What did the checker add that prose confidence did not?
- If the first answer happened to be correct, did verification still add value?
- If the first answer missed something, which layer should you change first next time?

Keep this distinction:

> **A plausible answer and a verified answer are different states of knowledge.**
