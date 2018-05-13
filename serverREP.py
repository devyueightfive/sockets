import zmq

serverIp = "127.0.0.1"
serverPort = 5555
url = f"tcp://{serverIp}:{serverPort}"


def makeReply(request):
    return str(float(request) ** 2)


def startServer():
    context = zmq.Context(1)
    with context.socket(zmq.REP) as serverSocket:
        serverSocket.bind(f"tcp://*:{serverPort}")
        while True:
            request = serverSocket.recv_string()
            reply = makeReply(request)
            serverSocket.send_string(reply)


if __name__ == "__main__":
    startServer()
