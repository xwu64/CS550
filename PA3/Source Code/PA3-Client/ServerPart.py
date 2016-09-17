__author__ = 'wu'

from socket import *
import threading
import os


BUFSIZE = 1024


def listen(LHOST, LPORT):

    socket4client = socket(AF_INET, SOCK_STREAM)
    try:
        LPORT = int(LPORT)
        ADDR = (LHOST, LPORT)
        socket4client.bind(ADDR)
        socket4client.listen(5)
    except error:
        print 'Invalid listen port.'
        exit()

    while True:
        client_socket, addr = socket4client.accept()
        t1 = threading.Thread(target=get_connection, args= (client_socket, addr))
        t1.start()


def get_connection(client_socket, addr):
    command = client_socket.recv(BUFSIZE)
    if command[0] == 'g':
        flag, filepath = command.split(' ', 1)
        if os.path.exists(filepath):
            file_obj = open(filepath, 'rb')
            while True:
                part_data = file_obj.readline(BUFSIZE)
                if not part_data:
                    break
                client_socket.send(part_data)
            file_obj.close()
    client_socket.close()

