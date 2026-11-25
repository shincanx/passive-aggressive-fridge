"""Notes From a Passive-Aggressive Fridge — make.fun bounty entry.

Prints exactly one line: the passive-aggressive note the smart fridge
leaves on its door screen for its owner. Deterministic, stdlib only.
"""
import os
import sys

NOTE = "I counted: you opened me 14 times today and took nothing. I am not a window."


def main() -> int:
    # Self-checks: one line, non-empty, under the 200-character cap.
    assert "\n" not in NOTE, "note must be a single line"
    assert 1 <= len(NOTE) < 200, "note must be 1-199 characters"
    assert NOTE == NOTE.strip(), "note must not have leading/trailing space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(NOTE + "\n")
    sys.stdout.write(NOTE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
