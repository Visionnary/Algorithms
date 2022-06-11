import dataGen


def insertionSort(arr):
    for i in range(1, len(arr)):
        key_item = arr[i].model
        j = i - 1
        test = arr[i]

        while j >= 0 and arr[j].model > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = test

    return arr
