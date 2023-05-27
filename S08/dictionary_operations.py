import re
from core_functions import *



def print_phone_book(data_set):
    irow = 1
    for key, sub in data_set.items():
        print (key,"\t",sub)
        irow += 1

def get_input(prompt = None):
    input_name = input(prompt)
    return str(input_name)

def search_subscriber(data_ph, subscriber):
    data_set = {}
    for key, sub in data_ph.items():
        for field in sub:
            #search though all fields in the list elements via regex
            if re.search(subscriber, field, re.IGNORECASE):
                data_set[key] = sub
    print("dataset size = ", len(data_set))
    return data_set

def search_by_code(data_ph, code):
    data_set = {}
    for key, sub in data_ph.items():
        if re.search(code, str(sub[2]), re.IGNORECASE):
            data_set[key] = sub
    print("dataset size = ", len(data_set))
    return data_set

def update_subscriber(data_ph,subscriber):
    idx = 0
    subscriber_rec = search_subscriber(data_ph, subscriber)
    try:
        if len(subscriber_rec) > 1:
            print_phone_book(subscriber_rec) #shows non single data
            idx = int(input("   Which subscriber would you like to edit: "))
            subscriber_rec = subscriber_rec[idx]
        #editing...
        print_menu(menu_editing_items)
        next_step = int(get_input("Enter your choice: "))
        new_value = get_input(f" New value of [{menu_editing_items[next_step]}]: ")
        data_ph[idx][next_step-1] =  new_value
        print("Subscriber updated successfully: ",data_ph[idx] )
    except:
        print("Something went wrong...")

def delete_subscriber(data_ph,subscriber):
    idx = 0
    subscriber_rec = search_subscriber(data_ph, subscriber)
    #ask conformation
    if len(subscriber_rec) > 1:
        print_phone_book(subscriber_rec) #shows non single data
        idx = int(input("   Which subscriber would you like to delete: "))
    subscriber_rec = subscriber_rec[idx]
    print("Subscriber ", data_ph[idx], " well be deleted.")
    print_menu(menu_delete_conformation)
    conformation = int(input("Are you sure?: "))
    while True:
        if conformation == 1:
            del data_ph[idx]
            print("Goes out...")
            break
        else:
            print("O'key...")
            exit()