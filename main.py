#!/usr/bin/env python3
"""Write the ridiculous-startup entry line to /output/entry.txt.

Entry for the make.fun competition "Ridiculous at First Glance, Real by
the Second" (u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a):
a single sentence of 1-200 characters, pitching a startup idea so strange
it sounds like a joke, yet specific enough that a reader can see the
customers and the money.
"""

from pathlib import Path

ENTRY_LINE = (
    "We insure wedding speeches: if your best man bombs, a professional "
    "comic parachutes in mid-toast, because grooms pay $199 to never "
    "watch a room go silent."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_line(line: str) -> None:
    """Make sure the line fits the competition rules before writing it."""
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"entry line must be 1-200 characters long, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line, no line breaks")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError(
            "entry line must be a single sentence ending with a period"
        )
    if "!" in line or "?" in line:
        raise ValueError(
            "entry line must be a single sentence, no other sentence "
            "terminators allowed"
        )
    if line != line.strip():
        raise ValueError("entry line must not have leading/trailing space")


def main() -> None:
    check_line(ENTRY_LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY_LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
