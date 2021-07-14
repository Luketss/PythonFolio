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
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock_code}&outputsize=full&apikey={API}'
        r = requests.get(url)
        data = r.json()
        for (index, value) in enumerate(data['Time Series (Daily)']):
            open_price = data['Time Series (Daily)'][value]['1. open']
            max_price = data['Time Series (Daily)'][value]['2. high']
            low_price = data['Time Series (Daily)'][value]['3. low']
            close_price = data['Time Series (Daily)'][value]['4. close']
            self.connection.insert_stock_price(value, open_price, close_price, max_price, low_price, self.stock_code)

        self.connection.commit_and_close()

    def plot(self):
        date = []
        open_price = []
        close_price = []
        max_price = []
        low_price = []

        prices = self.connection.get_stock_price()
        for (index, values) in enumerate(prices):
            date.append(values[1])
            open_price.append(values[2])
            close_price.append(values[3])
            max_price.append(values[4])
            low_price.append(values[5])

        fig = go.Figure(data=[go.Candlestick(x=date,
                open=open_price,
                high=max_price,
                low=low_price,
                close=close_price)
                ])

        fig.show()

if __name__ == '__main__':
    conn = db_Conn()
    conn.insert_stock('MSFT')
    tesla = Stock(STOCK, conn)
    #tesla.get_intraday_results()
    tesla.plot()
    
    
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

