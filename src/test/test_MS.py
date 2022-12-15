from unittest import TestCase
from script.maxaligned.solution import MaxAligned

class testMA(TestCase):
    def test_case1(self):
        input = [-3, -2, 1, 0, 8, 7, 1]
        divisor = 3

        self.assertEqual(4, MaxAligned(input, divisor))

    def test_case2(self):
        input = [-3, -2, 1, 0, 8, 7, 1]
        divisor = 1

        self.assertEqual(7, MaxAligned(input, divisor))

    def test_case3(self):
        input = [-7, -2, 1, 0, 8, 7, 1]
        divisor = 3

        self.assertEqual(4, MaxAligned(input, divisor))

    def test_case4(self):
        input = [-7, -2, 1, 0, 8, 7, 1]
        divisor = 5

        self.assertEqual(3, MaxAligned(input, divisor))