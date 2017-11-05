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
    for entry in files:
        if fnmatch.fnmatch(entry, pattern):
            print (entry)



def main():
    list_files()


if __name__ == "__main__":
    main()
