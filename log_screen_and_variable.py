# log print commands to a variable (redirect stdout) and screen

import sys


class Logger(object):
    
    def __init__(self):
        self.terminal = sys.stdout
        self.log = StringIO()

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)



def process_main():
    sys.stdout = Logger()
    print('test logger')
    result = sys.stdout.log.getvalue()
    sys.stdout = sys.stdout.terminal # restore back to default sys.stdout


if __name__ == '__main__':
    process_main()

