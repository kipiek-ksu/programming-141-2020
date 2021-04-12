"""
     Глущук Андрій 141
     Лабораторна робота №5
     Завдання 2
    5. Задано список. Написати програму, яка змінить матрицю таким чином, щоб всі
елементи нижче головної діагоналі були нульовими.
"""

import task_2_function
print("Select function:\n '1' - Randomize matrix\n '2' - Change to zero function\n '3' - Matrix out")
print("Type '0' to exit.")

select = None
while select != "0":
    select = input("Enter the number of function: ")

    if select == '1':
        task_2_function.list_random()
    elif select == '2':
        task_2_function.list_changetozero()
    elif select == '3':
        task_2_function.list_out()
    else:
        print("Incorrect number of function!")
        print("Select function:\n '1' - Randomize matrix\n '2' - Change to zero function\n '3' - Matrix out")
        print("Type '0' to exit.")
