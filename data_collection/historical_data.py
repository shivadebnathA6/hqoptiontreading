
import requests
import pandas as pd

def fetch_historical_data(symbol, api_key, start_date, end_date):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=full&datatype=csv'
    response = requests.get(url)
    data = pd.read_csv(pd.compat.StringIO(response.text))
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data[(data['timestamp'] >= start_date) & (data['timestamp'] <= end_date)]
    return data

if __name__ == "__main__":
    symbol = 'RELIANCE.BSE'
    api_key = 'your_alpha_vantage_api_key'
    start_date = '2020-01-01'
    end_date = '2021-01-01'
    data = fetch_historical_data(symbol, api_key, start_date, end_date)
    print(data.head())
