import unittest
from codility.lessons.lesson6.numberofdistinctintersection import *


class IntersectionTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([1, 5, 2, 1, 4, 0]), 11)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(IntersectionTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
