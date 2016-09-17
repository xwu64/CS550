__author__ = 'wu'


def welcome():
    print("Promgram Assignment3: Client\n"
          "Version: 1.0\n"
          "Author: XIAOLIANG WU\n"
          "Usage:\n"
          "\'Peer --help\' for more help.\n")


def help_doc():
    print """\
SYNOPSIS:
    0 [FILE ABSOLUTE PATH]          Register file to server.                Return register result
    1 [KEYWORD]                     look up files that name is KEYWORD.     Return file URL
    2 [FILE URL]                    Download file according URL.            Return download result
    3                               Exit.
    Test_register                   10K register operation                  Return time.
    Test_lookup                     10K look up operation                   Return time.
    Test_obtain [URL]               10K obtain time, each file less 10KB    Return time.
    """

if __name__ == '__main__':
    help_doc()

