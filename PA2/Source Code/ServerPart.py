__author__ = 'wu'

from socket import *
import threading
from multiprocessing.pool import ThreadPool


BUFSIZE = 1024


def serverlisten():
    config = open("Config", 'r')
    PORT = config.readline()
    HOST = ''
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
            PORT = config.readline()
        except ValueError:
            print('Without valid port')
            exit()

    print("This node use port "+ str(PORT)+ '\n')
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
                value = hashtable[part1]
                tcpCliSocket.send(value)
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

def main():
    serverlisten(21556)


if __name__ == '__main__':
    main()
