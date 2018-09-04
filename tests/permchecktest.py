import unittest
from codility.lessons.lesson4.permcheck import *


class PermCheckTest(unittest.TestCase):
    def test_2435(self):
        self.assertEqual(solution([2, 4, 3, 5]), True)

    def test_1234(self):
        self.assertEqual(solution([1, 2, 3, 4]), True)

    def test_5798(self):
        self.assertEqual(solution([5, 7, 9, 8]), False)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PermCheckTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
