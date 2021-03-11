"""2. Дано рядок, що містить повне ім'я файлу (наприклад, C:\WebServers\home\testsite\www\myfile.txt').
Виділіть з цього рядка ім'я файлу без розширення. """

link = input(r'Введите имя(пример: C:\WebServers\home\testsite\www\myfile.txt): ')
i = link.rfind('\\')
j = link.find('.', i)
name = link[i + 1 : j]
print(name)
