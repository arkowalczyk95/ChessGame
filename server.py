from socket import *
import chess
from termcolor import colored

import time
s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 8888))
s.listen(5)

while 1:
    client,addr = s.accept()
    # print 'Polaczenie z ' ,addr
    # text = colored('hello', 'grey'), colored('world', 'white'), colored('dzban', 'magenta')
    # client.send(text)
    client.send(time.ctime(time.time()))
    client.close()
