import unittest

from SUBPUB import clientSUB
from SUBPUB import serverPUB


class SomeTest(unittest.TestCase):

    def setUp(self):
        self.server = serverPUB.Server()
        self.server.startServer()

    def tearDown(self):
        try:
            self.server.stopServer()
            self.server.join()
        except:
            print("Sent stop Signal to Server.")

    def testGetNumberOfData(self):
        import time
        time.sleep(3)
        print("Test: getNumberOfData")
        number = 10
        result = clientSUB.Client.getData(number)
        self.assertEqual(number, len(result))
        print("Test Ended.")


if __name__ == "__main__":
    unittest.main()
