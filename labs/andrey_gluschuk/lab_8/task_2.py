"""
     Глущук Андрій 141
     Лабораторна робота №8
     Завдання 2
 8. З множини простих чисел менших ніж n виділити підмножину чисел виду
2n+1, 2n-1.
"""

s = set(range(0, int(input("Enter N: "))))
prime = set()

for number in s:
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k += 1
    if (k <= 0 and number != 0 and number != 1):
        set.add(prime, number)
print(prime, '\n')

print('2n + 1:', {2 * n + 1 for n in prime})
print('2n - 1:', {2 * n - 1 for n in prime})
