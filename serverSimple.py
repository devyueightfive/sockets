import socket

serverIP = '127.0.0.1'
serverPort = 10000
serverEndpoint = (serverIP, serverPort)


def makeReplyOn(message):
    return message


if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(1)
    server.bind(serverEndpoint)
    server.listen(5)
    while True:
        try:
            print("Server waiting connection ...")
            newSocket, addressInfo = server.accept()
            print("Server: received connection from {0}".format(addressInfo))
            with newSocket:
                while True:
                    message = newSocket.recv(1024)
                    print("Server: received message {0}".format(message))
                    if message:
                        reply = makeReplyOn(message)
                        print("Server: sent reply {0}".format(reply))
                        newSocket.sendall(reply)
                    else:
                        print("Client sent no data. It means end of connection.")
                        break
                newSocket.close()
        except (KeyboardInterrupt, SystemExit):
            print("Execution is interrupted...")
            break
        except Exception as error:
            print(f"Server error: {error}")
    server.close()
