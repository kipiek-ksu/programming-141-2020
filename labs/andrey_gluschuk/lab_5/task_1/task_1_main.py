"""
     Глущук Андрій 141
     Лабораторна робота №5
     Завдання 1
    1. Завдання:
Розробіть функції для здійснення наступних операцій зі списками:
1. Введення списку;
2. Заповнення списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук максимального елементу;
6. Сортування списку за зростанням (спаданням);
7. Пошук середнього арифметичного;
"""


import task_1_function
print("Select function:\n '1' - Enter list\n '2' - Random numbers\n '3' - List out")
print(" '4' - Search\n '5' - Max\n '6' - Sort\n '7' - Average\n Type '0' to exit.")

select = None
while select != "0":
    select = input("Enter the number of function: ")

    if select == '1':
        task_1_function.list_enter()
    elif select == '2':
        task_1_function.list_random()
    elif select == '3':
        task_1_function.list_out()
    elif select == '4':
        task_1_function.list_search()
    elif select == '5':
        task_1_function.list_max()
    elif select == '6':
        task_1_function.list_sort()
    elif select == '7':
        task_1_function.list_average()
    else:
        print("Incorrect number of function!")
        print("Select function:\n '1' - Enter list\n '2' - Random numbers\n '3' - List out")
        print(" '4' - Search\n '5' - Max\n '6' - Sort\n '7' - Average\n Type '0' to exit.")
    print()
