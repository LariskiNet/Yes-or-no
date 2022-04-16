from aiohttp import web
from aioalice import Dispatcher, get_new_configured_app

WEBHOOK_URL_PATH = 'https://github.com/LariskiNet/Yes-or-no.git'  # webhook endpoint

WEBAPP_HOST = 'localhost'
WEBAPP_PORT = 3001

dp = Dispatcher()


@dp.request_handler()
def handle_dialog(request, response, user_storage, alice_request):
    return alice_request.response('Привет этому миру!')


if __name__ == '__main__':
    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_URL_PATH)
    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)
