#!/usr/bin/env python3

import sys

xorstream = b''
with open(sys.argv[1]) as xorstream_hexf:
	for line in xorstream_hexf:
		line = line.strip()
		xorstream += bytes.fromhex(line)
print('xorstream size: 0x{:08x} ({})'.format(len(xorstream), len(xorstream)))

orig = open(sys.argv[2], 'rb').read()
print('input size: 0x{:08x} ({})'.format(len(orig), len(orig)))
xored = bytes([i[0] ^ i[1] for i in zip(orig, xorstream)])

with open(sys.argv[3], 'wb') as outf:
	outf.write(xored)
