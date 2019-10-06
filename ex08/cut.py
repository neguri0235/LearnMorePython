""" 
cut.py

$ python cut.py sample.txt
$ python cut.py sample.txt -c 3
$ python cut.py sample.txt -c 1-5
$ python cut.py sample.txt -d " " -f 3
$ python cut.py sample.txt -d " " -f 3-5
$ python cut.py sample.txt -d ":" -f 3-5
"""

import argparse
import glob
import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)


def file_read(name):
    logging.debug(name)
    try:
        data = []
        sys.stdin = open(name,'r')
        line = sys.stdin.readline()
        while line:
            data.append(line)
            line = sys.stdin.readline()
        return data
    except:
        print("oops file open fail")
        sys.exit(0)


def char_worker(option, data):
    """ work for characters """
    opt = option.split('-')
    start_pos, end_pos = 0, 0
    if len(opt) == 1:
        start_pos , end_pos = int(opt[0]), int(opt[0])
    elif len(opt) == 2:
        start_pos, end_pos = int(opt[0]), int(opt[1])
    else:
        print("wrong input range")
        sys.exit(0)

    logging.debug("start_pos %s " % start_pos)
    logging.debug("end_pos %s " % end_pos)

    for line in data:
        for idx in range(start_pos-1, end_pos):
            print(line[idx],end='')
        print()

def deli_worker(option1, option2, data):
    """ work for delimiters """
    logging.debug("deli_worker")
    logging.debug("option1 : %s" % option1)
    logging.debug("option2 : %s" % option2)
    opt = option2.split('-')
    start_pos, end_pos = 0, 0
    if len(opt) == 1:
        start_pos , end_pos = int(opt[0]), int(opt[0])
    elif len(opt) == 2:
        start_pos, end_pos = int(opt[0]), int(opt[1])
    else:
        print("wrong input range")
        sys.exit(0)

    logging.debug("start_pos %s " % start_pos)
    logging.debug("end_pos %s " % end_pos)
    for line in data:
        split_data = line.split(option1)
        if len(split_data) < end_pos:
            continue
        #logging.debug("length of split data %s" % len(split_data))
        for idx in range(start_pos-1, end_pos):
            print(split_data[idx],end='')
        print()
    pass

def stdout(data):
    """ simple print data """
    for line in data:
        print(line,end='')

def worker(args):
    """ main function, it receives the argument from command prompt"""
    data = file_read(args.file)
    logging.debug(data)
    
    if args.c:
        char_worker(args.c, data)
    elif args.d:
        deli_worker(args.d, args.f, data)
    else:
        stdout(data)

if __name__== "__main__":
    """entry point of cut module"""

    parser = argparse.ArgumentParser()
    parser.add_argument("file",  help="target file")
    parser.add_argument("-c",    help="characters=LIST")
    parser.add_argument("-d",    help="delimiter=DELIM")
    parser.add_argument("-f",    help="fields=LIST")    
    args = parser.parse_args()
    logging.debug("-------argument-------")
    logging.debug("file: %s" % args.file)
    logging.debug("char: %s" % args.c)
    logging.debug("deli: %s" % args.d)
    logging.debug("field: %s" % args.f)
    worker(args)


"""
    parser.add_argument("-c",    action="count", default=0, help="characters=LIST")
    parser.add_argument("-d",    action="count", default=0, help="delimiter=DELIM")
    parser.add_argument("-f",    action="count", default=0, help="fields=LIST")    
"""        