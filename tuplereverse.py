import sys
sys.path.append("D:\Python codes")
import unittest
import reversetuple
class Test_Dict(unittest.TestCase):
    def testcase(self):
        self.assertEqual(reversetuple.reverse((2,4,5,7,9)),(9, 7, 5, 4, 2))

if __name__ == "__main__":
    unittest.main()
