from flask import Flask, request
from palindrome import palindrome_count

app = Flask(__name__)

@app.route("/")
def home():
    sentence = request.args.get('text')
    num_of_palindromes = palindrome_count(sentence)

    output = {
        "error": False,
        "sentence entered": sentence,
        "answer": num_of_palindromes
    }

    print(f"Sentence: {sentence}, Palindrome Count: {num_of_palindromes}")
    return num_of_palindromes

if __name__ == '__main__':
    app.run(host = '0.0.0.0')