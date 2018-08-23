import unittest
from codility.lessons.lesson4.maxcounters import *


class MaxCountersTest(unittest.TestCase):
    def test_3446144_5(self):
        self.assertEqual(solution(5, [3,4,4,6,1,4,4]), [3,2,2,4,2])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MaxCountersTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
