import zmq

serverIp = "127.0.0.1"
serverPort = 10000
serverEndPoint = f"tcp://{serverIp}:{serverPort}"


def getReplies(fromRequests):
    replies = []
    context = zmq.Context(1)
    with context.socket(zmq.REQ) as clientSocket:
        clientSocket.connect(serverEndPoint)
        poll = zmq.Poller()

        for request in fromRequests:
            clientSent = clientSocket.send_string(str(request))
            print(clientSent)
            replyFromServer = clientSocket.recv_string()
            print(replyFromServer)
            replies.append(float(replyFromServer))
    context.term()
    return replies
