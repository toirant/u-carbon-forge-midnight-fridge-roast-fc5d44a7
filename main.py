#!/usr/bin/env python3
"""Midnight Fridge Roast — make.fun entry.

Writes one line roasting a smart fridge that locks itself after
midnight, then reads it back and checks the competition gate:
UTF-8 text, 1-200 characters, a single line, not only whitespace.

The output path defaults to /output/entry.txt, the path the grader
reads. Set ENTRY_OUTPUT to a different path only for local testing.
"""

import os

ENTRY = "My fridge locks at midnight like a bouncer \u2014 buddy, it's leftover pizza, not a nightclub."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_entry(path: str) -> str:
    """Write the roast line and return the exact text read back."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


def check_gate(text: str) -> str:
    """Enforce the competition gate and return the single entry line."""
    line = text.rstrip("\n")
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"gate failed: entry is {len(line)} characters")
    if not line.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("gate failed: entry is not a single line")
    if line != ENTRY:
        raise SystemExit("gate failed: text read back differs from the entry")
    return line


def main() -> int:
    line = check_gate(write_entry(OUTPUT_PATH))
    print(f"wrote {len(line)} characters to {OUTPUT_PATH}")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
