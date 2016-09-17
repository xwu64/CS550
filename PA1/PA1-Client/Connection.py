__author__ = 'wu'

from os import path
from CommandCheck import commandhandle

BUFSIZE = 1024


def connection(peerSocket, addr):
    msg = peerSocket.recv(BUFSIZE)
    result = commandhandle(msg)
    if result == False:
        peerSocket.send('410')
        peerSocket.close()
    elif result == True:
        print '\nUnkown header error in Connection.connetion().'
        peerSocket.close()
    else:
        fileObj = open(result, 'rb')
        rawData = 1
        counter = 0
        while rawData:
            rawData = fileObj.read(BUFSIZE)
            if not rawData:
                break
            peerSocket.send(rawData)
            counter +=1

        fileObj.close()
        peerSocket.close()
