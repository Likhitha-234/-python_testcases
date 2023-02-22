import sys
sys.path.append("D:\python codes")

import ithoccurance

import unittest
class Test_occurance(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(ithoccurance.ithoccurance(["hello","hello","hello","byee","likki","hello","abc","hello","yyg","hello"]),['hello', 'hello', 'hello', 'byee', 'likki', 'abc', 'hello', 'yyg', 'hello'])

if __name__=="__main__":
    unittest.main()
