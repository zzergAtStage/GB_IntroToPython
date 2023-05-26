import os
import csv
import re

#composing a file_path
def get_path(file_name):
    working_directory = os.getcwd()
    working_sub = '\\S08\\resource\\'
    file_path = working_directory + working_sub + file_name
    print(file_path + '\n')
    return file_path

def read_file(file_name):
   i_row = 0
   clients = []
   with open(file_name) as filedata:
        reader = csv.reader(filedata,delimiter=" ", quotechar='"')
        for row in reader:
            if i_row != 0:
                clients.append(row[0].split(','))
            i_row += 1
        
   return clients

def write_whole_file(file_name, clients):
    file_exists = os.path.exists(file_name)
    if file_exists == False:
        with open(file_name, "w", newline='' ) as filedata:
            data_writer = csv.writer(filedata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #header
            data_writer.writerow(['First Name', 'Last Name', 'Phone Number'])
            data_writer.writerows(clients)
    else:
        print(f"File {file_name} already exists!")