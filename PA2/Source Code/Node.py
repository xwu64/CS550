__author__ = 'wu'

import threading
from time import sleep
from datetime import datetime
from ServerPart import serverlisten
import Doc
from ClientPart import operation


def main():
    tlisten = threading.Thread(target=serverlisten, args=())
    tlisten.start()

    Doc.welcome()
    sleep(1)
    try:
        while 1:
            if not tlisten.is_alive:
                print('Bye!')
                break
            command = raw_input("> ")
            t1 = datetime.now()
            operation(command)
            t2 = datetime.now()
            print 'Time : ' + str(t2 - t1)
    except (KeyboardInterrupt,  SystemExit, ValueError), e:
        print e
        print("Bye!")
        tlisten._Thread__stop()
        exit()

    return 0


if __name__ == '__main__':
    main()
