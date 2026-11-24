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


def validate_entry(line: str) -> None:
    """Gate check: the file must hold exactly one line of 1-200 chars."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"


def main() -> None:
    validate_entry(ENTRY)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read back and confirm the file holds exactly the line, nothing else.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "entry.txt must contain exactly the entry line"
    validate_entry(written)

    print(ENTRY)


if __name__ == "__main__":
    main()
