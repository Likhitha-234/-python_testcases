import sys
sys.path.append("D:\Python codes")

import filterdict
import unittest
class Test_filter(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(filterdict.filterdict({'Jack': 12000, 'Max': 20000, 'Hack': 25000, 'Nack': 80000}),{'Jack': 12000})

if __name__=="__main__":
    unittest.main()
