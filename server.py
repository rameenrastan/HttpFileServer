# server module handling server-socket creation, life-cycle and user requests

import argparse
import os
import socket
import sys
from threading import Thread
import util

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
    print('Httpfs socket created...')
    try:
        sock.bind((host, port))
        print('Httpfs socket binding has completed...')
    except Exception as e:
        print('Httpfs has encountered an error: %s' % e)
        sys.exit()

    # listen on socket
    sock.listen(10)
    print("Httpfs socket now listening at: {host: '%s', port: %s}" % (host, port))

    # listen for any incoming connections
    while True:
        conn, addr = sock.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Received connection from: {ip: %s, port: %s}' % (ip, port))
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except Exception as e:
            print('Httpfs error encountered: %s' % e)

    # close socket
    sock.close()


# handle user requests
def client_thread(conn, ip, port):

    request = conn.recv(4096)
    request = request.decode('utf8').rstrip()
    print('Connection {ip: %s, port: %s} requested: %s' % (ip, port, request))

    # prepare response to send back to client
    response = process_request(request)

    response = response.encode('utf8')
    conn.sendall(response)
    conn.close()
    print('Connection from: {ip: %s, port: %s} has closed...' % (ip, port))


def process_request(request):
    if request == "get/":
        files = util.list_files()
        files_str = ""
        for f in files:
            files_str = files_str + f + "\n"
        return files_str
    else:
        return "Sorry, '%s' command does not exist" % request


def main():
    init_server()
    # list_files()
    # read_file("test.txt")


if __name__ == "__main__":
    main()
