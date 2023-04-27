
"""Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и 
количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""


first_element = int(input("First element of progression:"))
N = int(input("Enter a step of progression: "))
count_of_elements = int(input("Count of elements: "))
gen_arithmetical_list = [(first_element + (i-1) * N) for i in range(first_element,first_element+count_of_elements)] 

print(gen_arithmetical_list)