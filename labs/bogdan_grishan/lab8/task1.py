"""
З множини чисел [1..n] виділити перетин підмножин - чисел виду 4k+1 і
5k+4.
"""

C = int(input("Введите C: "))
N = {i for i in range(C)}

list1 = [4 * i + 1 for i in range(C)]
list2 = [5 * i + 4 for i in range(C)]

print(N.intersection(list1))
print(N.intersection(list2))