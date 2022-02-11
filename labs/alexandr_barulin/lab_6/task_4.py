def reorganisation(list_of_numbers):
    return list(filter(lambda x: x < 0, list_of_numbers)) + \
           list(filter(lambda x: x == 0, list_of_numbers)) + \
           list(filter(lambda x: x > 0, list_of_numbers))


def solution():
    list_of_numbers = [-1, 2, 3, -5, -10, -100, 100, 1000, 0, 2000, 7984, -72987]
    print(*reorganisation(list_of_numbers))


solution()