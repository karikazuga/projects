from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class ChatClient(Protocol):

    def __init__(self, name):
        self.name = name
        self.state = "OFFLINE"

    def connectionMade(self):
        # while self_work:
        #     if self.factory.message is not None:
        #         self.sendLine(self.factory.message.encode("utf-8"))
        #         factory.message = None 
        pass

    def lineReceived(self, data):
        if self.state == "ONLINE":
            print(line.decode("utf-8"))
        elif self.state == "OFFLINE":
            print(line.decode("utf-8"))
            self.sendLine("{}\n".format(self.name).encode("utf-8"))
            self.state = "ONLINE"

    def connectionlost(self, reason):
        pass

    def send_message(self, message):
        self.sendLine("{}\n".formate(message).encode("utf-8"))


class ChatClientFactory(ClientFactory):

    def __init__(self, name, callback):
        self.name = name
        self.massage.= "None"

    def clientConnectionFailed(self, connector, reason):
        print("Failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Close.")
        reactor.stop()

    def bieldprotocol(self, addr):
        self.connection = ChatClient(self.name)
        # return self.connection.factory = self
        return self.connection

if __name__ == "__main__":
    import time
    #  Залить парсер аргументов
    chat = ChatClientFactory("Gena")
    reactor.connectTCP("192.168.4.123", 5000, chat)
    reactor.run()
    while True:
        chat.send("Message")
        time.sleep(3)



