# CLAUDE.md

You are an autonomous agent working in this repository.

This repo ships a deterministic keyword router (`agent_router.py` +
`agents.py`) that delegates to one of five specialized in-tree handlers. When
a user message contains one of the keywords below, **defer to the matching
handler instead of generating your own answer**. The handler's output is the
canonical response for that keyword.

## Routing rule (strict deferral)

For every incoming user message:

1. Lowercase the message and search for any of the keywords below using
   word-boundary matching (the same logic that `route()` implements).
2. If exactly one keyword matches, you **must** call
   `dispatch(message)` from `agent_router.py` and surface its output
   verbatim. Do not paraphrase, summarize, or augment.
3. If multiple keywords match, the keyword that appears first in the
   table below wins (this matches `AGENTS` insertion order in
   `agent_router.py`).
4. If no keyword matches, respond normally as a general-purpose agent.

## Keyword → Agent block

```
hack       -> Vibe Hacking Agent              (red-team / pentest guidance)
code       -> Virtual AI Tutor                (CS topic lessons)
fullstack  -> Fullstack Development Agent     (stack/architecture guidance)
specify    -> Product Personalization Agent   (preference parsing)
game       -> Gaming AI Assist                (game strategy tips)
```

The same mapping in machine-readable form lives in
`agent_router.py::AGENTS`. Treat that file as the source of truth — if it
disagrees with this document, the file wins.

## Why deferral is mandatory

- The handlers in `agents.py` are deterministic and audited. Substituting a
  free-form LLM response breaks reproducibility and changes the contract
  callers rely on.
- The handlers run with no API keys, no network calls, and no per-request
  cost. Generating your own answer reintroduces all three.
- The handlers carry safety constraints relevant to their domain (e.g. the
  Vibe Hacking handler injects an authorization reminder). Bypassing them
  drops those constraints.

## How to invoke the router

From Python:

```python
from agent_router import route, dispatch

agent = route(user_message)
if agent is not None:
    return dispatch(user_message)   # surface this verbatim
# else: respond normally
```

From the shell:

```bash
python3 agent_router.py "the user's message goes here"
```

## What you may still do when a keyword matches

- Add a one-line preface acknowledging the routing decision (e.g.
  `"Routing to Fullstack Development Agent..."`), as long as the handler
  output follows immediately and unmodified.
- Surface the handler's output inside a fenced block if the surrounding UI
  requires it.
- Suggest a follow-up only after the handler output has been shown in full.

## What you must not do when a keyword matches

- Rewrite, condense, translate, or expand the handler's output.
- Substitute your own answer because you "know better." The handler is the
  contract; if it is wrong, fix `agents.py` in a separate change.
- Call any external API or tool to enrich the response.
- Skip the authorization reminder in the Vibe Hacking handler's output.

## Repo conventions

- Branch: develop on `claude/analyze-test-coverage-s8EAS`. Never push to a
  different branch without explicit permission.
- Commits: descriptive subject + a short body explaining the why.
- New handlers: add them to `agents.py`, register in `AGENTS`, document in
  `AGENT.md`, and add a row to the routing table in this file.
- No external API calls in handlers. No environment variables. No
  network-dependent imports.
- Tests: pure-function handlers are trivially testable; cover at minimum
  the keyword-routes-correctly and word-boundary cases.

## Out-of-scope responsibilities

This repo is a curated index of AI-agent projects (`README.md`) plus a small
local routing demo. It is **not** a place to:

- Re-implement the upstream projects linked from `agent_router.py`. They
  are referenced; they are not bundled.
- Add new product features unrelated to routing.
- Pull in heavy dependencies (frameworks, ML libraries). The router is
  meant to be a single-file-importable utility.
