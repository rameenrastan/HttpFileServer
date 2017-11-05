import os, fnmatch


# define directory name
directory = "server-files"


# print list of files within user dir
def list_files():
    files = os.listdir(directory)
    pattern = "*.txt"
    for entry in files:
        if fnmatch.fnmatch(entry, pattern):
            print (entry)



def main():
    list_files()


if __name__ == "__main__":
    main()
