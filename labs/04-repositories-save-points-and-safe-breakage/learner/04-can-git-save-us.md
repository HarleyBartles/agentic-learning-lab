# Lab 4 — Exercise 4: Can Git save us?

For each scenario, do not answer immediately.

First ask one useful diagnostic question.

Your three recurring questions are:

> Was it tracked?

> Was it published?

> Did anything escape the project boundary?

Try to classify each situation into one of these buckets:

1. Git can recover the project state.
2. Git can repair the project, but something has escaped the repository boundary.
3. Git has no recorded recovery path for the lost thing.

## Scenario 1 — deleted crew-call document

> An agent deleted tomorrow's crew-call document. Can Git save us?

What do you need to know before answering?

Then reveal:

> The file was tracked and the deletion is only in the working tree.

Classify it.

Now replay the question with this change:

> The document was a never-tracked local scratch file.

What changed?

## Scenario 2 — wrong call time

> An agent changed tomorrow's call time and committed it. Can Git save us?

Ask a diagnostic question.

Reveal:

> The commit has not been pushed yet.

Classify it.

Now change one fact:

> It was pushed to the remote repository.

Classify it again.

Final reveal:

> The stage manager already copied the wrong time into the crew WhatsApp.

Can Git repair the project? Can Git undo the message and its consequences?

## Scenario 3 — supplier order

> The agent changed a tracked supplier order from 20 lamps to 200. Can Git save us?

At first, assume this is only a project-file change.

Classify it.

Then reveal:

> The agent submitted the order through the supplier portal.

What changed about the recovery problem?

## Scenario 4 — secret exposure

> An agent accidentally committed a production credential, then immediately removed it again.

Is the current project content fixed?

Is the credential necessarily still secret?

What recovery action exists outside Git?

## Final reflection

Talk through:

- Why does `tracked` matter?
- Why does `published` matter even when Git can still correct the project?
- Why do external side effects change the recovery model?
- Which failures are cheap experiments and which require deliberate caution?

The broader idea is:

> **Reversibility depends on where the change happened, whether Git recorded it, whether recorded history was published, and whether consequences escaped the project boundary.**

Close on:

> **Be fearless with reversible state. Be deliberate with irreversible or external side effects.**

and:

> **Make experimentation cheap by controlling the blast radius.**
