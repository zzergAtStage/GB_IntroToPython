import os
import csv
from core_functions import *

#composing a file_path
def get_path(file_name):
    working_directory = os.getcwd()
    working_sub = '\\S08\\resource\\'
    file_path = working_directory + working_sub + file_name
    return file_path

def read_file(file_name):
   i_row = 0
   client = []
   clients = {} #changed to a dictionary
   with open(file_name) as filedata:
        reader = csv.reader(filedata,delimiter=" ", quotechar='"')
        for row in reader:
            if i_row != 0: #skip header
                client =  row[0].split(',')
                clients[i_row - 1] = client
            i_row += 1
        
   return clients

def write_whole_file(file_name, clients):
    file_exists = os.path.exists(file_name)
    headers = ['First Name', 'Last Name', 'Phone Number']
    while True:
        if file_exists == False:
            with open(file_name, "w", newline='' ) as filedata:
                #header
                data_writer = csv.writer(filedata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                data_writer.writerow(headers)
                for keys, value in clients.items():
                    data_writer.writerow(value)
            filedata.close()
            break
        else:
            print(f"File {file_name} already exists! Would you like to overwrite it?")
            print_menu(menu_delete_conformation)
            overwrite = int(input())
            file_exists = False if overwrite == 1 else True