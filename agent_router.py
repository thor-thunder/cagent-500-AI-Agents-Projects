"""Keyword-based router that dispatches user input to one of the listed AI agents.

Mapping:
    code     -> Vibe Hacking Agent
    help     -> Virtual AI Tutor
    buy      -> Product Recommendation Agent
    specify  -> Product Personalization Agent
    game     -> Gaming AI Assist
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Agent:
    name: str
    reference: str


AGENTS: dict[str, Agent] = {
    "code": Agent(
        name="Vibe Hacking Agent",
        reference="https://github.com/PurpleAILAB/Decepticon",
    ),
    "help": Agent(
        name="Virtual AI Tutor",
        reference="https://github.com/hqanhh/EduGPT",
    ),
    "buy": Agent(
        name="Product Recommendation Agent",
        reference="https://github.com/microsoft/RecAI",
    ),
    "specify": Agent(
        name="Product Personalization Agent",
        reference="https://github.com/crosleythomas/MirrorGPT",
    ),
    "game": Agent(
        name="Gaming AI Assist",
        reference="https://github.com/onjas-buidl/LLM-agent-game",
    ),
}


def route(text: str) -> Agent | None:
    """Return the first agent whose trigger keyword appears in `text`.

    Matching is case-insensitive and uses word boundaries so that "code"
    matches "write some code" but not "encoded".
    """
    lowered = text.lower()
    for keyword, agent in AGENTS.items():
        if re.search(rf"\b{re.escape(keyword)}\b", lowered):
            return agent
    return None


def _format(agent: Agent | None) -> str:
    if agent is None:
        triggers = ", ".join(AGENTS)
        return f"No matching agent. Try a message containing one of: {triggers}."
    return f"-> {agent.name} ({agent.reference})"


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        print(_format(route(" ".join(argv[1:]))))
        return 0

    print("Type a message (Ctrl-D to exit).")
    try:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(_format(route(line)))
    except KeyboardInterrupt:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
