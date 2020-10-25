def binary_search(arr, target):
    n = len(arr)
    if n == 0:
        return False
    low = 0; high = n-1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False
