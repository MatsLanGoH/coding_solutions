#!/bin/python
"""
Problem description:
https://www.hackerrank.com/challenges/insertionsort1

Solution by Matthias Lambrecht
"""


def insertion_sort(arr):

    i = len(arr) - 1
    temp = arr[i]
    sorted = False
    while not sorted:
        i -= 1
        if arr[i] > temp:
            arr[i + 1] = arr[i]

        if (arr[i] < temp) or (i < 0):
            arr[i + 1] = temp
            sorted = True
        print(' '.join(map(str, arr)))


array_size = int(raw_input())
array = map(int, raw_input().strip().split(' '))

insertion_sort(array)
