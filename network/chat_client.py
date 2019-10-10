from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver
from treading import tread
import time

MESSAGE = []


class Mesage():


    @event.Event.origin("new_message", post=True)
    def add_message(self, message):
        for _ in range(20):
            time.sleep(2)
        message.append("Батя в здании")


class ChatClient(Protocol):

    def __init__(self, name):
        self.name = name
        self.state = "OFFLINE"
        self.work = True
        event.Event(name="new_message", callback=self.send_message)

    def connectionMade(self):
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

    def send_message(self, *args, **kwargs):

        try:
            message = MESSAGE[0]
        except IndexError:
            print("Error")
        MESSAGE.remove(message)
        self.sendLine("{}\n".formate(message).encode("utf-8"))


class ChatClientFactory(ClientFactory):

    def __init__(self, name, callback):
        self.name = name

    def clientConnectionFailed(self, connector, reason):
        print("Failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Close.")
        reactor.stop()

    def bieldprotocol(self, addr):
        self.connection = ChatClient(self.name)
        message = Message()
        worker = Tread(target=message.add_message, args=[MESSAGE, ])
        worker.start()
        return self.connection


if __name__ == "__main__":

    chat = ChatClientFactory("Ruby")
    reactor.connectTCP("192.168.4.123", 5000, chat)
    reactor.run()
    # while True:
    #     chat.send("Message")
    #     time.sleep(3)



