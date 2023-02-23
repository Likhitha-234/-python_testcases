import sys
sys.path.append("D:\Python codes")
import sumofdigitsnumber

import unittest
class Test_res(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(sumofdigitsnumber.sum(1234),10)
    def testcase_2(self):
        self.assertEqual(sumofdigitsnumber.sum(-12345),"cant add negative numbers")
    def testcase_3(self):
        self.assertEqual(sumofdigitsnumber.sum(0),0)

if __name__=="__main__":
    unittest.main()
