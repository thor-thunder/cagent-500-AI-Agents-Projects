"""Local, no-API handlers for the five routed agents.

Every handler is a pure function: input string -> response string. There are
no network calls, no LLM invocations, no external services. Behavior is
deterministic and driven by keyword detection over the prompt.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Vibe Hacking Agent  (trigger: "hack")
# ---------------------------------------------------------------------------

_HACK_CATEGORIES: list[tuple[str, tuple[str, ...], list[str]]] = [
    (
        "Web application surface",
        ("web", "http", "https", "url", "site", "api", "endpoint", "graphql"),
        [
            "Passive recon: crt.sh, Wayback, GitHub dorks for leaked secrets",
            "Active recon: subdomain enum (amass, subfinder), virtual-host probing",
            "Crawl visible surface; harvest endpoints from JS bundles and sitemaps",
            "Probe well-known paths: /robots.txt, /.git/, /.env, /admin, /actuator",
            "Test top OWASP categories (injection, broken auth, SSRF, IDOR, XXE)",
            "Validate CSP, CORS, cookie flags, and HSTS posture",
        ],
    ),
    (
        "Network and host surface",
        ("network", "port", "host", "internal", "lan", "vpn", "subnet"),
        [
            "Identify in-scope ranges and live hosts (ARP/ICMP sweeps)",
            "TCP/UDP port scans with rate limits to avoid disruption",
            "Service/version detection; map to known CVEs",
            "Enumerate SMB/NFS/RDP shares and weak service configs",
            "Map trust relationships and pivot opportunities",
        ],
    ),
    (
        "Authentication and identity",
        ("auth", "login", "password", "credential", "token", "sso", "oauth", "jwt"),
        [
            "Test default and weak credentials against documented surface",
            "Verify rate limiting, account lockout, and MFA enforcement",
            "Inspect session token entropy, rotation, and revocation",
            "Check JWT header for alg=none, weak HMAC secrets, kid injection",
            "Audit OAuth flows for open redirects and PKCE bypasses",
        ],
    ),
    (
        "Cloud and container surface",
        ("cloud", "aws", "gcp", "azure", "s3", "iam", "kubernetes", "k8s", "docker", "container"),
        [
            "Enumerate public buckets/blobs and signed-URL exposure",
            "Review IAM for over-broad principals, wildcard actions, role chaining",
            "Check metadata-service access from compute (IMDSv1, SSRF chains)",
            "Audit cluster RBAC, service-account tokens, exposed dashboards",
            "Scan container images for embedded secrets and known CVEs",
        ],
    ),
    (
        "Mobile and client surface",
        ("mobile", "android", "ios", "apk", "ipa", "client"),
        [
            "Pull and decompile the package; inspect strings, manifests, certs",
            "Locate hardcoded keys, endpoints, and debug flags",
            "Intercept TLS with a trusted CA; test pinning bypasses where allowed",
            "Fuzz IPC, deeplinks, exported activities/components",
            "Check local storage for sensitive data at rest",
        ],
    ),
]

_HACK_PHASES = [
    "Scoping: confirm assets, rules of engagement, and authorization in writing",
    "Reconnaissance: passive then active, document everything observed",
    "Vulnerability identification: manual verification beats raw scanner output",
    "Exploitation: only within scope; capture proof without causing damage",
    "Post-exploitation: persistence and pivoting only if explicitly authorized",
    "Reporting: severity, reproduction steps, business impact, remediation",
]


def vibe_hacking(prompt: str) -> str:
    text = prompt.lower()
    matched = [
        (title, items)
        for title, keywords, items in _HACK_CATEGORIES
        if any(k in text for k in keywords)
    ]

    out = [
        "Vibe Hacking Agent",
        "==================",
        "",
        "Authorization reminder: only execute these steps against assets you",
        "own or have explicit written permission to test (CTFs, internal infra,",
        "signed pentest engagements).",
        "",
        "Engagement phases:",
    ]
    for phase in _HACK_PHASES:
        out.append(f"  - {phase}")
    out.append("")

    if matched:
        out.append("Surface-specific checklists detected from your prompt:")
        out.append("")
        for title, items in matched:
            out.append(f"## {title}")
            for item in items:
                out.append(f"  - {item}")
            out.append("")
    else:
        out.append("No specific surface detected; describe the target")
        out.append("(web, network, auth, cloud, mobile) for a tailored checklist.")

    return "\n".join(out).rstrip()


# ---------------------------------------------------------------------------
# Virtual AI Tutor  (trigger: "code")
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class _Lesson:
    summary: str
    vocabulary: tuple[str, ...]
    worked_example: str
    practice: tuple[str, ...]
    further_reading: tuple[str, ...]


_LESSONS: dict[str, _Lesson] = {
    "recursion": _Lesson(
        summary=(
            "Recursion is when a function solves a problem by calling itself on a "
            "smaller instance of the same problem and combining the result with a "
            "base case that does not recurse."
        ),
        vocabulary=("base case", "recursive case", "call stack", "tail call"),
        worked_example=(
            "factorial(n):\n"
            "  if n <= 1: return 1          # base case\n"
            "  return n * factorial(n - 1)  # recursive case"
        ),
        practice=(
            "Write `sum_list(xs)` recursively without using sum() or loops.",
            "Compute the nth Fibonacci number; then add memoization.",
            "Recursively reverse a string without using slicing.",
        ),
        further_reading=(
            "SICP, Chapter 1.2 (linear vs tree recursion)",
            "CLRS, Chapter 4 (recurrences and the master theorem)",
        ),
    ),
    "complexity": _Lesson(
        summary=(
            "Big-O describes how the runtime or memory of an algorithm grows as "
            "the input size n grows. It ignores constant factors and lower-order "
            "terms so you can compare algorithms apples-to-apples."
        ),
        vocabulary=("O(1)", "O(log n)", "O(n)", "O(n log n)", "O(n^2)", "amortized"),
        worked_example=(
            "Linear search is O(n): worst case touches every element.\n"
            "Binary search on a sorted array is O(log n): halves the range each step."
        ),
        practice=(
            "Prove that two nested loops over n items are O(n^2).",
            "Why is dict lookup O(1) average but O(n) worst case in Python?",
            "What is the amortized cost of appending to a Python list?",
        ),
        further_reading=(
            "CLRS, Chapter 3 (asymptotic notation)",
            "Sedgewick, Algorithms, 4th edition",
        ),
    ),
    "debugging": _Lesson(
        summary=(
            "Effective debugging is a search problem: reduce the gap between what "
            "you assumed and what is actually happening, one observation at a time."
        ),
        vocabulary=("repro", "bisect", "minimal example", "rubber duck", "stack trace"),
        worked_example=(
            "1. Reproduce reliably.\n"
            "2. Shrink to a minimal failing case.\n"
            "3. Form one hypothesis; design one experiment.\n"
            "4. Verify or falsify; update mental model.\n"
            "5. Repeat until root cause is identified, not just symptoms."
        ),
        practice=(
            "Find a bug in your last commit by `git bisect`.",
            "Add one print statement that proves a hypothesis right or wrong.",
            "Rewrite an obscure error message into a check that fails earlier.",
        ),
        further_reading=(
            "Zeller, Why Programs Fail",
            "Hunt & Thomas, The Pragmatic Programmer (chapter on debugging)",
        ),
    ),
    "data structures": _Lesson(
        summary=(
            "Pick a data structure by the operations you need to be cheap. Arrays "
            "give O(1) indexed access; hash maps give O(1) lookup by key; trees "
            "and heaps give ordered access with logarithmic updates."
        ),
        vocabulary=("array", "linked list", "hash map", "tree", "heap", "graph"),
        worked_example=(
            "Counting word frequency: a hash map (dict) gives O(1) update per word\n"
            "and O(n) total, vs O(n^2) if you scanned a list for each word."
        ),
        practice=(
            "Implement a stack and a queue using only lists.",
            "Use a heap to find the k largest numbers in a stream.",
            "Build an adjacency-list graph and run BFS from a chosen node.",
        ),
        further_reading=(
            "Skiena, The Algorithm Design Manual",
            "Goodrich & Tamassia, Data Structures and Algorithms in Python",
        ),
    ),
    "testing": _Lesson(
        summary=(
            "Tests pin down behavior so you can change code without fear. Good "
            "tests are fast, deterministic, and fail with a clear message that "
            "points at the cause, not just the symptom."
        ),
        vocabulary=("unit", "integration", "fixture", "mock", "coverage", "flaky"),
        worked_example=(
            "def test_sum_list_empty():\n"
            "    assert sum_list([]) == 0   # explicit edge case\n\n"
            "def test_sum_list_basic():\n"
            "    assert sum_list([1, 2, 3]) == 6"
        ),
        practice=(
            "Write a test that fails for the bug you most recently fixed.",
            "Add one property-based test using hypothesis.",
            "Identify a flaky test and remove the source of nondeterminism.",
        ),
        further_reading=(
            "Meszaros, xUnit Test Patterns",
            "Feathers, Working Effectively with Legacy Code",
        ),
    ),
}

_LESSON_TRIGGERS = {
    "recursion": ("recursion", "recursive", "recurse"),
    "complexity": ("big-o", "big o", "complexity", "runtime", "performance"),
    "debugging": ("debug", "bug", "stack trace", "traceback", "error"),
    "data structures": ("data structure", "list", "dict", "hash", "tree", "graph", "queue", "stack"),
    "testing": ("test", "unit test", "pytest", "tdd", "coverage"),
}


def tutor(prompt: str) -> str:
    text = prompt.lower()
    chosen: str | None = None
    for topic, triggers in _LESSON_TRIGGERS.items():
        if any(t in text for t in triggers):
            chosen = topic
            break

    if chosen is None:
        topics = ", ".join(_LESSONS)
        return (
            "Virtual AI Tutor\n"
            "================\n\n"
            "Tell me which topic you want to study. Available lessons:\n"
            f"  {topics}\n\n"
            "Example: 'help me with recursion' or 'explain big-o complexity'."
        )

    lesson = _LESSONS[chosen]
    out = [
        "Virtual AI Tutor",
        "================",
        f"Topic: {chosen}",
        "",
        "Summary:",
        f"  {lesson.summary}",
        "",
        "Key vocabulary: " + ", ".join(lesson.vocabulary),
        "",
        "Worked example:",
    ]
    for line in lesson.worked_example.splitlines():
        out.append(f"  {line}")
    out.append("")
    out.append("Practice problems:")
    for i, p in enumerate(lesson.practice, 1):
        out.append(f"  {i}. {p}")
    out.append("")
    out.append("Further reading:")
    for r in lesson.further_reading:
        out.append(f"  - {r}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Product Recommendation Agent  (trigger: "buy")
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class _Product:
    name: str
    price_usd: int
    why: str


_CATALOG: dict[str, tuple[tuple[str, ...], list[_Product]]] = {
    "headphones": (
        ("headphone", "headphones", "earbud", "earbuds", "earphone"),
        [
            _Product("Sony WH-1000XM5", 350, "Class-leading active noise cancellation, comfortable for long sessions"),
            _Product("Sennheiser HD 600", 400, "Reference-grade open-back tuning for music listening at a desk"),
            _Product("Apple AirPods Pro 2", 230, "Best-in-class integration if you live in the Apple ecosystem"),
        ],
    ),
    "laptop": (
        ("laptop", "macbook", "notebook", "ultrabook"),
        [
            _Product("Apple MacBook Air M3", 1100, "Fanless, all-day battery, strong single-thread performance"),
            _Product("Framework Laptop 13", 1200, "Repairable and upgradable; modular ports"),
            _Product("Lenovo ThinkPad X1 Carbon", 1500, "Excellent keyboard, business-grade Linux support"),
        ],
    ),
    "phone": (
        ("phone", "smartphone", "iphone", "android"),
        [
            _Product("Apple iPhone 15", 800, "Long software-support window; mature ecosystem"),
            _Product("Google Pixel 8", 700, "Cleanest Android build; very strong computational photography"),
            _Product("Samsung Galaxy S24", 800, "Best-in-class display; broad accessory ecosystem"),
        ],
    ),
    "coffee": (
        ("coffee", "espresso", "grinder", "brew"),
        [
            _Product("Baratza Encore ESP", 200, "Affordable burr grinder that handles both filter and espresso"),
            _Product("Hario V60 + kettle", 60, "Lowest-cost path to high-quality pourover at home"),
            _Product("Breville Bambino Plus", 500, "Compact entry to real espresso with steam wand"),
        ],
    ),
    "books": (
        ("book", "books", "read", "novel"),
        [
            _Product("The Pragmatic Programmer (Hunt & Thomas)", 35, "Career-shaping habits for working developers"),
            _Product("Designing Data-Intensive Applications (Kleppmann)", 50, "The reference for modern backend systems"),
            _Product("Project Hail Mary (Weir)", 18, "Approachable hard sci-fi for non-work reading"),
        ],
    ),
}


def _budget(text: str) -> int | None:
    m = re.search(r"\$?\s*(\d{2,5})\b", text)
    return int(m.group(1)) if m else None


def recommend(prompt: str) -> str:
    text = prompt.lower()
    matched_category: str | None = None
    for category, (keywords, _) in _CATALOG.items():
        if any(k in text for k in keywords):
            matched_category = category
            break

    if matched_category is None:
        cats = ", ".join(_CATALOG)
        return (
            "Product Recommendation Agent\n"
            "============================\n\n"
            f"Tell me what you want to buy. Known categories: {cats}.\n"
            "You can also include a budget, e.g. 'I want to buy headphones under $300'."
        )

    budget = _budget(text)
    products = _CATALOG[matched_category][1]
    if budget is not None:
        in_budget = [p for p in products if p.price_usd <= budget]
        rejected = [p for p in products if p.price_usd > budget]
    else:
        in_budget, rejected = products, []

    out = [
        "Product Recommendation Agent",
        "============================",
        f"Category: {matched_category}",
    ]
    if budget is not None:
        out.append(f"Budget: under ${budget}")
    out.append("")

    if not in_budget:
        out.append("Nothing in this category fits the stated budget.")
        out.append("Closest options above budget:")
        for p in rejected:
            out.append(f"  - {p.name} (${p.price_usd}) — {p.why}")
        return "\n".join(out)

    out.append("Recommended:")
    for p in in_budget:
        out.append(f"  - {p.name} (${p.price_usd}) — {p.why}")
    if rejected:
        out.append("")
        out.append("Stretch picks above budget:")
        for p in rejected:
            out.append(f"  - {p.name} (${p.price_usd}) — {p.why}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Product Personalization Agent  (trigger: "specify")
# ---------------------------------------------------------------------------

_LIKE_PAT = re.compile(r"\b(?:i\s+(?:like|love|enjoy|prefer)|favou?rite\s+is)\s+([a-z0-9$ &'\-]+?)(?=\.|;|,|\band\b|$)")
_DISLIKE_PAT = re.compile(r"\bi\s+(?:dislike|hate|avoid|don['’]t\s+(?:like|want))\s+([a-z0-9$ &'\-]+?)(?=\.|;|,|\band\b|$)")
_WANT_PAT = re.compile(r"\bi\s+(?:want|need|am\s+looking\s+for)\s+([a-z0-9$ &'\-]+?)(?=\.|;|,|\band\b|$)")
_BUDGET_PAT = re.compile(r"\$\s*(\d{2,5})|under\s+\$?\s*(\d{2,5})|max\s+\$?\s*(\d{2,5})")


def _clean_list(items: list[str]) -> list[str]:
    seen: list[str] = []
    for raw in items:
        item = raw.strip().rstrip(".").strip()
        if item and item not in seen:
            seen.append(item)
    return seen


def personalize(prompt: str) -> str:
    text = prompt.lower()
    likes = _clean_list(_LIKE_PAT.findall(text))
    dislikes = _clean_list(_DISLIKE_PAT.findall(text))
    wants = _clean_list(_WANT_PAT.findall(text))

    budget: int | None = None
    m = _BUDGET_PAT.search(text)
    if m:
        budget = int(next(g for g in m.groups() if g))

    out = [
        "Product Personalization Agent",
        "=============================",
        "",
        "Profile parsed from your message:",
    ]
    out.append(f"  Likes:    {', '.join(likes) if likes else '(none stated)'}")
    out.append(f"  Dislikes: {', '.join(dislikes) if dislikes else '(none stated)'}")
    out.append(f"  Wants:    {', '.join(wants) if wants else '(none stated)'}")
    out.append(f"  Budget:   {'under $' + str(budget) if budget is not None else '(none stated)'}")
    out.append("")

    suggestions: list[str] = []
    if wants:
        for w in wants:
            tail = f" within ${budget}" if budget else ""
            suggestions.append(
                f"For '{w}'{tail}: route via 'buy {w}' to get concrete picks."
            )
    if likes and not wants:
        suggestions.append(
            "You stated preferences but no concrete request. Add 'I want X' to "
            "trigger a recommendation."
        )
    if not likes and not wants and not dislikes:
        suggestions.append(
            "No preferences detected. Try: 'I like minimal design and I want "
            "headphones under $300.'"
        )

    out.append("Next steps:")
    for s in suggestions:
        out.append(f"  - {s}")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Gaming AI Assist  (trigger: "game")
# ---------------------------------------------------------------------------

_GAME_TIPS: dict[str, tuple[tuple[str, ...], list[str]]] = {
    "chess": (
        ("chess",),
        [
            "Opening principle: control the center, develop knights before bishops, castle early",
            "Before each move, scan for checks, captures, and threats — yours and theirs",
            "In the endgame, activate your king; it is a strong piece once queens are off",
            "When ahead in material, trade pieces but not pawns; when behind, do the opposite",
        ],
    ),
    "fps": (
        ("fps", "shooter", "valorant", "counter-strike", "cs:go", "cs2"),
        [
            "Pre-aim common angles at head height; you should never need to flick if held right",
            "Crosshair placement beats reflexes; keep it where the next enemy will appear",
            "Use sound: footsteps and reloads leak more information than the minimap",
            "Economy management often decides rounds before the first shot is fired",
        ],
    ),
    "rpg": (
        ("rpg", "skyrim", "witcher", "elden ring", "souls"),
        [
            "Specialize early: a focused build out-damages a balanced one in most systems",
            "Save before NPC dialogue branches if the game has irreversible faction choices",
            "Sell or stash crafting materials in tiers; don't hoard low-tier infinitely",
            "Upgrade gear before buying new gear — flat scaling usually beats sidegrades",
        ],
    ),
    "strategy": (
        ("strategy", "rts", "civ", "civilization", "starcraft", "age of empires"),
        [
            "Macro before micro: a stronger economy beats a better-controlled small army",
            "Scout continuously; the cost of a scout is much smaller than a surprise loss",
            "Identify your win condition early and tech toward it instead of reacting",
            "Trade favorably even when losing; preserved units snowball recovery",
        ],
    ),
    "puzzle": (
        ("puzzle", "sudoku", "tetris", "portal"),
        [
            "Find one forced move; chain forced moves before guessing",
            "When stuck, restate the constraints out loud — you usually missed one",
            "Tetris: keep the stack flat, leave one well column for the I-piece",
            "Sudoku: scan rows, columns, and boxes for naked singles before pencil marks",
        ],
    ),
}


def game_assist(prompt: str) -> str:
    text = prompt.lower()
    matched: list[tuple[str, list[str]]] = []
    for genre, (keywords, tips) in _GAME_TIPS.items():
        if any(k in text for k in keywords):
            matched.append((genre, tips))

    out = ["Gaming AI Assist", "================", ""]
    if not matched:
        genres = ", ".join(_GAME_TIPS)
        out.append(f"Tell me which game or genre. Known genres: {genres}.")
        out.append("Example: 'I'm losing every chess game' or 'tips for FPS aim'.")
        return "\n".join(out)

    for genre, tips in matched:
        out.append(f"## {genre.upper()}")
        for tip in tips:
            out.append(f"  - {tip}")
        out.append("")
    return "\n".join(out).rstrip()
