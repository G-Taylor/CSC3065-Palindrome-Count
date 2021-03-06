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
    def test_palindrome_count_1(self):
        response = self.app.get('/?text=lol')
        assert response.data.decode("utf-8") == '{"error": false, "sentence": "lol", "answer": 1}'


    def test_palindrome_count_10(self):
        response = self.app.get('/?text=lol aha anna, kayak, not a palindrome, civic, radar, madam racecar rotor stats')
        assert response.data.decode("utf-8") == '{"error": false, "sentence": "lol aha anna, kayak, not a palindrome, civic, radar, madam racecar rotor stats", "answer": 10}'


    def test_palindrome_count_remove_special_chars(self):
        response = self.app.get('/?text=spec-ial char:s sh@ould <a>ll b{e gone a;ha')
        assert response.data.decode("utf-8") == '{"error": false, "sentence": "spec-ial char:s sh@ould <a>ll b{e gone a;ha", "answer": 1}'


    def test_palindrome_count_remove_numbers(self):
        response = self.app.get('/?text=This str1ng should h4v3 thre3 palindromes m4ad4am t3enet w0ow')
        assert response.data.decode("utf-8") == '{"error": false, "sentence": "This str1ng should h4v3 thre3 palindromes m4ad4am t3enet w0ow", "answer": 3}'


    def test_palindrome_count_empty_string(self):
        response = self.app.get('/?text=')
        assert response.data.decode("utf-8") == '{"error": false, "sentence": "", "answer": 0}'


    def test_palindrome_count_incorrect_parameters_no_query(self):
        response = self.app.get('/')
        assert response.data.decode("utf-8") == '{"error": true, "sentence": "500 Error: Incorrect Parameters Used", "answer": 0}'


    def test_palindrome_count_incorrect_parameters_no_equals_sign(self):
        response = self.app.get('/?text')
        assert response.data.decode("utf-8") == '{"error": false, "sentence": "", "answer": 0}'

    def test_palindrome_count_incorrect_parameters_wrong(self):
        response = self.app.get('/text=this is a test')
        assert response.data.decode("utf-8") == '{"error": true, "sentence": "404 Error: Page Not Found", "answer": 0}'



if __name__ == '__main__':
    unittest.main()
