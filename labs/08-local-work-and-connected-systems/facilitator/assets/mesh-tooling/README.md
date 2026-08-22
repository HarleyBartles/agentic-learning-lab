# Lab 8 facilitator mesh tooling

These files are facilitator-owned reveal assets. Keep them outside the learner worker's root until Exercise 4.

They are not prerequisites for the learner and are not a coding exercise.

## Files

- `generate_index_mesh.py` — deterministic index generator with explicit `--check` and `--apply` modes.
- `test_generate_index_mesh.py` — executable contract tests for stale detection, regeneration, idempotence, and ignoring untracked local drafts.
- `pre-commit-check` — check-only hook policy; blocks a commit when generated indexes are stale.
- `pre-commit-apply` — apply-and-stage policy; explicitly regenerates and stages only the generated `INDEX.md` files reported by the tool.

## Tool contract

The generator follows a deliberate safety shape:

```text
--check
non-mutating
exit 0 when current
exit non-zero and name stale generated surfaces when drift exists

--apply
explicit mutation
write the deterministic generated surfaces
print only the paths it owns/wrote
```

The mesh is derived from Git's tracked/staged view rather than a raw working-tree scan. Untracked local drafts therefore do not silently enter generated navigation for a commit.

The durable lesson is broader than this script:

> **Inspect by default. Mutate explicitly.**

> **Generated state should be deterministic and idempotent before lifecycle automation is allowed to maintain it.**

## Hook policy comparison

The check-only hook is the simpler safety default: detect drift, block, then require an explicit `--apply` before retrying the commit.

The apply-and-stage hook is a more automated policy. It is acceptable here because the generator owns a narrow deterministic surface and the hook stages only paths emitted by that generator. Never replace that allow-list with a broad `git add .`.

A local `.git/hooks/pre-commit` hook only governs commits made through that configured checkout. Shared hook provisioning or CI can repeat the same check when a project needs a repository-wide guarantee; Lab 8 only needs the concept.
