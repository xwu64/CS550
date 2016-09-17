__author__ = 'wu'

from socket import *
import threading
import Doc


BUFSIZE = 1024


def client_listen(PORT):
    listen_client_socket = socket(AF_INET,SOCK_STREAM)
    HOST = ''
    try:
        PORT = int(PORT)
        ADDR = (HOST,PORT)
        listen_client_socket.bind(ADDR)
        listen_client_socket.listen(5)
    except (error, OverflowError):
        print 'Invalid port number.'
        exit()

    test_counter = 0
    while True:
        socket4client, addr = listen_client_socket.accept()
        t = threading.Thread(target=get_connection, args=(socket4client, addr))
        t.start()
        test_counter +=1

    return 0


def get_connection(socket4client, addr):
    command = socket4client.recv(BUFSIZE)
    result = operation(command)
    socket4client.send(result)
    socket4client.close()


def operation(command):

    try:
        flag, part_command = command.split(' ', 1)
    except ValueError:
        print("Invalid command, please try again. \'Node --help\' you will get help document.1\n")
        return 0

    if command == "Node --help":
        Doc.help_doc()
        return 1

    if flag == '0':
        try:
            key, value = part_command.split(' ', 1)
            result = rput(key, value)
        except ValueError, e:
            print("Invalid command, please try again. \'Node --help\' you will get help document.2\n")
            print e
            return 0

        if result is True:
            return "Put operation success.\n"
        else:
            return "Put operation fail.\n"


    if flag == '1':
        key = part_command
        value = rget(key)
        if value is False:
            return "Cannot find file."
        else:
            return value


'''
    if flag == '2':
        key = part_command
        result = rdelete(key)
        if result is True:
            print("Delete operation success.\n")
        else:
            print("Delete operation fail.\n")
        return 1

    if flag == 'test_0':
        KEY = part_command
        result = test0(KEY)
      #  print(result)
        print('fail operation number: ' + str(len(result)))
        return 1

    if flag == 'test_1':
        KEY = part_command
        result = test1(KEY)
      #  print(result)
        print('fail operation number: ' + str(len(result)))
        return 1

    if flag == 'test_2':
        KEY = part_command
        result = test2(KEY)
      #  print(result)
        print('fail operation number: ' + str(len(result)))
        return 1

    print("Invalid command, please try again. \'Node --help\' you will get help document.\n")
 '''


def gethashtable(key):
    sumkey = 0
    for each in key:
        sumkey += ord(each)

    index = sumkey%8
    return index


def rput(key, value):
    msg = "p " + key + " " + value
    flag = send(msg, value)
    return flag


def rget(key):
    msg = "g " + key
    value = send(msg, key)
    return value


def rdelete(key):
    msg = "d " + key
    flag = send(msg, key)
    return flag


def send(msg, key):
    index_num = gethashtable(key)
    #print msg

    #print("INDEX NUMBER = ", index_num)

    HOST = ''
    config = open("Config", "r")
    lines = config.read()
    config.close()
    lines = lines.split('\n')
    allconfig = []
    for each in lines:
        if len(each) > 9:
            allconfig.append(each)

    line = allconfig[index_num]
    replica_index= (index_num +1) % len(allconfig)
    replica_line = allconfig[replica_index]

    HOST, PORT = line.split(' ', 1)
    PORT = int(PORT)
    rHOST, rPORT = replica_line.split(' ', 1)
    rPORT = int(rPORT)

    ADDR = (HOST, PORT)
    rADDR = (rHOST, rPORT)

    sendSocket = socket(AF_INET, SOCK_STREAM)
    rsendSocket = socket(AF_INET, SOCK_STREAM)

    try:
        rsendSocket.connect(rADDR)
        rsendSocket.send(msg)
        result = rsendSocket.recv(BUFSIZE)
        rsendSocket.close()
    except error,e:
        print(rADDR, 'cannot connect to this node ' + str(index_num+1))
        print e

    try:
        sendSocket.connect(ADDR)
        sendSocket.send(msg)
        result = sendSocket.recv(BUFSIZE)  ##
        sendSocket.close()
    except error:
        print(ADDR, 'cannot connect to this node ' + str(index_num))

    if result == "000":
        return True
    if result == "001":
        return False
    if result == "101":
        return False
    if result == "200":
        return True
    if result == "201":
        return False
    if result == "777":
        return False
    return result


'''
def test0(KEY):
    fail_list = []
    for each in range(100000):
        key = key_generator(KEY, each)
   #     print('key generator '+ str(each) + ' ' + key)
        result = rput(key, key)
        if result is False:
            fail_list.append(key + ' ' + 'fail.')

    return fail_list


def test1(KEY):
    fail_list = []
    for each in range(100000):
        key = key_generator(KEY, each)
   #     print('key generator '+ str(each) + ' ' + key)
        result = rget(key)
        if result is False:
            fail_list.append(key + ' ' + 'fail.')
            #print key

    return fail_list



def test2(KEY):
    fail_list = []
    for each in range(100000):
        key = key_generator(KEY, each)
        #     print('key generator '+ str(each) + ' ' + key)
        result = rdelete(key)
        if result is False:
            fail_list.append(key + ' ' + 'fail.')
            #print key

    return fail_list


def key_generator(KEY, seq):
    msg = KEY + str(seq)
    return msg

'''
