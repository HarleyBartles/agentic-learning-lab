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

Stage it if it is meant to enter your next commit, then run it against `working/environment/`.

The supplied generator deliberately describes Git's staged/tracked project state rather than every unstaged file that happens to be lying around locally.

Inspect the changed `INDEX.md` files.

Ask:

- Did the generated root mesh discover `forgotten/`?
- Did it create a local index inside that directory?
- Does running the generator again without changing staged/tracked structure produce the same index content?

The intended properties are:

```text
deterministic
same staged/tracked project state -> same generated mesh

idempotent
running it again does not keep changing the result
```

That gives us a better rule:

> **Do not hand-maintain derived navigation when the project can regenerate it from source state.**

## But who remembers to run the generator?

Now there is still a human habit left:

> Remember to regenerate the mesh before every commit.

This is where a Git hook becomes useful.

A hook is a small action Git runs automatically at a particular lifecycle point. There are many kinds of hooks; this lab only needs one example.

The facilitator will provide a `pre-commit` hook for this lab.

Install it into the learner fork's Git hook location as directed by the facilitator.

Its job is deliberately small:

```text
before commit
→ regenerate the index mesh from staged/tracked Git state
→ stage only the generated INDEX.md files
→ continue the commit
```

Make and stage one harmless structural change inside the exercise environment, then commit it.

Inspect the commit or staged diff.

Ask:

- Did the relevant index change travel with the structural change?
- Did the hook stage unrelated project work?
- Would another person checking out this commit receive the matching navigation mesh?

## What does the hook actually guarantee?

A normal `.git/hooks/pre-commit` hook belongs to this local checkout.

So the guarantee is scoped:

> **Commits created through this configured checkout run the freshness step before they are created.**

That does not magically force another clone, another contributor, or a remote GitHub mutation to use the same hook.

A larger project can provision shared hook tooling or add remote checks when it needs a repository-wide guarantee. You do not need that machinery for this exercise.

## The principle

The point is not `pre-commit` as a magic filename.

The point is that important derived project state should have a reliable maintenance mechanism.

Earn:

> **If a navigation surface is derived from project state, regenerate it rather than hand-editing it.**

> **If freshness matters at commit time, encode that expectation into the commit path instead of relying on memory.**

The mesh is now more trustworthy because its contents are reproducible from the staged/tracked state it is designed to represent, and commits made through this configured checkout automatically carry the corresponding freshness update.

That does not make the index authoritative about every possible truth in the project. It makes the index a more reliable representation of the project structure it is designed to describe.

Keep that distinction. The next card widens the observation problem beyond the local filesystem entirely.