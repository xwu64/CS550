__author__ = 'wu'

from socket import *
from socket import error
import threading
import timeit
from time import sleep
import TextCollection
import CommandCheck
from PeerListen import peerListen
from TestFunction import *

BUFSIZE = 1024
LINE = '//////////////////////////////////////////////////\n'


def con2ser():
    print 'ready to connect'
    HOST = raw_input('Please input host ip adress:\n>')  #could set when set up client
    PORT = raw_input('\nPlease input server port\n>')
    PORT = int(PORT)
    ADDR = (HOST, PORT)
    socket4server = socket(AF_INET,SOCK_STREAM)
    try:
        socket4server.connect(ADDR)
    except error, e:
        print e
        print 'Please try other server, bye!'
        return True
    while True:
        data = socket4server.recv(BUFSIZE)
        if not data:
            print 'Cannot connect to server. Please try again'
            return True

        if data == LINE:
            while True:
                try:
                    command = raw_input('>')    # send message and recive message from different threat
                    msg = CommandCheck.commandCheck(command)

                except (KeyboardInterrupt, SystemExit, EOFError), e:
                    msg = 'p2p -Q'
                    socket4server.send(msg)
                    print 'bye!'
                    return False

                if msg is '901':
                    if registerTest(socket4server):
                        print 'Test files have been registered.'
                        continue
                    else:
                        print 'Unkown fail in test.'
                        continue

                if msg is '902':
                    downloadTest(socket4server)
                    continue

                if msg != True:
                        break

            socket4server.send(msg)
            if msg == 'p2p -Q':
                print 'Bye!'
                return False
        else:
            print(data)


def main():
    t = threading.Thread(target=peerListen)
    t.start()
    while True:
        if not t.is_alive:
            break

        try:
            if con2ser() is False:
                break
        except (KeyboardInterrupt,SystemExit), e:
            t._Thread__stop()
            break
        except ValueError, e:
            print e
            continue
    t._Thread__stop()

if __name__ == '__main__':
    main()
