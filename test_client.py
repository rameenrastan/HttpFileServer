# simple client to test sending requests to server-socket

import socket
import sys

def client():
    # create client socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(("localhost", 9999))
    except Exception as e:
        print(e)
        sys.exit()

    # handle user input to request from server
    clients_input = input("Please enter a request...\n")
    sock.send(clients_input.encode("utf8")) # we must encode the string to bytes
    server_response = sock.recv(4096).decode("utf8")

    print("Server Response: \n %s" % server_response)


def main():
    client()


if __name__ == "__main__":
    main()
