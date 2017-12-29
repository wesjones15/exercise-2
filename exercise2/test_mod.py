import unittest
from modtest import evenDivisors

class DivisorsTestCase(unittest.TestCase):

    def test_range_1_5(self):
        self.assertEqual(evenDivisors(1, 5, 5), [5])

    def test_range_1_7(self):
        self.assertEqual(evenDivisors(1, 7, 7), [7])

    def test_for_type(self):
        self.assertTrue(isinstance(evenDivisors(1, 5, 5), list))

    def test_of_short_series(self):
        expectedValue = [10, 12, 14, 16, 18, 20]
        self.assertEqual(evenDivisors(10, 20, 2), expectedValue)

if __name__ == '__main__':
    unittest.main()