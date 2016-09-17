__author__ = 'wu'

def introduction():
    print('Program Assignment 1: Client\n'
          'Version: 1.0\n'
          'Author: XIAOLIANG WU\n'
          'Usage:\n'
          '\'p2p --help\' for help text\n')

def helpText():
    print('NAME:\n'
          '\t p2p - peer to peer transfer file\n'
          'SYNOPSIS:\n'
          '\t p2p [OPTION]... [FILE ADDR]...\n'
          'DESCRIPTION:\n'
          '\t -r ABSOLUTE PATH\t register files in server index\n'
          '\t -f FILENAME\t     search files in server index\n'
          '\t -o PATH1>PATH2\t     download file from other peer. PATH1 = ip:port path, PATH2 is save path\n'
          '\t -h \t             print help text\n'
          '\t -Rtest\t             1000 register test\n'
          '\t -Rdownload\t             1000 download test\n'
          '\t -q \t             quit client\n')

def main():
    introduction()
    helpText()
if __name__ == '__main__':
    main()

