# Lab 4 — Exercise 3: Commit is not push

You are starting exactly where Exercise 2 ended.

The production-pack experiment has been reviewed and committed locally, but not pushed.

That means three states are already visible:

```text
working project state
clean
        ↓
local recorded history
contains the new reviewed commit
        ↓
published history in your GitHub fork
still ends at the previous commit
```

Do not create another throwaway commit just to demonstrate this gap. Use the real Exercise 2 commit.

## Part A — inspect the gap, then publish it

First inspect the project locally.

The working tree should be clean and the Exercise 2 commit should be present in local history.

Now inspect your GitHub fork.

The new commit should not be there yet.

Ask the agent:

> What exists locally now that the remote repository does not have yet?

Then say:

> Push the reviewed Exercise 2 commit.

Inspect the fork again.

The point is not merely that two commands exist. It is that you have just watched one already-understood project state move from local recorded history into published history.

Earn:

> **Commit records work. Push publishes recorded work.**

## Part B — wrong but unpublished

Now create a new mistake while keeping the same distinction visible.

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

- What changed when you committed the Exercise 2 result?
- What changed only when you pushed it in this exercise?
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
