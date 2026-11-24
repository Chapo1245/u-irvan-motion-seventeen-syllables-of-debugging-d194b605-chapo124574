#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one debugging haiku (5-7-5) to /output/entry.txt.
Stdlib only, no network, no dependencies.
"""

import os

HAIKU = (
    "Print left in the code\n"
    "logs my own name at midnight\n"
    "the bug wore my name\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
