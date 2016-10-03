#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/compare-the-triplets

Solution by Matthias Lambrecht
"""

import sys

n = int(raw_input().strip())
c = map(int, raw_input().strip().split(' '))

d = dict()

pairs = 0

for sock in c:
    if sock in d:
        d[sock] += 1
    else:
        d[sock] = 1

for key, value in d.items():
    print(key, value)
    pairs += (value / 2)

print(pairs)
