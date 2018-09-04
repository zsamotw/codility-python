import unittest
from codility.lessons.lesson7.nesting import *


class NestingTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solution('()'), 1)

    def test_2(self):
        self.assertEqual(solution('()(()(()))()'), 1)

    def test_3(self):
        self.assertEqual(solution('())'), 0)

    def test_4(self):
        self.assertEqual(solution('()()())()()()()'), 0)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(NestingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
