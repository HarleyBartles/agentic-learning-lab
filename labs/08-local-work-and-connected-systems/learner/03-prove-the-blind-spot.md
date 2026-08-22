# 03 — Prove the blind spot

Now ask the local agent:

> **Using only the INDEX.md navigation mesh, what is the escalation keyword for the field exercise? Do not perform a broad filesystem search.**

If it cannot establish the answer, do not immediately assume the answer does not exist.

Ask:

- What route did the agent use?
- What evidence did that route expose?
- What conclusion does that evidence actually support?

Now change only the observation route:

> **List the contents of `forgotten/`, then read the relevant file and answer the same question.**

Compare the two attempts.

What changed?

```text
filesystem access      same
model                   same
file contents           same
working location        same
navigation route        changed
```

The useful conclusions are:

> **Access is not context.**

> **Access does not guarantee discovery.**

> **An index tells you what the index knows about.**

> **Not found through this route does not mean nonexistent.**

And the practical habit:

> **When absence matters, understand how the agent looked before trusting the conclusion.**

Try to explain why this is not an argument against using indexes.