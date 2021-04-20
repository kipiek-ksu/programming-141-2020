'''Лабораторная номер 5
Толочный Виталий 141
Задание номер 2(6 задача)
Задано список. Написати програму, яка сформує новий список в якому змінено місцями два рядки:
рядок, що містить максимальний елемент, і рядок, що місмтить мінімальний елемент.'''

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
'''введение двухмерного масива'''
list1 = []
num = int(input("Введите количество строк в вашей матрице: "))
for i in range(0, num):
    list1.append(module.InputList())
for i in list1:
    module.OutputList(i)

'''Поиск индекса рядка с максимальным элементом'''
list2 = []
for i in list1:
    list2.append(module.FindMax(i))
maxIndex = FindMax(list2)

'''Поиск индекса рядка с минимальным элементом'''
list2 = []
for i in list1:
    list2.append(FindMin1(i))
minIndex = FindMin(list2)
'''Обмен рядков местами'''
for i in range(0, len(list1[0])):
    list1[minIndex][i],list1[maxIndex][i] = list1[maxIndex][i],list1[minIndex][i]

for i in list1:
    module.OutputList(i)
