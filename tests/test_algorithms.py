import random
import unittest
import sys
import collections

from hypothesis import given
import hypothesis.strategies as st

from algorithms import any_of
from algorithms import all_of
from algorithms import none_of
from algorithms import sort
from algorithms import binary_search
from algorithms import unique
from algorithms import lexicographical_compare
from algorithms import make_heap
from algorithms import push_heap
from algorithms import pop_heap
from algorithms import partition
from algorithms import sort_heap


class AnyOfTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        ans = any_of(arr, lambda x: x%2==0)
        self.assertFalse(ans)

    @given(st.lists(st.integers().filter(lambda x: x%2 == 0), min_size=1))
    def test_true(self, arr):
        ans = any_of(arr, lambda x: x%2==0)
        self.assertTrue(ans)

    @given(st.lists(st.integers().filter(lambda x: x%2 != 0), min_size=1))
    def test_false(self, arr):
        ans = any_of(arr, lambda x: x%2==0)
        self.assertFalse(ans)


class AllOfTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        ans = all_of(arr, lambda x: x%2==0)
        self.assertTrue(ans)

    @given(st.lists(st.integers().filter(lambda x: x%2 == 0), min_size=1))
    def test_true(self, arr):
        ans = all_of(arr, lambda x: x%2==0)
        self.assertTrue(ans)

    @given(st.lists(st.integers().filter(lambda x: x%2 != 0), min_size=1))
    def test_false(self, arr):
        ans = all_of(arr, lambda x: x%2==0)
        self.assertFalse(ans)


class NoneOfTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        ans = none_of(arr, lambda x: x > 0)
        self.assertTrue(ans)

    @given(st.lists(st.integers(min_value=1)))
    def test_true(self, arr):
        ans = none_of(arr, lambda x: x < 0)
        self.assertTrue(ans)

    @given(st.lists(st.integers().filter(lambda x: x%2 == 0), min_size=1))
    def test_false(self, arr):
        ans = none_of(arr, lambda x: x%2==0)
        self.assertEqual(ans, False)


class SortTestCase(unittest.TestCase):

    def _is_invariant_satisfied(self, out, arr, reverse=False, comp=None):
        if comp is None:
            return out == sorted(arr, reverse=reverse)
        else:
            return all(comp(f, s) for f, s in zip(out, out[1:]))

    @given(st.lists(st.integers()))
    def test_sort_ascending_integer_without_comparator_func(self, arr):
        out = sort(arr)
        self.assertTrue(self._is_invariant_satisfied(out, arr))
        self.assertEqual(collections.Counter(arr), collections.Counter(out))

    @given(st.lists(st.integers()))
    def test_sort_descending_integer_without_comparator_func(self, arr):
        out = sort(arr, reverse=True)
        self.assertTrue(self._is_invariant_satisfied(out, arr, reverse=True))
        self.assertEqual(collections.Counter(arr), collections.Counter(out))

    @given(st.lists(st.text()))
    def test_sort_ascending_string_without_comparator_func(self, arr):
        out = sort(arr)
        self.assertTrue(self._is_invariant_satisfied(out, arr))
        self.assertEqual(collections.Counter(arr), collections.Counter(out))

    @given(st.lists(st.text()))
    def test_sort_descending_string_without_comparator_func(self, arr):
        out = sort(arr, reverse=True)
        self.assertTrue(self._is_invariant_satisfied(out, arr, reverse=True))
        self.assertEqual(collections.Counter(arr), collections.Counter(out))


class BinarySearchTestCase(unittest.TestCase):

    @given(st.integers())
    def test_empty(self, target):
        arr = []
        arr.sort()
        self.assertFalse(binary_search(arr, target))

    @given(st.lists(st.integers(), min_size=1))
    def test_binary_search_true(self, arr):
        arr.sort()
        target = random.choice(arr)
        self.assertTrue(binary_search(arr, target))

    @given(st.lists(st.integers(), min_size=1))
    def test_binary_search_false(self, arr):
        arr.sort()
        target = arr[-1] + 1
        self.assertFalse(binary_search(arr, target))


class UniqueTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        self.assertEqual(unique(arr), [])

    def test_one(self):
        arr = [1, 1, 2, 2, 2, 3, 4, 5, 6, 6]
        self.assertEqual(unique(arr), [1, 2, 3, 4, 5, 6])

    def test_two(self):
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(unique(arr), [1, 2, 3, 4, 5, 6])

    def test_three(self):
        arr = [1, 2, 2, 3, 2, 4, 4, 5, 6, 5]
        self.assertEqual(unique(arr), [1, 2, 3, 2, 4, 5, 6, 5])


class LexicographicalCompareTestCase(unittest.TestCase):

    @given(st.text(), st.text())
    def test_strings(self, first, second):
        self.assertEqual(lexicographical_compare(first, second), first < second)

    @given(st.lists(st.text()), st.lists(st.text()))
    def test_list_of_string(self, first, second):
        self.assertEqual(lexicographical_compare(first, second), first < second)

    @given(first=st.lists(st.text()), second=st.text())
    def test_list_and_string(self, first, second):
        second = list(second)
        self.assertEqual(lexicographical_compare(first, second), first < second)

    @unittest.skipIf(sys.version_info < (3, 6), "dictionary not ordered in version below 3.6")
    def test_list_and_dictionary(self):
        first = ['B', 'a', 'r']
        second = {'F': 1, 'o': 2, 'f': 3}
        self.assertEqual(lexicographical_compare(first, second), True)


class MakeHeapTestCase(unittest.TestCase):

    def _is_heap_variant_satisfied(self, arr):
        n = len(arr)
        endpos = len(arr)
        for pos in reversed(range(n//2)):
            leftpos = 2*pos + 1
            rightpos = 2*pos + 2
            if not arr[pos] >= arr[leftpos]:
                return False
            if rightpos < endpos and not arr[pos] >= arr[rightpos]:
                return False
        return True

    @given(st.lists(st.integers()))
    def test_make_heap(self, arr):
        out = make_heap(arr)
        self.assertTrue(self._is_heap_variant_satisfied(out))
        self.assertEqual(collections.Counter(arr), collections.Counter(out))


class PushHeapTestCase(unittest.TestCase):

    def _is_heap_variant_satisfied(self, arr):
        n = len(arr)
        endpos = len(arr)
        for pos in reversed(range(n//2)):
            leftpos = 2*pos + 1
            rightpos = 2*pos + 2
            if not arr[pos] >= arr[leftpos]:
                return False
            if rightpos < endpos and not arr[pos] >= arr[rightpos]:
                return False
        return True

    @given(st.lists(st.integers()))
    def test_push_heap(self, arr):
        arr = make_heap(arr)
        out = push_heap(arr, 5)
        self.assertTrue(self._is_heap_variant_satisfied(out))
        self.assertEqual(collections.Counter(arr) + collections.Counter([5]),
                         collections.Counter(out))


class PopHeapTestCase(unittest.TestCase):

    def _is_heap_variant_satisfied(self, arr):
        n = len(arr)
        endpos = len(arr)
        for pos in reversed(range(n//2)):
            leftpos = 2*pos + 1
            rightpos = 2*pos + 2
            if not arr[pos] >= arr[leftpos]:
                return False
            if rightpos < endpos and not arr[pos] >= arr[rightpos]:
                return False
        return True

    def test_empty(self):
        arr = []
        item, out = pop_heap(arr)
        self.assertIsNone(item)
        self.assertEqual(out, arr)

    @given(st.lists(st.integers(), min_size=1))
    def test_pop_heap(self, arr):
        arr = make_heap(arr)
        exp_out = max(arr)
        item, out = pop_heap(arr)
        self.assertTrue(self._is_heap_variant_satisfied(out))
        self.assertEqual(exp_out, item)
        self.assertEqual(collections.Counter(out) + collections.Counter([item]),
                         collections.Counter(arr))


class PartitionTestCase(unittest.TestCase):

    def _is_invariant_satisfied(self, out, pred):
        first_half = True
        for ele in out:
            if pred(ele) and not first_half:
                return False
            if not pred(ele):
                first_half = False
        return True

    @given(st.lists(st.integers()))
    def test_partition_even_func(self, arr):
        pred = (lambda x: x%2 == 0)
        out = partition(arr, pred)
        self.assertTrue(self._is_invariant_satisfied(out, pred))
        self.assertEqual(collections.Counter(arr), collections.Counter(out))


class HeapSortTestCase(unittest.TestCase):

    def _is_invariant_satisfied(self, out, arr, reverse=False):
        return out == sorted(arr, reverse=reverse)

    @given(st.lists(st.integers()))
    def test_sort_heap_ascending_integer(self, arr):
        out = sort_heap(arr)
        self.assertTrue(self._is_invariant_satisfied(out, arr))

    @given(st.lists(st.integers()))
    def test_sort_heap_descending_integer(self, arr):
        out = sort_heap(arr, reverse=True)
        self.assertTrue(self._is_invariant_satisfied(out, arr, reverse=True))

    @given(st.lists(st.text()))
    def test_sort_heap_ascending_string(self, arr):
        out = sort_heap(arr)
        self.assertTrue(self._is_invariant_satisfied(out, arr))

    @given(st.lists(st.text()))
    def test_sort_heap_descending_string(self, arr):
        out = sort_heap(arr, reverse=True)
        self.assertTrue(self._is_invariant_satisfied(out, arr, reverse=True))
