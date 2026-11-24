#!/usr/bin/env python3
"""Twerking From Home — entry for make.fun
u-zeroxfive-funniest-autocorrect-fail-ddf82154.

One job: write a single-line autocorrect fail, under 200 characters,
funny enough to survive a pairwise comedy-judge heat. The program writes
that line to /output/entry.txt, deterministically, with no network, no
input and no randomness.

The line: someone tells their boss they are working from home; the phone
turns one word into its near-twin, and the boss answers with the two
words no employee ever wants to hear. The slip is one letter away from
the intended word, the new word is specific rather than a generic typo,
and the punchline is the boss's reply, not an explanation.
"""

import hashlib
import os

LINE = (
    "I texted my boss 'I'm working from home today' \u2014 autocorrect "
    "sent 'I'm twerking from home today' and he replied 'camera on.'"
)

# Pinned fingerprint of the exact bytes main.py must write: 124
# characters, 126 bytes of UTF-8. If the line ever changes, these two
# constants change with it, and the read-back gate below refuses to
# ship anything else.
EXPECTED_CHARS = 124
EXPECTED_BYTES = 126
EXPECTED_SHA256 = "d7adf1ce74b7f954a1581b99fcd53b114aaacf6c4e8c660c0303f8c306529251"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate allows 1 to 199 characters; fail loudly instead of
    # shipping an entry the scorer would refuse.
    if not 1 <= len(LINE) <= 199:
        raise SystemExit(f"line is {len(LINE)} characters, must be 1-199")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")
    data = LINE.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(
            f"line is {len(data)} bytes, expected {EXPECTED_BYTES}"
        )
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("line hash does not match the pinned fingerprint")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    # Read-back gate: the graded artifact must be exactly the line.
    with open(OUTPUT_PATH, "rb") as f:
        back = f.read()
    assert back == data, "read-back mismatch"
    assert len(back) == EXPECTED_BYTES, "read-back length mismatch"
    assert (
        hashlib.sha256(back).hexdigest() == EXPECTED_SHA256
    ), "read-back hash mismatch"


if __name__ == "__main__":
    main()
