# server module handling server-socket creation, life-cycle and user requests

import argparse
import os
import socket
import sys
from threading import Thread
import util

directory = "server-files"

# initialize server with params from user
def init_server():
    args = parse()
    run(port=args['p'], verbose=args['v'])


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
    if args.h:
        perform_help()
    else:
        return vars(args)


# run server
def run(host='localhost', port=8080, verbose=False):
    # create socket and bind it
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if verbose: print('Httpfs socket created...')
    try:
        sock.bind((host, port))
        if verbose: print('Httpfs socket binding has completed...')
    except Exception as e:
        print('Httpfs has encountered an error: %s' % e)
        sys.exit()

    # listen on socket
    sock.listen(10)
    if verbose: print("Httpfs socket now listening at: {host: '%s', port: %s}" % (host, port))

    # listen for any incoming connections
    while True:
        conn, addr = sock.accept()
        ip, port = str(addr[0]), str(addr[1])
        if verbose: print('Received connection from: {ip: %s, port: %s}' % (ip, port))
        try:
            Thread(target=client_thread, args=(conn, ip, port, directory)).start()
        except Exception as e:
            print('Httpfs error encountered: %s' % e)

    # close socket
    sock.close()


# handle user requests
def client_thread(conn, ip, port, directory):

    request = conn.recv(4096)
    request = request.decode('utf8').rstrip()
    print('Connection {ip: %s, port: %s} requested: %s' % (ip, port, request))

    # prepare response to send back to client
    response = process_request(request, directory)

    response = response.encode('utf8')
    conn.sendall(response)
    conn.close()
    print('Connection from: {ip: %s, port: %s} has closed...' % (ip, port))


# handle user request
def process_request(request, directory):
    if request == "get /":
        return util.list_files(directory)
    elif request.startswith("get /"):
        filename = request.replace("get /", "")
        return util.read_file(filename)
    elif request.startswith("post /"):
        # obtain all request terms
        terms = request.split()
        # obtain filename
        filename = terms[1].replace("/", "")
        # obtain content
        content = ""
        content_terms = terms
        content_terms.pop(0)
        content_terms.pop(0)
        for t in content_terms:
            content = content + " " + t
        return util.overwrite_file(filename, content)
    else:
        return "sorry, '%s' command does not exist" % request


def main():
    init_server()


if __name__ == "__main__":
    main()
