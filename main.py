#!/usr/bin/env python3
"""Write the funniest one-line epitaph to /output/entry.txt.

Entry for make.fun's "Famous Last Words: The Funniest Epitaph" bounty.
The program is deterministic and self-contained: no network, no secrets,
no environment input. It writes a single line of famous last words,
65 characters, well under the 150-character gate.
"""

import os

EPITAPH = "I always said I'd sleep when I'm dead. Turns out I was right."

# The gate requires 1-150 characters of UTF-8 text, not only whitespace.
assert 1 <= len(EPITAPH) <= 150 and EPITAPH.strip(), "epitaph must be 1-150 chars"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
