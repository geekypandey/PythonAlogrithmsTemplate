import heapq


def make_heap(arr):
    arr_copy = arr.copy()
    heapq._heapify_max(arr_copy)
    return arr_copy
