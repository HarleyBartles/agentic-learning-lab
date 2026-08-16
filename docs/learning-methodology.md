# Learning methodology and origin

This document records the curriculum-wide teaching method behind the Agentic Learning Lab and the origin story that should be revisited at the end of the curriculum.

## This is not a coding course

The curriculum does not teach the learner to code, operate Git manually, write shell commands, build databases by hand, or become the manual implementation layer for an agent.

It teaches the learner to use agents to achieve goals while progressively understanding the work those agents perform.

The learner's role is to:

- decide what outcome they want;
- instruct the agent;
- place the agent in an environment where the work can happen;
- inspect what the agent actually did;
- verify the result against evidence rather than trusting the completion message;
- question anything they do not understand;
- ask the agent to explain its implementation and reasoning;
- use that new understanding to give the next instruction.

The core loop is:

> **Learner instruct -> Agent do -> Learner inspect, verify and question -> Agent explain -> Learner instruct again.**

The loop is iterative. The learner does not need a complete specification or complete implementation knowledge before useful work can begin.

## Accomplish first; understand progressively

The central methodology is:

> **The learner knows how to use agents to accomplish things before they fully understand the implementation, while using the work itself to progressively build that understanding.**

This is not an argument for remaining ignorant of implementation. It is a way to enter unfamiliar implementation without requiring mastery as a prerequisite for useful work.

Code, Git commands, configuration, SQL, scripts, tool calls, technical drawings, or other technical artifacts should not be hidden merely because the learner does not yet know how to produce them manually.

Instead:

1. let the agent perform useful work;
2. inspect the artifact or state it produced;
3. verify that the result is real and correct enough to continue;
4. ask the agent to explain unfamiliar parts;
5. change the requirement and inspect what changes;
6. repeat until the learner's mental model becomes stronger.

This means the curriculum can teach the learner **how to learn with an agent** beyond the curriculum itself.

If the learner later wants to learn programming, CAD, data analysis, automation, electronics, research practice, or another unfamiliar craft, the same loop applies. They do not need to wait until they have completed a conventional course before attempting a meaningful project. They can use real agent work as material for inspection, questioning, explanation, correction, and progressively deeper understanding.

## The learner is not the agent's hands

The curriculum should avoid turning technical knowledge into unnecessary manual ceremony.

The learner does not need to type a Git command merely to prove they know what Git is doing. They do need to understand the state transition the command caused well enough to direct the agent and judge the result.

The learner does not need to hand-write a Python script merely to be allowed to use one. They should be able to inspect the script, ask what it does, understand why it exists, run or verify it appropriately, and direct changes to it.

A useful test is:

> Are we teaching a durable mental model and the ability to direct work, or are we making the learner imitate actions the agent can already perform safely?

## Do not turn access surfaces into a hierarchy

The curriculum must not become `on-disk good, cloud bad`.

Different agent surfaces expose different project representations, capabilities, permissions, costs, and safety boundaries. The correct question is not which surface is morally or universally superior. It is which environment gives the agent the state and capabilities needed for the task.

This repository itself is evidence of that principle.

During the early curriculum-design phase, including the creation of the first mature labs and the detailed planning of Lab 4, Harley's manual setup was minimal:

1. create the GitHub repository;
2. connect the repository to the cloud ChatGPT GitHub connector;
3. discuss, inspect, question, and steer.

The repository was then developed through cloud ChatGPT using the GitHub connector. An on-disk agent was not required to produce the mature curriculum structure that existed at that point.

That history should be preserved as a deliberate counterexample to any simplistic message that serious agentic work requires an on-disk agent. Direct local access is extremely useful for some jobs. Connector-mediated cloud work can also produce substantial, persistent, inspectable project state when the access surface is appropriate.

The lesson is the one established earlier in the curriculum:

> Agents can work through different surfaces. What matters is where authoritative state lives, what environment the agent is working in, and what capabilities that environment provides.

## The repository is a worked example of the methodology

The Agentic Learning Lab did not begin from a complete curriculum specification.

It emerged through the same loop the curriculum teaches:

```text
vague goal
    ↓
learner instruction
    ↓
agent proposes or changes project state
    ↓
learner inspects, questions, accepts, rejects, or redirects
    ↓
agent explains and revises
    ↓
useful decisions are persisted
    ↓
repeat
```

The facilitator knew enough to drive the process critically. They did not need to know the complete shape of the finished curriculum before beginning.

This is an important distinction to make explicit in the epilogue:

> The interesting fact is not that the facilitator already knew how to build the finished framework.
>
> The facilitator knew enough to drive the process critically, inspect what emerged, reject weak ideas, preserve useful ones, and keep iterating.

## Verbatim origin prompt

The following is the first prompt that started the curriculum-design conversation. Preserve it verbatim for the final retrospective. Do not tidy it into a better specification before showing it to the learner.

> I'm going to teach my brother a few things about using agentic AI. I don't really have a learning plan or anything. I know a whole bunch of stuff through my own hard earned learning but not sure what's valuable to pass on and what's better to allow him to discover. He's not dumb, he's an intelligent guy. He's not a coder though - I think I'll need to start with some basic engineering concepts like source control. For example, the benefit of having a repo for your agents to work in for a project - project isolation, persistent agent operating environment and so on. 
>
> He doesn't yet know what he really wants to do with AI so we need to give him the use cases. For example he'll have the preconception of "I don't need agents on disk, chatgpt in the cloud serves my purposes so far" which we'll want to break by showing him how having agents on disk enables them to deep dive a project (repo) and work in a proper setup agentic operating environment, even if the repo's concern isn't code. We can also show examples such as "if you're asking a cloud agent to write something and you're copying and pasting or downloading the output to your computer, why not just get an on-disk agent to write the thing directly" and so on.
>
> What do you think a learning plan should look like. I'm not a teacher, he's not my student. We'll teach and learn conversationally with examples probably from my own repo's. 

The prompt matters because it is visibly incomplete, contains assumptions that the curriculum later complicated, and does not remotely specify the framework that eventually emerged.

In particular, the initial prompt leans toward breaking a `cloud is enough` preconception by demonstrating on-disk work. The resulting curriculum became more nuanced: cloud, local, connected, and mixed environments are selected according to what the project and task require. The repository's own construction through a cloud connector is evidence of that refinement.

## Final retrospective principle

At the end of the curriculum, the learner should be able to look back at this repository and recognise that the method used to build the course is the same method they have been taught to use elsewhere:

> Start before you know everything. Give the agent a real environment and a useful goal. Inspect the work. Verify it. Ask why. Correct it. Persist what matters. Then instruct again.

The goal is not dependence on an agent's answers. The goal is progressively stronger learner judgment while the agent performs more of the implementation work.