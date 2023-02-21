import sys
sys.path.append("D:\Python codes")
import fifthelement
import unittest

class Test_Alternate(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(fifthelement.alter(20),[5,10,15])
    def testcase_2(self):
        self.assertEqual(fifthelement.alter(30),[5,10,15,20,25])


if __name__=="__main__":
    unittest.main()
