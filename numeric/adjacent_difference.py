import itertools

def adjacent_difference(arr):
    return list(itertools.starmap(lambda x, y: y-x, zip(arr, arr[1:])))
