from file_operation import *


prefix = ""
file_name = f'\\S08\\resourse\\{prefix}phonebook.txt'
data_ph = read_file(file_name)
print(type(data_ph), data_ph)

prefix = 'exp_'
new_file_name =  file_name
print(new_file_name)
write_whole_file(new_file_name, data_ph)
    