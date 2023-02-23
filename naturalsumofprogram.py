import sys
sys.path.append("D:\Python codes")

import naturalsumcode

import unittest
class Test_natural(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(naturalsumcode.naturalsum(10),55)

if __name__=="__main__":
    unittest.main()
