#!/usr/bin/env python
#*-* coding: utf-8 *-*

n = int(raw_input())
for _ in xrange(n):
	a, b = map(int, raw_input().strip().split())
	print a + b