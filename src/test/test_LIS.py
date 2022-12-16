from unittest import TestCase
from script.longestincseq.solution import LIS

class testLIS(TestCase):
    def test_case1(self):
        input = [(2,3,20),(2,1,10)]
        num = 3

        self.assertEqual(50, LIS(num, input))