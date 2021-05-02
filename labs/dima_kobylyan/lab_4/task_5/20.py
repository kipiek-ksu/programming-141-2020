"""5(20)Дано список чисел .Порахуйте,скільки в ньому пар елементів , рівних один одному.
Вважаеться , що будь-які два елементи, рівні один одному утворюють одну пару ,яку
необхідно порахувати """
import random

lst = []
for i in range(10):
    lst.append(random.randint(0, 11))
lst.sort()
print(lst)
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j and lst[i] == lst[j]:
            print("рівні один одному елементи = ", (lst[i]))
            print(len(lst[i]))

