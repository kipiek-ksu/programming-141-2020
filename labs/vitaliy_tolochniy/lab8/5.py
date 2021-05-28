"""Лабораторная работа 8
Толочный Виталий 141
Задача 5
Описати програму з використанням словника, у якій зберігаються дані про
країни та назви міст. Для кожного міста знайти країну, у якій воно знаходиться.
Знайти країни з мінімальною та максимальною кількістю міст."""

dict0 = dict()
def inputDict():
    print("Введите значения в следующем порядке: Страна Город : ")
    l1 = [i for i in input().split()]
    if dict0.get(l1[0]) == None:
        l2 = []
        l2.append(l1[1])
        dict0[l1[0]] = l2
    else:
        dict0[l1[0]].append(l1[1])        

def outputDict():
    for key, value in dict0.items():
        print("Страна: ", key, "Город: ", value)
        
def MinMaxCities():
    d1 = dict()
    Min = 1000
    Max = 0
    for key, value in dict0.items():
        if len(value) > Max:
            d1["Max"] = key
            Max = len(value)
        if len(value) < Min:
            d1["Min"] = key
            Min = len(value)
    return d1

num = int(input("Сколько пар Страна и город вы хотите ввести?: "))
for i in range(num):
    inputDict()
outputDict()
print(MinMaxCities())
