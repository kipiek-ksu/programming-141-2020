"""
     Глущук Андрій 141
     Лабораторна робота №6
     Завдання 3
 5. is_prime(n: int) -> bool: n (n >= 1) є простим числом
"""


def is_prime(n):
    """
    Counts the number of digits and the sum of digits in a number.
    Outputs a tuple of the number of digits and sum of digits.
    """
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
        i += 1
    return (count < 2)


x = int(input("Enter a number: "))
print(is_prime(x))
