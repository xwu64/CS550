__author__ = 'wu'


from socket import *
import threading
from time import sleep
import CommandAnalysis

def intorduction():
    print('Program Assignment 1(Server)\n'
          'Version: 1.0\n'
          'Author: XIAOLIANG WU\n'
          'Usage:\n'
          ' \'p2p --help\' for help text')

BUFSIZE = 10240
LINE = '//////////////////////////////////////////////////\n'

def connection(addr, client):
    client.send('Connecting with server. Your IP is ' + str(addr[0]) + ':' + str(addr[1]) + '.\n')
    sleep(0.0001)
    client.send(LINE)
    try:
        while True:
            command = client.recv(BUFSIZE)
            if not command:
                break

            if command.rfind('p2p') != 0:
                t = threading.Thread(target=DivCommand, args=(command,client,addr))
                t.start()
            else:
                t = threading.Thread(target=HandleCommand, args=(command,client,addr))
                t.start()
    except error:
        t._Thread__stop()

def DivCommand(command, client,addr):
    while command.rfind('p2p') != 0:
        p2pS = command.rfind('p2p')
        commandt = command[p2pS:]
        command = command[:p2pS]
        HandleCommand(commandt, client, addr)
    HandleCommand(commandt, client, addr)

def HandleCommand(command,client,addr):
    try:
        buf = CommandAnalysis.commandAnalysis(addr,command)
    except (IndexError), e:
        print e
        print command
        print command[5]
        exit()
    if isinstance(buf, str):  # if the type of buf is string, send message directly
        client.send(buf)
    elif isinstance(buf, list):  # if the type of buf is list, send every element respectively
        for each in buf:
            client.send(each)
            sleep(0.05)
    elif buf == True:  # This client is disconnect
        client.close()
        print 'Close successfully'
        quit()

    else:  # Unkown type, maybe error
        print('CommandAnalysis exception, this type is: ', type(buf))
    sleep(1)
    client.send(LINE)






def main(HOST = '', PORT = 21557):
    ADDR = (HOST, PORT)

    tcpSerSocket = socket(AF_INET,SOCK_STREAM)
    try:
        tcpSerSocket.bind(ADDR)
    except OverflowError, e:
        print 'Port number is larger than maximum'
        exit()
    tcpSerSocket.listen(15)


    counter = 0

    try:
        while True:
            print('Waiting for connection...\n')
            tcpCliSocket, addr = tcpSerSocket.accept()
            thread = threading.Thread(target=connection, args=(addr, tcpCliSocket))
            print('Thread %d Connected from: ' % counter, addr, '\n')
            thread.start()
            counter+=1
    except (KeyboardInterrupt, SystemExit), e:
        fobj = open('ResourceIndex','w')
        fobj.write('')
        fobj.close()
        thread._Thread__stop()

if __name__ == '__main__':
    port = raw_input('Input port number: ')
    try:
        port = int(port)
    except (ValueError,OverflowError),e:
        print 'Invalid port number.'
        exit()
    main(PORT = port)


