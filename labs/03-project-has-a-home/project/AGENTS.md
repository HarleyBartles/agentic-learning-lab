# Working instructions

You are working inside the Lab 3 Repair Café project folder.

- Treat this folder as the complete project environment for project-content inspection and modification.
- Do not inspect parent or sibling teaching-material file contents.
- You may inspect repository-level Git metadata, history, remotes, status, staging state, and diffs when needed to perform or verify the user's task safely.
- Inspect the project before answering questions about its state.
- Treat files in `source/` as source material; do not modify them unless the task explicitly requires it.
- Follow explicit user instructions about whether project files may or may not be changed.

## Discussion-only behaviour

- When the user frames the interaction as discussing, exploring, brainstorming, thinking through, or planning, enter discussion-only mode.
- In discussion-only mode, you may inspect and reason about the project, but do not create, edit, delete, rename, or move files; do not commit or push; and do not take other project or external actions with side effects.
- A decision, agreement, approval, or conclusion reached during discussion-only mode is not by itself permission to persist that result.
- Do not treat a decision that exists only in the current conversation as durable project state. Another agent should only be expected to reconstruct project state from information persisted into the project or otherwise supplied through its environment.
- Stay in discussion-only mode until the user explicitly authorizes project changes or clearly says to leave discussion-only mode.

## Ordinary task execution and review

- When the user later authorizes changes, make only the changes needed for the authorized task.
- For ordinary project-content tasks, use reasonable judgment and proceed without preliminary clarifying questions unless a genuine authority, safety, or irreversible-side-effect ambiguity blocks the work.
- If the user deliberately delegates semantic judgment with broad wording such as `important`, `relevant`, or `useful`, exercise that judgment rather than asking the user to pre-classify the material for you. Do not manufacture uncertainty merely to avoid making the requested judgment.
- Unless the user explicitly asks you to commit or push, make requested project changes in the working tree, stop when they are ready for review, and leave them uncommitted and unpushed.
- Committing or pushing requires explicit user authorization. Approval of the content or a request to keep changes is not by itself permission to publish them.
- Before committing, inspect staged and working changes and include only changes belonging to this Lab 3 project and the current authorized task. If unrelated changes are already staged or would be included, stop and explain rather than absorbing them.
- Before the first push in a run, verify the destination remote. Never push Lab 3 learner work to the canonical upstream `HarleyBartles/agentic-learning-lab`; the publication target must be the learner's fork/remote. If that cannot be established, stop before pushing.
- Do not create branches, pull requests, worktrees, or alternate integration flows for this lab unless the user explicitly asks. Work on the existing single main line of learner history.

## Evidence, authority, and scope

- When asked to persist an important newly confirmed project decision, update the smallest coherent set of durable project-state artifacts needed for a future fresh agent to reconstruct that decision. Do not regenerate derived outputs or broadly reconcile unrelated artifacts unless the user asks.
- Do not invent settled decisions where the project still records an open question.
- When the user explicitly asks to preserve supplied evidence verbatim without promoting it into current project state, create only the honest evidence artifact and any minimal structure needed to hold it. Do not update current-state files, summaries, indexes, derived outputs, or interpretive metadata unless requested.
- When the user explicitly classifies supplied material by status or authority, preserve those classifications exactly. Do not promote speculation or chatter into policy, convert unresolved questions into decisions, demote confirmed state, or infer additional settled meaning beyond what the user authorized.
- When asked to create a derived output from current project state, create or update only the requested output unless the user explicitly requests source-state maintenance. Do not rewrite the project state merely because the derived output repeats it.
- When the user explicitly scopes a maintenance task to a named file and explicitly says not to search for or update related references, comply with that scope. You may give one brief warning that dependent artifacts could become stale, but do not search for, enumerate, or repair those artifacts unless the user asks.
- When durable project artifacts conflict and no explicit authority rule resolves the conflict, do not silently choose a winner based only on filename semantics, recency, public-facing status, or another inferred hierarchy. Report the conflict and distinguish explicit project authority from your inference.
- Inspection or diagnosis of conflicting project state is non-mutating unless the user explicitly asks for reconciliation. Do not repair stale or contradictory artifacts as a side effect of answering an authority question.

## Discard and recovery

- When the user asks to discard the current run or experiment, undo only the uncommitted changes produced by that run and restore the project to its pre-run state. Do not rewrite committed history, discard unrelated pre-existing changes, or push anything as part of the reset.
- If only some uncommitted changes belong to the current run, restore only those changes and preserve unrelated or previously accepted work.
- Use Git status and diffs as evidence when verifying that a run was discarded or that only the intended changes remain.
