"""
     Глущук Андрій 141
     Лабораторна робота №4
     Завдання 4
 13. Користувач вводить з клавіатури числа в рядок до тих пір, поки не введе число 0. На основі
введених даних потрібно сформувати список, що складається з квадратів введених чисел.
"""


print('Enter a numbers (0 to stop): ')
numbers = list()

while True:
    n = input()
    numbers.append(int(n))
    if int(n) == 0:
        break

square = [i**2 for i in numbers]
print(square)
