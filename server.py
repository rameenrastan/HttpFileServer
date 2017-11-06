# server module handling server-socket creation, life-cycle and user requests

import argparse
import os
import socket
import sys
from threading import Thread

# initialize server with params from user
def init_server():
    args = parse()
    print("args port: %s" % args['p'])
    run(port=args['p'])


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


def run(host='localhost', port=8080):

    # create socket and bind it
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('httpfs socket created...')
    try:
        sock.bind((host, port))
        print('httpfs socket binding has completed...')
    except Exception as e:
        print('httpfs has encountered an error: %s' % e)
        sys.exit()

    # listen on socket
    sock.listen(10)
    print("socket now listening at: {host: '%s', port: %s}" % (host, port))

    # listen for any incoming connections
    while True:
        conn, addr = sock.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Received connection from: {ip: %s, port: %s}' % (ip, port))
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except Exception as e:
            print('httpfs error encountered: %s' % e)

    # close socket
    sock.close()


# handle user requests
def client_thread(conn, ip, port):

    request = conn.recv(4096)
    request = request.decode('utf8').rstrip()
    print('user request: %s' % request)

    response = request.encode('utf8')
    conn.sendall(response)
    conn.close()
    print('connection from: {ip: %s, port: %s} has closed...' % (ip, port))





















# run web-server
# def run_server(host="localhost", port=8080):
#     listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         print("httpfs initiated...")
#         listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         listener.bind((host, port))
#         listener.listen(10)
#         print("httpfs listening on (host: %s, port: %s)" % (host, port))
#         while True:
#             print("httpfs is listening for incoming connections...")
#             conn, addr = listener.accept()
#             print("Got a connection from %s" % str(addr))
#             threading.Thread(target=handle_client, args=(conn, addr)).start()
#     except Exception as e:
#         print("httpfs error occured: %s" % (e))
#     finally:
#         print("httpfs closing...")
#         listener.close()
#
#
# # server handle user requests
# def handle_client(conn, addr):
#     try:
#         while True:
#             data = conn.recv(1024)
#             if not data:
#                 break
#             conn.sendall(data)
#     finally:
#         conn.close()


def main():
    init_server()
    # list_files()
    # read_file("test.txt")


if __name__ == "__main__":
    main()
