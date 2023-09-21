import unittest
from sort_linear import sort_array

class TestSortArray(unittest.TestCase):
    def test_sort_array_empty(self):
        self.assertEqual(sort_array([]), [])

    def test_sort_array_single(self):
        self.assertEqual(sort_array([1]), [1])

    def test_sort_array_sorted(self):
        self.assertEqual(sort_array([1, 2, 3]), [1, 2, 3])

    def test_sort_array_unsorted(self):
        self.assertEqual(sort_array([3, 2, 1]), [1, 2, 3])

    def test_sort_array_duplicates(self):
        self.assertEqual(sort_array([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])

    def test_sort_array_negative(self):
        self.assertEqual(sort_array([-3, -2, -1]), [-3, -2, -1])

    def test_sort_array_mixed(self):
        self.assertEqual(sort_array([3, -2, 1, 0, -1]), [-2, -1, 0, 1, 3])

if __name__ == '__main__':
    unittest.main()