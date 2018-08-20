import unittest
import sys
sys.path.insert(0, r'/home/tw/it/python/')
from codility.lessons.lesson1.binarygap import *

class BinaryGapTest(unittest.TestCase):

    def test_binary_gap_for_9(self):
        self.assertTrue(solution(9), 2)
        print("in first test")

    def test_binary_gap_for_529(self):
        self.assertEqual(solution(529), 4)

    def test_binary_gap_for_1041(self):
        self.assertEqual(solution(1041), 5)

    def test_binary_gap_for_15(self):
        self.assertEqual(solution(15), 0)


    def test_binary_gap_for_32(self):
        self.assertEqual(solution(32), 0)

    def test_binary_gap_for_maxsize(self):
        self.assertEqual(solution(2147483647), 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BinaryGapTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
