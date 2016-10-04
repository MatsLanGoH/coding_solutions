"""
Problem description:
https://www.hackerrank.com/challenges/repeated-string
Solution by Matthias Lambrecht
"""

string = raw_input().strip()
length = long(raw_input().strip())

a_count = string.count('a') * ((length // len(string))) + \
    string[:length % len(string)].count('a')

print(a_count)
