import dataGen

def defaultSort(array):
    newList = array
    newList = sorted(array, key=lambda array:array["model"])
    return newList
