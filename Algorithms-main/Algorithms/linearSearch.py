def linearSearch(arr1, search):
    for index, i in enumerate(arr1):
        if i.model == int(search):
            return index
    return "Not Found"
