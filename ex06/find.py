# find . -name "*.txt" -print
# find . -name "*.rb" -exec rm {} \;

import sys
import os
import glob
import subprocess

def isHelp(string):
    if string[1] == '--help' or string[1] == '-h':
        print('find - search for files in a directory hierarchy')
        return True
    else:
        return False

def parse(arg):
    for e in arg:
        print(e)

def run(arg):
    redirect = False
    size = len(arg)

    if size == 1:
        print('do nothing')
        return
    elif size == 2:
        if isHelp(arg) == True:
            return
    else:
        parse(arg)

if __name__ == "__main__":
    run(sys.argv)