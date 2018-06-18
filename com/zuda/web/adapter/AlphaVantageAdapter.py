import requests
from requests import Response

from com.zuda.web.model.Kline import Kline

ALPHAVANTAGE_URL: str = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
MARKET_DATA = 'Time Series (Daily)'
OPEN = '1. open'
HIGH = '2. high'
LOW = '3. low'
CLOSE = '4. close'
VOLUME = '5. volume'

response: Response = requests.get(ALPHAVANTAGE_URL)


def isRequestSuccessful():
    return response.status_code == 200


if isRequestSuccessful():
    unparsedContent: dict = response.json()
    print('Successfully obtained response:')
    marketDataDict: dict = unparsedContent[MARKET_DATA]
    for tickerDate in iter(marketDataDict):
        dailyDate = marketDataDict[tickerDate]
        kline = Kline(date=tickerDate,
                      open=dailyDate[OPEN],
                      close=dailyDate[CLOSE],
                      high=dailyDate[HIGH],
                      low=dailyDate[LOW],
                      volume=dailyDate[VOLUME])
        print(kline)
