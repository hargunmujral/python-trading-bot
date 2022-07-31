# Creating an algorithmic trading bot with alpaca to
# track the S&P 500 and trade based on Up and Down trends

import alpaca_trade_api as tradeapi
import os
from dotenv import load_dotenv
import threading
import time
import datetime
import logging
import argparse

# get key and secret from .env file
load_dotenv()

api_key_id = os.getenv("API_KEY_ID")
api_secret_id = os.getenv("API_SECRET_ID")
base_url = "https://paper-api.alpaca.markets"

api = tradeapi.REST(api_key_id, api_secret_id, base_url=base_url)

# Get account info
def get_account_info():
    account = api.get_account()
    print(account.status)
    return account

# Order stock
def order_stock(symbol, qty, side, type, time_in_force):
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side=side,
        type=type,
        time_in_force=time_in_force
    )
    return order

# Still needs to be implemented
def run_trading_algorithm():
    return 0

if __name__ == "__main__":
    get_account_info()
    selection = input("Select an option: 1. Buy 2. Sell 3. Algorithmic Mode 4. Exit: ")
    if selection == "1":
        # For now we will hard code the purchase of one SPY share to test
        order_stock("SPY", 1, "buy", "market", "gtc")
    elif selection == "2":
        order_stock("SPY", 1, "sell", "market", "gtc")
    elif selection == "3":
        run_trading_algorithm()
    elif selection == "4":
        exit()
    else:
        print("Invalid input")
        exit()