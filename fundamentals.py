import requests
import os
from dotenv import load_dotenv
import yfinance as yf
from statistics import mean

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

        yf_ticker = yf.Ticker(t)
        info = yf_ticker.info
        try:
            current_price = info['currentPrice']
        except:
            print('ERROR: yfinance is not able to get the current price')
            current_price = 0

        print(f'Checking {len(data)} years of data for {t} ...')

        symbol = t

        earningsYield_list = []
        dividendYield_list = []
        payoutRatio_list = []

        netIncomePerShare_list = []
        cashPerShare_list = []
        bookValuePerShare_list = []
        tangibleBookValuePerShare_list = []

        peRatio_list = []
        pbRatio_list = []
        ptbRatio_list = []

        debtToEquity_list = []
        currentRatio_list = []

        roic_list = []
        returnOnTangibleAssets_list = []
        roe_list = []



        # STORING COLLECTED DATA. IF PROBLEMS, TRY EXCEPT EACH VALUE
        for i in data:
            earningsYield_list.append(i['earningsYield'])
            dividendYield_list.append(i['dividendYield'])
            payoutRatio_list.append(i['payoutRatio'])

            netIncomePerShare_list.append(i['netIncomePerShare'])
            cashPerShare_list.append(i['cashPerShare'])
            bookValuePerShare_list.append(i['bookValuePerShare'])
            tangibleBookValuePerShare_list.append(i['tangibleBookValuePerShare'])

            peRatio_list.append(i['peRatio'])
            pbRatio_list.append(i['pbRatio'])
            ptbRatio_list.append(i['ptbRatio'])

            debtToEquity_list.append(i['debtToEquity'])
            currentRatio_list.append(i['currentRatio'])

            roic_list.append(i['roic'])
            returnOnTangibleAssets_list.append(i['returnOnTangibleAssets'])
            roe_list.append(i['roe'])

        final_data = {
            'earningsYield_last': earningsYield_list[0],
            'dividendYield_last': dividendYield_list[0],
            'payoutRatio_last': payoutRatio_list[0],
            'payoutRatio_AVG': mean(payoutRatio_list),

            'netIncomePerShare_last': netIncomePerShare_list[0],
            'netIncomePerShare_change': (netIncomePerShare_list[0]-netIncomePerShare_list[-1])/netIncomePerShare_list[-1],
            'cashPerShare_last': cashPerShare_list[0],
            'cashPerShare_change': (cashPerShare_list[0]-cashPerShare_list[-1])/cashPerShare_list[-1],
            'bookValuePerShare_last': bookValuePerShare_list[0],
            'bookValuePerShare_change': (bookValuePerShare_list[0]-bookValuePerShare_list[-1])/bookValuePerShare_list[-1],
            'tangibleBookValuePerShare_last': tangibleBookValuePerShare_list[0],
            'tangibleBookValuePerShare_change': (tangibleBookValuePerShare_list[0]-tangibleBookValuePerShare_list[-1])/tangibleBookValuePerShare_list[-1],

            'peRatio_last': peRatio_list[0],
            'peRatio_on5years': current_price / mean(netIncomePerShare_list),
            'pbRatio_last': pbRatio_list[0],
            'pbRatio_on5years': current_price / mean(bookValuePerShare_list),
            'ptbRatio_last': ptbRatio_list[0],
            'ptbRatio_on5years': current_price / mean(tangibleBookValuePerShare_list),

            'debtToEquity_last': debtToEquity_list[0],
            'debtToEquity_AVG': mean(debtToEquity_list),
            'debtToEquity_change': (debtToEquity_list[0]-debtToEquity_list[-1])/debtToEquity_list[-1],
            'currentRatio_last': currentRatio_list[0],
            'currentRatio_AVG': mean(currentRatio_list),
            'currentRatio_change': (currentRatio_list[0]-currentRatio_list[-1])/currentRatio_list[-1],

            'roic_last': roic_list[0],
            'roic_AVG': mean(roic_list),
            'roic_change': (roic_list[0]-roic_list[-1])/roic_list[-1],
            'returnOnTangibleAssets_last': returnOnTangibleAssets_list[0],
            'returnOnTangibleAssets_AVG': mean(returnOnTangibleAssets_list),
            'returnOnTangibleAssets_change': (returnOnTangibleAssets_list[0]-returnOnTangibleAssets_list[-1])/returnOnTangibleAssets_list[-1],
            'roe_last': roe_list[0],
            'roe_AVG': mean(roe_list),
            'roe_change': (roe_list[0]-roe_list[-1])/roe_list[-1]
        }

        for key, value in final_data.items():
            print(f'{key}: {value}')
        return final_data

        """
        initialize dict items to return:

        earningsYield - LAST
        dividendYield - LAST
        payoutRatio - LAST and AVG 5/7 YEARS

        netIncomePerShare - LAST
        cashPerShare - LAST
        bookValuePerShare - LAST
        tangibleBookValuePerShare - LAST

        peRatio - LAST and over AVG EPS of 5/7 YEARS
        pbRatio - LAST and over AVG BV of 5/7 YEARS
        ptbRatio - LAST and over AVG TBV of 5/7 YEARS

        debtToEquity - LAST and AVG 5/7 YEARS
        currentRatio - LAST and AVG 5/7 YEARS

        roic - LAST and AVG 5/7 YEARS
        returnOnTangibleAssets - LAST and AVG 5/7 YEARS
        roe - LAST and AVG 5/7 YEARS

        """
        # in data a list of dict. Each dict is a year of data

get_fundamentals(ticker)