"""
     Глущук Андрій 141
     Лабораторна робота №6
     Завдання 2
 5. sum_range(a: int, b: int) -> int: сума всіх цілих чисел між a та b
"""


def sum_range(x, y):
    """
    Returns the sum of all integers between A and B (not including them).
    """
    i = 0
    for number in range(x + 1, y):
        i += number
    return i


a = int(input("Enter a number A: "))
b = int(input("Enter a number B: "))
print("Sum of numbers in range(A, B): ", sum_range(a, b))
