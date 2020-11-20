import heapq


def push_heap(arr, item):
    arr_copy = arr.copy()
    arr_copy.append(item)
    heapq._siftdown_max(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy
