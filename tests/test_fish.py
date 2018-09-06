import unittest
from codility.lessons.lesson7.fish import *


class FishTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution([4,3,2,1,5], [0,1,0,0,0]), 2)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FishTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
