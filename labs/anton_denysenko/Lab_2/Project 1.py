'''3. Дано три числа. Знайти суму двох найбільших з них.'''

import heapq
A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))
C = int(input("Введите третье число: "))
mylist = [A, B, C]
G = (heapq.nlargest(2, mylist))
print(G[0] + G[1])