# Дано двозначне число. Знайти суму і добуток його цифр.
# Гришан Богдан 141 група.

number = int(input("Введите двузначное число: "))

numeral1 = number % 10
numeral2 = number // 10
sum_ = numeral1 + numeral2
prod = numeral1 * numeral2

print("Сумма цифр равна: " + str(sum_))
print("Произвдение цифр равно: " + str(prod))
