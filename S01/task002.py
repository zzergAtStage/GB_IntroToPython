"""Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |"""
a = 0
sum = 0
while a < 100 or a > 999:
    a = int(input("Input third digit number: "))

while a > 0:
    sum += a % 10
    a = a//10
print("sum of number is: " + str(sum))