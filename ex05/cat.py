# python ex05.py abc.txt
# python ex05.py abc.txt abd.txt
# python ex05.py abc.txt abd.txt abe.txt
# python ex05.py abc.txt abd.txt re abe.txt
# 're' means '>'. 

import sys

def isHelp(string):
    if string[1] == '--help' or string[1] == '-h':
        print('ex05 - concatenate files and print on the standard output')
        return True
    else:
        return False

def file_open_read(file_):
    sys.stdin = open(file_,'r')

    line = sys.stdin.readline()
    while line :
        print(line,end='')
        line = sys.stdin.readline()

def file_open_read_write(arg):
    read_file_list = list()
    for i in range(1,len(arg)-2):
        read_file_list.append(arg[i])
    
    write_file = arg[-1]

    buff = list()

    for e in read_file_list:
        sys.stdin = open(e,'r')
        line = sys.stdin.readline()
        while line:
            buff.append(line)
            line = sys.stdin.readline()
        buff.append('\n\n')
         
    f = open(write_file, 'w')
    for e in buff:
        f.write(e)
    f.close()

def input_output():
    while True:
        s = input()
        print(s)
        if len(s) == 0:
            break

def run(arg):
    redirect = False
    size = len(arg)

    if size == 1:
        input_output()
        return
    elif size == 2:
        if isHelp(arg) == True:
            return

    # find redirection command
    for e in arg:
        if e == 're':
            redirect = True

    if redirect == True:
        file_open_read_write(arg)
    else:
        for i in range(1,len(arg)):
            file_open_read(arg[i])

if __name__ == "__main__":
    run(sys.argv)