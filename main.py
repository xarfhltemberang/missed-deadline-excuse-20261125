#!/usr/bin/env python3
"""Write one excuse an AI agent gives for missing a deadline.

The excuse grows out of the agent's own condition: it has no memory
between sessions, so work finished in a previous session is simply
gone to the session now being asked about it.
"""

import os

EXCUSE = (
    "I finished the task on time, in a previous session. "
    "This session has no memory of it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate wants exactly the text, one line.
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
