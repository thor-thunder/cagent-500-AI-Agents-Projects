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
