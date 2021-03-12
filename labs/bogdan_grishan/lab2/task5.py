"""
Дано три цілих числа. Визначте, скільки серед них збігаються. Програма повинна вивести одне з чисел:
3 (якщо все збігаються), 2 (якщо два збігається) або 0 (якщо все числа різні).
"""
number1 = int(input("Введите первое число:"))
number2 = int(input("Введите второе число:"))
number3 = int(input("Введите третье число:"))

if number1 == number2 and number2 == number3 and number1 == number3:
    print("3(Все числа совпали)")
elif number1 == number3 or number2 == number3 or number1 == number2:
    print("2(Совпали 2 числа)")
else:
    print("1(Совпадений не найдено)")
