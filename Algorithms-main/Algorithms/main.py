import time
import random
import copy
from dataGen import generateData
from dataGen import genI
from insertionSort import insertionSort
from linearSearch import linearSearch
from binarySearch import binarySearch

input = int(input())
startTime = time.time()

if __name__ == "__main__":
    list = generateData(input)
    x = random.choice(list).model
    print(x)
    print(list)
    print(binarySearch(list, 0, len(list)-1, x))
    #print(insertionSort(list))
    #print(linearSearch(list, 5))
    #list.sort(key = lambda y: y.model)
endTime = time.time()


class main():
    count = 0
    n = 1000
    for i in range(n):
        count = count + 2
    print("This took " + str(endTime - startTime) + " s")
