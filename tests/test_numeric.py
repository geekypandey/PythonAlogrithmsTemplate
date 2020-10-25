import random
import unittest

from numeric import accumulate, adjacent_difference, partial_sum


class AccumuateTestCase(unittest.TestCase):

    def test_empty(self):
        arr = []
        self.assertEqual(accumulate(arr), 0)

    def test_one(self):
        arr = [1,2,3,4,5]
        self.assertEqual(accumulate(arr), 15)

    def test_with_initial_value(self):
        arr = [1,2,3,4,5]
        self.assertEqual(accumulate(arr, 5), 20)

    def test_on_random_list(self):
        arr = [random.randint(1, 500) for _ in range(500)]
        self.assertEqual(accumulate(arr), sum(arr))

    def test_on_random_list_with_initial_value(self):
        arr = [random.randint(1, 500) for _ in range(500)]
        self.assertEqual(accumulate(arr, 50), sum(arr) + 50)


class AdjacentDiffereceTestCase(unittest.TestCase):

    def _adjacent_difference(self, arr):
        ans = []
        n = len(arr)
        for i in range(1, n):
            ans.append(arr[i]-arr[i-1])
        return ans

    def test_empty(self):
        arr = []
        self.assertEqual(adjacent_difference(arr), self._adjacent_difference(arr))

    def test_one(self):
        arr = [1,2,3,4,5]
        self.assertEqual(adjacent_difference(arr), self._adjacent_difference(arr))

    def test_on_random_list(self):
        arr = [random.randint(-500,500) for _ in range(500)]
        self.assertEqual(adjacent_difference(arr), self._adjacent_difference(arr))


class PartialSumTestCase(unittest.TestCase):

    def _partial_sum(self, arr):
        ans = []
        for a in arr:
            if len(ans) == 0:
                ans.append(a)
            else:
                ans.append(a + ans[-1])
        return ans

    def test_empty(self):
        arr = []
        self.assertEqual(partial_sum(arr), self._partial_sum(arr))

    def test_one(self):
        arr = [1,2,3,4,5]
        self.assertEqual(partial_sum(arr), self._partial_sum(arr))

    def test_func_parameter(self):
        arr = [1,2,3]
        self.assertEqual(partial_sum(arr, lambda x, y: x*y), [1,2,6])

    def test_on_random_list(self):
        arr = [random.randint(-500,500) for _ in range(500)]
        self.assertEqual(partial_sum(arr), self._partial_sum(arr))
