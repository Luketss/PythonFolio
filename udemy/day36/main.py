import requests

from alpha_api import API
from db_connection import db_Conn

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

class Stock:
    def __init__(self, stock_code):
        self.stock_code: str = stock_code

    def get_intraday_results(self) -> None:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={self.stock_code}&interval=5min&apikey={API}'
        r = requests.get(url)
        #data = r.json()
        print(r.text)
        # for (index, value) in enumerate(data['Time Series (Daily)']):
        #     print(data['Time Series (Daily)'][value]['1. open'])
    

if __name__ == '__main__':
    tesla = Stock(STOCK)
    tesla.get_intraday_results()
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

