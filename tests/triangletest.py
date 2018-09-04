import unittest
from codility.lessons.lesson6.triangle import *


class TriangleTest(unittest.TestCase):
    def test_1234(self):
        self.assertEqual(solution([1, 2, 3, 4]), True)

    def test_10251820(self):
        self.assertEqual(solution([10, 2, 5, 1, 8, 20]), True)

    def test_105051(self):
        self.assertEqual(solution([10, 50, 5, 1]), False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TriangleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
