import sys
sys.path.append("D:\python test cases")
import palindromeprogram_unit_test
import unittest

class Test_palindromeprogram(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(mergesort_unit_test.merge([5,6,3,4,2,1]),([0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 8, 10]))
    def testcase_2(self):
        self.assertEqual(mergesort_unit_test.merge([10,8,3,6,0,1]),([0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 8, 10]))
   


if __name__=="__main__":
    unittest.main()
