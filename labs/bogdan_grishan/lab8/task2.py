"""
З множини чисел [1..n] виділити підмножину простих чисел виду k2+1
"""

C = int(input("Введите C: "))
N = {i for i in range(C)}
list1 = [i * i + 1 for i in range(C)]
print(N.intersection(list1))