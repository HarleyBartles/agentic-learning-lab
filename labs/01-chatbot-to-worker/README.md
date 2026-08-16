# Lab 1 — From chatbot to worker

Status: **Mature and ready to run.**

This lab is the complete learning experience for Module 1.

It has three deliberately separate repository surfaces:

- `learner/` contains the learner-facing exercise cards. Reveal them one at a time.
- `mission/` is the actual working project used in the exercises.
- `facilitator/` contains the rationale, setup, prompts, observations, and teaching notes for running the lab.

Across those materials, the learner runs the same mission four times under different environmental constraints:

1. ordinary cloud ChatGPT with complete context supplied into the conversation;
2. ordinary cloud ChatGPT with critical context omitted;
3. a local Codex worker operating directly in the mission workspace;
4. cloud ChatGPT inside a persistent ChatGPT Project populated with the mission material.

The learner should work from the current learner card rather than reading all of the facilitator material or later cards in advance.

The on-disk worker used in Exercise 3 should be scoped to `mission/`, not to this whole lab directory. That keeps the worker's project environment limited to the task contract, source material, and output area rather than exposing the teaching choreography.

Exercise 4 deliberately creates a separate cloud project environment rather than connecting ChatGPT to the repository. The learner manually populates that cloud environment so they can observe both the benefit of persistent cloud project context and the remaining human responsibility for keeping separate project environments fresh.

The machinery that makes the local scope convenient, and the deeper mechanics behind ChatGPT Projects, are not the subject of Lab 1. The learner is observing how different environments change context and artifact transport before later labs explain the mechanisms in detail.
