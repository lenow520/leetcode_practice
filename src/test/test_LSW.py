from unittest import TestCase
from script.largestsum.solution import MaxSumWeight

class testMSW(TestCase):
    def test_case1(self):
        input = [(2,3,20),(2,1,10)]
        num = 3

        self.assertEqual(50, MaxSumWeight(num, input))

    def test_case2(self):
        input = [(2,3,2),(1,2,1),(4,2,5),(3,5,14)]
        num = 5

        self.assertEqual(76, MaxSumWeight(num, input))

    def test_case3(self):
        input = [(2,3,70),(2,1,10)]
        num = 3

        self.assertEqual(150, MaxSumWeight(num, input))