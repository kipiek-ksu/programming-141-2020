"""
     Глущук Андрій 141
     Лабораторна робота №6
     Завдання 1
 5. digit_sum_count(d: int) -> Tuple[int, int]: кількість та суму цифр числа
"""


def digit_sum_count(x):
    """
    Counts the number of digits and the sum of digits in a number.
    Outputs a tuple of the number of digits and sum of digits.
    """
    digit_count = 0
    sum_count = 0
    temp = abs(x)
    if x == 0:
        digit_count = 1
    while temp > 0:
        digit_count += 1
        sum_count += temp % 10
        temp //= 10
    return digit_count, sum_count


a = int(input("Enter a number: "))
print("Number of digits, sum of digits: ", digit_sum_count(a))
