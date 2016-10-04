"""
Problem description:
https://www.hackerrank.com/challenges/jumping-on-the-clouds
Solution by Matthias Lambrecht
"""

n = int(raw_input().strip())
clouds = map(int, raw_input().strip().split(' '))

pos = 0
steps = 0

while pos < len(clouds) - 1:
    if pos + 2 < n and clouds[pos + 2] == 0:
        pos += 2
        steps += 1
    elif clouds[pos + 1] == 0:
        pos += 1
        steps += 1

print(steps)
