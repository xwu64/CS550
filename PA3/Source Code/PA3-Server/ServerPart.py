
__author__ = 'wu'

from socket import *
from time import sleep
import threading
from multiprocessing.pool import ThreadPool


BUFSIZE = 1024


def serverlisten():
    config = open("Config", 'r')
    line = config.readline()
    HOST, PORT = line.split(' ', 1)
    tcpSocket = socket(AF_INET, SOCK_STREAM)
    hashtable = {}

    while PORT:
        try:
            PORT = int(PORT)
            ADDR = (HOST, PORT)
            tcpSocket.bind(ADDR)
            tcpSocket.listen(5)
            break
        except error:
            try:
                line = config.readline()
                HOST, PORT = line.split(' ', 1)
            except ValueError:
                print('Without valid port')
                exit()
        except ValueError:
            print('Without valid port')
            exit()

    print("This node use "+ HOST + " " +str(PORT)+ '\n')
    config.close()
    pool = ThreadPool(processes=1)
    async_result = pool.apply_async(ini_table,())
    while True:
        #print("Waiting for connection.")
        tcpCliSocket, addr = tcpSocket.accept()
        return_value = async_result.get()
        async_result = pool.apply_async(get_connection, (tcpCliSocket, addr, hashtable))


    return 0


def get_connection(tcpCliSocket, addr, hashtable):
    try:
        command = tcpCliSocket.recv(BUFSIZE)
        if command[0] == "p":
            try:
                part0, part1, part2 = command.split(" ", 2)
                hashtable[part1] = part2
                tcpCliSocket.send("000")
                return hashtable
            except Exception, e:
                print e
                tcpCliSocket.send("001")
                return hashtable
        if command[0] == "g":
            part0, part1 = command.split(" ", 1)
            try:
                urls = get_url(hashtable, part1)
                if len(urls) == 0:
                    tcpCliSocket.send('101')
                else:
                    tcpCliSocket.send(urls)
                return hashtable
            except KeyError:
                tcpCliSocket.send("101")
                return hashtable
        if command[0] == "d":
            part0, part1 = command.split(" ", 1)
            try:
                del hashtable[part1]
                tcpCliSocket.send("200")
                return hashtable
            except KeyError:
                tcpCliSocket.send("201")
                return hashtable

        tcpCliSocket.close()

    except Exception, e:
        print ("ServerPart.py ", e)
        tcpCliSocket.send("777")
        tcpCliSocket.close()
    return 0


def ini_table():
    table = {}
    return table


def get_url(hashtable, filename):
    all_key = hashtable.keys()
    all_value = hashtable.values()
    indices = [i for i, x in enumerate(all_value) if x == filename]
    msg = ''
    for each in indices:
        msg = msg + all_key[each] + '\n'

    return msg


def main():
    serverlisten(21556)


if __name__ == '__main__':
    main()
