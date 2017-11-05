import os, fnmatch


# define directory name
directory = "server-files"


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


def main():
    list_files()
    read_file("test.txt")


if __name__ == "__main__":
    main()
