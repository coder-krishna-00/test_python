#!/usr/bin/python3

myfile = "/home/john/sample_dir/f1"
try:
    file = open(myfile, "r")    #r for readonly, a for append, w for write
except FileNotFoundError as e:
    print("File is not found.")
    print(e)
    exit(1)
for line in file:
    print(line)
