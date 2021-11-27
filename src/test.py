import unittest
from app import app
from palindrome import palindrome_count

class PalindromeTest(unittest.TestCase):

    # Setup and teardown
    def setUp(self):
        self.app = app.test_client()


    def tearDown(self):
        pass

    # backend function test
    def testPalindromeCount(self):
        count = palindrome_count('This is a palindrome test: repaper, aha')
        self.assertEqual(count, 2)


    # Web API tests
    def testPalidromeCount1(self):
        response = self.app.get('/?text=lol')
        assert response.data.decode("utf-8") == '{"error": false, "sentence entered": "lol", "answer": 1}'

if __name__ == '__main__':
    unittest.main()
