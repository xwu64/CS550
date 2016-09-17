__author__ = 'wu'

from socket import *
import threading
from datetime import datetime
import Doc
import os


BUFSIZE = 1024
TESTFILENUM = 10000


def client_part(LPORT):
    print 'Input server IP address:'
    HOST = raw_input('> ')
    print 'Input server port:'
    PORT = raw_input('> ')

    while True:
        print 'Input command:'
        command = raw_input('> ')

        if command == 'Peer --help':
            Doc.help_doc()
            continue

        if command == 'Test_register':
            makefiles(TESTFILENUM)
            t1 = datetime.now()
            for i in range(TESTFILENUM):
                testR(HOST,PORT,LPORT,i)
            t2 = datetime.now()
            print (t2 - t1)
            continue

        flag = command.split(' ', 1)
        if flag[0] == 'Test_obtain':
            t1 = datetime.now()
            for i in range(TESTFILENUM):
                testO(LPORT, flag[1], i)
            t2 = datetime.now()
            print (t2 - t1)
            continue

        if command == 'Test_lookup':
            t1 = datetime.now()
            for i in range(TESTFILENUM):
                testL(HOST, PORT, LPORT, i)
            t2 = datetime.now()
            print (t2-t1)
            continue

        if command[0] == '0' or command[0] == '1':
            try:
                msg = pretreatment(command, LPORT)
                if msg is False:
                    print 'Invalid command.'
                    continue
                result = send(HOST, PORT, msg)
                print result
                continue
            except Exception, e:
                print(e)
                continue
        elif command[0] == '2':
            try:
                host, port, msg = pretreatment(command, LPORT)
                if msg is False:
                    print 'Invalid command.'
                    continue
                result = download(host, port, msg)
                print result
                continue
            except Exception, e:
                print e
                continue
        elif command[0] == '3':
            exit()

        print 'Invalid command, try again.'
        print type(command)
        continue
        print result


def pretreatment(command, LPORT):
    if command[0] == '0':
        flag, file_path = command.split(' ', 1)
        file_path = os.path.expanduser(file_path)
        other, filename = file_path.rsplit('/', 1)

        if os.path.exists(file_path) == False:
            print 'Invalid file path.'
            return False

        myname = getfqdn(gethostname())
        myaddr = gethostbyname(myname)
        msg = '0 ' + myaddr + ':' + str(LPORT) + file_path + ' ' + filename
        return msg

    if command[0] == '1':
        flag, keyword = command.split(' ', 1)
        msg = '1 ' + keyword
        return msg

    if command[0] == '2':
        flag, url = command.split(' ',1)
        host, other = url.split(':', 1)
        port, path = other.split('/', 1)
        path = '/' + path
        msg = 'g '+ path
        return (host, port, msg)

    return False


def send(HOST, PORT, msg):
    socket4server = socket(AF_INET, SOCK_STREAM)
    try:
        PORT = int(PORT)
        ADDR = (HOST, PORT)
        socket4server.connect(ADDR)
    except (error, OverflowError):
        print 'Cannot connect to server'
        socket4server.close()
        exit()

    socket4server.send(msg)
    result = socket4server.recv(BUFSIZE)

    return result


def download(HOST, PORT, msg):
    socket4client = socket(AF_INET, SOCK_STREAM)
    try:
        PORT = int(PORT)
        ADDR = (HOST, PORT)
        socket4client.connect(ADDR)
    except error:
        print 'Cannot connect to target peer.'
        return False
    socket4client.send(msg)
    other, filename = msg.rsplit('/', 1)
    filename = filename + '.download'
    file_obj = open(filename, 'wb')
    while True:
        part_data = socket4client.recv(BUFSIZE)
        file_obj.write(part_data)
        if not part_data:
            break
    file_obj.close()
    socket4client.close()
    return True


def makefiles(number):
    for each in range(number):
        each = str(each)
        path = os.path.realpath(each+'.test')
        fileobj = open(path,'w')
        fileobj.write(each*10)
        fileobj.close()
    return True


def testR(HOST, PORT, LPORT, counter):
    filename = str(counter) + '.test'
    path = os.path.realpath(filename)
    command = '0 ' + path
    msg = pretreatment(command, LPORT)
    send(HOST,PORT,msg)



def testL(HOST, PORT, LPORT, counter):
    filename = str(counter) + '.test'
    command = '1 ' + filename
    msg = pretreatment(command, LPORT)
    send(HOST,PORT,msg)


def testO(LPORT, URL, counter):
    command = '2 ' + URL + '/' + str(counter) + '.test'
    host, port, msg = pretreatment(command, LPORT)
    download(host, port, msg)


if __name__ == '__main__':
    client_part(1342)
