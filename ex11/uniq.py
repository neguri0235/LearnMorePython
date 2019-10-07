import sys
import logging
import argparse
from pprint import pprint as pp

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)


def read_data_from():
#    raw_data = list(filter(None, map(lambda s : s.rstrip(),sys.stdin.readlines())))
    raw_data = sys.stdin.readlines()
    remove_new_line = map(lambda s: s.rstrip(), raw_data)
    remove_empty_str = list(filter(None,remove_new_line))
    return remove_empty_str

def make_dict(data):
    d = dict()
    for e in data:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    return d



def worker(args):
    data = read_data_from()
    dict_data = make_dict(data)
#    pp(dict_data)
    logging.debug(dict_data)

    if args.count:
        for key, val in dict_data.items():
            print('{} {}'.format(val,key))
        sys.exit(0)
    if args.repeated:
        for key, val in dict_data.items():
            if val >=2 :
                print(key)
        sys.exit(0)

    if args.unique:
        for key, val in dict_data.items():
            if val == 1:
                print(key)
    for key in dict_data:
        print(key)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--count', action='store_true', dest='count', help='prefix lines by the number of occurrences')
    parser.add_argument('-d','--repeated', action='store_true', dest='repeated', help='only print duplicate lines')
    parser.add_argument('-u', '--unique', action='store_true', dest='unique', help='only print unique lines')
    args = parser.parse_args()

    logging.debug(args.count)
    logging.debug(args.repeated)
    logging.debug(args.unique)
    worker(args)