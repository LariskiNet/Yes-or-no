from flask import Flask, request
from aioalice import *
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

dp = Dispatcher()


@app.route('/')
def index():
    return 'Flask is running!'


@app.route("/", methods=['POST'])
def main():
    logging.info(request.json)


@dp.request_handler()
async def handle_all_requests(alice_request):
    return alice_request.response('Привет этому миру!')

if __name__ == "__main__":
    app.run(ssl_context=('cert.pem', 'key.pem'))
