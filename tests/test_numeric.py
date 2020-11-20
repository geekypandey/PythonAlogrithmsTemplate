import unittest

from hypothesis import given
import hypothesis.strategies as st

from numeric import accumulate
from numeric import adjacent_difference
from numeric import partial_sum


class AccumulateTestCase(unittest.TestCase):

    @given(st.lists(st.integers()))
    def test_accumulate_without_init(self, arr):
        self.assertEqual(accumulate(arr), sum(arr))

    @given(st.lists(st.integers()), st.integers())
    def test_accumulate_with_init(self, arr, init):
        self.assertEqual(accumulate(arr, init=init), sum(arr) + init)


class AdjacentDiffereceTestCase(unittest.TestCase):

    def _is_invariant_satisfied(self, out, arr):
        if len(arr) < 2:
            return not out
        else:
            if len(out) != len(arr) - 1:
                return False
            return (sum(out) == (arr[-1] - arr[0]))

    @given(st.lists(st.integers()))
    def test_adjacent_difference(self, arr):
        out = adjacent_difference(arr)
        self.assertTrue(self._is_invariant_satisfied(out, arr))


class PartialSumTestCase(unittest.TestCase):

    def _is_invariant_satisfied(self, out, arr):
        n = len(arr)
        if len(out) != len(arr):
            return False
        for idx in reversed(range(1, n)):
            if (out[idx] - out[idx-1]) != arr[idx]:
                return False
        return True

    @given(st.lists(st.integers()))
    def test_partial_sum_without_func(self, arr):
        out = partial_sum(arr)
        self.assertTrue(self._is_invariant_satisfied(out, arr))

    @given(st.lists(st.integers()))
    def test_partial_sum_with_func(self, arr):
        pass
