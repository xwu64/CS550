__author__ = 'wu'

from socket import *
from socket import error
import threading
from Connection import connection

BUFSIZE = 1024


def peerListen():
    HOST = ''
    PORT = 12121
    ADDR = (HOST, PORT)
    clientListen = socket(AF_INET, SOCK_STREAM)
    try:
        clientListen.bind(ADDR)
        clientListen.listen(5)
    except error, e:
        clientListen.close()
        print '\n'
        print str(e)+':port 12121. Please retry after this port is avaliable.'
        print '\nbye!'
        exit()
    while True:
        try:
            peerSock, addr = clientListen.accept()
        except Exception, e:
            clientListen.close()
            print '\n'+e
            print '\nbye!'
            exit()
        t = threading.Thread(target=connection, args=(peerSock, addr))
        t.start()

    clientListen.close()

def main():
    peerListen()

if __name__ == '__main__':
    main()

