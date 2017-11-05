import argparse
import os

# parse user input
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

# perform user help request
def perform_help():
    print('\nhttpfs is a simple file server.')
    print('Usage:\n\thttpfs [-v] [-p PORT] [-d PATH-TO-DIR]\n')
    print('The commands are:\n\n\t-v\tPrints debugging messages.')
    print('\t-p\tSpecifies the port number that the server will listen and serve at. Default is 8080.')
    print('\t-d\tSpecifies the directory that the server will use to read/write requested files. \n\t\tDefault is the current directory when launching the application')


def main():
    print(parse())


if __name__ == '__main__':
    main()
