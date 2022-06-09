import time
import random
import copy
import dataGen
from bubbleSort import bubbleSort
from insertionSort import insertionSort

def main():
 startTime = time.time()
 count = 3
 n =1000
 for i in range(n):
    count = count + 2
 endTime = time.time()
 print("\n\nThis took " + str(endTime - startTime) + " s")

def getTimeToRun(randomList, alg):
  newList = copy.deepcopy(randomList)
  timeStart = time.time()
  if(alg == "bubble"): 
    insertionSort(newList)
  elif (alg == "defaultSort"):
    newList.sort()
  timeEnd = time.time()
  return timeEnd - timeStart

def getRandomList(listSize):
  randomList = [0] * listSize
  for j in range(listSize):
    randomList[j] = round(random.random() * listSize)
  return randomList

if __name__ == "__main__":
    List = []
    List.append(dataGen.generateData(10))
    print(insertionSort(List))

