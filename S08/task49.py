from file_operation import *
from dictionary_operations import *
from core_functions import *
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
file_name = get_path('phonebook.txt')
data_ph = read_file(file_name)
print("Data was readed successful")
data_res = []
#menu
while True:
    option = ''
    try:
        print_menu(menu_items)
        option = int(input('Enter your choice: '))
    except: #user may input non number value
        print('Wrong input. Please enter a number ...')
    if option == 1:
        print_phone_book(data_ph)
    elif option == 2:
        data_res = search_subscriber(data_ph, get_input("Enter name or surname: "))
        print_phone_book(data_res)
    elif option == 3:
        data_res = search_by_code(data_ph, get_input("Enter region code: "))
        print_phone_book(data_res)
    elif option == 4:
        subscriber = input("Enter name or surname: ")
        update_subscriber(data_ph, subscriber)
    elif option == 8:
        write_whole_file(file_name, data_res)
        print("Arivederchi! ")
        exit()

file_name = get_path('exp_phonebook.csv')
write_whole_file(file_name, data_ph)

data_set = update_subscriber(data_ph, sub)