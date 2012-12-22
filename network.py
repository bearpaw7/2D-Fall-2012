'''

client/server

'''

import socket as socketLib

PORT = 2013
BACKLOG = 10 # tcp connection backlog

class Network():
    def __init__(self, isServer):
        self.server = isServer
        self.netSocket = socketLib.socket(socketLib.AF_INET, socketLib.SOCK_STREAM)
        if isServer == True:
            self.netSocket.bind( ('0.0.0.0', PORT) )
            self.netSocket.listen(BACKLOG)

    def getExternalIP(self):
        return(
            [ip for ip in socketLib.gethostbyname_ex(
                socketLib.gethostname())[2] if not ip.startswith("127.")]
            [:1]
        )

    
if __name__ == '__main__':
    print '\'network.py\' is not the correct startup script'
    print 'Attempting to execute main.py...'
    try:
        #execfile('main.py')
        n = Network(True)
    finally:
        print 'Exited sabot.py'