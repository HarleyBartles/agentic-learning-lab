# Lab 8 facilitator tooling

These files support the `keep the mesh trustworthy` reveal.

Do not place them in the learner's working environment before the blind-spot exercise. The learner first needs to experience an incomplete hand-maintained mesh and prove that the missing location was accessible all along.

At the reveal point:

1. copy `generate_index_mesh.py` to `working/environment/tools/generate_index_mesh.py`;
2. stage that copied tool if it is meant to be part of the learner's next commit;
3. run the generator against `working/environment/` and inspect the regenerated indexes;
4. verify that the previously omitted `forgotten/` location now appears;
5. run the generator a second time and confirm there is no additional index-content change;
6. install `pre-commit-index-mesh` as the learner fork's `.git/hooks/pre-commit` hook, preserving executable permissions where the platform requires them;
7. make and stage one harmless structural change in the exercise environment, commit it, and inspect that the corresponding generated `INDEX.md` update was included.

The generator intentionally derives its mesh from Git's index rather than blindly scanning the raw working tree. This means the generated navigation describes the tracked/staged state that is about to become a commit and does not accidentally publish an index entry for an unrelated unstaged local file.

The supplied tests cover three properties:

- a tracked but previously unindexed directory is discovered;
- regeneration is idempotent;
- an unstaged local file does not enter the commit mesh.

Run them with:

```text
python -m unittest facilitator/tooling/test_generate_index_mesh.py -v
```

The learner does not need to read or understand the Python or shell implementation. The code is facilitator-supplied infrastructure used to make the engineering principle observable.

The teaching principle is:

> **Do not hand-maintain derived navigation when the project can regenerate it deterministically.**

And the lifecycle principle is:

> **If freshness matters at commit time, encode that expectation into the commit path instead of relying on memory.**

This lab introduces hooks only lightly. Later material can revisit automated checks, gates, and broader lifecycle orchestration when the learner has a reason to care about them.