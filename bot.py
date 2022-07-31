# Creating an algorithmic trading bot with alpaca to
# track the S&P 500 and trade based on Up and Down trends

import alpaca_trade_api as tradeapi
import threading
import time
import datetime
import logging
import argparse

# get key and secret from .env file
api_key_id = open(".env").read().split("\n")[0]
api_secret_id = open(".env").read().split("\n")[1]
base_url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(api_key_id, api_secret_id, base_url=base_url)
