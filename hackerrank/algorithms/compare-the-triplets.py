#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/compare-the-triplets

Solution by Matthias Lambrecht
"""

# Get input
triplet_a = [int(n) for n in raw_input().split()]
triplet_b = [int(n) for n in raw_input().split()]

assert len(triplet_b) == len(triplet_a)

score_a = 0
score_b = 0

for index, val in enumerate(triplet_a):
    if triplet_a[index] > triplet_b[index]:
        score_a += 1
    elif triplet_a[index] < triplet_b[index]:
        score_b += 1

# Output results
print("{} {}".format(score_a, score_b))
