import time

import alpaca_trade_api as tradeapi
from Other_Projects.my_secrets import AlpacaTrading

alpaca_endpoint = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(AlpacaTrading.API_KEY_ID, AlpacaTrading.API_SECRET_KEY, alpaca_endpoint)
account = api.get_account()

def get_price(symbol):
    stock_data_p = api.get_latest_trade(symbol).__getattr__('p')
    stock_data_ap = api.get_latest_quote(symbol).__getattr__('ap')
    stock_data_bp = api.get_latest_quote(symbol).__getattr__('bp')
    return stock_data_p
    # return (stock_data_p * 3 + stock_data_ap + stock_data_bp) / 5


if __name__ == '__main__':
    symbol = 'NFLX'
    buy_sell_qty = 200
    last_action = 'sell'
    buy_price = 0
    previous_price = get_price(symbol)

    while True:
        current_price = get_price(symbol)
        # print(current_price)

        if current_price > previous_price:
            if last_action == 'sell':
                api.submit_order(symbol, buy_sell_qty)
                last_action = 'buy'
                buy_price = current_price
                print(f'\nBought {buy_sell_qty}x {symbol} at ${current_price} each for a total of ${current_price * buy_sell_qty}')

            elif current_price > buy_price:
                api.submit_order(symbol, buy_sell_qty, 'sell')
                last_action = 'sell'
                print(f'Sold {buy_sell_qty}x {symbol} at ${current_price} each for a total of ${current_price * buy_sell_qty}\n')

        # print(f'{previous_price=}, {current_price=}')
        previous_price = current_price
        time.sleep(1)
