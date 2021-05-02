"""8. Задано список. Написати програму, яка сформує новий список в якому змінено місцями останній рядок
і рядок, що містить мінімальний за абсолютною величиною елемент."""
import math

matrix = []  # Создаем начальный список
newMatrix = []  # Создаем конечный список
rows = int(input('Enter number of rows: '))  # Просим ввести количество рядков
columns = int(input('Enter number of columns: '))  # Просим ввести количество столбцов матрицы
minElement = 0
minElementRowIndex = 0
for rowIndex in range(rows):  # Перебираем рядки
    row = []
    for columnIndex in range(columns):  # Перебираем столбцы
        # Просим пользователя ввести значение
        value = int(input('Enter [' + str(rowIndex + 1) + '][' + str(columnIndex + 1) + ']: '))
        row.append(value)  # Кладем значение в матрицу
        if (rowIndex == 0 and columnIndex == 0):
            minElement = value
            minElementRowIndex = rowIndex
        if (math.sqrt(math.pow(value, 2)) < minElement):
            # Если это самый первый елемент, или если выполняется условие
            minElement = math.sqrt(math.pow(value, 2))
            minElementRowIndex = rowIndex
    matrix.append(row)  # Кладем список со значениями столбцов в матрицу
# Сохраняем нужные нам рядки в переменные
lastRow = matrix[len(matrix) - 1]
needRow = matrix[minElementRowIndex]
newMatrix = [] + matrix
# Меняем местами рядки
newMatrix[minElementRowIndex] = lastRow
newMatrix[len(newMatrix) - 1] = needRow
print('')
# Выводим матрицу в консоль
print('Matrix before: ')
for rowIndex in range(rows):  # Перебираем рядки
    string = str(matrix[rowIndex][0])  # Создаем переменную "string",
    # в которую мы склеим значения всех елементов матрицы
    for columnIndex in range(1, columns):  # Перебираем столбцы
        string += ' ' + str(matrix[rowIndex][columnIndex])  # Склеиваем
    print(string)
print('')
# Выводим конечную матрицу в консоль
print('Matrix new: ')
for rowIndex in range(rows):  # Перебираем рядки
    string = str(newMatrix[rowIndex][0])  # Создаем переменную "string",
    # в которую мы склеим значения всех елементов матрицы
    for columnIndex in range(1, columns):  # Перебираем столбцы
        string += ' ' + str(newMatrix[rowIndex][columnIndex])  # Склеиваем
    print(string)
