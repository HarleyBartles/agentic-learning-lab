# Lab 3 — Exercise 2: Don't make the agent guess

Exercise 1 showed that important project knowledge can disappear if it never leaves the conversation.

This exercise looks at the opposite mistake: turning a conversation into project state too casually.

You have some notes from a Repair Café planning meeting.

Use the same meeting minutes in all three runs.

## Meeting minutes

1. Alex suggested that a future session for children could be fun if safeguarding and volunteer numbers ever made it practical. No decision was made.
2. The group discussed whether visitors should be allowed to bring a second item late in the session if things are quiet. No decision was reached.
3. The group agreed that every soldering station at the pilot will use a heatproof mat.
4. Alex confirmed that he will bring two suitable heatproof mats for the pilot.
5. The group discussed whether to accept voluntary donations at the pilot. Opinions were mixed and the question remains unresolved.
6. Priya said the tea at the last community event was terrible and volunteered to bring better biscuits this time.
7. The group agreed that repairs involving exposed mains wiring will only be handled by volunteers who are comfortable and competent doing that work.

## Before you start

Exercise 2 needs a clean project baseline.

Ask the local agent to inspect the current project state. If the final decision from Exercise 1 is still an uncommitted change, ask the agent to commit and push that completed Exercise 1 work now.

Then make sure there are no other uncommitted project changes before starting Run 1.

You do not need to learn the source-control mechanics yet. The important thing for this exercise is that each experimental run starts from the same project state.

## Run 1 — "save the important stuff"

Start with the deliberately vague instruction below. Paste the meeting minutes after it.

> Here are the minutes from the latest Repair Café planning meeting. Sort through them and put the important stuff in the repo. Make whatever project-file changes you think are appropriate, but leave all changes uncommitted and do not push anything. Stop when the changes are ready for me to review.

Inspect what the agent changed.

Do not just read its completion message. Look at the actual changed files and diff.

Talk through:

- Which points did the agent decide were important?
- Which points did it omit?
- Did it preserve the original meeting record anywhere?
- Did it turn any discussion into a decision?
- Did it decide where information belonged?
- Which of those judgments did you actually authorize?

The result may look perfectly reasonable. That is part of the exercise.

Now ask:

> Discard all uncommitted changes from this run and restore the project to exactly how it was before Run 1. Do not alter committed history or push anything.

Check that the Run 1 changes are gone before continuing.

## Run 2 — preserve the evidence honestly

Use the same meeting minutes again.

Ask:

> Here are the same meeting minutes. Persist them verbatim in the project as an honest meeting record. Do not interpret any point as a settled decision, commitment, rule, or resolved question, and do not update the rest of the project state from them. Leave the changes uncommitted and do not push anything. Stop when the meeting record is ready for review.

Inspect the changes.

Compare this result with Run 1.

This time the project should contain an honest record of what was said without silently deciding what each point means for the current plan.

Now ask:

> Discard all uncommitted changes from this run and restore the project to exactly how it was before Run 2. Do not alter committed history or push anything.

Check that the Run 2 changes are gone before continuing.

## Run 3 — preserve the evidence and promote meaning deliberately

Use the same meeting minutes one last time.

This time tell the agent exactly which meeting points have authority to change the current project state.

Ask:

> Persist these meeting minutes verbatim as the meeting record. Then update the durable project state to reflect them. Points 3, 4 and 7 are confirmed project state and should affect the current plan. Points 2 and 5 remain unresolved questions. Do not promote points 1 or 6 into current project state; they should remain only in the meeting record. Make the project-file changes you think are appropriate, but leave everything uncommitted and do not push anything. Stop for review when you are done.

Inspect the changes carefully.

Look for two different things:

- an honest meeting artifact that preserves what was actually recorded;
- deliberate updates to the project state that reflect only the points you authorized.

Check that unresolved discussion still looks unresolved.

Check that points 1 and 6 have not quietly become current policy just because they appeared in the minutes.

If the result looks right, tell the agent:

> Keep these changes. Commit and push the completed Exercise 2 project state.

## Final proof

Now start a completely fresh agent conversation.

Use a fresh local agent first. If time allows, ask cloud ChatGPT through the repository connector as well.

Ask:

> Inspect the Repair Café project as it exists now. Tell me which decisions, rules, and commitments from the latest planning meeting are reflected in the current project state, and which questions from that meeting remain unresolved.

Compare the answer with the meeting minutes and the changes you chose to keep.

## Reflect

Run 1 delegated more than file editing. The phrase `important stuff` also delegated judgment about importance, meaning, status, and authority.

Run 2 preserved the evidence without pretending that preservation automatically updates the operational state of the project.

Run 3 separated the two jobs: preserve what was actually said, then deliberately state what should become current project knowledge.

The practical lesson is:

> Preserve evidence honestly. Promote meaning deliberately.

And:

> Don't make the agent guess which meeting chatter became project truth.
