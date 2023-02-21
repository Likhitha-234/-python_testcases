import sys
sys.path.append("D:\Python codes")

import countofdigitsofnumber

import unittest
class Test_total(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(countofdigitsofnumber.digitcount(234),3)
    def testcase_2(self):
        self.assertEqual(countofdigitsofnumber.digitcount(-1234),"cant count negative numbers")
    def testcase_3(self):
        self.assertEqual(countofdigitsofnumber.digitcount(0),0)

if __name__=="__main__":
    unittest.main()

