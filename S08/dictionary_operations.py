import re
from core_functions import *

menu_editing_items = {
    1: 'Name',
    2: 'Surname',
    3: 'Region code',
    4: 'Phone number'
}

def print_phone_book(data_set):
    irow = 1
    for sub in data_set:
        print (irow,"\t",sub)
        irow += 1

def get_input(prompt = None):
    input_name = input(prompt)
    return str(input_name)

def search_subscriber(data_ph, subscriber):
    data_set = []
    for sub in data_ph:
        for field in sub:
            #search though all fields in the list elements via regex
            if re.search(subscriber, field, re.IGNORECASE):
                data_set.append(sub)
    print("dataset size = ", len(data_set))
    return data_set

def search_by_code(data_ph, code):
    data_set = []
    for sub in data_ph:
        print("type: ",type( sub[2]), str(sub[2]))
        if re.search(code, str(sub[2]), re.IGNORECASE):
            data_set.append(sub)
    print("dataset size = ", len(data_set))
    return data_set

def update_subscriber(data_ph,subscriber):
    subscriber_rec = search_subscriber(data_ph, subscriber)
    if len(subscriber_rec) > 1:
        print_phone_book(subscriber_rec) #shows non single data
        try:
            idx = int(input("   Which subscriber would you like to edit: "))
            subscriber_rec = subscriber_rec[idx - 1]
        except:
            print("Wrong input...")
    #editing...
    print_menu(menu_editing_items)
    next_step = get_input("Enter your choice: ")

        