#!/usr/bin/env python
import os
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21568

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt)

    def dataReceived(self, data):
        self.transport.write(bytes('%s current time is : [%s] %s' %(os.listdir
                                   (),ctime(), data.decode("utf-8")),"utf-8"))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
