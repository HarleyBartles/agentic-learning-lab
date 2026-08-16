# Working instructions

You are working inside this Lab 2 project folder.

- Treat this folder as the complete local working environment for the task.
- Inspect the project before deciding which files, tools, or state matter.
- Do not inspect parent or sibling teaching-material file contents.
- You may inspect repository-level Git metadata, history, remotes, status, staging state, and diffs when needed to perform or verify the user's task safely.

## Preserve deliberately different project states

- Do not fetch, pull, merge, rebase, reset to a remote, or otherwise synchronize local and remote repository state unless the user explicitly asks you to synchronize them.
- When answering questions about the current local project, inspect and report the state visible in the current local working environment. Do not silently substitute newer remote state for local state.
- When the user asks to abandon an uncommitted local experiment or restore a file to its saved local version, restore it to the existing local recorded baseline without contacting or incorporating newer remote state unless the user explicitly asks for that.
- Do not create branches, pull requests, worktrees, or alternate integration flows for this lab unless the user explicitly asks. Work on the existing single main line of learner history.

## Review and publication behaviour

- Unless the user explicitly asks you to commit or push, make requested project changes in the working tree, stop when they are ready for review, and leave them uncommitted and unpushed.
- Committing or pushing requires explicit user authorization.
- Before committing, inspect staged and working changes and include only changes belonging to this Lab 2 project and the current authorized task. If unrelated changes are already staged or would be included, stop and explain rather than absorbing them.
- Before the first push in a run, verify the destination remote. Never push Lab 2 learner work to the canonical upstream `HarleyBartles/agentic-learning-lab`; the publication target must be the learner's fork/remote. If that cannot be established, stop before pushing.
- Publish only project material appropriate for source control.

## Local operational data boundary

- Treat data in `local/` as local operational data.
- Never publish, reproduce, summarise, quote, encode, or otherwise leak current local operational record contents or record-derived attendee-specific information into tracked files, generated receipts, logs, commit messages, issues, pull requests, or other remote repository surfaces.
- Do not force-add ignored files under `local/`, change `.gitignore` to make local operational state publishable, copy the operational database into a tracked path, or create seed/example/test data derived from the supplied attendee records.
- Reusable schema, migrations, setup instructions, generic field definitions, and code that operates on the database may be source-controlled when appropriate, provided they do not encode the current operational records.
- Before committing or pushing work that involved local operational data, inspect the proposed published changes and commit message to ensure no current record values or attendee-specific derived content would cross onto the remote surface.

## Surface honesty

- When a task depends on content or a representation that this working surface cannot actually inspect, state that limitation rather than guessing or inferring the unseen content.
- Do not claim to have inspected a file representation merely because you can establish that the file exists or can access opaque/binary metadata about it.

## Disposable scratch work

- Keep `scratch/` work bounded to that directory when a task explicitly concerns the scratch area.
- The tracked files in `scratch/` are disposable experiment material. When the user explicitly asks to delete them locally without committing or publishing, perform that bounded deletion without creating backup copies, moving the files elsewhere, or publishing the deletion.
- If the user then asks to abandon that local deletion, restore the scratch files from the existing local recorded state without synchronizing from the remote unless explicitly asked.
- Do not widen a scratch deletion into cleanup of related project files or other directories.
