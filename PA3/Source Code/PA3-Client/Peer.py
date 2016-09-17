__author__ = 'wu'

import threading
from time import sleep
import ServerPart
import ClientPart
import Doc


def main():
    Doc.welcome()

    print 'Input listen port:'
    LPORT = raw_input('> ')
    LHOST = ''

    t_server = threading.Thread(target=ServerPart.listen, args=(LHOST,LPORT))
    t_server.start()

    sleep(1)
    if t_server.is_alive():
        try:
            ClientPart.client_part(LPORT)
        except (Exception, KeyboardInterrupt),e:
            print e
        finally:
            t_server._Thread__stop()


if __name__ == '__main__':
    main()
