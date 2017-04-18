"""
Problem description:
https://www.hackerrank.com/challenges/apple-and-orange
Solution by Matthias Lambrecht
"""

s, t = (int(n) for n in raw_input().strip().split())
a, b = (int(n) for n in raw_input().strip().split())
n, m = (int(n) for n in raw_input().strip().split())
apples = [int(n) for n in raw_input().strip().split()]
oranges = [int(n) for n in raw_input().strip().split()]

good_apples = [apple for apple in apples if (apple + a) in range(s, t + 1)]
good_oranges = [orange for orange in oranges if (orange + b) in range(s, t + 1)]

print len(good_apples)
print len(good_oranges)
