__author__ = 'wu'

from os import path
from StateCode import stateDir
from Option import *


def opt(option, addr):
    if option == '-r':
        return register(addr)
    elif option == '-f':
        return search(addr)
    elif option == '-o':
        return download(addr)
    elif option == '-c':
        return cancelShare(addr)
    elif option == '-h':
        return helpDoc()
    elif option == '-Rtest':
        return '901'
    elif option == '-Rdownload':
        return '902'
    elif option == '-q':
        return close()
    else:
        return False


def commandCheck(command):  # check command from user
    word = command.split(' ', 2)
    if len(word) != 3:
        word.append(' ')
    if word[0] != 'p2p':
        print (stateDir['400']+'. Try \'p2p -h\' for more help\n')
        return True

    addr = word[2]
    msg = opt(word[1], addr)

    if  msg is False:
        print (stateDir['400']+'. Try \'p2p -h\' for more help\n')
        return True
    elif msg == '001':
        return True
    else:
        return msg


def commandhandle(msg):
    msg = msg.split(' ', 2)
    if msg[0] == 'p2p' and msg[1] == '-O':
        filepath = msg[2]
        if path.exists(filepath):
            return filepath
        else:
            return False
    return True

def main():
    while True:
        command = raw_input('>> ')
        print commandCheck(command)
if __name__ == '__main__':
    main()