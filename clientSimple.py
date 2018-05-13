import socket
import time
import sys

serverIP = '127.0.0.1'
serverPort = 10000
serverEndpoint = (serverIP, serverPort)

messages = ['Hello', ',', 'world', '!']
attempts = 5

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(1)

    for attempt in range(attempts):
        try:
            client.connect(serverEndpoint)
            break
        except ConnectionRefusedError:
            print(f"Client {attempt} attempt to connect ...")
            time.sleep(3)
            continue
        except Exception as error:
            print(f"Client : {error}")
            continue
        else:
            sys.exit()

    for message in messages:
        print("Client sent {0}".format(message))
        client.sendall(message.encode())
        reply = client.recv(1024)
        print("Client received {0}".format(reply))

    print("Client: closing socket.")
    client.close()
