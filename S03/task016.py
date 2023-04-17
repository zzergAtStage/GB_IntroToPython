"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Ввод: 5
Ввод: 3 2 3 7 5
Ввод: 3
-> 2"""
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()

N = int(input("Parameter #1 (list size): "))
data_collection = []
str_prompt = "Parameter #2 ({0} numbers in row with spaces): ".format(N)
data_collection = input(str_prompt).split()

while (len(data_collection) != N):
    data_collection = input(str_prompt).split()
print("Your list is: ",data_collection)
for i in range(len(data_collection)):
    data_collection[i] = int(data_collection[i])
X = int(input("Parameter #3 (base number): "))
if X in data_collection:
    print("->{0}".format(X))
else:
    print("->None")
