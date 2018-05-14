import unittest

from .clientSUB import Client

from .serverPUB import Server


class SomeTest(unittest.TestCase):

    def setUp(self):

    def testGetNumberOfData(self):
        number = 10
        result = Client.getData(number)
        self.assertEqual(number, len(result))
