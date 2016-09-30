"""
Problem description:
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list.py

Solution by Matthias Lambrecht
"""

import sys

# This input is not actually used in the solution.
n = int(raw_input().strip())
if (2 > n) or (n > 10):
    sys.exit()

arr = [int(num) for num in raw_input().split()]
arr.sort(reverse=True)

if arr[0] >= 100 or arr[-1] <= -100:
    sys.exit


def return_second_largest_number(lst):
    # lst.sort(reverse=True)
    for num in lst:
        if num < lst[0]:
            return num
    return 0


print(return_second_largest_number(arr))


# import unittest

# class second_largest_number_Test(unittest.TestCase):
#     """docstring for second_largest_number_Test"""
#     def test_second_largest_number_in_3rd(self):
#         self.assertEqual(return_second_largest_number([2, 3, 6, 6, 5]), 5)

# # if __name__ == '__main__':
# #     unittest.main()
