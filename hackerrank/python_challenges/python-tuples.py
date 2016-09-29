"""
Problem description:
https://www.hackerrank.com/challenges/python-tuples

Solution by Matthias Lambrecht
"""

raw_input()

buffer = []

for el in raw_input().split():
    buffer.append(int(el))

print(buffer)
print(tuple(buffer))

print(hash(tuple(buffer)))

