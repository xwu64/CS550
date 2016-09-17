__author__ = 'wu'


def welcome():
    print("Promgram Assignment2: Node\n"
          "Version: 1.0\n"
          "Author: XIAOLIANG WU\n"
          "Usage:\n"
          "\'Node --help\' for more help.\n")


def help_doc():
    print("SYNOPSIS:\n"
          "\t0 [KEY] [VALUE]\t\tInsert value\n"
          "\t1 [KEY]\t\tGet value\n"
          "\t2 [KEY]\t\tDelete value\n"
          "\ttest_0 KEY\t\tEvaluation_put\n"
          "\ttest_1 KEY\t\tEvaluation_get\n"
          "\ttest_2 KEY\t\tEvaluation_del\n"
          "\tNode --help\t\tHelp document\n")



def main():
    help_doc()
if __name__ == '__main__':
        main()


'''
State code
000 put success
001 put fail
101 get fail
200 del success
201 del fail
777 unknown fail
'''

