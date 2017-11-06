# file utility module used for listing, reading, updating files


import os
import fnmatch


# print list of files within user dir
def list_files():
    files = os.listdir(directory)
    pattern = "*.txt"
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            print(file)


# read file contents
def read_file(file):
    # open file for read only
    f = open(directory + "/" + file, "r")
    print("/n" + f.read() + "/n")
