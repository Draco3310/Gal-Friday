# fetch_market_data.py

from krakenex import API

def fetch_ohlcv(api, symbol, timeframe):
    # Fetch OHLCV data from Kraken
    return api.query_public('OHLC', {'pair': symbol, 'interval': timeframe})

# Add more data fetching functions here
