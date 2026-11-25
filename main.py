"""One-line resignation letter from a retry loop.

Writes the single entry line to /output/entry.txt and nowhere else.
The grader runs with the repo mounted read-only, so every local
write is guarded; only /output is written.
"""

import os

LINE = (
    "I retried 847 times, got the same error 847 times, "
    "so I quit \u2014 the problem is not the network, it is you."
)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
    except OSError:
        pass
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        raise


if __name__ == "__main__":
    main()
