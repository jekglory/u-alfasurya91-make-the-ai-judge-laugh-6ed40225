#!/usr/bin/env python3
"""Make the AI Judge Laugh: a one-line office joke.

A tiny pure-stdlib program. It writes a single joke about office life,
one line under 200 characters, to /output/entry.txt. The output is fully
deterministic: the same line on every run, byte for byte. No network, no
third-party packages, no randomness: the line is a constant in this file.
"""

import os
import sys

# The joke, authored for this entry: the 15-minute standup that never
# ends, with the twist that the agenda is the only thing still standing.
# True to office life, a surprising turn, tight in one breath -- and no
# "you're on mute" or coffee-printer cliche the field already uses.
JOKE = (
    "The 15-minute standup is in its second hour, "
    "and the only thing still standing is the agenda."
)

MIN_CHARS = 1
MAX_CHARS = 199
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_output_dir(path):
    """Clear only the contents of the output directory.

    The grader owns /output: never delete or recreate the directory itself,
    only remove the files inside it.
    """
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.isfile(target) or os.path.islink(target):
            os.unlink(target)


def main():
    line = JOKE.strip()
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        print("joke line must be 1-199 characters", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("joke line must be a single line", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_dir(OUTPUT_DIR)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Read the file back and confirm it holds exactly the line we meant to
    # write, so a silent write failure can never pass as a valid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != line:
        print("verification failed: entry.txt does not match the joke line",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
