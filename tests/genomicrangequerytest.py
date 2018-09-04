import unittest
from codility.lessons.lesson5.genomicrangequery import *


class GenomicRangeQueryTest(unittest.TestCase):
    def test_CAGCCTA_n2(self):
        self.assertEqual(solutionN2(
            'CAGCCTA', [2, 5, 0], [4, 5, 6]), [2, 4, 1])

    def test_CAGCCTA(self):
        self.assertEqual(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]), [2, 4, 1])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GenomicRangeQueryTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
