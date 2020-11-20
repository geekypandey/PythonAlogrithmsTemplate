from functools import cmp_to_key
from functools import partial


def _cap_on_func(func, x, y):
    if func(x, y):
        return -1
    else:
        return 1


def sort(arr, func=None, reverse=False):
    if func:
        func = partial(_cap_on_func, func)
        return sorted(arr, key=cmp_to_key(func), reverse=reverse)
    else:
        return sorted(arr, reverse=reverse)
