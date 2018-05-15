import threading

import zmq
from colorama import Fore, Style


class Client(threading.Thread):
    replies = None

    def __init__(self, number: int):
        super().__init__()
        self._serverIp = "127.0.0.1"
        self._serverPort = 5555
        self._serverEndPoint = f"tcp://{self._serverIp}:{self._serverPort}"
        self.number = number
        self.replies = []

    def run(self):
        print(f"{Fore.YELLOW}Client started.{Style.RESET_ALL}")
        context = zmq.Context(1)
        with context.socket(zmq.SUB) as clientSocket:
            try:
                clientSocket.connect(self._serverEndPoint)
                clientSocket.subscribe('')  # to all topics
                for n in range(self.number):
                    replyFromServer = clientSocket.recv_string()
                    print(f"{Fore.YELLOW}Received {replyFromServer}{Style.RESET_ALL}")
                    self.replies.append(float(replyFromServer))
            finally:
                pass
        context.term()
        print(f"{Fore.YELLOW}Client Closed.{Style.RESET_ALL}")

