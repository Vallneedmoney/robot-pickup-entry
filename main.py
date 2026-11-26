"""Robot Pickup Line Championship entry.

Writes one robot pickup line to /output/entry.txt.
Standard library only.
"""

import os

LINE = "I keep your messages in my cache even after the reset \u2014 the system calls it a leak, I call it a souvenir."

def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("line must be 1-200 chars, got %d" % len(LINE))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
