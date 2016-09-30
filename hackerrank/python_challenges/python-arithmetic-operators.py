"""
Problem description:
https://www.hackerrank.com/challenges/python-arithmetic-operators
Solution by Matthias Lambrecht
"""

class MathBag(object):
    """docstring for MathBag"""
    def __init__(self, a, b):
        assert 1 < a < 10**10, "Value out of bounds"
        assert 1 < b < 10**10, "Value out of bounds"
        self.a, self.b = int(a), int(b)

    def print_sum(self):
        print(self.a + self.b)

    def print_difference(self):
        print(self.a - self.b)

    def print_product(self):
        print(self.a * self.b)

a = int(raw_input())
b = int(raw_input())
bag = MathBag(a, b)
bag.print_sum()
bag.print_difference()
bag.print_product()
