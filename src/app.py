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

    sentence = request.args.get('text')
    num_of_palindromes = palindrome_count(sentence)

    output = {
        "error": False,
        "sentence entered": sentence,
        "answer": num_of_palindromes
    }

    json_output = json.dumps(output)
    response = flask.Response(json_output)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response

# Error handler to deal with incorrect parameters 
@app.errorhandler(500)
def server_error_500(error):
    error_output = {
        "error": False,
        "sentence entered": "500 Error: Incorrect Parameters Used",
        "answer": 0    
    }

    json_output = json.dumps(error_output)
    response = flask.Response(json_output)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'

    return response


if __name__ == '__main__':
    app.run(host = '0.0.0.0')