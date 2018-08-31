from socket import *
import chess
from termcolor import colored

print('Hello world!')
r = "Arrr"
print 'Pirate ',r
from socket import *
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))
tm = s.recv(1024)
s.close()
print 'Czas serwera: ', tm
