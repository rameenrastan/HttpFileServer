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
        file_content = "\n" + f.read() + "\n"
        return file_content
    except:
        return "%s file does not exist" % file


#overwrite file conents
def overwrite_file(file, content):
    # open file for overwrite
    f = open(directory + "/" + file, "w+")
    if not content:
        return "please specify content for %s" % file
    f.write(content)
    f.seek(0)
    response = "\n" + f.read() + "\n"
    return response
