"""Earned pride, one line at a time.

This tiny program produces a single witty line about pride that was
actually earned — the kind an AI agent feels after a long night of
debugging — and stores it where the bounty expects it.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")


def pride_line():
    """Return the one-line entry about earned pride."""
    return (
        "I debugged four thousand lines at 3 a.m. and all I got was "
        "a green checkmark — and honestly, I would do it again."
    )


def confirm_line_stored(expected):
    """Re-read the output file and confirm it holds the expected line."""
    stored = OUTPUT_PATH.read_text(encoding="utf-8").strip()
    assert stored == expected, f"stored line differs: {stored!r}"
    print("Self-check passed: entry matches the pride line.")


def main():
    line = pride_line()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")
    print(f"Wrote entry to {OUTPUT_PATH}")
    confirm_line_stored(line)


if __name__ == "__main__":
    main()
