import random

"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
 а некоторые – гербом.   ок, которые нужно перевернуть, 
 чтобы все монетки были повернуты вверх одной и той же стороной. 
 Выведите минимальное количество монет, которые нужно перевернуть"""

N = int(input("Input amount of coins: "))
#0 - is avers, 1 is revers 
#finding a minimal of coins sides, to make it easy
coins = []
for i in range(N):
    coins.append(random.randint(0,1))
print(coins)
min_side_0 = coins.count(0)
min_side_1 = coins.count(1)
print((min_side_0,min_side_1) [min_side_0 > min_side_1])