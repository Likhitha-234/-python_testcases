import sys
sys.path.append("D:\Python codes")

import characterstring

import unittest
class Test_res(unittest.TestCase):
    def testcas_1(self):
        self.assertEqual(characterstring.totalch("likhitha"),8)
    def testcase_2(self):
        self.assertEqual(characterstring.totalch(""),0)

if __name__=="__main__":
    unittest.main()
