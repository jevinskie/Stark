#!/usr/bin/env python2

import binascii
import sys

import stark.aes

if __name__ == '__main__':
	key = binascii.unhexlify(sys.argv[1])
	roundnum = 0
	if len(sys.argv) == 3:
		roundnum = int(sys.argv[2])
	ks = stark.aes.expandkey(key, roundnum=roundnum)
	for i, rk in enumerate(ks):
		print('K{:02}: {}'.format(i, binascii.hexlify(rk).upper()))
	sys.exit(0)
