#Обчислити дробову частину середнього геометричного трьох заданих позитивних чисел
#Барулін Олександр 141 група

number1 = float(input(" Введите первое позитивное число: "))
number2 = float(input(" Введите второе позитивное число: "))
number3 = float(input(" Введите третье позитивное число: "))

mean = (number1*number2*number3)**1/3

if number1 < 0 or number2 < 0 or number3 < 0:
    print("Введено неверное значение")
else:
    print("Средннее геометрическое трех чисел равно:" + str(mean))