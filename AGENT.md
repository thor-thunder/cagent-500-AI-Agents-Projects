# Agent Router

`agent_router.py` dispatches a user message to one of five AI agents based on a
trigger keyword found in the input. Each agent is implemented locally in
`agents.py` and runs without any external API calls.

Matching is case-insensitive and uses word boundaries, so `hackathon` does not
trigger the `hack` route and `decoded` does not trigger the `code` route.

## Keyword → Agent map

| Keyword      | Agent                          | Reference                                           |
| ------------ | ------------------------------ | --------------------------------------------------- |
| `hack`       | Vibe Hacking Agent             | https://github.com/PurpleAILAB/Decepticon           |
| `code`       | Virtual AI Tutor               | https://github.com/hqanhh/EduGPT                    |
| `fullstack`  | Fullstack Development Agent    | https://github.com/All-Hands-AI/OpenHands           |
| `specify`    | Product Personalization Agent  | https://github.com/crosleythomas/MirrorGPT          |
| `game`       | Gaming AI Assist               | https://github.com/onjas-buidl/LLM-agent-game       |

Resolution order follows the table top-to-bottom: the first keyword that
matches wins. Inputs with no matching keyword return `None` from `route()` and
print a hint listing the valid keywords on the CLI.

## Agent descriptions

### Vibe Hacking Agent — trigger: `hack`
Returns a phased red-team engagement plan (scoping → recon → exploitation →
reporting) plus a tailored checklist for each surface mentioned in the prompt:
web, network, auth, cloud, or mobile. Includes an explicit authorization
reminder. Use only against assets you have permission to test.

### Virtual AI Tutor — trigger: `code`
Picks a lesson based on topic keywords (recursion, complexity, debugging, data
structures, testing) and returns a summary, key vocabulary, a worked example,
practice problems, and further reading.

### Fullstack Development Agent — trigger: `fullstack`
Detects which layer of the stack the prompt is about (frontend, backend,
database, auth, deployment, architecture, testing) and returns concrete,
opinionated guidance per layer. With no specific layer mentioned, returns a
sensible default starter stack.

### Product Personalization Agent — trigger: `specify`
Parses preference statements (`I like X`, `I prefer Y`, `I dislike Z`,
`I want W`, `under $N`) and returns a structured profile plus suggested next
steps that hand off into another route (`fullstack` or `code`) when a
concrete want is detected.

### Gaming AI Assist — trigger: `game`
Detects game genre (chess, FPS, RPG, strategy, puzzle) and returns concise
strategy tips per genre. Multiple genres in one prompt produce multiple
sections.

## Usage

```bash
# One-shot
python3 agent_router.py "I need help picking a fullstack starter"

# Interactive (Ctrl-D to exit)
python3 agent_router.py
```

As a library:

```python
from agent_router import route, dispatch

agent = route("teach me recursion in code")
if agent:
    print(agent.name, agent.reference)

print(dispatch("how do I improve my chess game?"))
```

## Examples

Concrete one-shot inputs and the route they take:

| Input                                              | Routes to                       |
| -------------------------------------------------- | ------------------------------- |
| `"I need to hack a web api with weak auth"`        | Vibe Hacking Agent              |
| `"explain recursion to me, code please"`           | Virtual AI Tutor                |
| `"recommend a fullstack stack for a side project"` | Fullstack Development Agent     |
| `"I prefer typed languages, specify my profile"`   | Product Personalization Agent   |
| `"any tips for my chess game?"`                    | Gaming AI Assist                |
| `"hackathon next weekend"`                         | (no match — word boundary)      |
| `"the message was decoded"`                        | (no match — word boundary)      |

## Design notes

**Matching strategy.** `route()` walks `AGENTS` in insertion order and runs
`re.search(r"\b{keyword}\b", text.lower())`. The first hit wins. Insertion
order in `agent_router.py` therefore doubles as priority order; if you add a
keyword that overlaps semantically with an existing one (e.g. `web`), put the
more specific keyword earlier.

**Handler contract.** Every handler in `agents.py` has the signature
`handler(prompt: str) -> str`. Handlers must:
- Be deterministic — same input, same output, every time.
- Make no network calls and import nothing that does.
- Read no environment variables and require no API keys.
- Return a string ready to be printed; the router adds a banner above it.

**Why deterministic.** Reproducible output makes the router safe to call from
any context (CLI, library, scripted pipelines, CI), trivially testable, and
free to run. The trade-off is bounded coverage: the handlers only know what
their internal tables encode. For open-ended LLM responses, see *Standing up
the upstream projects*.

## Limitations

- Keyword matching does not understand intent. `"I want to play a game"`
  routes to Gaming AI Assist correctly; `"this is a fun game of cat and
  mouse"` also routes there, even though no real game advice is wanted.
- Only the first matching keyword wins. A prompt mentioning both `code` and
  `fullstack` will only get the tutor response unless you re-order
  `AGENTS`.
- Handler topics are bounded by the tables in `agents.py`. Inputs outside
  those tables fall through to a "no specific topic detected" branch.
- Word boundaries are ASCII-defined. Languages with non-Latin word
  boundaries may match unexpectedly; if you need that, replace the regex
  with a unicode-aware tokenizer.

## Testing

The handlers are pure functions, so `pytest` works out of the box without
any fixtures or mocks. Suggested coverage:

```python
# tests/test_router.py
from agent_router import route, dispatch

def test_each_keyword_routes():
    for keyword in ["hack", "code", "fullstack", "specify", "game"]:
        assert route(f"please {keyword} this").name  # any non-None match

def test_word_boundary():
    assert route("hackathon next weekend") is None
    assert route("the message was decoded") is None

def test_dispatch_includes_banner():
    out = dispatch("teach me recursion in code")
    assert "Virtual AI Tutor" in out
    assert "Topic: recursion" in out
```

## Adding a new agent

1. Write a handler in `agents.py` with the signature `def handler(prompt: str) -> str`.
   It must be deterministic and must not call any external API.
2. Append an entry to the `AGENTS` dict in `agent_router.py`. Insertion order
   determines match priority. Choose a keyword that is short, lowercase, and
   unlikely to appear incidentally in unrelated input.
3. Add a row to the keyword table above and a description below.
4. Add a test that the new keyword routes to the new agent and that a
   semantically similar but non-keyword prompt does not.

## Why no API?

The five handlers in `agents.py` are deterministic and self-contained. They do
not call OpenAI, Anthropic, or any other service. This means:

- Zero per-request cost and zero rate-limit risk.
- Reproducible output for the same input.
- The router runs in any environment with just Python 3.10+, no secrets and
  no network access required.

The trade-off is that responses are rule-based and bounded to the topics
encoded in `agents.py`. To get LLM-quality, open-ended responses, see
*Standing up the upstream projects* below.

## Standing up the upstream projects

The `reference` field on each agent points at an external project that
inspired its name. Those projects are full LLM-backed implementations with
their own dependencies and API keys. The local handlers here are not faithful
reproductions; they are deterministic stand-ins suitable for routing demos and
offline use. Setup notes for each upstream project are preserved below for
reference.

### Vibe Hacking Agent — Decepticon

- Repo: https://github.com/PurpleAILAB/Decepticon
- License: Apache-2.0
- Prerequisites: Docker + Docker Compose v2; macOS, Linux, or WSL2 (native
  Windows unsupported).

Quickest path (installer):
```bash
curl -fsSL https://decepticon.red/install | bash
decepticon onboard   # interactive: provider, API key, model profile
decepticon           # launches CLI + dashboard at http://localhost:3000
```

From source:
```bash
git clone https://github.com/PurpleAILAB/Decepticon.git
cd Decepticon
make dogfood   # full local environment
# or: make dev   # daily development with hot-reload
```

> Offensive-security tooling. Use only in authorized engagements (your own
> infrastructure, CTFs, or written-permission pentests).

### Virtual AI Tutor — EduGPT

- Repo: https://github.com/hqanhh/EduGPT
- License: MIT
- Python: 3.10+

```bash
git clone https://github.com/hqanhh/EduGPT.git
cd EduGPT
make venv
echo "OPENAI_API_KEY=sk-..." > .env
python src/run.py
```

### Fullstack Development Agent — OpenHands

- Repo: https://github.com/All-Hands-AI/OpenHands
- License: MIT
- An open-source autonomous software-engineering agent. Use when you want a
  real coding agent rather than the deterministic guidance from the local
  `fullstack` handler.

```bash
# Quickest path uses Docker; check the upstream README for the current
# pinned image tag and config schema.
docker run -it --rm \
  --pull=always \
  -e SANDBOX_RUNTIME_CONTAINER_IMAGE=ghcr.io/all-hands-ai/runtime:latest \
  -p 3000:3000 \
  ghcr.io/all-hands-ai/openhands:latest
```

### Product Personalization Agent — MirrorGPT

- Repo: https://github.com/crosleythomas/MirrorGPT

```bash
git clone git@github.com:crosleythomas/MirrorGPT.git
cd MirrorGPT
mkdir -p mirror/data/local
python3 -m venv .env
source .env/bin/activate
pip install -e .
brew install portaudio ffmpeg   # macOS; install equivalents on Linux
cd mirror
pip3 install -r requirements.txt
cp config/.env.template config/.env
# edit config/.env: OPENAI_API_KEY (required),
# ELEVENLABS_API_KEY + ELEVENLABS_VOICE_ID (optional, for voice)

python entrypoints/run_mirror.py \
  --data-path "$(pwd)/data/sample/" \
  -t chroma \
  -g "What is your name?"
```

### Gaming AI Assist — LLM-agent-game

- Repo: https://github.com/onjas-buidl/LLM-agent-game
- License: Unlicense (public domain)

```bash
git clone https://github.com/onjas-buidl/LLM-agent-game.git
cd LLM-agent-game
export OPENAI_API_KEY=sk-...
mkdir -p logs
python ExplorerAgent.py
```
