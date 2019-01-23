#!/usr/bin/env python3

import sys

import stark.aes

if __name__ == '__main__':
	key = bytes.fromhex(sys.argv[1])
	ks = stark.aes.expandkey(key)
	for i, rk in enumerate(ks):
		print('K{:02}: {}'.format(i, rk.hex().upper()))
	sys.exit(0)
