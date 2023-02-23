import sys
sys.path.append("D:\Python codes")

import duplicateoflist

import unittest
class Test_duplicate(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(duplicateoflist.duplicate(([1,2,3,1,4,51,1,2,76,51])),([1, 2, 3, 4, 51, 76]))

if __name__=="__main__":
    unittest.main()
