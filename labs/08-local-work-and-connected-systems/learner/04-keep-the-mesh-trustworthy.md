# 04 — Keep the mesh trustworthy

You just proved that the index mesh can be incomplete even while the missing folder is fully accessible.

That creates a more important engineering question:

> **If we are going to use this mesh to navigate the project, how do we keep it trustworthy?**

A tempting answer is:

> Remember to update `INDEX.md` whenever project structure changes.

That is a human habit, not a reliable system.

## Do not repair derived navigation by hand

The facilitator will now give you a small index generator.

Copy the supplied generator into:

`working/environment/tools/generate_index_mesh.py`

The tool is deliberately self-describing. If you want to know how to use it, ask the tool for help rather than guessing its interface.

Then have the agent regenerate the complete mesh for `working/environment/`.

Inspect what changed.

Ask:

- Did the regenerated root mesh discover `forgotten/`?
- Did it create the missing local index beneath that directory?
- If you regenerate again without changing the project structure, does the mesh stay the same?
- Is the result now derived from project state rather than from somebody remembering to edit several index files correctly?

Name the useful properties:

```text
deterministic
same source state -> same generated mesh

idempotent
regenerate again -> no accumulating change
```

That gives us a stronger engineering rule:

> **Do not hand-maintain derived navigation when the project can regenerate it from source state.**

And:

> **If a representation is important enough for agents to rely on, make it reproducible.**

## One problem remains

We have solved this question:

> Can the project regenerate a trustworthy mesh when asked?

We have **not** solved this one:

> What makes sure the regeneration happens at the right time?

Do not solve that here.

For now, notice the difference:

```text
tool exists
!=
tool is always used when it should be
```

That distinction will matter later in the curriculum.

Keep the generator in the working environment. It will become useful evidence for a later lesson about repeated instructions, workflow, and lifecycle automation.

The next card widens the observation problem beyond the local filesystem entirely.