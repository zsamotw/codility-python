import unittest
from codility.lessons.lesson2.cyclicrotation import *


class CyclicRotationTest(unittest.TestCase):

    def test_rotation_for_38976(self):
        self.assertEqual(solution([3, 8, 9, 7, 6], 3), [9, 7, 6, 3, 8])

    def test_rotation_for_000(self):
        self.assertEqual(solution([0, 0, 0], 3), [0, 0, 0])

    def test_rotation_for_1234(self):
        self.assertEqual(solution([1, 2, 3, 4], 4), [1, 2, 3, 4])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CyclicRotationTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
