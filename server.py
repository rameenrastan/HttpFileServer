import fnmatch
import os
import socket
import sys


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


def init():
    print("web-server socket initiated...")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = "localhost"
    port = 2727
    serversocket.bind((address, port))
    serversocket.listen(5)
    print("web-server socket listening (address: %s, port: %s)" % (address, port))
    while True:
        print("web-server socket listening for incoming connections...")
        (clientsocket, address) = serversocket.accept()
        ct = client_thread(clientsocket)
        ct.run()


def main():
    init()
    list_files()
    read_file("test.txt")


if __name__ == "__main__":
    main()
