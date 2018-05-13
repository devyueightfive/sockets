import unittest

import clientREQ


class MyCase(unittest.TestCase):

    def testRequest_from_list(self):
        requests = [1, 2, 3, 4, 5]
        repliesFromServer = clientREQ.getReplies(requests)
        replies = [1, 4, 9, 16, 25]
        self.assertEqual(repliesFromServer, replies, 'incorrect replies')


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
