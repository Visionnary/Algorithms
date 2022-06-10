def linearSearch(arr, x):
 
    for i in range(len(arr)):
 
        if arr[i].model == x:
            return i
 
    return -1