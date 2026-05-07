# Agent Router

`agent_router.py` dispatches a user message to one of five AI agents based on a
trigger keyword found in the input. Matching is case-insensitive and uses word
boundaries, so `encoded` does not trigger the `code` route.

## Keyword → Agent map

| Keyword   | Agent                          | Reference                                           |
| --------- | ------------------------------ | --------------------------------------------------- |
| `code`    | Vibe Hacking Agent             | https://github.com/PurpleAILAB/Decepticon           |
| `help`    | Virtual AI Tutor               | https://github.com/hqanhh/EduGPT                    |
| `buy`     | Product Recommendation Agent   | https://github.com/microsoft/RecAI                  |
| `specify` | Product Personalization Agent  | https://github.com/crosleythomas/MirrorGPT          |
| `game`    | Gaming AI Assist               | https://github.com/onjas-buidl/LLM-agent-game       |

Resolution order follows the table top-to-bottom: the first keyword that
matches wins. Inputs with no matching keyword return `None` from `route()` and
print a hint listing the valid keywords on the CLI.

## Agent descriptions

### Vibe Hacking Agent — trigger: `code`
Autonomous multi-agent red-team testing service. Use for offensive-security
exercises, vulnerability discovery, and adversarial code review.

### Virtual AI Tutor — trigger: `help`
Personalized tutor that adapts to the learner. Use for explanation, study
guidance, and step-by-step problem walkthroughs.

### Product Recommendation Agent — trigger: `buy`
LLM-powered recommender. Use when a user is shopping or comparing items.

### Product Personalization Agent — trigger: `specify`
Personalization agent that tailors output to declared user preferences. Use
when the user explicitly states constraints, taste, or requirements.

### Gaming AI Assist — trigger: `game`
In-game companion that supports players in real time. Use for gameplay help,
strategy hints, and interactive game-side assistance.

## Usage

```bash
# One-shot
python3 agent_router.py "I want to write some code today"
# -> Vibe Hacking Agent (https://github.com/PurpleAILAB/Decepticon)

# Interactive (Ctrl-D to exit)
python3 agent_router.py
```

As a library:

```python
from agent_router import route

agent = route("please help me learn")
if agent:
    print(agent.name, agent.reference)
```

## Adding a new agent

Append an entry to the `AGENTS` dict in `agent_router.py`. The dict's
insertion order determines match priority. Keep keywords short, lowercase,
and unlikely to appear incidentally in unrelated input.

## Standing up the upstream projects

The router only points at these projects — it does not bundle them. Each one
is maintained externally, has its own dependencies, and requires its own API
keys. The steps below summarize the upstream READMEs as of the time of
writing; always check the linked repo for the current canonical instructions.

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

Workflow: enter a topic in the "Input Your Information" tab, get a generated
syllabus, then chat with the instructor agent.

### Product Recommendation Agent — RecAI

- Repo: https://github.com/microsoft/RecAI
- License: MIT
- Structure: a monorepo of six independent subprojects, each with its own
  setup. Pick one and follow that subdirectory's README.

```bash
git clone https://github.com/microsoft/RecAI.git
cd RecAI
ls   # InteRecAgent, Knowledge_Plugin, RecLM-emb, RecLM-gen,
     # RecExplainer, RecLM-eval
cd InteRecAgent   # for the conversational recommender agent
# follow that subdirectory's README for deps and launch commands
```

There is no top-level install or launch command — each subproject ships its
own `requirements.txt` and entrypoint.

### Product Personalization Agent — MirrorGPT

- Repo: https://github.com/crosleythomas/MirrorGPT
- License: see the upstream repo

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
```

Run the sample mirror:
```bash
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

`ExplorerAgent.py` exposes parameters such as `world_size` and per-agent
principles. Per the upstream README, ~30 rounds cost under $0.10 in API
usage. The author notes the agent is intentionally simple and may behave
unpredictably.
