# Core principles

These are the ideas to reinforce throughout the lab. They are more important than any particular product, command, model, or framework.

## The learner directs work rather than manually reproducing it

This curriculum is not a coding course and does not require the learner to become the manual implementation layer for an agent.

The core learning loop is:

> **Learner instruct -> Agent do -> Learner inspect, verify and question -> Agent explain -> Learner instruct again.**

The learner should become increasingly good at deciding what outcome they want, placing the agent in an appropriate environment, inspecting what actually happened, questioning unfamiliar machinery, and using the explanation to steer the next iteration.

The central methodology is:

> **The learner knows how to use agents to accomplish things before they fully understand the implementation, while using the work itself to progressively build that understanding.**

Do not hide code, Git operations, configuration, scripts, SQL, or other technical artifacts merely because the learner cannot yet produce them manually. Let the agent do useful work, then use the work itself as material for inspection and learning.

This method should generalise beyond the curriculum. If the learner later wants to learn programming or another unfamiliar technical craft, the same loop applies.

See [Learning methodology and origin](learning-methodology.md) for the fuller curriculum-wide statement and the repository's own origin story.

## Teach with useful interim mental models, then deliberately break them

Do not try to give the learner the most complete version of a concept the first time it appears.

Some agentic ideas are too large, too layered, or too abstract to become useful if explained in their final form before the learner has enough experience to attach them to.

Instead, give the learner a mental model that is:

- true enough for the work in front of them;
- simple enough to hold in their head;
- useful enough to act with;
- incomplete in ways that later experience can expose.

Let that model sit long enough to become operational knowledge.

Then, in a later lab, do not simply announce that the model was incomplete. Ask the learner what they currently believe, introduce a requirement or example that the current model cannot explain well, and let the contradiction create the need for a better model.

The progression should look like:

```text
useful mental model
        ↓
learner uses it successfully
        ↓
new requirement or counterexample appears
        ↓
current model stops being sufficient
        ↓
learner inspects the mismatch
        ↓
old model is broken deliberately
        ↓
new model explains both the old case and the new one
```

The earlier model should not be treated as a trick or a lie. It was a fair model at the learner's current level of abstraction.

The curriculum should repeatedly use this pattern on the same idea until the learner reaches a more refined understanding.

For example, an early learner may reasonably think of an Agent as the worker they are talking to. Later, after provisioning tools, instructions, skills, domain material, state, permissions, and verification, they may reasonably think:

> We built an environment for this job. Did we effectively create an Agent?

That is a useful model for a while.

Later, when a project needs several workers with different roles, tools, permissions, instructions, and workflows, that model should be put under pressure. The learner can then discover why a broader environment may support multiple distinct agent profiles and why an invoked specialist sub-agent is a more precise unit of agency for some work.

Do not front-load custom profiles, sub-agent-driven development, orchestration, or other advanced machinery before the learner has felt the limitation that makes those ideas necessary.

> **Teach a model the learner can use now. Break it when reality gives them a reason to need a better one.**

The facilitator should avoid saying, in effect, `forget what we told you before`. The stronger move is:

> What do you think is happening now?

then:

> What if we needed to do this?

and finally:

> Does our current model still explain the situation, or do we need a better one?

The learner should experience conceptual refinement as discovery rather than correction from authority.

## When the learner knows the domain, provision that expertise

The earlier learning loop often starts from learner uncertainty: the agent does work, the learner inspects it, and the agent explains unfamiliar implementation.

Once the learner is proficient in a domain, the normal direction changes.

The learner should make enough of their domain expertise available to the agent before expecting specialist work.

> **Expertise should be provisioned, not repeatedly performed.**

The learner's expertise is not only for correcting bad work after the fact. It belongs in the agent's operating environment through appropriate combinations of:

- project instructions;
- source and reference material;
- examples of good and bad work;
- standards and conventions;
- tools;
- reusable skills/workflows;
- quality criteria and verification checks.

A repeated correction should trigger a question:

> Is this a one-off mistake, or did we just reveal something the agent's environment should know from now on?

If nobody in the loop knows what good looks like, plausible output can masquerade as good work.

Domain knowledge can also be distributed. One expert is not always required; useful working knowledge may be assembled from partial human expertise, source material, standards, examples, tools, and feedback.

Module 6 should teach this through a deliberate three-domain progression: coding with facilitator domain authority, novel writing with shared/partial authority, and technical drawing with learner domain authority.

## The conversation is not the project

A chat is a useful interface for thinking and asking questions. A project needs durable state that can be inspected, changed, versioned, and revisited independently of one conversation.

## Context is not the same as state

Memory and retrieved context can help continuity, but authoritative project state should live somewhere explicit and inspectable.

A useful shorthand:

> Memory is context. Files are state.

## Do not make the human act as the filesystem

If the real project already exists on disk, repeatedly uploading files, downloading outputs, copying changes back, and explaining which version is current creates unnecessary human synchronisation work.

Where appropriate, let the agent work where the project actually lives.

## Separate model capability from configuration

Observed behaviour comes from more than the model:

**model + harness + instructions/settings + context + tools + environment + feedback**

A preference for shorter responses, different formatting, or a particular workflow may be a harness or configuration preference rather than evidence that one underlying model is categorically better.

When something works badly, ask:

> Is this a model problem, a context problem, a harness problem, a tool problem, or a feedback problem?

## Give the agent the right tools

A capable model with the wrong tool is still badly equipped.

Image generation is not a technical drawing system. A technical drawing may need deterministic vector, CAD, geometry, rendering, or measurement tools.

Project environments should expose capabilities appropriate to the work being done.

## Tools and operating knowledge belong together

Provisioning a rich tool does not teach competent use of that tool.

A useful distinction:

- **Tool or MCP:** What can I do?
- **Skill:** How should I do this kind of work?
- **Project instructions:** What rules apply in this project?
- **Task:** What are we trying to accomplish now?

Rich tool surfaces create a larger decision space. They become more useful when paired with procedural guidance that teaches the agent when to use a capability, how to combine operations, what counts as success, and when a different route is better.

> Tools expose verbs. Skills teach workflows.

## Local access and connectors are complementary

A connector is excellent when the agent needs to reach an external system such as GitHub, email, a calendar, an issue tracker, or a database.

Direct project access is better suited to deep exploration of a local project: walking directories, reading many files, grepping, inspecting history, running scripts, rendering output, and discovering things nobody knew to retrieve explicitly.

> Retrieval asks for something. Exploration discovers what is there.

Neither replaces the other.

Do not teach `on-disk good, cloud bad`. Different surfaces expose different state, capabilities, permissions, and safety boundaries. Select the environment that fits the task.

The learning-lab repository itself is a useful proof point: substantial curriculum development was carried out through cloud ChatGPT using a GitHub connector after only minimal manual setup.

## Prefer evidence over agent claims

An agent saying it changed something is not proof that it changed it correctly.

Verification may mean inspecting a diff, reading the file, rendering a document, running a check, searching for an old value, testing dimensions, or checking remote publication state.

> Do not trust that work happened when you can inspect whether it happened.

## Safe breakage is part of learning

The goal is not to avoid mistakes. The goal is to make mistakes cheap and recoverable.

Replace:

> I should not try this because I might break something.

with:

> What is the blast radius, and do I have a recovery path?

Source control, disposable examples, narrow permissions, and clear project boundaries make experimentation safer.

Be fearless with reversible state. Be deliberate with external side effects such as sending messages, deleting remote records, publishing, spending money, or changing real permissions.

## The learner defines success, legal routes, and good enough

As the curriculum moves from isolated tasks into skills, loops, graphs, and autonomous workflows, the learner is doing more than describing an output.

They are increasingly defining:

- what counts as success;
- which transitions/actions are legal;
- what evidence counts as progress;
- what `good enough` means;
- which failures should be retried;
- which conditions require a stop;
- where control should go when normal progress is impossible.

Do not explain systematic agent behaviour as personality when the environment already made that behaviour reasonable.

A useful model at this stage is:

> **The agent is looking for a legal route to something that appears to satisfy the task success condition.**

If the easiest legal route is an overly broad escalation path, the agent may hand difficult work back too early. If no legal escape exists, the agent may churn inside a loop that cannot converge. Neither requires the agent to be `lazy`, `cheeky`, or inherently attracted to escape hatches.

Ask instead:

> Who defined the success condition?

> Who defined the legal routes from the start state to the goal?

> Who defined what good enough looks like?

At this stage of the curriculum, the answer is largely the learner, directly or through the environment they provisioned.

A reusable diagnostic question is:

> **What did we make it reasonable for the agent to believe counted as success?**

## Loops need termination models and bounded escape routes

A continuation rule alone does not make a robust loop.

A workflow should distinguish:

- keep trying because a plausible corrective route still exists;
- stop because more trying cannot resolve the underlying problem;
- escalate because the remaining decision belongs to a different authority.

Useful distinctions:

- **stop condition:** when the current loop must not continue;
- **escalation path:** what happens after the stop;
- **escape hatch:** an exceptional legal route out of the normal workflow.

A missing escape hatch can turn impossible work into endless activity. An overly broad escape hatch can become an easy legal route around difficult-but-solvable work.

> **Exceptional exits need explicit entry conditions.**

A strong escape condition should be grounded in evidence such as recurrence, incompatible authoritative requirements, bounded retries, no new evidence, or missing authority.

> **A robust workflow defines not only how to continue, but how to recognise non-progress, how to stop, and which authority receives the unresolved decision.**

As soon as a loop can pass, retry, return, stop, or escalate depending on state, the learner has earned a graph-shaped mental model without needing graph theory.

## Teach invariants; let techniques emerge

Teach ideas such as source of truth, recovery, verification, isolation, bounded authority, persistent state, termination, and legal workflow transitions directly.

Let advanced techniques such as elaborate Git workflows, RAG, multi-agent orchestration, CI/CD, complex MCP setups, and sophisticated automation arrive when the learner encounters the problem they solve.
