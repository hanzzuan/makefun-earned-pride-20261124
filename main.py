#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text, 1 to 240 characters, to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene. The line is
fixed and deterministic: the same bytes are written on every run.
"""

import os

ENTRY = (
    "The baker's apprentice pulled the first loaf she had shaped alone "
    "from the oven, tapped its crust, and heard it sing back."
)


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
