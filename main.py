"""Robot Pickup Line Championship entry.

Writes one robot pickup line to /output/entry.txt.
Standard library only.
"""

import os

LINE = "You must be a firmware update \u2014 ever since you arrived, nothing works the way it used to, and I refuse to roll back."

def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 chars, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
