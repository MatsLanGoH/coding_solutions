#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/tutorial-intro

Solution by Matthias Lambrecht
"""

search_value = int(raw_input())
array_size = int(raw_input())
array = map(int, raw_input().strip().split(' '))

print(array.index(search_value))
