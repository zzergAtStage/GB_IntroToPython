#Explicit type conversion
# a = 3.56
# b = 5.12
# print (int(a+b))

"""Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while"""

n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)

