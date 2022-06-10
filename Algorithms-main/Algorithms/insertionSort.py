import dataGen

def insertionSort(array):
    for i in range(1, len(array)):
        key_item = array[i].model
        j = i - 1
        test = array[i]

        while j >= 0 and array[j].model > key_item:
            array[j + 1] = array[j]
            j -= 1

            
        array[j + 1] = test
        
    return array
