import heapq


def pop_heap(arr):
    arr_copy = arr.copy()
    if not arr_copy:
        return (None, arr_copy)
    item = heapq._heappop_max(arr_copy)
    return (item, arr_copy)
