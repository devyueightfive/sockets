import unittest

from SUBPUB import clientSUB
from SUBPUB import serverPUB


class SomeTest(unittest.TestCase):

    def setUp(self):
        self.server = serverPUB.Server()
        self.server.start()

    def tearDown(self):
        try:
            print("Sent stop Signal to Server.")
            self.server.stopServer()
            self.server.join()
        finally:
            print("Test Ended.")

    def testGetNumberOfData(self):
        import time
        time.sleep(3)
        print("Test: getNumberOfData")
        number = 10
        self.client = clientSUB.Client(number)
        self.client.start()
        self.client.join()
        result = self.client.replies
        self.assertEqual(number, len(result))


class AnotherTest(unittest.TestCase):
    def setUp(self):
        pass


if __name__ == "__main__":
    unittest.main()
