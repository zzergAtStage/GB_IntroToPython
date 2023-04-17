import os

def cls():
   os.system('cls' if os.name=='nt' else 'clear')

cls()
"""Задача 18: Требуется найти в массиве A[N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
Ввод: 5
Ввод: 1 2 6 4 9
Ввод: 8
-> 9"""

N = int(input("Parameter #1 (list size): "))
data_collection = []
str_prompt = "Parameter #2 ({0} numbers in row with spaces): ".format(N)
data_collection = input(str_prompt).split()

while (len(data_collection) != N):
    data_collection = input(str_prompt).split()
print("Your list is: ",data_collection)
#check inputted values
for i in range(len(data_collection)):
    data_collection[i] = int(data_collection[i])
X = int(input("Parameter #3 (base number): "))
#main action
min_gap = X - data_collection[0]
current_closest = 0
for i in range(len(data_collection)):
    tmp_min_gap = abs( X - data_collection[i])
    if tmp_min_gap < min_gap: 
       min_gap = tmp_min_gap
       current_closest = i
print("Closest element is {0}".format(data_collection[current_closest]))