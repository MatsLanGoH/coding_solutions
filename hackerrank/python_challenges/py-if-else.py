"""
Problem description:
https://www.hackerrank.com/challenges/py-if-else

Solution by Matthias Lambrecht
"""


def pyIfElse(n):
    if 1 <= n <= 100:
        if n % 2 != 0 or n in xrange(6, 21):
            output = "Weird"
        else:
            output = "Not Weird"
        print(output)
        return output


input = int(raw_input().strip())

pyIfElse(input)


"""
# Test cases

import unittest


class pyIfElseTest(unittest.TestCase):
    def test_is_odd_weird(self):
        self.assertEqual(pyIfElse(3), "Weird")

    def test_is_even_in_2to5_not_weird(self):
        self.assertEqual(pyIfElse(4), "Not Weird")

    def test_is_even_in_6to20_weird(self):
        self.assertEqual(pyIfElse(20), "Weird")

    def test_is_even_greater_than_20_not_weird(self):
        self.assertEqual(pyIfElse(32), "Not Weird")


if __name__ == '__main__':
    unittest.main()
"""
