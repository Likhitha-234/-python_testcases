import sys
sys.path.append("D:\python codes")
import fibonacciprogram

import unittest



class Test_Fibonacci(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(fibonaaciprogram.fibonacci(9),[0,1,1,2,3,5,8,13,21])
    def testcase_1(self):
        self.assertEqual(fibonacciprogram.fibonacci(4),[0,1,1,2])
    def testcase_1(self):
        self.assertEqual(fibonacciprogram.fibonacci(7),[0,1,1,2,3,5,8])


if __name__=="__main__":
    unittest.main()
