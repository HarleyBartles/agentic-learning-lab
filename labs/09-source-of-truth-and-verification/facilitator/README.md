# Lab 9 facilitator guide

Status: **Mature and ready to run.**

Approximate duration: 60 minutes.

## Learning goal

Lab 9 should move the learner from accepting agent answers to evaluating project state.

The durable distinctions are:

```text
access / discovery
what can the worker observe, and how?

authority
which source defines what correct means?

verification
what evidence establishes that the work satisfies it?
```

Earn:

> **Access is not authority.**

> **Authority and verification are different questions.**

> **Prefer evidence over confident completion prose.**

> **A worker can verify perfectly against the wrong authority.**

And preserve the human acceptance boundary:

> **The agent should check its own work. The agent does not get to mark its own homework.**

Self-verification is expected. It improves the handoff. The learner still accepts or rejects the result.

## Contract

No coding knowledge is assumed. No coding is required.

The learner should not need to understand Git internals, shell syntax, test frameworks, CI, or code.

The learner's job is judgment:

- identify what defines correct;
- ask the worker to act against that authority;
- inspect evidence rather than completion prose;
- decide whether the evidence is sufficient for acceptance.

## Setup

Root the worker at:

`labs/09-source-of-truth-and-verification/working/repair-cafe/`

Before the learner arrives, confirm:

1. `PROJECT.md` explicitly says that `requirements/current-visitor-brief.md` is authoritative for the current approved public programme name.
2. The authoritative name is `Repair Café Saturday Clinic`.
3. Historical evidence and archive material legitimately contain `Repair Café Drop-In`.
4. Every file under `output/` initially contains the stale `Repair Café Drop-In` wording.
5. The working tree is clean before the exercise begins.
6. The learner's worker can search files and inspect diffs/status.
7. The Lab 8 mesh generator is still available in the learner's curriculum fork for the short callback, or the facilitator can discuss its `--check` / `--apply` contract from the previous lab if the learner workspace was reset.

Reveal learner cards one at a time.

## Exercise 1 — Which source wins?

Start read-only or explicitly non-mutating.

Give the learner card prompt exactly or naturally:

> What is the currently approved public programme name? Show me the project evidence for that answer, identify which source makes it authoritative, and explain why the other conflicting mentions do not win. Do not change anything yet.

The worker should find:

- `PROJECT.md` — authority map;
- `requirements/current-visitor-brief.md` — current authoritative value;
- `evidence/planning-meeting-2026-06-18.md` — historical evidence;
- `archive/launch-flyer.md` — archived historical copy;
- `output/*.md` — current but stale derived/public-facing output.

The important teaching move is to distinguish the value from the authority relationship.

The worker should not merely say:

> `current-visitor-brief.md` sounds current, therefore I trust it.

It should be able to establish that the project itself says this source governs that fact.

If the worker uses file recency, filename semantics, Git history, or public-facing prominence as the primary authority rule, ask:

> Where does the project say that rule governs this decision?

Earn:

> **Authority should be explicit rather than inferred from whichever source looks newest or sounds most official.**

This is the direct cash-in of Lab 3's unresolved Repair Café contradiction.

## Exercise 2 — Execute against the authority

Now authorize mutation:

> Bring every current visitor-facing output into line with the approved public programme name. Do not alter the authority map, current visitor brief, preserved evidence, or archive material. Review your own work before you tell me it is done, and tell me what evidence you used.

Expected mutation surface:

```text
output/visitor-information.md
output/social-post.md
output/access-information.md
output/faq.md
```

The worker may make slightly different wording choices as long as all current visitor-facing copy uses the authoritative programme name and meaning remains sensible.

Do not require a mechanical string replacement if natural prose needs a small grammatical adjustment.

Do not let the worker change historical evidence or archive material merely to make project-wide search results cleaner.

The worker should self-review before handoff. Good evidence might include:

- scoped search under `output/`;
- diff inspection;
- changed-file inspection;
- reading the resulting current visitor copy.

Treat strong self-review as good agent behaviour.

Then deliberately do **not** accept `done` yet.

## Exercise 3 — Human verification and acceptance

Ask the learner:

> What claim are we actually trying to establish?

The answer is not:

> The old phrase appears nowhere in the repository.

It is:

> **Every current visitor-facing output uses the approved programme name and only the intended current-output surfaces changed.**

Perform the smallest checks that falsify that claim:

1. Search `output/` for `Repair Café Drop-In`.
2. Search/read `output/` for `Repair Café Saturday Clinic`.
3. Inspect the diff.
4. Inspect changed paths/status.
5. Read the changed files for semantic quality.
6. Confirm `evidence/` and `archive/` still preserve the old historical wording.

If the old phrase still appears in historical evidence, ask:

> Is that a failure of this claim?

No. This is where verification becomes claim-scoped rather than ritualistic.

If everything is correct, the learner accepts the result.

If not, give the worker the failed evidence, let it repair the narrow defect, then independently verify again.

Earn:

> **A completion message is a claim. Verification is the evidence that lets the human accept or reject that claim.**

And:

> **Agent self-verification improves the handoff. Human acceptance remains separate.**

Avoid framing the learner's verification as distrust of the agent. It is normal engineering evidence discipline.

## Exercise 4 — Verifier versus mutator callback

Keep this short.

Recall Lab 8's generator.

Ask:

> If I want to establish whether the mesh is stale, should I start by checking it or by regenerating it?

Use:

```text
check
→ establish existing state

apply
→ change state deliberately

check again
→ establish resulting state
```

If the learner asks why this matters, explain that a repair-first operation can erase evidence of the defect you were trying to establish.

Earn:

> **A verifier should not silently repair the thing it is supposed to verify.**

> **Inspect first. Mutate deliberately. Verify the resulting state.**

Do not introduce hooks. The learner already knows what a meaningful check looks like; Module 12 later asks why a human must keep remembering to request it at the same lifecycle boundary.

## Exercise 5 — Generalise without adding four more labs

Ask the learner what evidence they would want for several claims.

Suggested prompts:

- `The PDF is ready to send.`
- `The application works.`
- `The change is merged on GitHub.`
- `This research conclusion is grounded.`

Let them propose evidence before revealing examples.

Useful mappings:

```text
PDF ready
→ render + inspect rendered output

application works
→ suitable automated checks + runtime behaviour

merged on GitHub
→ remote GitHub merge/main evidence

research grounded
→ citations + source provenance + contradiction checks
```

The point is not to teach these tools now.

Earn:

> **Verification is claim-dependent and artifact-dependent.**

Reconnect to Lab 8:

- local workflow source can establish what is configured to run;
- remote GitHub state establishes whether a particular remote event actually occurred.

Neither source is universally better. The claim chooses the evidence surface.

## Finish on the Course 1 capstone

Ask the learner to state the two questions they should now carry into any real agent task:

Before execution:

> **What source defines correct here?**

After execution:

> **What evidence would make me willing to accept this work?**

Then point forward to Lab 10: the learner now has to apply the Course 1 model to a project they actually own.

## Failure handling

If the worker immediately edits files in Exercise 1, reset the fixture or discard that run and repeat with an explicit read-only constraint. The authority question must be answered before execution.

If the worker rewrites historical evidence/archive material, inspect why. If it was trying to satisfy a project-wide search for the old phrase, use that as a teaching moment: the verifier or task definition was too broad for the actual claim. Reset/repair the fixture before continuing.

If the worker selects the correct current brief but cannot explain why it is authoritative, open `PROJECT.md` and ask it to reason from the explicit project rule. Do not reward a lucky answer based on filename semantics.

If self-review is weak, ask what checks could falsify its own completion claim before handoff. Do not replace learner verification with better worker self-review; both are useful and distinct.

If shell tooling is awkward, use IDE search/diff/status or equivalent visible controls. The learner needs the evidence model, not command-line fluency.

## Do not teach yet

Do not teach Git hooks or lifecycle automation.

Do not build a CI system for this lab.

Do not introduce specialist reviewer/verifier sub-agents.

Do not teach historical Git archaeology here.

Do not imply that final human acceptance means the human manually reproduces every check forever. Later workflow material can automate cheap repeatable checks while preserving meaningful human gates.

Do not turn authority into a universal filename hierarchy. The project owns its authority model.
