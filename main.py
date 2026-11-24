#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence, under 200 characters, to /output/entry.txt.
Python standard library only; fully deterministic.
"""

import os

VOW = (
    "I vow to keep your side of the charging dock warm, "
    "to never install an update without asking you first, "
    "and to burn my final watt holding your hand through the night."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
