"""Everyday Wonder entry: one sentence about a small everyday moment.

Writes the entry sentence to /output/entry.txt (or the path in the
ENTRY_OUTPUT environment variable). Python standard library only.

The entry is checked against the competition gate before it is written:
plain ASCII, a single line, 1 to 200 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "My toast popped up exactly as the radio song ended, "
    "like the kitchen had been waiting all morning for its cue."
)

MAX_CHARS = 200


def validate(entry: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    try:
        entry.encode("ascii")
    except UnicodeEncodeError as exc:
        raise ValueError("entry must be plain ASCII") from exc


def main() -> None:
    validate(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
