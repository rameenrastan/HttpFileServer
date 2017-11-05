import os, fnmatch
import socket
import threading

# define directory name
directory = "server-files"

def server(host, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host, port))
        listener.listen(10)
        while True:
            conn, addr = listener.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
    finally:
        listener.close()

def handle_client(conn, addr):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
    finally:
        conn.close()        


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
    server('',8080)
    list_files()
    read_file("test.txt")


if __name__ == "__main__":
    main()
