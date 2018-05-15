import unittest

from SUBPUB import clientSUB
from SUBPUB import serverPUB


class ServerFirst(unittest.TestCase):

    def setUp(self):
        print("ServerFirst Test: getNumberOfData")
        self.server = serverPUB.Server()
        self.server.start()

    def tearDown(self):
        self.server.stopServer()
        self.server.join()
        print("Test Ends.")

    def testGetNumberOfData(self):
        import time
        seconds = 3
        print(f"Client sleeps {seconds} seconds")
        time.sleep(seconds)
        number = 10
        self.client = clientSUB.Client(number)
        self.client.start()
        self.client.join()
        result = self.client.replies
        self.assertEqual(number, len(result))


class ClientFirst(unittest.TestCase):
    def setUp(self):
        print("ClientFirst Test: getNumberOfData")
        self.number = 10
        self.client = clientSUB.Client(self.number)
        self.client.start()

    def testGetNumberOfData(self):
        import time
        seconds = 3
        print(f"Server sleeps {seconds} seconds")
        time.sleep(seconds)
        self.server = serverPUB.Server()
        self.server.start()
        self.client.join()
        result = self.client.replies
        self.assertEqual(self.number, len(result))

    def tearDown(self):
        self.server.stopServer()
        self.server.join()
        print("Test Ends.\n")

class NoServer(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
