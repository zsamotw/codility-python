import unittest
import sys
sys.path.insert(0, r'/home/tw/it/python/')
from codility.lessons.lesson4.frogriverone import *


class FrogRiverOneTest(unittest.TestCase):
    def test_12345_3(self):
        self.assertEqual(solution([1, 2, 3, 4, 5], 3), 2)

    def test_13142354_5(self):
        self.assertEqual(solution([1, 3, 1, 4, 2, 3, 5, 4], 5), 6)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FrogRiverOneTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
