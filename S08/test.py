menu_items = {
    0: '=========MENU==========',
    1:  'Print whole phone book',
    2:  'Search subscriber by name/surname', 
    3:  'Search subscribers by region code',
    4:  'Search and edit subscriber',
    5:  'Delete subscriber',
    6:  'Reload a phone book',
    7:  'Save changes to a file',
    8:  'Exit.'
}

menu_editing_items = {
    1: 'Name',
    2: 'Surname',
    3: 'Region code',
    4: 'Phone number'
}


# def print_menu(menu_items_f):
#     for key in menu_items_f.keys():
#         print(key, ' - ', menu_items[key])

def print_menu(menu_items_f):
    for key, value in menu_items_f.items():
        print(key, ' - ', value)



print_menu(menu_items)
print("\n")
print_menu(menu_editing_items)
