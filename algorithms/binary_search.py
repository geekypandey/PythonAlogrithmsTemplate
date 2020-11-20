def binary_search(arr, target):
    if not arr:
        return False
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high-low)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return False
