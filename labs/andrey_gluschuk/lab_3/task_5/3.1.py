"""
     Глущук Андрій 141
     Лабораторна робота №3
     Завдання 1
 5. Підрахувати k - кількість тризначних натуральних чисел, сума цифр яких дорівнює n (1≤n≤27).
"""


n = int(input("Enter a number N (1≤N≤27): "))
i = 100
count = 0

if 1 <= n <= 27:
    while 99 < i < 1000:
        if (i // 100) + (i % 100 // 10) + (i % 10) == n:
            print(i)
            count += 1
        i += 1
    print("Amount of numbers: ", count)
else:
    print("Error. 1 ≤ N ≤ 27.")