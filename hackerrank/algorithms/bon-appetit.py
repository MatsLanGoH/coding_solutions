#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/bon-appetit

Solution by Matthias Lambrecht
"""

allergy = int(raw_input().strip().split()[-1])
items = [int(n) for n in raw_input().strip().split()]
charged = int(raw_input().strip())

actual = sum([item for idx, item in enumerate(items) if idx != allergy]) / 2

if actual == charged:
    print("Bon Appetit")
else:
    print(charged - actual)
