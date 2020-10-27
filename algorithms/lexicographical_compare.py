def lexicographical_compare(first, second):
    for e, f in zip(first, second):
        if f < e:
            return False
        elif e < f:
            return True
    if len(second) <= len(first):
        return False
    return True
