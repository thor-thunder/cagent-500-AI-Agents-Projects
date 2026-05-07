# Agent Router

`agent_router.py` dispatches a user message to one of five AI agents based on a
trigger keyword found in the input. Each agent is implemented locally in
`agents.py` and runs without any external API calls.

Matching is case-insensitive and uses word boundaries, so `hackathon` does not
trigger the `hack` route and `decoded` does not trigger the `code` route.

## Keyword → Agent map

| Keyword   | Agent                          | Reference                                           |
| --------- | ------------------------------ | --------------------------------------------------- |
| `hack`    | Vibe Hacking Agent             | https://github.com/PurpleAILAB/Decepticon           |
| `code`    | Virtual AI Tutor               | https://github.com/hqanhh/EduGPT                    |
| `buy`     | Product Recommendation Agent   | https://github.com/microsoft/RecAI                  |
| `specify` | Product Personalization Agent  | https://github.com/crosleythomas/MirrorGPT          |
| `game`    | Gaming AI Assist               | https://github.com/onjas-buidl/LLM-agent-game       |

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

### Product Recommendation Agent — trigger: `buy`
Detects a category (headphones, laptop, phone, coffee, books) and returns
ranked picks with rationale and price. Honors a stated budget such as
`under $300`; lists stretch picks separately when present.

### Product Personalization Agent — trigger: `specify`
Parses preference statements (`I like X`, `I prefer Y`, `I dislike Z`,
`I want W`, `under $N`) and returns a structured profile plus suggested next
steps, including a hand-off into the `buy` route when a concrete want is
detected.

### Gaming AI Assist — trigger: `game`
Detects game genre (chess, FPS, RPG, strategy, puzzle) and returns concise
strategy tips per genre. Multiple genres in one prompt produce multiple
sections.

## Usage

```bash
# One-shot
python3 agent_router.py "I want to buy headphones under \$300"

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

## Adding a new agent

1. Write a handler in `agents.py` with the signature `def handler(prompt: str) -> str`.
   It must be deterministic and must not call any external API.
2. Append an entry to the `AGENTS` dict in `agent_router.py`. Insertion order
   determines match priority. Choose a keyword that is short, lowercase, and
   unlikely to appear incidentally in unrelated input.
3. Add a row to the keyword table above and a description below.

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

### Product Recommendation Agent — RecAI

- Repo: https://github.com/microsoft/RecAI
- License: MIT
- Structure: a monorepo of six independent subprojects, each with its own
  setup. Pick one and follow that subdirectory's README.

```bash
git clone https://github.com/microsoft/RecAI.git
cd RecAI
cd InteRecAgent   # or another subproject
# follow that subdirectory's README for deps and launch commands
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
