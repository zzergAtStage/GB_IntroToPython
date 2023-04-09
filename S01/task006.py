"""Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
 и получали билет с номером. Счастливым билетом называют такой билет с
 шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
 Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
 Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no"""

# get user input and check count of digits
ticket_number = int(input("Input number of ticket (now we'll check it!):"))
part_one = 0
part_two = 0
current_digit = 0
while ticket_number > 0:
    if current_digit < 3:
        part_one += ticket_number % 10
    else:
        part_two += ticket_number % 10
    current_digit += 1
    ticket_number //=10

print(f"Your ticket is lucky:({part_one} = {part_two})", part_one == part_two)