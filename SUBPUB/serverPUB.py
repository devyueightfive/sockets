import zmq
import random
import time


class Server:
    _serverIp = "127.0.0.1"
    _serverPort = 5555
    _serverEndPoint = f"tcp://{_serverIp}:{_serverPort}"

    @staticmethod
    def _makeMessage():
        return str(random.random())

    @staticmethod
    def startServer():
        context = zmq.Context(1)
        with context.socket(zmq.PUB) as serverSocket:
            serverSocket.bind(f"tcp://*:{serverPort}")
            while True:
                message = Server._makeMessage()
                serverSocket.send_string(message)
                time.sleep(random.random())
