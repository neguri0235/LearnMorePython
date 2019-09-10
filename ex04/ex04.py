import sys
#import argparser

def isHelp(string):
    if string[1] == '--help' or string[1] == '-h':
        print(string[0], '\nshow help message\n-h:\n--help:')
        # print help string
        return True
    else:
        return False

def doSomething(command):
    print(command)

def run(arg):
    size = len(arg) # get size of argument
    if size == 1:
        return
    elif size == 2:
        if isHelp(arg) == True:
            return
    for e in arg:
        doSomething(e)

if __name__ == "__main__":
    run(sys.argv)