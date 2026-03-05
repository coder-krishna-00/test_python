#!/usr/bin/python3

myfile = "/home/john/sample_dir/f2"
try:
    file = open(myfile, "a")    #r for readonly, a for append, w for write
except FileNotFoundError as e:
    print("File is not found.")
    print(e)
    exit(1)

movies = ["The Avengers", "The Lord of the rings", "James Bond"]

for movie in movies:
    file.write(movie + "\n")
file.close()
