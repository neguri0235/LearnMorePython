'''
grep [OPTIONS] PATTERN [FILE]
grep [OPTIONS] [-e PATTERN | -f FILE][FILE...]

$ grep hello abc.txt
$ grep -i HelLo abc.txt
$ grep include abc.txt abd.txt
$ grep include *.txt
'''

import re
import sys
import glob
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

def run(args):
    logging.debug("-------argument-------")
    logging.debug("pattern: %s" % args.pattern)
    logging.debug("file: %s" % args.file)
    data = extract_target_file_list(args.file)
    run_matcher(data, args.pattern)


def using_glob(file_list):
    logging.debug("-------glob list -------")
    logging.debug("len = %d" % len(file_list))
    glob_list = []
    for file in file_list:
        glob_list.append(glob.glob(file,recursive=True))
        for e in glob_list:
            logging.debug("%s" % e)
    logging.debug("glob list %d" % len(glob_list))
    return glob_list    

def extract_target_file_list(file):
    data = using_glob(args.file)
    return data

def file_open(name):
    try :
        logging.debug("each file name %s" % name)       
        logging.debug("each file name %s" % name)
        sys.stdin = open(name,'r')
        line = sys.stdin.readline()
        dump_data = []
        while line :
            line = sys.stdin.readline()
            dump_data.append(line)
        return dump_data
    except:
        print("FILE NOT FOUND %s" % name)
        sys.exit(0)

def run_matcher(files,pattern):
    logging.debug("-------matchers-------")
    logging.debug("find file list length = %d" % len(files))
    logging.debug("matcher pattern: %s" % pattern)
    for file in files:
        dump = file_open(file)
        for line in dump:
            if pattern in line:
                if len(files) == 1:
                    print(line.strip())
                else:
                    print(file+":"+line.strip())

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i",      help="options" )
    parser.add_argument("pattern", help="search pattern")
    parser.add_argument("-f",      help="file for pattern")
    parser.add_argument("file",    nargs = '*' ,help="file")    
    args = parser.parse_args()
    run(args)