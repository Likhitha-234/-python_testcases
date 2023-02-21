import sys
sys.path.append("D:\Python codes")
import unittest
import swapoffirstandlastvalue
class Test_Swap(unittest.TestCase):
    def testcase(self):
        self.assertEqual(swapoffirstandlastvalue.swap_firstandlast([2,3,4,5,6,7,8]),[8, 3, 4, 5, 6, 7, 2])


if __name__ == "__main__":
    unittest.main()
