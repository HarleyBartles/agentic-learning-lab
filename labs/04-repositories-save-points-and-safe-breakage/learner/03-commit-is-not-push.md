# Lab 4 — Exercise 3: Commit is not push

This exercise makes three states visible:

```text
working project state
        ↓ commit
local recorded history
        ↓ push
published history in your GitHub fork
```

Start from a clean project where local and remote history are aligned.

## Part A — stop between commit and push

Ask the agent to make one harmless wording improvement in `working/handover-notes.md`.

Review the diff.

Then say:

> Commit that change, but do not push it.

Inspect the project locally.

The working tree should be clean and the new commit should exist.

Now inspect your GitHub fork.

The new commit should not be there yet.

Ask:

> What exists locally now that the remote repository does not have yet?

Then say:

> Push it.

Inspect the fork again.

## Part B — wrong but unpublished

Ask the agent:

> Change the load-in start in `production/access-and-load-in.md` from 08:00 to 07:30, commit the change locally, and do not push it.

Once the commit exists, reveal:

> That was wrong. Load-in remains 08:00. Explain our recovery options before changing anything.

Let the agent explain the difference between correcting unpublished local history and correcting already-published history.

Then tell it to recover the project so the incorrect 07:30 state does not remain in the local history you intend to publish.

You do not need to perform or memorise the Git commands yourself.

Inspect the result and verify that the fork was never given the incorrect change.

## Part C — wrong and published

Now ask:

> Change the crew-call assembly point in `production/crew-call.md` from Stage Door to Loading Bay. Commit and push that change.

Inspect the fork so you know the wrong state really was published.

Then reveal:

> That was wrong. Crew still assemble at Stage Door. Explain the recovery position before changing anything.

This time, correct the project with a new forward commit and push it.

Inspect the history.

You should see the shape:

```text
known good state
↓
wrong published change
↓
corrective change
```

The current state is correct again even though history still records that the mistake happened.

## Reflect

Talk through:

- What changed when you committed?
- What changed when you pushed?
- Why might you deliberately commit without immediately pushing?
- Why was the unpublished mistake easier to reshape?
- Why did the published mistake get a forward correction instead?
- Can current project state be correct while history still contains a mistake?
- If three local commits existed and you pushed once, what would that push publish?

Useful ideas:

> **Commit records work. Push publishes recorded work.**

> **`Commit and push` is two instructions, not one state called finished.**

> **Committed does not mean irreversible.**

> **Published history can be corrected without pretending the mistake never happened.**
