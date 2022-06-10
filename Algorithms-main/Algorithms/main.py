import time
import random
import copy
import dataGen
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from linearSearch import linearSearch
from defaultSort import defaultSort
input = int(input())
startTime = time.time()
if __name__ == "__main__":
     #print(insertionSort(dataGen.generateData(input)))
     #print(linearSearch(dataGen.generateData(input)))
     list = dataGen.generateData(input)
     list.sort(key = lambda y: y.model)
     print(list)
endTime = time.time()
class main():
  count = 0
  n = 1000
  for i in range(n):
    count = count + 2
  print("This took " + str(endTime - startTime) + " s")



# def getTimeToRun(randomList, alg):
#     newList = copy.deepcopy(randomList)
#     timeStart = time.time()
#     if(alg == "bubble"):
#         insertionSort(newList)
#     elif (alg == "defaultSort"):
#         newList.sort()
#     timeEnd = time.time()
#     return timeEnd - timeStart


# def getRandomList(listSize):
#     randomList = [0] * listSize
#     for j in range(listSize):
#         randomList[j] = round(random.random() * listSize)
#     return randomList



