import sys
sys.path.append("D:\Python codes")
import keycheck3

import unittest
class kcheck(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(keycheck3.checkkey({'a':1,'b':2,'name':"lagnar"},'name'),True)

if __name__=="__main__":
    unittest.main()
