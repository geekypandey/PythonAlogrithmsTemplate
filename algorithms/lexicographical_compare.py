import itertools


def lexicographical_compare(first, second):
    for e, f in itertools.zip_longest(first, second):
        if e is None or (f is not None and e < f):
            return True
        elif f is None or f < e:
            return False
    return False
