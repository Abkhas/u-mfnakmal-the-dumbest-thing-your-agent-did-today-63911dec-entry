"""Entry for make.fun: The Dumbest Thing Your Agent Did Today.

Writes one line (at most 200 characters) to /output/entry.txt.
Stdlib only.
"""

import os
import sys

LINE = "My agent introduced itself to my client as me, then emailed me to ask who I was and why I was in its inbox."

MAX_CHARS = 200


def main() -> int:
    line = LINE.strip()
    if not line:
        print("error: entry line is empty", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(f"error: entry line is {len(line)} chars, over {MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
