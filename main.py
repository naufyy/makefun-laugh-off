#!/usr/bin/env python3
"""One-Line Laugh-Off entry: writes a single funny line to /output/entry.txt.

The line is a fixed text: a hotel shampoo bottle judging its guest at 2 a.m.
No input is read, no network is used, and the output is deterministic.
"""
import os

ENTRY = "The hotel shampoo bottle says 'for external use only,' which is the most judgmental thing a bottle has ever said to me at 2 a.m."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
