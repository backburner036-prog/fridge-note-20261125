"""Notes From a Passive-Aggressive Fridge -- make.fun entry.

Writes one line, a smart fridge's passive-aggressive note to its owner,
to /output/entry.txt.
"""

from pathlib import Path

LINE = "Your leftovers have lived in here since March. I named them. They don't pay rent."
OUT_PATH = Path("/output/entry.txt")
MIN_LEN = 1
MAX_LEN = 200


def trim_to_gate(text: str) -> str:
    """Collapse stray whitespace at the edges; the gate counts characters."""
    return " ".join(text.split())


def check_gate(text: str) -> str:
    """The sealed scorer wants 1-200 chars of non-blank UTF-8 text."""
    cleaned = trim_to_gate(text)
    assert MIN_LEN <= len(cleaned) <= MAX_LEN, (
        f"entry is {len(cleaned)} chars, gate wants 1-200"
    )
    assert cleaned.strip(), "entry must not be blank"
    return cleaned


def drop_line(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    # Round-trip: what the grader reads must be exactly what we wrote.
    assert path.read_text(encoding="utf-8") == text, "entry.txt round-trip mismatch"


def main() -> None:
    drop_line(OUT_PATH, check_gate(LINE))


if __name__ == "__main__":
    main()
