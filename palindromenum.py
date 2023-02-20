import sys
sys.path.append("D:\Python codes")

import palindromenumber

import unittest
class Test_pallin(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(palindromenumber.pallindrome(121),"the number is pallindrome")
    def testcase_2(self):
        self.assertEqual(palindromenumber.pallindrome(-4),"negative numbers")
    def testcase_3(self):
        self.assertEqual(palindromenumber.pallindrome(12),"the number is not pallindrome")

if __name__=="__main__":
    unittest.main()
