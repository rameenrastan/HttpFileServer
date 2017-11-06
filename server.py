# server module handling server-socket creation, life-cycle and user requests

import socket
import threading

# define directory name
directory = "server-files"

def server(host, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("web-server socket initiated...")
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((host, port))
        listener.listen(10)
        print("web-server listening ( host: %s, port: %s ) " % (host, port))
        while True:
            print("web-server is listening for incoming connection...")
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



def main():
    server('',8080)
    list_files()
    read_file("test.txt")


if __name__ == "__main__":
    main()
