from file_operation import *



file_name = get_path('phonebook.txt')
data_ph = read_file(file_name)
print(type(data_ph), data_ph)

print(data_ph[0])
file_name = get_path('exp_phonebook.txt')
write_whole_file(file_name, data_ph)
    