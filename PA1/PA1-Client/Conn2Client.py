__author__ = 'wu'

from socket import *
from socket import error
from StateCode import stateDir


BUFSIZE = 1024


def conn2client(addr, path):
    socket4client = socket(AF_INET, SOCK_STREAM)
    try:
        ip_port, rpath = addr.split(' ', 1)
        ip, port = ip_port.split(':')
    except ValueError:
        print 'This is a invalid command. Please input right ommand.'
        return True
    port = 12121
    ADDR = (ip, port)


    try:
        socket4client.connect(ADDR)
    except error, e:
        print e
        print stateDir['411']
        return '411'
    msg = 'p2p -O ' + rpath
    socket4client.send(msg)
    rawData = socket4client.recv(BUFSIZE)

    if rawData == '410':
        print stateDir[rawData]
        return '410'

    fileObj = open(path, 'wb')
    while True:
        fileObj.write(rawData)
        rawData = socket4client.recv(BUFSIZE)
        if not rawData:  # if the rpath is invalid
            break


    fileObj.close()
    print rpath + '>' + path + ' complete'
    return '001'

