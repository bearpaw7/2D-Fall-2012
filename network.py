'''

client/server

'''

import socket as socketLib

SERVER_PORT = 2013
CLIENT_PORT = 2014
BACKLOG = 10 # tcp connection backlog

class Network():
    def __init__(self, isServer):
        self.server = isServer
        if isServer == True:
            self.netSocket = socketLib.socket(socketLib.AF_INET, socketLib.SOCK_STREAM)
            self.netSocket.bind( ('0.0.0.0', SERVER_PORT) )
            self.netSocket.listen(BACKLOG)
    
if __name__ == '__main__':
    print '\'network.py\' is not the correct startup script'
    print 'Attempting to execute main.py...'
    try:
        #execfile('main.py')
        n = Network(True)
    finally:
        print 'Exited sabot.py'