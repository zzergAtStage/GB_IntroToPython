
"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, 
а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа."""


X = int(input("X: "))
Y = 0
right_range = 1000
while (not Y <= right_range or Y == 0): 
    Y = int(input("Y: ")) #just example how to do value check
adding_secret_nums = X + Y
multiplying_secret_nums = X * Y
print("{0} + {1}".format(X,Y), " = ", (X + Y))
print("{0} * {1}".format(X,Y), " = ", (X * Y))

#generating an answer by loop
is_find = False
i = 0
while i <= right_range and not is_find:
    y= 0
    while y <= right_range and not is_find:
        if (i+y == adding_secret_nums) and (i*y == multiplying_secret_nums): 
            print("Secret numbers are:{0},{1}".format(i,y))
            is_find = True
            breakpoint
        y += 1
    i += 1
if is_find :
    None 
else:print("Something went wrong...")