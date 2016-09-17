__author__ = 'wu'

####################################################
#SYNOPSIS
#       p2p [OPTION] [FILE]
#DESCRIPTION
#       -R      register in index
#       -F      search in index
#       -C      cancel registed file
#       -Q      quit client
#       -X      delete invalid file from index
####################################################

def commandAnalysis(addr, command):
    if command[5] == 'R':   # Registration Function
        indexObj = open('ResourceIndex','r')
        index = indexObj.read()
        indexObj.close()
        index = index.split('\n')


        path = command[7:]
        filename = path.split('/')
        filename = filename[len(filename) - 1]
        mean = filename + '\t' + str(addr[0]) + ':' + str(addr[1]) + '\t' + path
        for each in index:
            if each == mean:
                return 'You have registered this file. Before you register this file, you need cancel this file from server.\n'

        indexObj= open('ResourceIndex', 'a')
        indexObj.write('\n'+mean)
        '''
        for each in index:
            if len(each) == 0:
                continue
            indexObj.write(each+'\n')
            '''
        indexObj.close()
        return 'This file have been registered successfully.\n'

    if command[5] == 'F':   # Search Function
        indexObj = open('ResourceIndex','a+')
        index = indexObj.read()
        index = index.split('\n')
        path = command[7:]
        filename = path.split('\t')
        filename = filename[len(filename) - 1]
        consequence = ['FILENAME\tIP\tPATH']
        for each in index:
            words = each.split('\t')
            column1 = words[0]
            if column1.find(filename) == -1:
                continue
            else:
                consequence.append((each+'\n'))

        indexObj.close()
        return consequence

    if command[5] == 'C':   # Cancel Function
        indexObj = open('ResourceIndex', 'r')
        index = indexObj.read()
        indexObj.close()
        index = index.split('\n')
        ipaddr = str(addr[0]) + ':' + str(addr[1])
        path = command[7:]
        for eachIndex in range(len(index)-1):
            columns = index[eachIndex].split('\t')
            if columns[1] == ipaddr:
                if columns[2] == path:
                    index = index[:eachIndex] + index[eachIndex+1:]
                    indexObj = open('ResourceIndex', 'w')
                    for each in index:
                        if len(each) == 0:
                            continue
                        indexObj.write(each+'\n')
                    indexObj.close()
                    return 'This file would not be shared.'

        return 'This file does not exist in the index.'

    if command[5] == 'Q':
        indexObj = open('ResourceIndex', 'r')
        index = indexObj.read()
        indexObj.close()
        index = index.split('\n')
        ipaddr = str(addr[0]) + ':' + str(addr[1])

        for eachIndex in range(len(index) -1):
            if len(index[eachIndex]) == 0:
                continue
            columns = index[eachIndex].split('\t')
            if columns[1] == ipaddr:
                index[eachIndex] = ''

        indexObj = open('ResourceIndex', 'w')

        for each in index:
            if len(each) == 0:
                continue
            indexObj.write(each+'\n')

        indexObj.close()
        print ipaddr + ' client is quit.'
        return True

    if command[5]  is 'X':
        indexObj = open('ResourceIndex', 'r')
        index = indexObj.read()
        indexObj.close()
        path = command[7:]
        index = index.split('\n')
        for eachIndex in range(len(index)-1):
            columns = index[eachIndex].split('\t', 1)
            if columns[1] == path:
                index = index[:eachIndex] + index[eachIndex+1:]
                indexObj = open('ResourceIndex', 'w')
                for each in index:
                    if len(each) == 0:
                        continue
                    indexObj.write(each+'\n')
                indexObj.close()

        print 'Cleaning invalid file from index successfully. '+path

    if command[5] == 'G':
        indexObj =open('ResourceIndex', 'r')
        msg = indexObj.readline()
        msglist = []
        while msg:
            if len(msg) < 5:
                msg = indexObj.readline()
                continue
            try:
                msg = msg.split('\t')
                msg = msg[1]+' '+msg[2]
            except (IndexError):
                msg = indexObj.readline()

            msglist.append(msg)
            print msg
            msg = indexObj.readline()

        temp = msglist.pop()
        temp = temp+'\n'
        msglist.append(temp)
        return msglist






def main():
    command = raw_input('command >')
    addr = raw_input('addr >')
    consequence = commandAnalysis(addr, command)
    print(consequence)

if __name__ == '__main__':
    main()
