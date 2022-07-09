# import socket
# sock = socket.socket()
# sock.connect((('46.229.214.188', 80)))
# sock.send(b'sakovdmitry@gmail.com:xxxxxxx')
# data = sock.recv(1024)
# print(data)
# sock.close()

from tornado.ioloop import IOLoop, PeriodicCallback
from tornado import gen
from tornado.websocket import websocket_connect


class Client(object):
    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout
        self.ioloop = IOLoop.instance()
        self.ws = None
        self.connect()
        PeriodicCallback(self.keep_alive, 20000).start()
        self.ioloop.start()

    @gen.coroutine
    def connect(self):
        print("trying to connect")
        try:
            self.ws = yield websocket_connect(self.url)
        except Exception as e:
            print("connection error")
        else:
            print("connected")
            self.run()

    @gen.coroutine
    def run(self):
        # self.ws.send(b'sakovdmitry@gmail.com:\t\xe1\x0c(\x0e\x8d\xdc\x99\x0e\x9c\xa9\xc8\x01e.\xc66\xeb\x9c\x9c\xe0$\xf1\x84\x95\xcc\xf2\xae#\xe1\xf8\xbd')
        while True:
            msg = yield self.ws.read_message()
            print(msg)
            if msg is None:
                print("connection closed")
                self.ws = None
                break

    def keep_alive(self):
        if self.ws is None:
            self.connect()
        else:
            self.ws.write_message("keep alive")

if __name__ == "__main__":
    client = Client("ws://46.229.214.188:80", 5)
