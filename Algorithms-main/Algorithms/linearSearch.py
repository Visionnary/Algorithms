import dataGen


def linearSearch(arr, search):
    for index, i in enumerate(arr):

        if i.model == int(search):
            return index

    return "Not Found"
