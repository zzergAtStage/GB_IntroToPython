"""Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N."""

N = int(input("Input case N: "))

exponentiation = 0
exponent = 1
while True:
    exponentiation = 2 ** exponent
    if exponentiation < N:
        print("{0}^{1} = {2}".format(2,exponent,exponentiation))
        exponent +=2
    else:
        break

