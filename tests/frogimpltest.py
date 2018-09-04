import unittest
from codility.lessons.lesson3.frogimpl import *


class FrogImplTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FrogImplTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
