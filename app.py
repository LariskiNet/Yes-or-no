from flask import Flask, request
from aioalice import *
import logging
from dialogic.dialog_connector import DialogConnector
from dialogic.dialog_manager import TurnDialogManager
from dialogic.server.flask_server import FlaskServer
from dialogic.cascade import DialogTurn, Cascade
csc = Cascade()
app = Flask(__name__)
dp = Dispatcher()
logging.basicConfig(level=logging.DEBUG)

@app.route("/", methods=['POST'])
def main():
    logging.info(request.json)


@csc.add_handler(priority=10, regexp='(hello|hi|привет|здравствуй)')
def hello(turn: DialogTurn):
    turn.response_text = 'Привет! Это единственная условная ветка диалога.'


@csc.add_handler(priority=1)
def fallback(turn: DialogTurn):
    turn.response_text = 'Я вас не понял. Скажите мне "Привет"!'
    turn.suggests.append('привет')

dm = TurnDialogManager(cascade=csc)
connector = DialogConnector(dialog_manager=dm)
server = FlaskServer(connector=connector)


if __name__ == "__main__":
    app.run(ssl_context='adhoc')
