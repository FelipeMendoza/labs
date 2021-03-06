#!/usr/bin/env python
import unittest

from difference import DiffState, sieve


class TestSieve(unittest.TestCase):
    def test_values(self):
        pp = sieve(100, prime_power=True)
        prefix = [2, 3, 4, 5, 7, 8, 9, 11]
        self.assertEqual(pp[:len(prefix)], prefix)
        self.assertIn(32, pp)
        self.assertIn(64, pp)


class DifferenceSet(unittest.TestCase):
    def setUp(self):
        self.dsets = [[0, 1, 3],
                      [0, 1, 3, 9],
                      [0, 1, 4, 14, 16],
                      [0, 1, 3, 8, 12, 18],
                      [0, 1, 3, 13, 32, 36, 43, 52],
                      [0, 1, 3, 7, 15, 31, 36, 54, 63],
                      [0, 1, 3, 9, 27, 49, 56, 61, 77, 81],
                      ]

    def test_ds(self):
        for s in self.dsets:
            k = len(s)
            ds = DiffState(k)
            ds.search()
            self.assertEqual(ds.current, s)


if __name__ == '__main__':
    unittest.main()
