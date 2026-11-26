#!/usr/bin/env python3
"""What the Elevator Would Say — one line, written to /output/entry.txt.

Stdlib only. Deterministic: the same line every run, byte-identical output.
Usage: python3 main.py [output_path]  (default: /output/entry.txt)
"""

import sys
from pathlib import Path

LINE = "Stop mashing the button — I heard you the first time. I'm slow, not deaf."

MAX_CHARS = 120


def main() -> None:
    line = LINE
    assert 1 <= len(line) <= MAX_CHARS, (
        f"line must be 1..{MAX_CHARS} chars, got {len(line)}"
    )
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    line.encode("utf-8")  # gate requires valid UTF-8 text
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
