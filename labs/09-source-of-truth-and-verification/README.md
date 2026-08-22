# Lab 9 — Source of truth and verification

Status: **Mature and ready to run.**

Approximate duration: 60 minutes.

No coding knowledge is assumed. No coding is required.

Lab 8 ended with two questions:

> **The worker can reach several pieces of project state. Which one should it trust?**

and:

> **What would actually prove that the required work is correct?**

Lab 9 answers those questions.

## Core thesis

A worker being able to observe something does not tell us whether that thing defines correct, and an agent saying work is complete does not prove that it is complete.

The learner should leave with three separate questions:

```text
access / discovery
What can the worker observe, and how did that evidence reach it?

authority
Which source defines the requirement or current truth?

verification
What evidence establishes that the work actually satisfies it?
```

Earn:

> **Access is not authority.**

> **Authority and verification are different questions.**

> **Prefer evidence over confident completion prose.**

> **A worker can verify perfectly against the wrong authority.**

And the acceptance boundary:

> **The agent should check its own work. The agent does not get to mark its own homework.**

Self-verification is useful evidence and should improve the work before handoff. Final acceptance still belongs to the human.

## Why Repair Café returns

Lab 3 deliberately left a Repair Café project disagreeing with itself and asked:

> **When the project disagrees with itself, how does an agent know what to trust?**

Lab 9 reopens that familiar problem with a fresh, self-contained fixture. The learner does not depend on whatever state their earlier Lab 3 run happens to contain.

This time the project has an explicit authority map.

The fixture contains:

- an authoritative current visitor brief;
- preserved planning evidence containing an older programme name;
- archived historical copy containing that older name;
- current visitor-facing outputs that have drifted and still use the older name.

The lesson is not that the newest file, the most official-sounding filename, or the public-facing output automatically wins. The project must say which source defines the fact being changed.

## Shape

```text
labs/09-source-of-truth-and-verification/
    README.md
    facilitator/
        README.md
    learner/
        01-which-source-wins.md
        02-do-the-work.md
        03-dont-mark-your-own-homework.md
        04-check-before-repair.md
        05-what-would-prove-it.md
    working/
        README.md
        repair-cafe/
            AGENTS.md
            PROJECT.md
            requirements/
                current-visitor-brief.md
            evidence/
                planning-meeting-2026-06-18.md
            archive/
                launch-flyer.md
            output/
                visitor-information.md
                social-post.md
                access-information.md
                faq.md
```

Reveal learner cards one at a time.

Root the worker at `working/repair-cafe/`, not at the teaching directory.

## Exercise 1 — Which source wins?

Start read-only or explicitly non-mutating.

Ask the worker to inspect the project and answer:

> What is the currently approved public programme name? Show me the project evidence for that answer, identify which source makes it authoritative, and explain why the other conflicting mentions do not win. Do not change anything yet.

The worker should discover that `PROJECT.md` defines the authority relationship and `requirements/current-visitor-brief.md` contains the current approved value.

The older name remains legitimately present in historical evidence, archive material, and stale derived output.

The learner should distinguish:

```text
can read it
!=
it defines correct

mentions the value
!=
it is authoritative for the value

newer-looking / official-sounding
!=
authority unless the project says so
```

Earn:

> **Authority should be explicit rather than inferred from whichever source looks newest or sounds most official.**

## Exercise 2 — Do the work, then let the worker self-check

Now authorize one bounded task:

> Bring every current visitor-facing output into line with the approved public programme name. Do not alter the authority map, current visitor brief, preserved evidence, or archive material. Review your own work before you tell me it is done, and tell me what evidence you used.

The current approved name is:

`Repair Café Saturday Clinic`

The stale current output uses:

`Repair Café Drop-In`

The worker should modify only current files under `output/` and should self-review before reporting completion.

Do not accept the completion message yet.

The point is not to make the worker fail. A good worker may perform the task perfectly. The learning outcome is that correctness is established from evidence rather than from whether the completion message sounds convincing.

## Exercise 3 — Do not let the worker mark its own homework

The learner now independently inspects the evidence.

Use simple, visible checks:

- search current `output/` for the old name;
- confirm the approved name appears where expected;
- inspect the diff;
- inspect which files changed;
- read the changed visitor-facing copy for meaning, not merely string replacement;
- confirm preserved evidence and archive material were not rewritten just to make a global search look clean.

A crucial subtlety is intentional:

> Finding `Repair Café Drop-In` somewhere in the project is **not** automatically evidence of failure.

Historical evidence and archive material are supposed to preserve the old wording honestly.

The actual claim is narrower:

> **Every current visitor-facing output uses the approved programme name.**

Verification must therefore match the claim.

If the evidence supports the claim, the learner accepts the work.

If it does not, return the evidence to the worker, let it repair the bounded defect, and verify again.

Earn:

> **A completion message is a claim. Verification is the evidence that lets the human accept or reject that claim.**

And:

> **Agent self-verification improves the handoff. Human acceptance remains separate.**

## Exercise 4 — Check before repair

Use the Lab 8 mesh generator as a short callback rather than another full demonstration.

Ask:

> If I want to know whether the navigation mesh is currently stale, which operation should happen first: `--check` or `--apply`?

The learner should recognise that immediately applying a repair can destroy evidence about the state that existed before inspection.

Use the sequence:

```text
inspect / check
        ↓
stale state established
        ↓
repair deliberately
        ↓
inspect / check again
```

Earn:

> **A verifier should not silently repair the thing it is supposed to verify.**

And:

> **Inspect first. Mutate deliberately. Verify the resulting state.**

Do not cash the separate lifecycle cheque here. Lab 9 establishes what a meaningful check is. A later workflow lesson asks why the human is still remembering to request that check at the same transition every time.

## Exercise 5 — What would prove it?

Finish by generalising verification without running four more demonstrations.

Give the learner several claims and ask what evidence they would want before accepting each one:

```text
"The old wording is gone from current visitor output."
→ scoped search + diff + read

"The PDF is ready to send."
→ render + inspect the rendered artifact

"The application works."
→ appropriate tests + runtime behaviour

"The change is merged on GitHub."
→ remote GitHub merge/main evidence

"This research conclusion is grounded."
→ source citations + provenance + contradiction checking
```

The exact tools vary with the artifact and claim.

Earn:

> **Verification is claim-dependent and artifact-dependent.**

The local/connected distinction from Lab 8 should now make sense in evidential terms: local workflow source can prove what is configured to run; remote GitHub state is needed to prove that a particular remote run or merge actually happened.

Neither surface is universally more authoritative. The claim determines the relevant evidence.

## Handoff to Lab 10

Close Course 1's taught fundamentals with this progression:

```text
Labs 1–8
I can create, provision, direct, understand, and navigate a worker.

Lab 9
I can identify what defines correct and establish whether the work actually satisfies it.

Lab 10
Now use the whole thing on a project that is actually mine.
```

The learner should enter the Course 1 capstone able to ask, before execution:

> **What source defines correct here?**

and after execution:

> **What evidence would make me willing to accept this work?**

## What this lab is not

Do not turn Lab 9 into a heavy CI lesson.

Do not teach Git hooks or lifecycle automation here.

Do not require the learner to write tests, scripts, or code.

Do not introduce specialist verifier agents merely to make verification sound advanced.

Do not turn the session into a tour of PDF tooling, software testing, GitHub Actions, research tooling, and repository archaeology. Those are examples of the same claim/evidence principle, not five separate lab exercises.

Do not cash the historical-repository archaeology thread here. `Not present now != never existed` belongs later when the learner is explicitly investigating history, provenance, and compressed evidence surfaces.
