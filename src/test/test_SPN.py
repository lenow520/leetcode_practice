from unittest import TestCase
from script.smallestpositive.solution import Solution

class testSPN(TestCase):
    def test_case1(self):
        input = [3, 2, 1, 4, 8, 7, 1]

        self.assertEqual(5, Solution(input))

    def test_case2(self):
        input = [-3, -2, -1, -4, -8, -7, -1]

        self.assertEqual(1, Solution(input))

    def test_case3(self):
        input = [-3, -2, 1, -4, -8, -7, -1]

        self.assertEqual(2, Solution(input))

    def test_case4(self):
        input = [-3, -2, 1, 4, -8, -7, -1]

        self.assertEqual(2, Solution(input))

    def test_case5(self):
        input = [-3, 2, 1, 4, 3, 0, -1]

        self.assertEqual(5, Solution(input))

    def test_case6(self):
        input = [-3, 2, 1, 4, 3, 5, -1]

        self.assertEqual(6, Solution(input))