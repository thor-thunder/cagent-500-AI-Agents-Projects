"""Keyword-based router that dispatches user input to one of the listed AI agents.

Mapping:
    hack     -> Vibe Hacking Agent
    code     -> Virtual AI Tutor
    buy      -> Product Recommendation Agent
    specify  -> Product Personalization Agent
    game     -> Gaming AI Assist

Handlers are local and deterministic. There are no external API calls.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable
from dataclasses import dataclass

from agents import game_assist, personalize, recommend, tutor, vibe_hacking


@dataclass(frozen=True)
class Agent:
    name: str
    reference: str
    handler: Callable[[str], str]


AGENTS: dict[str, Agent] = {
    "hack": Agent(
        name="Vibe Hacking Agent",
        reference="https://github.com/PurpleAILAB/Decepticon",
        handler=vibe_hacking,
    ),
    "code": Agent(
        name="Virtual AI Tutor",
        reference="https://github.com/hqanhh/EduGPT",
        handler=tutor,
    ),
    "buy": Agent(
        name="Product Recommendation Agent",
        reference="https://github.com/microsoft/RecAI",
        handler=recommend,
    ),
    "specify": Agent(
        name="Product Personalization Agent",
        reference="https://github.com/crosleythomas/MirrorGPT",
        handler=personalize,
    ),
    "game": Agent(
        name="Gaming AI Assist",
        reference="https://github.com/onjas-buidl/LLM-agent-game",
        handler=game_assist,
    ),
}


def route(text: str) -> Agent | None:
    """Return the first agent whose trigger keyword appears in `text`.

    Matching is case-insensitive and uses word boundaries so that "hack"
    matches "ethical hack today" but not "hackathon".
    """
    lowered = text.lower()
    for keyword, agent in AGENTS.items():
        if re.search(rf"\b{re.escape(keyword)}\b", lowered):
            return agent
    return None


def dispatch(text: str) -> str:
    agent = route(text)
    if agent is None:
        triggers = ", ".join(AGENTS)
        return f"No matching agent. Try a message containing one of: {triggers}."
    header = f"-> {agent.name} ({agent.reference})"
    body = agent.handler(text)
    return f"{header}\n\n{body}"


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        print(dispatch(" ".join(argv[1:])))
        return 0

    print("Type a message (Ctrl-D to exit).")
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(dispatch(line))
            print()
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
