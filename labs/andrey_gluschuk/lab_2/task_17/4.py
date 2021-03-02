'''
 Глущук Андрій 141
 Лабораторна робота №2
    17. Дано три цілих числа. Визначте, скільки серед них збігаються. Програма повинна вивести одне з
    чисел: 3 (якщо все збігаються), 2 (якщо два збігається) або 0 (якщо все числа різні)
'''

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))
c = int(input("Enter number C: "))

if a == b and b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)