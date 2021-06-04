"""Лабораторная работа 10
Толочный Виталий 141
Задача 6
Описати клас, який містить інформацію: про співробітників Міжрегіонального інституту бізнесу.
Структура запису - прізвище, рік народження, стаж роботи, оклад. Розробити програму, що за
прізвищем визначає стаж роботи."""

def findYears(workers, sur):
    for i in workers:
        if i.surname == sur:
            return i.yearsOfWork
    
class Worker:
    surname = ""
    yearOfBirth = 0
    yearsOfWork = 0
    salary = 0

    def __init__(self, surname, yearOfBirth, yearsOfWork, salary ):
        self.surname = surname 
        self.yearOfBirth = yearOfBirth
        self.yearsOfWork = yearsOfWork
        self.salary = salary
        
workers = []
a = int(input("Сколько рабочих вы хотите ввести?: "))
print("Входные данные в формате: фамилия, год рождения, годы работы, заработная плата: ")
for i in range(a):
    l1 = [j for j in input().split()]
    worker = Worker(l1[0],l1[1],l1[2],l1[3])
    workers.append(worker)

sur = input("Введите фамилию или 0, если вы закончили: ")
while(sur != "0"):
    print(findYears(workers, sur))
    sur = input("Введите фамилию или 0, если вы закончили: ")
