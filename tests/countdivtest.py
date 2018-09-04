import unittest
from codility.lessons.lesson5.countdiv import *


class CountDivTest(unittest.TestCase):
    def test_6_11_2(self):
        self.assertEqual(solution(6, 11, 2), 3)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CountDivTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
