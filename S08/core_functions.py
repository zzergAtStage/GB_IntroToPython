
#function to get prompt
def get_prompt(choice_int = None):
    if choice_int == None:
        default_prompt =    ("===== USER MENU ======\n"
                            "1. Search subscriber by name/surname"
                            "2. ") 
        
        
        return ""
    return "default"

#menu options
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
#menu editing
menu_editing_items = {
    1: 'Name',
    2: 'Surname',
    3: 'Region code',
    4: 'Phone number'
}
#delete conformation
menu_delete_conformation = {
    1: 'Yes',
    2: 'No',
    3: 'Oh no, let\'s fall back!'
}
# THIS code works not as inspected - the keys from menu_items is used as addresses 
# while iterator goes over second collection!!!!
# def print_menu(menu_items_f):
#     for key in menu_items_f.keys():
#         print(key, ' - ', menu_items[key])

def print_menu(menu_items_f):
    for key, value in menu_items_f.items():
        print(key, ' - ', value)
