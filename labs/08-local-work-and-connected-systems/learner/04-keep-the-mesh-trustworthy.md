# 04 — Keep the mesh trustworthy

You just proved that the index mesh can be incomplete even while the missing folder is fully accessible.

That creates a more important engineering question:

> **If we are going to use this mesh to navigate the project, how do we keep it trustworthy?**

A tempting answer is:

> Remember to update `INDEX.md` whenever project structure changes.

That is a human habit, not a reliable system.

## Do not repair it by hand

The facilitator will now give you a small index generator.

Copy the supplied generator into:

`working/environment/tools/generate_index_mesh.py`

Stage it if it is meant to enter your next commit.

The generator has two deliberately different modes:

```text
--check
inspect only
report whether the generated mesh matches tracked/staged project state
make no changes

--apply
explicit mutation
regenerate the INDEX.md files from tracked/staged project state
```

Start with the non-mutating path:

> Run the generator with `--check`.

It should report that the mesh is stale without repairing anything.

That earns a broader tooling rule:

> **A maintenance tool that can mutate project state should also offer a safe inspection path, and mutation should be explicit.**

Then run it with `--apply` and inspect the changed `INDEX.md` files.

Ask:

- Did the generated root mesh discover `forgotten/`?
- Did it create a local index inside that directory?
- Does `--check` now report the mesh as current?
- Does another `--apply` with no structural change produce byte-identical index content?

The intended properties are:

```text
deterministic
same tracked/staged project state -> same generated mesh

idempotent
run --apply again -> no accumulating change
```

The supplied generator deliberately describes Git's tracked/staged project state rather than every unstaged file that happens to be lying around locally.

That gives us a better rule:

> **Do not hand-maintain derived navigation when the project can regenerate it from source state.**

## But who remembers to check it?

There is still a human habit left:

> Remember to check or regenerate the mesh before every commit.

This is where a Git hook becomes useful.

A hook is a small action Git runs automatically at a particular lifecycle point. There are many kinds of hooks; this lab only needs one example: `pre-commit`.

There are two reasonable policies.

### Policy A — check and block

```text
before commit
→ run generator --check
→ if stale, block the commit
→ human or agent deliberately runs --apply
→ inspect/stage the generated change
→ retry commit
```

This is the easier safety model: the hook detects drift but does not silently mutate the commit.

### Policy B — apply and stage the owned generated files

```text
before commit
→ run generator --apply
→ stage only the INDEX.md files owned by the generator
→ continue commit
```

This is more automated. It is defensible because generation is deterministic and idempotent and the staging allow-list is narrow.

It must not broadly `git add` unrelated project work.

The facilitator will provide both hook examples. Compare them and choose one for the exercise.

Make and stage one harmless structural change inside the exercise environment, then commit it.

Inspect the result.

Ask:

- Did the relevant index change travel with the structural change?
- If the check-only policy was used, did the stale commit get blocked before mutation?
- If the apply-and-stage policy was used, did it stage only the generated indexes it owns?
- Would another person checking out the resulting commit receive the matching navigation mesh?

## What does a local hook actually guarantee?

A normal `.git/hooks/pre-commit` hook belongs to this checkout.

So its guarantee is scoped:

> **Commits created through this configured checkout run the chosen freshness policy before they are created.**

That does not magically force another clone, contributor, web edit, or remote mutation to use the same hook.

A larger project can provision shared hook tooling or enforce the same non-mutating check in CI when it needs a repository-wide gate. You do not need to build that machinery here.

## The principle

The point is not `pre-commit` as a magic filename.

The point is that important derived project state should have a reliable maintenance mechanism.

Earn:

> **If a navigation surface is derived from project state, regenerate it rather than hand-editing it.**

> **If freshness matters at a lifecycle boundary, encode the check there instead of relying on memory.**

> **Inspect by default. Mutate explicitly.**

The mesh is now more trustworthy because its contents are reproducible from the tracked/staged state it is designed to represent and the commit path has an explicit freshness policy.

That does not make the index authoritative about every possible truth in the project. It makes the index a more reliable representation of the project structure it is designed to describe.

Keep that distinction. The next card widens the observation problem beyond the local filesystem entirely.