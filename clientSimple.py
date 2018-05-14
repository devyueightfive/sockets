import socket
import time
from pprint import pprint

serverIP = '127.0.0.1'
serverPort = 10000
serverEndpoint = (serverIP, serverPort)

myMessages = ['Hello', ',', 'world', '!']
attempts = 3


def send(messages):
    replies = []
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(1)

    try:
        """Connect to the serverEndPoint and send some messages"""
        for attempt in range(attempts):
            try:  # connect to the server
                client.connect(serverEndpoint)
                break
            except ConnectionRefusedError:
                print(f"Client: {attempt} attempt to connect ...")
            if attempt == attempts - 1:
                print(f"Client: Can't connect to the server {serverEndpoint} ...")
                return replies
            time.sleep(2)

        # send messages
        for message in messages:
            print("Client sent {0}".format(message))
            client.sendall(message.encode())
            reply = client.recv(1024)
            print("Client received {0}".format(reply))
            replies.append(reply)

    except KeyboardInterrupt:
        print("Interrupted by user")
        return replies
    except Exception as error:
        print(f"Client: {error}")
        return replies

    print("Client: closing socket.")
    client.close()

    return replies


if __name__ == "__main__":
    response = send(myMessages)
    pprint(response)
