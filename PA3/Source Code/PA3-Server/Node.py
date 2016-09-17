__author__ = 'wu'

import threading
from time import sleep
from datetime import datetime
from ServerPart import serverlisten
import Doc
from ClientPart import operation, client_listen


def main():
    Doc.welcome()
    tlisten = threading.Thread(target=serverlisten, args=())
    tlisten.start()

    sleep(1)
    try:
        print 'Input port number connected by client.'
        PORT = raw_input('> ')
        client_listen(PORT)
    except (KeyboardInterrupt,  SystemExit, ValueError), e:
        print e
        print("Bye!")
        tlisten._Thread__stop()

    return 0


if __name__ == '__main__':
    main()
