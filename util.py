# file utility module used for listing, reading, updating files


import os
import fnmatch

directory = "server-files"


# print list of files within user dir
def list_files():
    files_str = ''
    files = os.listdir(directory)
    pattern = "*.txt"
    file_list = []
    for file in files:
        if fnmatch.fnmatch(file, pattern):
            files_str = files_str + file + "\n"

    if not files:
        return "no files found..."
    else:
        return files_str


# read file contents
def read_file(filename):
    try:
        f = open(directory + "/" + filename, "r")
        response = "File: " + filename + "\n" + f.read()
        return response
    except:
        return "%s file does not exist" % filename


#overwrite file conents
def overwrite_file(filename, content):
    # open file for overwrite
    f = open(directory + "/" + filename, "w+")
    if not content:
        return "please specify content for %s" % file
    f.write(content)
    f.seek(0)
    response = "File: " + filename + "\n" + f.read()
    return response
