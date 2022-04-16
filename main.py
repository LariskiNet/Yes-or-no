from alice_blue import *
import logging
logging.basicConfig(level=logging.DEBUG)
access_token = AliceBlue.login_and_get_access_token(
    username='username', password='password', twoFA='1860', api_secret='api_secret', app_id='app_id')
alice = AliceBlue(username='username', password='password',
                  access_token=access_token)
print(alice.get_balance())  # get balance / margin limits
print(alice.get_profile())  # get profile
print(alice.get_daywise_positions())  # get daywise positions
print(alice.get_netwise_positions())  # get netwise positions
print(alice.get_holding_positions())  # get holding positions
