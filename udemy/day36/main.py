import json
import requests
import pandas as pd

import plotly.graph_objects as go

from datetime import datetime
from alpha_api import API
from db_connection import db_Conn

STOCK = "TSCO"
COMPANY_NAME = "Tesla Inc"

class Stock:
    def __init__(self, stock_code, connection):
        self.stock_code: str = stock_code
        self.connection = connection

    def get_intraday_results(self) -> None:
        try:
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock_code}&apikey={API}'
            r = requests.get(url)
            data = r.json()

            for (index, value) in enumerate(data['Time Series (Daily)']):
                open_price = data['Time Series (Daily)'][value]['1. open']
                max_price = data['Time Series (Daily)'][value]['2. high']
                low_price = data['Time Series (Daily)'][value]['3. low']
                close_price = data['Time Series (Daily)'][value]['4. close']
                self.connection.insert_stock_price(value, open_price, close_price, max_price, low_price, self.stock_code)

            self.connection.commit_and_close()
        except ValueError as e:
            print(f'Error {e}')


    def plot(self, stock_id) -> None:
        date = []
        open_price = []
        close_price = []
        max_price = []
        low_price = []
        day_variation = []
        
        prices = self.connection.get_stock_price(stock_id[0])

        for (index, values) in enumerate(prices):
            date.append(values[1])
            open_price.append(values[2])
            close_price.append(values[3])
            max_price.append(values[4])
            low_price.append(values[5])
            day_variation.append(self.check_day_variation(values[1], float(values[2]), float(values[3])))

        fig = go.Figure(data=[go.Candlestick(x=date,
                open=open_price,
                high=max_price,
                low=low_price,
                close=close_price)
                ])

        fig.show()
        #self.write_diff_day(day_variation)

    def write_diff_day(self, day_variation):
        dict_price = {date:difference for (date, difference) in day_variation}
        with open('result.json', 'a') as f:
            f.write(json.dumps(dict_price))

    def check_day_variation(self, date, open_price, close_price) -> tuple:
        return (date, (close_price / open_price - 1) / 100)

if __name__ == '__main__':
    conn = db_Conn()
    conn.insert_stock(STOCK)
    stock_id = conn.get_stock_id(STOCK)
    tesla = Stock(STOCK, conn)
    #tesla.get_intraday_results()
    tesla.plot(stock_id)

