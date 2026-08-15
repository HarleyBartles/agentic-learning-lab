# Labs

This directory is for deliberately disposable exercises.

Nothing here should be precious. The point is to create situations where the learner can make changes, inspect them, break things, and recover safely.

Suggested exercises:

- `01-break-a-file/` — make a bad edit and restore it.
- `02-break-five-files/` — make a broad multi-file change and inspect the diff.
- `03-delete-something/` — delete tracked content and recover it.
- `04-bad-agent-refactor/` — give an agent an overly broad instruction, inspect the result, and undo it.
- `05-bad-commit/` — commit a mistake and recover from the commit.
- `06-published-mistake/` — later, push a harmless bad commit to the shared remote and recover.

The exercises should be introduced conversationally rather than treated as homework.

## Recovery habit

When something surprising happens:

1. stop;
2. inspect state;
3. understand the diff;
4. decide what to keep;
5. restore or revert what is wrong.

The lab should reinforce that experimentation is safe when the blast radius is controlled and a recovery path exists.
