#
# Глущук Андрій 141
# Лабораторна робота №1
# 9. Дано двозначне число. Знайти суму і добуток його цифр.
#

x = int(input("Вкажіть двозначне число: "))

if x > 99 or x < 10:
    print("Введене число не є двозначним.")
else:   # Перевірка числа на двозначність
    sum      = (x // 10) + (x % 10)
    multiply = (x // 10) * (x % 10)
    print("Сума    цифр: " + str(sum) + '\n' + "Добуток цифр: " + str(multiply))
