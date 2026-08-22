# 04 — Check before repair

Recall the Lab 8 mesh generator.

Suppose you want to know whether the navigation mesh is currently stale.

Which operation should happen first?

```text
--check
or
--apply
```

Talk it through before running anything.

The useful sequence is:

```text
check
→ establish the current state

repair deliberately
→ change the state

check again
→ establish the resulting state
```

If you repair first, you may erase the evidence that the thing was wrong before you inspected it.

Earn:

> **A verifier should not silently repair the thing it is supposed to verify.**

And:

> **Inspect first. Mutate deliberately. Verify the resulting state.**

Do not solve the `who remembers to run the check every time?` problem here. That is a later workflow lesson.