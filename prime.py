import sys
sys.path.append("D:\python codes")
import Primeprogram

import unittest


class Test_prime(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(Primeprogram.prime(4),"yes it is not prime")

if __name__=="__main__":
    unittest.main()

