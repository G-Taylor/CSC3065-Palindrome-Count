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
    def test_palindrome_count(self):
        count = palindrome_count('This is a palindrome test: repaper, aha')
        self.assertEqual(count, 2)


    # Web API tests
    def test_palidrome_count_1(self):
        response = self.app.get('/?text=lol')
        assert response.data.decode("utf-8") == '{"error": false, "sentence entered": "lol", "answer": 1}'


    def test_palidrome_count_10(self):
        response = self.app.get('/?text=lol aha anna, kayak, not a palindrome, civic, radar, madam racecar rotor stats')
        assert response.data.decode("utf-8") == '{"error": false, "sentence entered": "lol aha anna, kayak, not a palindrome, civic, radar, madam racecar rotor stats", "answer": 10}'


    def test_palidrome_count_remove_special_chars(self):
        response = self.app.get('/?text=spec-ial char:s sh@ould <a>ll b{e gone a;ha')
        assert response.data.decode("utf-8") == '{"error": false, "sentence entered": "spec-ial char:s sh@ould <a>ll b{e gone a;ha", "answer": 1}'


    def test_palidrome_count_remove_numbers(self):
        response = self.app.get('/?text=This str1ng should h4v3 thre3 palindromes m4ad4am t3enet w0ow')
        assert response.data.decode("utf-8") == '{"error": false, "sentence entered": "This str1ng should h4v3 thre3 palindromes m4ad4am t3enet w0ow", "answer": 3}'


    def test_palidrome_count_empty_string(self):
        response = self.app.get('/?text=')
        assert response.data.decode("utf-8") == '{"error": false, "sentence entered": "", "answer": 0}'


    def test_palidrome_count_incorrect_parameters(self):
        response = self.app.get('/')
        assert response.data.decode("utf-8") == '{"error": true, "sentence entered": "500 Error: Incorrect Parameters Used", "answer": 0}'


if __name__ == '__main__':
    unittest.main()
