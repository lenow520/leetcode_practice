from unittest import TestCase
# from script.wordsplit.solution import WordSplit
from script.wordsplit.solution2 import WordSplit

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

    def test_case5(self):
        input = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]

        self.assertEqual('base,ball', WordSplit(input))

    def test_case6(self):
        input = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z,BASEBA"]

        self.assertEqual('base,ball', WordSplit(input))

    def test_case7(self):
        input = ["baseball", "apple,bat,cat,goodbye,HELLO,yellow,why,a,t"]
        self.assertEqual('not possible', WordSplit(input))

    def test_case8(self):
        input = ['HELLOHELLO', "apple,bat,cat,goodbye,HELLO,yellow,why,a,t,HELL"]
        self.assertEqual('not possible', WordSplit(input))


    def test_case9(self):
        input = ["hellcat", "hellcaaat,a,t"]

        self.assertEqual('not possible', WordSplit(input))

    def test_case10(self):
        input = ['HELLOHELO', "HELLO,a,t,HELL"]

        self.assertEqual('not possible', WordSplit(input))

    def test_case11(self):
        input = ['aaabbc', "AAA,aaa,bb,bbc"]

        self.assertEqual('aaa,bbc', WordSplit(input))
