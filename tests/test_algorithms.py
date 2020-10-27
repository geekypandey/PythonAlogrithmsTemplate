import random
import unittest
import sys

from algorithms import any_of, all_of, none_of, sort, binary_search, unique, \
        lexicographical_compare


class AnyOfTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        ans = any_of(arr, lambda x: x>0)
        self.assertEqual(ans, False)

    def test_true(self):
        arr = [1,2,3,4,5]
        ans = any_of(arr, lambda x: x%2==0)
        self.assertEqual(ans, True)

    def test_false(self):
        arr = [1,3,5,7,9]
        ans = any_of(arr, lambda x: x%2==0)
        self.assertEqual(ans, False)


class AllOfTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        ans = all_of(arr, lambda x: x>0)
        self.assertEqual(ans, True)

    def test_true(self):
        arr = [1,2,3,4,5]
        ans = all_of(arr, lambda x: x>0)
        self.assertEqual(ans, True)

    def test_false(self):
        arr = [1,2,5,7,9]
        ans = all_of(arr, lambda x: x%2==0)
        self.assertEqual(ans, False)


class NoneOfTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        ans = none_of(arr, lambda x: x>0)
        self.assertEqual(ans, True)

    def test_true(self):
        arr = [1,2,3,4,5]
        ans = none_of(arr, lambda x: x<0)
        self.assertEqual(ans, True)

    def test_false(self):
        arr = [1,2,5,7,9]
        ans = none_of(arr, lambda x: x%2==0)
        self.assertEqual(ans, False)


class SortTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        self.assertEqual(sort(arr), [])

    def test_sorted_list(self):
        arr = [1,2,5,7,9]
        self.assertEqual(sort(arr), [1,2,5,7,9])

    def test_unsorted_list(self):
        arr = [5,4,3,2,1]
        self.assertEqual(sort(arr), [1,2,3,4,5])

    def test_random_list(self):
        arr = [random.randint(-500,500) for _ in range(500)]
        arr_copy = arr[:]
        self.assertEqual(sort(arr), sorted(arr_copy))

    def test_on_strings(self):
        arr = ['python', 'java', 'ruby', 'haskell', 'cplusplus', 'scala']
        arr_copy = arr[:]
        self.assertEqual(sort(arr, lambda x, y: len(x) < len(y)), sorted(arr_copy, key=len))

    def test_on_numbers_using_comparator_function(self):
        arr = [5,4,3,2,1]
        self.assertEqual(sort(arr, lambda x, y: x < y), [1,2,3,4,5])

    def test_descending_sort(self):
        arr = [1,2,3,4,5]
        self.assertEqual(sort(arr, reverse=True), [5,4,3,2,1])

    def test_descending_sort_using_comparator_function(self):
        arr = [1,2,3,4,5]
        self.assertEqual(sort(arr, lambda x, y : x > y), [5,4,3,2,1])

    def test_repeated_numbers(self):
        arr = [1,5,5,3,4,5,2,2,8,9,9,6,4,5,4,3,4,5]
        arr_copy = arr[:]
        self.assertEqual(sort(arr), sorted(arr_copy))


class BinarySearchTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        self.assertEqual(binary_search(arr, 5), False)

    def test_true(self):
        arr = [1,2,3,4,5]
        self.assertEqual(binary_search(arr, 4), True)

    def test_false(self):
        arr = [1,2,3,4,5]
        self.assertEqual(binary_search(arr, 99), False)

    def test_on_random_list_false(self):
        arr = [random.randint(-500, 500) for _ in range(500)]
        arr.sort()
        self.assertEqual(binary_search(arr, 999), False)


class UniqueTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        self.assertEqual(unique(arr), [])

    def test_one(self):
        arr = [1,1,2,2,2,3,4,5,6,6]
        self.assertEqual(unique(arr), [1,2,3,4,5,6])

    def test_two(self):
        arr = [1,2,3,4,5,6]
        self.assertEqual(unique(arr), [1,2,3,4,5,6])

    def test_three(self):
        arr = [1,2,2,3,2,4,4,5,6,5]
        self.assertEqual(unique(arr), [1,2,3,2,4,5,6,5])


class LexicographicalCompareTestCase(unittest.TestCase):

    def test_empty(self):
        first = []
        second = []
        self.assertEqual(lexicographical_compare(first, second), False)

    def test_strings_true(self):
        first = "Bar"
        second = "Foo"
        self.assertEqual(lexicographical_compare(first, second), True)

    def test_strings_false(self):
        first = "Foo"
        second = "Bar"
        self.assertEqual(lexicographical_compare(first, second), False)

    def test_strings_almost_equal(self):
        first = "Fooo"
        second = "Foo"
        self.assertEqual(lexicographical_compare(first, second), False)

    def test_strings_and_list(self):
        first = "Foo"
        second = ['B', 'a', 'r']
        self.assertEqual(lexicographical_compare(first, second), False)

    def test_list_and_list(self):
        first = ['F', 'o', 'o']
        second = ['B', 'a', 'r']
        self.assertEqual(lexicographical_compare(first, second), False)

    @unittest.skipIf(sys.version_info < (3,6), "dictionary not ordered in version below 3.6")
    def test_list_and_dictionary(self):
        first = ['B', 'a', 'r']
        second = {'F':1, 'o': 2, 'f':3}
        self.assertEqual(lexicographical_compare(first, second), True)



if __name__ == '__main__':
    unittest.main()

