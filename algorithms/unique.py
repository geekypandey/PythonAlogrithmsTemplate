def unique(arr):
    out = []
    for a in arr:
        if len(out) > 0 and out[-1] == a:
            continue
        out.append(a)
    return out
