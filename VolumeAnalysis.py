# VolumeAnalysis.py

import pandas as pd
import ccxt

class VolumeAnalysis:
    def __init__(self, symbols):
        self.symbols = symbols  # List of symbols like ['BTC/USD', 'DOGE/USD', 'XRP/USD']
        self.exchange = ccxt.kraken()
        
    def fetch_data(self, symbol):
        ohlcv = self.exchange.fetch_ohlcv(symbol, '1m')
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        return df
    
    def calculate_ema(self, symbol, period=14):
        df = self.fetch_data(symbol)
        ema = df['volume'].ewm(span=period, adjust=False).mean()
        return ema
    
    def calculate_obv(self, symbol):
        df = self.fetch_data(symbol)
        df['obv'] = (df['volume'] * (~df['close'].diff().lt(0) * 2 - 1)).cumsum()
        return df['obv']
