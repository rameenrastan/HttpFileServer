# file utility module used for listing, reading, updating files


import os
import fnmatch

directory = "server-files"

# print list of files within user dir
def list_files():
    files = os.listdir(directory)
    pattern = "*.txt"

    file_list = []
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            file_list.append(file)

    return file_list

# read file contents
def read_file(file):
    # open file for read only
    f = open(directory + "/" + file, "r")
    print("/n" + f.read() + "/n")
