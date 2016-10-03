#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/python-mod-divmod

Solution by Matthias Lambrecht
"""

from __future__ import division

# Input
a = int(raw_input())
b = int(raw_input())

# Output
print(a // b)
print(a % b)
print(divmod(a, b))
