import random
import time
from binarySearch import binarySearch
from dataGen import generateData
from insertionSort import insertionSort
from linearSearch import linearSearch
''' Selectively remove specific hashtags to see run the trials you want'''



timeArr = []
input = [5, 10, 100, 1000, 10000, 30000, 50000, 75000]
quantity = [5, 10, 100, 1000, 10000, 30000, 50000, 75000]
for input in quantity:
    list1 = generateData(input)
    # insertionSort(list1)
    # list.sort(key=lambda y: y.model)
    
    for j in range(1,11):
        # x = random.choice(list1).model
        # y = 10000000000
        startTime = time.time()
        # insertionSort(list1)
        # list1.sort(key=lambda y: y.model)
        # for i in range(0, 20):
        #     print(list1[i])
        # for j in range(len(list1) - 20, len(list1)):
        #     print(list1[j])
        # linearSearch(list1, y)
        # binarySearch(list1, 0, len(list1) - 1, y)
        # for i in range(0, 20):
        #     print(list1[i])
        # for j in range(len(list1) - 20, len(list1)):
        #     print(list1[j])
        endTime = time.time()
        random.shuffle(list1)
        diff = endTime - startTime
        timeArr.append(diff)

print(timeArr)
