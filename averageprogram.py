import sys
sys.path.append("D:\Python codes")

import averagelist

import unittest
class Test_avg(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(averagelist.average([1,2,3,4,5]),3)

if __name__=="__main__":
    unittest.main()
