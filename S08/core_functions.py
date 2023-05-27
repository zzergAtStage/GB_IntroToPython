
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
    5:  'Reload a phone book',
    6:  'Save changes to a file',
    7:  'Exit.'
}
#menu editing
menu_editing_items = {
    1: 'Name',
    2: 'Surname',
    3: 'Region code',
    4: 'Phone number'
}
def print_menu(menu_items_f):
    for key in menu_items_f.keys():
        print(key, ' - ', menu_items[key])


