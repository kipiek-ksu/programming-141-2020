"""
1. Введення списку;
2. Заповнення списку випадковими числами;
3. Виведення списку;
4. Пошук елементу за значенням;
5. Пошук максимального елементу;
6. Сортування списку за зростанням (спаданням);
7. Пошук середнього арифметичного;
"""


def list_enter():
    """Entering the list by the user."""
    a = input("Enter list: ").split()
    x = list(map(int, a))
    print(x)
    return x


lst = list_enter()


def list_random():
    """
    Replacing the list entered by the user with a list of random numbers from 0 to 9,
    with the same size.
    """
    import random
    a = len(lst)
    list.clear(lst)
    for i in range(a):
        lst.append(random.randint(0, 9))
    print(lst)
    return lst


def list_out():
    """List output."""
    print(lst)


def list_search():
    """Search for an item in the list."""
    x = int(input('Enter search letter/number: '))
    if x in lst:
        print(x, "is in list.")
    else:
        print(x, "isn't in list.")


def list_max():
    """Finds the maximum item in the list."""
    maximum = max(lst)
    print(maximum)
    return maximum


def list_sort():
    """Sorts the list from minimum to maximum and back."""
    print("From min: ", sorted(lst), "\nFrom max: ", sorted(lst, reverse=True))
    return lst


def list_average():
    """Prints the average value of a list item."""
    a = [x for x in map(float, lst)]
    print(str(sum(lst) / len(lst)))
    return a
