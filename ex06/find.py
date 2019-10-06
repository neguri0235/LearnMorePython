import sys
import os
import glob
import subprocess
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s = %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def matcher(name, file_list):
    logging.debug("-------matched list -------")
    logging.debug("matcher: %s" % name)
    match_file_list = []
    return match_file_list

def traverse_dir(path):
    logging.debug("-------file list -------")
    all_file_list = []
    for dir_name, sub_dir_name, file_list in os.walk(path):
        logging.debug("base directory: %s" % dir_name)
        for fname in file_list:
            logging.debug(fname)
    return all_file_list

def using_glob(path,name):
    base_condition = path+'/**/'+name
    glob_list = glob.glob(base_condition,recursive=True)
    logging.debug("-------glob list -------")
    for e in glob_list:
        logging.debug("%s" % e)
    return glob_list    

def print_result(result):
    for e in result:
        print(e)

def execute(exec_list, find_list):
    if exec_list[1] != "{}" or exec_list[2] != "\;":
        logging.debug("exec option size is wrong [%d]" % len(args.exec))
        return 

    prog = exec_list[0]

    for e in exec_list:
        logging.debug("exec option exist & len=[%s]" % e)
        pass

    for file in find_list:
        subprocess.call([prog,file])

def run(args):
#    all_file_list = traverse_dir(args.path)
#    match_file_list = matcher(args.name, all_file_list)
    find_result = using_glob(args.path, args.name)
    print_result(find_result)

    if args.exec:
        logging.debug("exec option exist & len=[%d]" % len(args.exec))
        execute(args.exec, find_result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="base directory")
    parser.add_argument("-name", help="file name or directory name")
    parser.add_argument("-exec", nargs = 3, help="execute")    
    args = parser.parse_args()
    logging.debug("-------argument-------")
    logging.debug("path: %s" % args.path)
    logging.debug("name: %s" % args.name)
    logging.debug("exec: %s" % args.exec)
    run(args)