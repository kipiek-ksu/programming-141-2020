"""
Дано рядок. Виведіть третій символ цього рядка,
перші п'ять символів цього рядка, всі символи у зворотному порядку.
"""

string = input(str("Введите строку:"))

print(string[2],string[:5], string[::-1], sep='\n')
