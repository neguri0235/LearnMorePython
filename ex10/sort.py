import sys
import logging
import argparse

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def read_from_stdin():
    input_raw = sys.stdin.readlines()
    data = list(filter(None,map(lambda s : s.rstrip(), input_raw)))
    return data

def output(data):
    for e in data:
        print(e)

def do_sort_with_nemeric(data):
    data.sort(key=int)
    output(data)

def do_sort_reverse(data):
    data.sort(reverse=True)
    output(data)

def do_sort_default(data):
    data.sort()
    output(data)

def do_sort_ignore_case(data):
    data = sorted(data, key=str.upper)
    output(data)

def worker(args):
    data = read_from_stdin()
    if args.numeric:
        do_sort_with_nemeric(data)
        sys.exit(0)
    
    if args.reverse:
        do_sort_reverse(data)
        sys.exit(0)
    if args.case:
        do_sort_ignore_case(data)
        sys.exit(0)

    do_sort_default(data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--reverse', action='store_true', dest='reverse', help='reverse the result of comparisons')
    parser.add_argument('-f','--ignore-case', action='store_true', dest='case', help='fold lower case to upper case characters')
    parser.add_argument('-g', '--general-numeric-sort', action='store_true', dest='numeric', help='compare according to general numerical value')
    args = parser.parse_args()

    logging.debug(args.reverse)
    logging.debug(args.case)
    logging.debug(args.numeric)
    worker(args)