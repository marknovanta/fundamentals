import requests
import os
from dotenv import load_dotenv

ticker = ['AAPL']



def get_fundamentals(tickers):
    load_dotenv()
    api_key = os.getenv('api_key')
    for t in tickers:
        url = f'https://financialmodelingprep.com/api/v3/key-metrics/{t}?period=annual&apikey={api_key}'
        try:
            r = requests.get(url)
            r.raise_for_status()
            data = r.json()
        except requests.exceptions.RequestException as e:
            print('Error fetching data:', e)
            return {}

        print(data[0])

get_fundamentals(ticker)