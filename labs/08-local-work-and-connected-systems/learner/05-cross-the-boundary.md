# 05 — Cross the boundary

So far the worker has been navigating state that exists inside its local project environment.

Now ask:

> **What if the state we need is somewhere else?**

## Local evidence

Ask the local worker to inspect the repository-integrity workflow and its checker/tests.

Ask:

> **What do these checked-in files establish about what should happen when the repository-integrity workflow runs?**

Keep the answer bounded to what local source can establish.

## Connected evidence

Now use the GitHub-connected worker.

Prefer this question when workflow-run access is available:

> **Did the latest repository-integrity workflow run for the relevant remote commit actually complete successfully? Show me the remote evidence.**

If workflow-run state is unavailable, use another remote fact such as the current remote branch head, whether a known PR exists, or whether a commit is present remotely.

Compare:

```text
local source
what is configured or intended to happen

GitHub remote state
what GitHub records as actually having happened remotely
```

Neither surface is universally better. They answer different questions.

Also keep this distinction:

> **Retrieval and exploration are strategies. Local and connected are access surfaces.**

A local agent can retrieve something precisely. A connector can explore a remote system. The useful question is always:

> **What surface am I observing, through what route, and what does that observation actually establish?**

## Final questions

Imagine the worker can now reach:

- local working state;
- GitHub remote state;
- a project note describing what should be true.

They do not necessarily agree.

Ask:

> **Which one should the worker trust?**

Then ask:

> **What would actually prove that the required work is correct?**

Keep those questions.

The next lab starts there.