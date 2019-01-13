#!/usr/bin/env python
#*-* coding: utf-8 *-*

n = int(raw_input())

for _ in xrange(n):
	a = map(int, raw_input())
	if a[0] == 1:
		zero_count=0
		for i in a:
			if i == 0:
				zero_count = zero_count + 1
		if zero_count >= 2	and zero_count % 2 == 0:
			print 'TRUE'
		else:
			print 'FALSE'
	else:
		print 'FALSE'