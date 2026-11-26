#!/usr/bin/env python3
"""Roast the Smart Fridge: write one roast line to /output/entry.txt.

One line, one sentence, under 160 characters: the smart fridge beeps
about the open door, then uses its screen to advertise salad at me.
The sting is the last clause: it snitches and it profits from snitching.
Deterministic: the same bytes on every run, no input, no network.
"""

import os

ENTRY = "My smart fridge beeps when I leave the door open, then flashes an ad for salad \u2014 a snitch with a side hustle."

OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open(OUT_PATH, "wb") as f:
        f.write(data)
    # The grader collects the outputs as another user: leave it world-readable.
    os.chmod(OUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
