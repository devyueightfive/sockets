import unittest

import REQREP.clientREQ as clientREQ
import standardSockets.clientSimple as clientSimple


class MyMQCase(unittest.TestCase):

    def testRequest_from_list(self):
        requests = [1, 2, 3, 4, 5]
        repliesFromServer = clientREQ.getReplies(requests)
        replies = [1, 4, 9, 16, 25]
        self.assertEqual(repliesFromServer, replies, 'incorrect replies')


class MySimpleCase(unittest.TestCase):

    def testRequest_from_list(self):
        requests = [1, 2, 3, 4, 5]
        repliesFromServer = clientSimple.getRepliesFrom(requests)
        replies = [1, 4, 9, 16, 25]
        self.assertEqual(repliesFromServer, replies, 'incorrect replies')


if __name__ == '__main__':
    unittest.main()
