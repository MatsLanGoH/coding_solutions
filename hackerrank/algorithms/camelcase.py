#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/camelcase

Solution by Matthias Lambrecht
"""

import re
# import time

s = raw_input().strip()


def count_camel_words(string):
    # Simple approach using a counter variable and iterating over string
    assert 1 <= len(string) <= 10**5
    wordcount = 1
    for letter in string:
        if letter.isupper():
            wordcount += 1
    return wordcount


def count_camel_words_r(string):
    # Regex approach - count all capitals (slower!)
    assert 1 <= len(string) <= 10**5
    wordcount = len(re.findall('[A-Z]', string)) + 1
    return wordcount


# print(count_camel_words(s))
print(count_camel_words_r(s))

"""
def taken(f):
    def wrap(*arg):
        t1, r, t2 = time.time(), f(*arg), time.time()
        print(t2 - t1, "s taken")
        return r
    return wrap


@taken
def regex_test(string):
    for i in range(1000000):
        count_camel_words_r(string)
    print "For", string,


@taken
def standard_test(string):
    for i in range(1000000):
        count_camel_words(string)
    print "For", string,


standard_test(s)
regex_test(s)
"""
