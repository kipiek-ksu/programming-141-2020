"""
     Глущук Андрій 141
     Лабораторна робота №7
     Завдання 5
1.  Описати рекурсивну функцію Fact (N) дійсного типу, яка обчислює значення
    факторіала
    N! = 1 · 2 · ... · N
    (N> 0 - параметр цілого типу). За допомогою цієї функції обчислити факторіали
    п'яти даних чисел.
"""
result = []


def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n


for i in range(5):
    x = int(input("Введите число: "))
    result.append({x: fact(x)})
print(result)  # Вывод результата выполнил не с помощью print(fact(x)), а списком словарей