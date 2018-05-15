import zmq

from pprint import pprint


class Client:
    _serverIp = "127.0.0.1"
    _serverPort = 5555
    _serverEndPoint = f"tcp://{_serverIp}:{_serverPort}"

    @staticmethod
    def getData(number):
        replies = []
        context = zmq.Context(1)
        with context.socket(zmq.SUB) as clientSocket:
            clientSocket.connect(Client._serverEndPoint)
            clientSocket.subscribe('')
            for n in range(number):
                replyFromServer = clientSocket.recv_string()
                print(f"Received {replyFromServer}")
                replies.append(float(replyFromServer))
        context.term()
        return replies
