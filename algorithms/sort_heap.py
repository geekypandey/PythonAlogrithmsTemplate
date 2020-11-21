import heapq


def sort_heap(arr, reverse=False):
    _heapify = heapq.heapify
    _heappop = heapq.heappop
    arr_copy = arr.copy()

    if reverse:
        _heapify = heapq._heapify_max
        _heappop = heapq._heappop_max

    _heapify(arr_copy)
    return [_heappop(arr_copy) for _ in range(len(arr_copy))]
