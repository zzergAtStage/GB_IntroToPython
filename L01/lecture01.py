#Explicit type conversion
a = 3.56
b = 5.12
print (int(a+b))

"""Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while"""

N = int(input("Input N"))
i = 1
result = 1
while i < N:
    i += 1
    result *= i

print("Result N! = ", result )


