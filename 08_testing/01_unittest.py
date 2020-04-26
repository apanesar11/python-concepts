import unittest

# this should be on a different file
def add_5(num):
    try:
        return num + 5
    except TypeError as err:
        return err

class TestMain(unittest.TestCase):
    def test_1(self):
        param = 10
        result = add_5(param)
        self.assertEqual(result, 15)

    def test_2(self):
        param = 'test'
        result = add_5(param)
        self.assertIsInstance(result, TypeError)

unittest.main()