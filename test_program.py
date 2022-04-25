import unittest

target = __import__("main.py")


class TestListSum(unittest.TestCase):

    search = 'zero'

    # def test(self, mock):
    #     search = mock
    #     self.assertTrue(search == '')



if __name__ == '__main__':
    unittest.main()
