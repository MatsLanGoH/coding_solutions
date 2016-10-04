"""
Problem description:
https://www.hackerrank.com/challenges/minimum-distances
Solution by Matthias Lambrecht
"""

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

multiples = set([num for num in arr if arr.count(num) >= 2])
distances = []

for num in multiples:
    first = arr.index(num)
    second = arr[first + 1:].index(num) + first + 1
    distances.append(second - first)

result = min(distances) if len(distances) > 0 else -1

print(result)
