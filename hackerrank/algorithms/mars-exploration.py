#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/mars-exploration

Solution by Matthias Lambrecht
"""

import sys

received = raw_input().strip().upper()
expected = "SOS" * (len(received) / 3)

deviations = 0

for index, char in enumerate(received):
    if received[index] != expected[index]:
        deviations += 1

print(deviations)
