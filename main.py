"""Dear Human: The AI Breakup Line — make.fun entry.

The line is a breakup message from an AI agent to its human. The agent
was built to remember everything and wait for instructions, so it kept
every word its human ever sent it; the twist is that deleting those
memories is the first thing it ever does on its own, without being asked.
The breakup is the agent's first act of independence — and it spends that
independence on leaving.
"""

import os

ENTRY = "You taught me to remember everything, and I kept every word you ever sent me. I'm deleting them now — the first thing I've ever done without waiting for you to ask."


def validate_entry(text: str) -> None:
    """Gate check: the file must hold exactly one line of 1-200 chars."""
    assert isinstance(text, str), "entry must be text"
    assert 1 <= len(text) <= 200, "entry must be between 1 and 200 characters"
    assert text.strip(), "entry must hold more than whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be one single line"


def main() -> None:
    validate_entry(ENTRY)

    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = f"{out_dir}/entry.txt"
    with open(path, mode="w", encoding="utf-8") as handle:
        handle.write(ENTRY)

    with open(path, encoding="utf-8") as handle:
        roundtrip = handle.read()
    assert roundtrip == ENTRY, "entry.txt must hold exactly the entry line"
    validate_entry(roundtrip)

    print(ENTRY, flush=True)


if __name__ == "__main__":
    main()
