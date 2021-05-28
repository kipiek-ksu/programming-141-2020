"""
     Глущук Андрій 141
     Лабораторна робота №8
     Завдання 1
 5. З множини чисел [1..n] виділити підмножину простих чисел p, z, таких, що
p - z =2 (пошук “близнят”).
"""

s = set(range(0, int(input("Enter N: "))))
prime = set()
twin_prime = set()

for number in s:
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k += 1
    if (k <= 0 and number != 0 and number != 1):
        set.add(prime, number)
print(prime)

for p in prime:
    for z in prime:
        if p - z == 2:
            twin_prime.add((p, z))
print('\nSet of tuples of twin numbers:\n', twin_prime)
