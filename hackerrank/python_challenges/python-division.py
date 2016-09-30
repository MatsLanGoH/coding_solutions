"""
Problem description:
https://www.hackerrank.com/challenges/python-division
Solution by Matthias Lambrecht
"""


class MathBag(object):
    """docstring for MathBag"""
    def __init__(self, a, b):
        self.a, self.b = int(a), int(b)

    def print_float_division(self):
        result = float(self.a) / float(self.b)
        print(result)

    def print_integer_division(self):
        result = self.a / self.b
        print(result)


a = int(raw_input())
b = int(raw_input())
bag = MathBag(a, b)
bag.print_integer_division()
bag.print_float_division()
