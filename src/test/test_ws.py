from unittest import TestCase
from script.wordsplit.solution import WordSplit

class testWS(TestCase):
    def test_case1(self):
        input = ["hellocat", "apple,bat,cat,goodbye,hello,yellow,why,a,t"]

        self.assertEqual('hello,cat', WordSplit(input))

    def test_case2(self):
        input = ["hellcat", "apple,bat,cat,goodbye,hello,yellow,why,t,a"]

        self.assertEqual('not possible', WordSplit(input))

    def test_case3(self):
        input = ["hellcat", "apple,bat,cat,goodbye,hello,yellow,why,t,a,hellcat"]

        self.assertEqual('not possible', WordSplit(input))

    def test_case4(self):
        input = ["hellcat", "hellcat"]

        self.assertEqual('not possible', WordSplit(input))

    def test_case4(self):
        input = ["hellcat", "hellcaaat,a,t"]

        self.assertEqual('not possible', WordSplit(input))

    def test_case5(self):
        input = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]

        self.assertEqual('base,ball', WordSplit(input))