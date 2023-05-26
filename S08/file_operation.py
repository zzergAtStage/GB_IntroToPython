import os
import csv
import re

#composing a file_path
def get_path(file_name):
    working_directory = os.getcwd()
    file_path = working_directory + file_name
    print(file_path)
    return file_path

def read_file(file_name):
   file_path = get_path(file_name = file_name)
   i_row = 0
   clients = []
   with open(file_path) as filedata:
        reader = csv.reader(filedata,delimiter=" ", quotechar='"')
        for row in reader:
            if i_row == 0:
                print(f'Column names are {", ".join(row)}')
                i_row += 1
            else:
                clients.append(row)
            i_row += 1
        
   return clients

def write_whole_file(file_name, clients):
    file_path = get_path(file_name=file_name)
    with open(file_path, "w", newline='' ) as filedata:
       data_writer = csv.writer(filedata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       #header
       data_writer.writerow(['First Name', 'Last Name', 'Phone Number'])
       data_writer.writerows(clients)