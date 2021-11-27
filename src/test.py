import unittest
from app import app
from palindrome import palindrome_count

class PalindromeTest(unittest.TestCase):

    # Setup and teardown
    def setUp(self):
        self.app = app.test_client()


    def tearDown(self):
        pass

    
    def testPalindromeCount(self):
        count = palindrome_count('This is a palindrome test: repaper, aha')
        self.assertEqual(count, 2)

  
if __name__ == '__main__':
    unittest.main()
