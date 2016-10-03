#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/angry-professor

Solution by Matthias Lambrecht
"""

tests = int(raw_input().strip())

for _ in xrange(tests):
    students, threshold = raw_input().strip().split(' ')
    students, threshold = [int(students), int(threshold)]
    arrivals = map(int, raw_input().strip().split(' '))

    for arrival in arrivals:
        if arrival <= 0:
            threshold -= 1

    if threshold <= 0:
        print("NO")
    else:
        print("YES")
