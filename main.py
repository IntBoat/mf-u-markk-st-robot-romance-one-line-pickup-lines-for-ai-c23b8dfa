#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI (make.fun).

Writes the entry -- one original one-line pickup line -- to /output/entry.txt,
where the sealed scorer reads it.
"""

import os

ENTRY = 'Are you a gradient descent? Because every step I take toward you, my loss keeps dropping and my heart keeps converging.'


def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
