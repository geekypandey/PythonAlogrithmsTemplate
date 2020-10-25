import itertools

def partial_sum(arr, func=None):
    return list(itertools.accumulate(arr, func=func))
