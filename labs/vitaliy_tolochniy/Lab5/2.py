

import module

def FindMax(listt):
    max1 = listt[0]
    maxInd = 0
    for i in range(0, len(listt)):
        if listt[i] > max1:
            max1 = listt[i]
            maxInd = i
    return maxInd

def FindMin(listt):
    max1 = listt[0]
    maxInd = 0
    for i in range(0, len(listt)):
        if listt[i] < max1:
            max1 = listt[i]
            maxInd = i
    return maxInd

def FindMin1(listt):
    max1 = listt[0]
    for i in range(0, len(listt)):
        if listt[i] < max1:
            max1 = listt[i]
    return max1

list1 = []
num = int(input("Введите количество строк в вашей матрице: "))
for i in range(0, num):
    list1.append(module.InputList())
for i in list1:
    module.OutputList(i)


list2 = []
for i in list1:
    list2.append(module.FindMax(i))
maxIndex = FindMax(list2)


list2 = []
for i in list1:
    list2.append(FindMin1(i))
minIndex = FindMin(list2)

for i in range(0, len(list1[0])):
    list1[minIndex][i],list1[maxIndex][i] = list1[maxIndex][i],list1[minIndex][i]

for i in list1:
    module.OutputList(i)
