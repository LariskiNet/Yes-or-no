from flask import Flask, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=['POST'])
def main():
    return '<h1>flask app<h1>'


if __name__ == '__main__':
    app.run()
