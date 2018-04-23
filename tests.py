import server
import unittest

class MyAppTests(unittest.TestCase):

    def setUp(self):
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get('/')
        self.assertIn('<h1>Hello</h1>', result.data)

if __name__ == '__main__':
    # If called like a script, run our tests
    unittest.main()