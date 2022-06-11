
def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid].model == x:
            return mid
        elif arr[mid].model < x:
            l = mid + 1
        else:
            r = mid - 1
    return "Not Found"
