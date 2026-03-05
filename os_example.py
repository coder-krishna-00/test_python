#!/usr/bin/env python3

import os

'''
This function checks if file exists.
You can give absolute path to find any file.
If the file doesnot exists this will create it.
'''
file = input("Enter a file name: ")
def file_exists (file):
    if os.path.isfile(file):
        print("File exists.")
    else:
        print("File does not exist. /n Creating it...")
        os.system("touch {}".format(file))
        print("Done. Here it is: ")
        os.system("ls | grep {}".format(file))

file_exists (file)
# print(os.getcwd())
# os.system('pwd')

# print(os.listdir())
# os.system('ls')