__author__ = 'wu'

import os
from TextCollection import helpText
from StateCode import stateDir
import Conn2Client


def register(addr):
    path = os.path.expanduser(addr)
    try:
        open(path, 'r')
    except IOError, e:
        print(stateDir['401']+'. Please check your file path\n')
        return True

    msg = 'p2p -R ' + path
    return msg


def download(addr):
    try:
        ipaddr, path = addr.split('>')
    except ValueError:
        print 'This is a invalid command. Please input right command.'
        return True

    ip = ipaddr.split(' ')
    ip = ip[0]
    path = os.path.expanduser(path)

    if os.path.exists(path) == False:  #Invalid path
        print 'This is a invalid save path. Please input right path.'
        return True

    filename = ipaddr.split(' ')
    filename = filename[1].split('/')
    filename = filename[len(filename)-1]
    if os.path.exists(path+'/'+filename):
        filename_temp = filename.rsplit('.', 1)
        filename = filename_temp[0] + '_' + ip + '.' + filename_temp[1]
        path = path + '/' + filename
        print 'This is a invalid file name. File name is changed to', filename  #del this code after test
    else:
        path = path + '/'+filename
    result = Conn2Client.conn2client(ipaddr, path)
    if result == '410':
        ip, rpath = ipaddr.split(' ', 1)
        return 'p2p -X ' + ip + '\t' + rpath
    elif result == '411':
        return True
    return result


def search(addr):
    words = addr.split('/')
    filename = words[len(words)-1]
    msg = 'p2p -F ' + filename
    return msg


def cancelShare(addr):
    path = os.path.expanduser(addr)
    msg = 'p2p -C ' + path
    return msg


def helpDoc():
    print(helpText())
    return True


def close():
    msg = 'p2p -Q'
    return msg


def main():
    addr = raw_input()
    path = os.path.expanduser(addr)
    f = open(path, 'r')
    word = f.read()
    print(word)

if __name__ == '__main__':
    main()
