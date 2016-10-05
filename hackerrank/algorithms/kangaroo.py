"""
Problem description:
https://www.hackerrank.com/challenges/kangaroo
Solution by Matthias Lambrecht
"""

x, a, y, b = (map(int, raw_input().strip().split()))

# brute force stuff.

if a <= b:
    print("NO")
else:
    # counter = 0
    while x < y:
        # counter += 1
        x += a
        y += b

        if x == y:
            print("YES")
            break
        if x > y:
            print("NO")
            break




# first step : get least common multiple for a and b
# second step : do something with x and y


