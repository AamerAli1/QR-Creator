import glob
import shutil
import os
import time
from datetime import datetime



def check_if_to_print(to_print):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    list_of_files = glob.glob(to_print+"\*.txt")
    if list_of_files:
        print("Printing :" + list_of_files[0] + "       " + timestamp)
        return True
    else:
        print("Nothing to print"+ "       " + timestamp)
        return False



def get_new_file(to_print):
    # getting the latest file name
    # this will be an initially empty folder and soon as there is file in it , it will be processed
    list_of_files = glob.glob(to_print + "\*.txt")  # * means all if need specific format then *.csv
    if list_of_files:
        file_to_print = max(list_of_files, key=os.path.getctime)
        return file_to_print




    # moving the file to done after printing
def move_done_file(file_to_print,done):
    src = file_to_print
    name_of_file = str(src)
    name_of_file = list(map(str,name_of_file.split("\\")))
    name = name_of_file[-1]
    dest = done + name
    shutil.move(src, dest)

def move_err_file(file_to_print,error_pdf):
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M:%S")
    src = file_to_print
    name_of_file = str(src)
    name_of_file = list(map(str, name_of_file.split("\\")))
    name = name_of_file[-1]
    dest = error_pdf + name
    print("Error occured with file: " + name + "       " + timestamp)
    shutil.move(src, dest)


# # checking if the file is moved
# list_of_files_done = glob.glob(file_to_print)  # * means all if need specific format then *.csv
# if list_of_files_done:
#     print(True)