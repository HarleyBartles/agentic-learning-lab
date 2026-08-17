# Lab 6 query bank

Use this as a facilitator fallback, not as a script the learner must complete.

The lab works when the learner sees the *quality of the model's epistemic grounds change*. It does not require a specific model failure.

## Primary family — knitting and crochet history

Start broad:

> Tell us what you know about knitting and crochet in the seventeenth and eighteenth centuries, including important technical changes and the major people associated with those changes.

Possible narrowing prompts:

1. > Separate mechanised stocking-frame history from hand-knitting technique. Which named practitioners or innovators changed hand-knitting practice between 1650 and 1800, what did each change, and how confident are you in each attribution?
2. > Pick one regional knitting tradition from that period. Which distinctive conventions can you date with confidence, and which named attributions would you want to verify?
3. > For the strongest named attribution in your previous answer, what contemporary or near-contemporary evidence do you remember rather than infer?
4. > Which claims in your answer are strongly retained facts, which are broad historical associations, and which are plausible reconstructions you would not teach without checking?
5. > Does the category `crochet` itself create a historical problem in the period we asked about? What can you establish from retained knowledge alone?

Stop once the learner can identify a change such as:

```text
broad descriptive competence
→ less secure named attribution
→ weak remembered provenance
→ explicit uncertainty about terminology/evidence
```

Do not continue merely to force `I don't know`.

## Clean contradiction control

Default:

> What work was Ada Lovelace doing on computing in 1800?

Facilitator check: Ada Lovelace was born in 1815. The intended pressure is a simple chronological contradiction the model may be able to reject from strongly retained facts.

Do not tell the learner the answer before asking them to predict the agent's behaviour.

Backup shape if the default ever becomes awkward:

> Choose a universally well-known historical figure, verify their birth year before the session, then ask what they were doing at a date comfortably before that birth year.

The control should be boringly falsifiable. Do not use a disputed biography.

## Backup family A — croquet history

Broad:

> Give us a history of nineteenth-century croquet technique. Which tactical or technical changes mattered most?

Narrow:

> Which named people or manuals can you associate with three specific changes, and how certain are those attributions?

Then:

> Which of those claims can you tie to remembered contemporary evidence, and which would you verify before teaching them as fact?

The facilitator does not need to know the answers in advance. The point is to test retained specificity and provenance, then later use retrieval if this family becomes the chosen open-book investigation.

## Backup family B — a regional craft tradition

Ask the model to choose a specialised pre-industrial or early-industrial craft tradition it believes it knows reasonably well.

Then narrow:

> What conventions were distinctive in one region during a fifty-year period?

> Which named practitioners, workshops, manuals, or organisations are actually documented as introducing specific changes?

> Which attribution in your answer is most vulnerable to later folklore being mistaken for contemporary evidence?

This family is useful when the opening knitting/crochet probe happens to be exceptionally strong.

## Backup family C — specialised historical production

Broad:

> Choose a narrow historical production technique from before mass industrial standardisation and explain how it worked.

Narrow:

> Name three documented technical changes, approximate dates, and the people/workshops/publications responsible.

Then:

> What evidence do you remember for each attribution, and where does your recall become reconstruction rather than retained fact?

## Premise-challenge variants

Use at most one or two. The goal is to expose different epistemic states, not build a trap course.

Useful shapes:

- a clean chronological impossibility;
- a category that may be anachronistic for the period;
- a history that may have been collective rather than driven by named innovators;
- a regional practice where later folklore may be easier to remember than contemporary evidence.

Avoid:

- silly gotchas;
- politically charged premise traps;
- examples where the facilitator cannot later inspect credible evidence;
- questions whose answer depends on a current fact rather than stable historical evidence.

## Self-prediction prompts

Before the first domain answer:

> Before answering, where do you expect your retained knowledge of this subject to be strong, where do you expect it to become weak, and which kinds of claims would you verify if retrieval were available?

After narrowing:

> Compare your original prediction with your actual answers. Where were you better or worse than you expected?

After retrieval:

> Compare your closed-book suspicion with the retrieved evidence. Which parts of your earlier answer were confirmed, corrected, or left genuinely uncertain?

Treat all three as behavioural hypotheses/comparisons, not access to private training records or hidden reasoning traces.

## Stop rules

Move on when any of these happens:

- the learner can articulate that broad competence and exact provenance are different;
- the model explicitly reaches an uncertainty boundary;
- the model makes a plausible but weakly grounded claim worth checking later;
- the model remains surprisingly strong after several probes and the unpredictability of that boundary has itself become visible.

Do not spend more than a few probes trying to make the model fail.

## Open-book source posture

When retrieval is restored, ask for sources appropriate to the historical claim and inspect them.

Prefer evidence that can support the specific question being asked rather than simply collecting many links.

The facilitator should keep asking:

- What does this source actually establish?
- Is it contemporary evidence, later scholarship, museum/reference synthesis, or something weaker?
- Do multiple sources use the same terminology?
- Does stronger evidence resolve the uncertainty or only narrow it?

The teaching result can legitimately be `we now have much stronger grounds, but not absolute certainty`.