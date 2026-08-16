# Lab 4 — Repositories, save points, and safe breakage

Status: **Scaffolded; ready for a dry run and refinement.**

Approximate duration: 1 hour.

Labs 1–3 have already let the learner benefit from source-control discipline without asking them to understand it. Lab 4 cashes that cheque.

The learner should leave with a practical recovery model rather than a Git command vocabulary:

> **What is the blast radius, and do I have a recovery path?**

The lab uses a small fictional theatre-production project. The local agent should be rooted at `project/`, not at the teaching directory.

The exercises are:

1. `learner/01-how-did-it-put-that-back.md` — delete and edit tracked files, inspect the difference between working state and recorded state, restore them, and compare this with never-tracked ignored local state.
2. `learner/02-make-a-mess.md` — let the agent make a broad multi-file restructuring, inspect the diff as primary evidence, keep only the useful parts, and commit only once the learner understands the resulting state.
3. `learner/03-commit-is-not-push.md` — make commit and push visible as two separate transitions, then compare recovery from an unpublished mistake with correction after publication.
4. `learner/04-can-git-save-us.md` — classify progressively revealed failure scenarios using three diagnostic questions: was it tracked, was it published, and did anything escape the project boundary?

The standing project instructions continue the review-stop convention from Lab 3: requested changes remain uncommitted and unpushed unless the learner explicitly asks to commit or push.

Keep the operating model deliberately simple:

> one repository, one main line of history, one agent changing it at a time.

Do not introduce branches, PRs, worktrees, merge strategies, or concurrent-agent isolation yet. A later advanced lab will deliberately break this simplifying assumption.

Core lines to earn:

> The working project can be messy without destroying the last state you understood.

> Don't tell me you changed it. Show me the diff.

> A commit is a state you understand and want a recovery point for.

> Commit records work. Push publishes recorded work.

> Be fearless with reversible state. Be deliberate with irreversible or external side effects.
