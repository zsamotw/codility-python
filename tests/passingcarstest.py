import unittest
from codility.lessons.lesson5.passingcars import *


class PassingCarsTest(unittest.TestCase):
    def test_01011(self):
        self.assertEqual(solution([0,1,0,1,1]), 5)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PassingCarsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
