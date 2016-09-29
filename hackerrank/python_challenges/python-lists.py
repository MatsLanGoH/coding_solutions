"""
Problem description:
https://www.hackerrank.com/challenges/python-lists

Solution by Matthias Lambrecht
"""

import sys

c = int(raw_input())
lst = list()

for _ in range(c):
    inp = raw_input().split()

    if inp[0] != "print":
        # eval is unsafe, use getattr instead!
        getattr(lst, inp[0])(*(map(int, inp[1:])))
    else:
        print(lst)
