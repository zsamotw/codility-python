import unittest
import sys
sys.path.insert(0, r'/home/tw/it/python/')
from codility.lessons.lesson3.tapeequilibrium import *


class TapeEquilibriumTest(unittest.TestCase):
    pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TapeEquilibriumTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
