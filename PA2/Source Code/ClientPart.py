__author__ = 'wu'

from time import sleep
from socket import *
import Doc


BUFSIZE = 1024


def operation(command):

    try:
        flag, part_command = command.split(' ', 1)
    except ValueError:
        print("Invalid command, please try again. \'Node --help\' you will get help document.\n")
        return 0


    if command == "Node --help":
        Doc.help_doc()
        return 1

    if flag == '0':
        try:
            key, value = part_command.split(' ', 1)
            result = rput(key,value)
        except ValueError:
            print("Invalid command, please try again. \'Node --help\' you will get help document.\n")
            return 0

        if result is True:
            print("Put operation success.\n")
        else:
            print("Put operation fail.\n")
        return 1

    if flag == '1':
        key = part_command
        value = rget(key)
        if value is False:
            print("Cannot find value.")
        else:
            print("Use key:"+ key+ ", get value: "+str(value)+"\n")
        return 1

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
    return 0


def gethashtable(key):
    sumkey = 0
    for each in key:
        sumkey += ord(each)

    index = sumkey%8
    return index


def rput(key, value):
    msg = "p " + key + " " + value
    flag = send(msg, key)
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

    PORT = config.readline()
    while index_num:
        PORT = config.readline()
        index_num -= 1
    PORT = int(PORT)


    ADDR = (HOST, PORT)

    sendSocket = socket(AF_INET, SOCK_STREAM)
    try:
        sendSocket.connect(ADDR)
    except error:
        print(ADDR, 'cannot connect to this node.')
        exit()
    sendSocket.send(msg)
    result = sendSocket.recv(BUFSIZE)  ##
    sendSocket.close()
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


