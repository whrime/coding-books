#!/usr/bin/env python

from twisted.internet import protocol, reactor

HOST = '127.0.0.1'
PORT = 21568

class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = (input('> ')).encode("utf-8")
        if data:
            print("...sending %s ..."%data.decode("utf-8"))
            self.transport.write(data)
        else:
            self.transport.loseConnection()
    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode("utf-8"))
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()

reactor.connectTCP(HOST, PORT, TSClntFactory())
reactor.run()
