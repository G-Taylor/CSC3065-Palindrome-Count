from logging import error
import flask
import json
from flask import Flask, request, Response
from palindrome import palindrome_count

app = Flask(__name__)

@app.route("/")
def home():
    sentence = ''
    num_of_palindromes = 0

    if request.args.get('text') == '':
        output = {
            "error": False,
            "sentence entered": "",
            "answer": 0
        }    
    else:
        sentence = request.args.get('text')
        num_of_palindromes = palindrome_count(sentence)

        output = {
            "error": False,
            "sentence entered": sentence,
            "answer": num_of_palindromes
        }

    print(f"Sentence: {sentence}, Palindrome Count: {num_of_palindromes}")

    json_output = json.dumps(output)
    response = flask.Response(json_output)

    return response


@app.errorhandler(500)
def server_error_500(error):
    error_output = {
        "error": False,
        "sentence entered": "500 Error: Incorrect Parameters Used",
        "answer": 0    
    }

    json_output = json.dumps(error_output)
    response = flask.Response(json_output)

    return response


if __name__ == '__main__':
    app.run(host = '0.0.0.0')