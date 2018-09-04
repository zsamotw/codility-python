import unittest
from codility.lessons.lesson2.oddoccurencesinarray import *


class OddOccurencesInArrayTest(unittest.TestCase):

    def test_rotation_for_121(self):
        self.assertEqual(solution([1, 2, 1]), 2)

    def test_rotation_for_12111(self):
        self.assertEqual(solution([1, 2, 1, 1, 1]), 2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(OddOccurencesInArrayTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
