"""7. Задано список (якщо треба згенерувати відповідний список). Написати програму, яка визначає добуток
від‘ємних парних чисел першого стовпчика."""
import random  # Импортируем библиотеку для генерации рандомных чисел
# Предлагаем пользователю сгенерировать список автоматически, или ввести вручную
firstCommand = input('Enter "generate" to auto-generate list of numbers, or "custom" to enter your own list: ')
# Создаем переменные
matrix = []
composition = 1
if firstCommand == 'generate':  # Если пользователь захотел сгенерировать список автоматически
    matrixSize = 10  # Указываем размер матрицы по умолчанию
    for rowIndex in range(matrixSize):  # Переюираем рядки
        row = []
        for columnIndex in range(matrixSize):  # Перебираем столбцы
            row.append(random.randint(-100, 100))  # Заполняем матрицу
        matrix.append(row)  # Кладем список со значениями столбцов в матрицу
elif firstCommand == 'custom':  # Если пользователь хочет ввести список вручную
    columns = int(input('Enter number of columns: '))  # Просим ввести количество столбцов матрицы
    rows = int(input('Enter number of rows: '))  # Просим ввести количество рядков
    for rowIndex in range(rows):  # Перебираем рядки
        row = []
        for columnIndex in range(columns):  # Перебираем столбцы
            # Просим пользователя ввести значение
            value = input('Enter [' + str(rowIndex) + '][' + str(columnIndex) + ']: ')
            row.append(int(value))  # Кладем значение в матрицу
        matrix.append(row)  # Кладем список со значениями столбцов в матрицу
else:
    print('Error: undefined command: "' + firstCommand + '"')
    exit()
print('')
print('Matrix: ')
for rowIndex in range(matrixSize):  # Перебираем рядки
    string = str(matrix[rowIndex][0])  # Создаем переменную "string",
    # в которую мы склеим значения всех елементов матрицы
    for columnIndex in range(1, matrixSize):  # Перебираем столбцы
        string += ' ' + str(matrix[rowIndex][columnIndex])  # Склеиваем
    print(string)
# Находим произведение отрицательных четных чисел первой колонки
for row in matrix:
    if row[0] < 0 and row[0] % 2 == 0:  # Если число меньше нуля и четное
        composition *= row[0]  # Умножаем
print(composition)
