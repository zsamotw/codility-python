import unittest
from codility.lessons.lesson5.minavagtwoslice import *


class MinAvgTwoSlice(unittest.TestCase):
    def test_4225158(self):
        self.assertEqual(solution([4, 2, 2, 5, 1, 5, 8]), 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MinAvgTwoSlice)
    unittest.TextTestRunner(verbosity=2).run(suite)
