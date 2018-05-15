import random
import threading
import time

import zmq

from SUBPUB import StopException


class Server(threading.Thread):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.daemon = True
        self._serverIp = "127.0.0.1"
        self._serverPort = 5555
        self._serverEndPoint = f"tcp://{self._serverIp}:{self._serverPort}"
        self.toStop = 0

    @staticmethod
    def _makeMessage():
        return str(random.random())

    def startServer(self):
        self.start()

    def run(self):
        print("Server started")
        context = zmq.Context(1)
        with context.socket(zmq.PUB) as serverSocket:
            serverSocket.bind(f"tcp://*:{self._serverPort}")
            while True:
                try:
                    if not self.toStop:
                        message = Server._makeMessage()
                        print(f"Server sent: {message}")
                        serverSocket.send_string(message)
                        time.sleep(random.random())
                    else:
                        break
                except StopException:
                    break
                except KeyboardInterrupt:
                    break
        context.term()
        print("Server stopped.")

    def stopServer(self):
        self.toStop = 1
