__author__ = 'wu'


import os
from time import sleep
from Option import *


BUFFSIZE = 1024
LINE = '//////////////////////////////////////////////////\n'

def registerTest(socket4server):
    def newfiles(number):
        for each in range(number):
            each = str(each)
            path = os.path.expanduser('~/'+each+'.test')
            fileobj = open(path,'w')
            fileobj.write(each)
            fileobj.close()
        return True

    FILENUMBER = 1000
    newfiles(FILENUMBER)
    for each in range(FILENUMBER):
        each = str(each)
        path = os.path.expanduser('~/'+each+'.test')
        msg = register(path)
        socket4server.send(msg)
        sleep(0.01)

    return True


def downloadTest(socket4server):
    msg = 'p2p -G'
    socket4server.send(msg)
    addrlist = []
    while True:
        info = socket4server.recv(BUFFSIZE)
        if not info:
            print 'Download complete.'
            break
        if info == LINE:
            break
        addr = info[:len(info)-1] + '>~/'
        addrlist.append(addr)

    for each in addrlist:
        try:
            code = download(each)
            print code
        except Exception:
            continue
    print 'Download testing complete.'




    return True


def main():
    registerTest(123)


if __name__ == '__main__':
    main()
