# simple client to test sending requests to server-socket

import socket

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 9999))
    msg = s.recv(1024)
    s.close()
    print (msg.decode('ascii'))

def main():
    client()


if __name__ == "__main__":
    main()
