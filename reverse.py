import sys
sys.path.append("D:\python codes")
import reverseprogram
import unittest
class Test_rev(unittest.TestCase):
    def testcase_1(self):
        self.assertListEqual(reverseprogram.reverse([1,2,3,4]),[4,3,2,1])


if __name__=="__main__":
    unittest.main()
