def partition(arr, pred):
    a = arr.copy()
    first = 0
    last = len(a) - 1
    while first < last:
        while pred(a[first]):
            first += 1
            if first == last:
                return a
        while not pred(a[last]):
            last -= 1
            if first == last:
                return a
        a[first], a[last] = a[last], a[first]
        first += 1
    return a
