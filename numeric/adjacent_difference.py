def adjacent_difference(arr):
    return [s - f for f, s in zip(arr, arr[1:])]
