'''
1. Level 1 is having command line options for the most basic sed usage of replacing one string with another.
2. Level 2 is enabling regular expressions in those command line options.
3. Level 3 is implementing the sed expression format.

ls -l | sed -e "s/zedshaw/author/g"
ls -l | sed -e "s/Jul [0-9][0-9]/DATE/g"
'''

import sys
import logging
import argparse
import glob

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

def make_file_list(files):
    file_list = glob.glob(files,recursive=True)
    if 'sed.py' in file_list:
        file_list.remove("sed.py")
    logging.debug("target file list %s" % file_list)
    return file_list

def func_replacement(opt, file_list):
    regex = opt[1]
    dest = opt[2]
    add_job = str()
    if len(opt) == 4:
        add_job = opt[3]
    logging.debug("regex: [%s]" % regex)
    logging.debug("dest: [%s]" % dest)
    logging.debug("additional job: [%s]" % add_job)

    for e in file_list:
        out = []
        sys.stdin = open(e, 'r', encoding='utf-8')
        data = sys.stdin.readline()
        while data:
            out.append(data.replace(regex,dest))
            data = sys.stdin.readline()

#        if add_job == 'g':
        f = open(e,'w')
        for e in out:
             f.write(e)
        f.close()

def worker(args):
    logging.debug(args.file)
    file_list = make_file_list(args.file)
    opt = args.expression.split('/')

    if opt[0] == 's':
        logging.debug("replacement")
        func_replacement(opt, file_list)
    else:
        logging.debug("not implemented")

    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--expression", help="add the  script to the commands")
    parser.add_argument("file", nargs='?', default='*.*', help="taret file")
    args = parser.parse_args()
    worker(args)