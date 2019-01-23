#!/usr/bin/env python3

import sys

import stark.aes

if __name__ == '__main__':
	key = bytes.fromhex(sys.argv[1])
	roundnum = 0
	if len(sys.argv) == 3:
		roundnum = int(sys.argv[2])
	ks = stark.aes.expandkey(key, roundnum=roundnum)
	for i, rk in enumerate(ks):
		print('K{:02}: {}'.format(i, rk.hex().upper()))
	sys.exit(0)
