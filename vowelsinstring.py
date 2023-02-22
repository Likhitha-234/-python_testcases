import sys
sys.path.append("D:\Python codes")

import vowels1

import unittest
class Test_vowelss(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(vowels1.vowels("likki"),['a','e'])

if __name__=="__main__":
    unittest.main()
