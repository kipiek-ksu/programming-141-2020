
Толочний Виталiй 141
Розробіть функції для здійснення наступних операцій зі списками:
1. Введення списку;
2. Заповнення списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук максимального елементу;
6. Сортування списку за зростанням (спаданням);


import random


def InputList():

    print(
        "Введите в строку последовательность, которую вы хотите преобразовать в список, разделите элементы пробелом: ")
    listt = [int(i) for i in input().split()]
    return listt


def RandInt(Num):

    listt = []
    for i in range(0, Num):
        listt.append(int(random.randint(1, 100)))
    return listt


def OutputList(listt):

    for i in range(0, len(listt)):
        listt[i] = str(listt[i])
    print(' '.join(listt))


def FindAnElement(listt, el):

    for i in range(0, len(listt)):
        if listt[i] == el:
            return i
    return -1


def FindMax(listt):

    max1 = listt[0]
    for i in listt:
        if i > max1:
            max1 = i
    return max1


def SortList(listt, reverse):

    for i in range(0, len(listt)):
        listt[i] = int(listt[i])
    for i in range(1, len(listt)):
        b = len(listt) - 1
        while (b >= i):
            if listt[b - 1] > listt[b]:
                listt[b - 1], listt[b] = listt[b], listt[b - 1]
            b -= 1
    print(listt)
    if reverse:
        l2 = listt[::-1]
        for i in listt[::-1]:
            l2.append(i)
        return l2
    return listt


def Averege(listt):

    S = 0
    for i in listt:
        S += int(i)
    return S / len(listt)
