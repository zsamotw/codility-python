import unittest
from codility.lessons.lesson4.missinginteger import *


class MissingIntegerTest(unittest.TestCase):
    def test_1345(self):
        self.assertEqual(solution([1,3,4,5]), 2)

    def test_123457(self):
        self.assertEqual(solution([1,2,-3,4,5,7]), 3)

    def test_32(self):
        self.assertEqual(solution([-3,-2]), 1)

    def test_53248(self):
        self.assertEqual(solution([5,3,2,4,8]), 6)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MissingIntegerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
