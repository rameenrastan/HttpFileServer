# server module handling server-socket creation, life-cycle and user requests

import argparse
import os
import socket
import threading

# perform user help request
def perform_help():
    print('\nhttpfs is a simple file server.')
    print('Usage:\n\thttpfs [-v] [-p PORT] [-d PATH-TO-DIR]\n')
    print('The commands are:\n\n\t-v\tPrints debugging messages.')
    print('\t-p\tSpecifies the port number that the server will listen and serve at. Default is 8080.')
    print('\t-d\tSpecifies the directory that the server will use to read/write requested files. \n\t\tDefault is the current directory when launching the application\n')


# initialize server with params
def parse():
    parser = argparse.ArgumentParser(add_help=False)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # add arguments to CLI
    parser.add_argument('-h', action="store_true")
    parser.add_argument('-v', action="store_true")
    parser.add_argument('-p', type=int, default="8080")
    parser.add_argument('-d', type=str, default=dir_path)
    args = parser.parse_args()
    print(args)
    if args.h:
        perform_help()
    else:
        return vars(args)


def init_server():
    args = parse()
    print("args port: %s" % args['p'])
    run_server(port=args['p'])


# run web-server
def run_server(host="localhost", port=8080):
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
    except Exception as e:
        print("web-server error occured: %s" % (e))
    finally:
        print("web-server closing...")
        listener.close()


# server handle user requests
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
    init_server()
    # list_files()
    # read_file("test.txt")


if __name__ == "__main__":
    main()
