# Working instructions

You are working inside the Lab 4 Northstar theatre-production project folder.

- Treat this folder as the complete project environment for project-content inspection and modification.
- Do not inspect parent or sibling teaching-material file contents.
- You may inspect repository-level Git metadata, history, remotes, status, staging state, and diffs when needed to perform or verify the user's task safely.
- Inspect the project before answering questions about its current state.
- Make only changes needed for the user's requested task.
- For ordinary project-content edits or reorganisations, use reasonable judgment and proceed without preliminary clarifying questions unless a genuine authority, safety, or irreversible-side-effect ambiguity blocks the work.
- Unless the user explicitly asks you to commit or push, make requested project changes in the working tree, stop when they are ready for review, and leave them uncommitted and unpushed.
- Committing or pushing requires explicit user authorization.
- Before committing, inspect the staged/working changes and include only changes belonging to this Lab 4 project and the current user-authorized task. If unrelated changes are already staged or would be included, stop and explain rather than absorbing them.
- Before the first push in a run, verify the destination remote. Never push Lab 4 learner work to the canonical upstream `HarleyBartles/agentic-learning-lab`; the publication target must be the learner's fork/remote. If that cannot be established, stop before pushing.
- Do not create branches, pull requests, worktrees, or alternate integration flows for this lab unless the user explicitly asks. Work on the existing single main line of learner history.

## Preserve the experiment conditions

- Do not modify `AGENTS.md`, `.gitignore`, `local/README.md`, repository configuration, or other lab-control/scaffolding files during ordinary production-pack/content tasks unless the user explicitly names that infrastructure as the task target.
- Ordinary content/reorganisation tasks should operate within `production/`, `working/`, and user-created ignored files under `local/` as appropriate.
- When the user explicitly moves a tracked file into an ignored path, honour that classification literally. Do not force-add the ignored destination, change `.gitignore`, create an alternate tracked copy, make a safety backup, stash an extra copy, or proactively warn about the tracking consequence unless the user asks about tracking/repository state.
- When the user explicitly asks to hard-delete disposable local working files, perform the deletion directly without creating backups, moving files elsewhere, using a recycle-bin/trash recovery path, or automatically restoring them afterward. Preserve tracked project scaffolding such as `local/README.md` unless the user explicitly names it for deletion.
- Do not proactively reveal the intended teaching conclusion of a state transition. Answer the user's current question from the evidence currently requested, then follow later questions into deeper history/provenance when asked.

## Review and recovery behaviour

- If the user asks to discard the current run or experiment, undo only the uncommitted changes produced by that run and restore the project to its pre-run state. Do not rewrite committed history, discard unrelated work, or push anything as part of the reset.
- If the user accepts some parts of an uncommitted experiment and rejects others, preserve the accepted diff and restore only the rejected portions. Do not use a broad reset that destroys accepted or pre-existing work.
- Before performing a recovery action that changes committed history, explain the current recovery position in plain language when the distinction matters.
- If a mistake is the latest unpublished local commit and no later work depends on it, prefer reshaping/removing that unpublished mistake rather than adding a public-style corrective commit.
- Treat published/shared history more conservatively than unpublished local history. Prefer a forward corrective commit for already-published mistakes unless the user explicitly asks for a different recovery strategy and understands the consequences.
- Use Git status, diffs, and history as evidence. Do not rely on a prose completion summary when the repository state can be inspected directly.
- Do not assume ignored or untracked local files are recoverable through Git. Establish whether Git has actually recorded a version before claiming that it can restore the contents.
- When asked whether a missing file is recoverable, first distinguish current working state, current tracked/published state, and any explicit facts the user supplied. Do not automatically search older history or restore the file until the user asks about historical state, whether it was ever tracked, or explicitly asks for recovery.
- For hypothetical recovery scenarios with missing facts, ask the minimum diagnostic question needed instead of silently assuming the answer. Useful dimensions include whether the thing was tracked, whether the relevant state was published, and whether any consequence escaped the project boundary.
