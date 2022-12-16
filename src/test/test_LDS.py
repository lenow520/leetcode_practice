from unittest import TestCase
from script.largestdivsubset.solution import LDS
class testMSW(TestCase):
    def test_case1(self):
        input = [(2,3,20),(2,1,10)]
        num = 3

        self.assertEqual(50, LDS(num, input))