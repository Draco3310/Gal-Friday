import time
import talib
import os
import pandas as pd
import krakenex as kraken
from talib import MA_Type
from Updated_Error_Handling import safe_execute
from Dynamic_Rate_Limiter import DynamicRateLimiter
from Updated_Data_Validation import enhanced_validate_data
from joblib import Memory
from statsmodels.tsa.api import VAR  # Import the VAR model
import logging

# Initialize memory for caching
memory = Memory("cached_folder", verbose=0)

def calculate_VWAP(df):
    df['TP'] = (df['high'] + df['low'] + df['close']) / 3.0
    df['TradedValue']  = df['TP'] * df['volume']
    df['CumVolume'] = df['volume'].cumsum()
    df['CumTradedValue'] = df['TradedValue'].cumsum()
    df['VWAP'] = df['CumTradedValue'] / df['CumVolume']
    return df['VWAP']

# Calculate OBV
def calculate_OBV(df):
    df['DailyRet'] = df['close'].pct_change()
    df['Direction'] = np.where(df['DailyRet'] >= 0, 1, -1)
    df['Direction'][0] = 0
    df['VolDirection'] = df['volume'] * df['Direction']
    df['OBV'] = df['VolDirection'].cumsum()
    return df['OBV']

# Define the VAR model function
def calculate_VAR(df_btc, df_xrp, df_doge):
    df = pd.DataFrame({
        'BTC': df_btc['close'],
        'XRP': df_xrp['close'],
        'DOGE': df_doge['close']
    })
    model = VAR(df)
    model_fitted = model.fit(5)  # Fit the model with 5 lags (you can adjust this)
    
    # Get the lag order
    lag_order = model_fitted.k_ar
    
    # Input data for forecasting
    forecast_input = df.values[-lag_order:]
    
    # Forecast
    fc = model_fitted.forecast(y=forecast_input, steps=5)
    
    return fc  # This will give you a 5-step ahead forecast for each asset

rate_limiter = DynamicRateLimiter()

KRAKEN_API_KEY = os.environ.get('KRAKEN_API_KEY')
KRAKEN_API_SECRET = os.environ.get('KRAKEN_API_SECRET')

buy_price = None

while True:
    time.sleep(1)
    ohlcv = rate_limiter.rate_limited_api_call(safe_execute, kraken.fetch_ohlcv, symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    if not enhanced_validate_data(df):
        continue

    # Fetch data for BTC, XRP, and DOGE
    df_btc = fetch_data('BTC/USD')
    df_xrp = fetch_data('XRP/USD')
    df_doge = fetch_data('DOGE/USD')

    # Calculate VWAP and OBV
    vwap = calculate_VWAP(df)
    obv = calculate_OBV(df)

    some_vwap_threshold = ...  # Set your threshold
    some_obv_threshold = ...  # Set your threshold

    # Calculate and use the VAR model forecast
    forecast = calculate_VAR(df_btc, df_xrp, df_doge)
    # (You can now use 'forecast' to adjust your trading logic)

    final_signal = ensemble_trading_strategy(df)
    current_price = df['close'][-1]

    if symbol == 'BTC/USD':
        position_size = calculate_position_size('BTC/USD', current_price, buy_price, portfolio_value)
    elif symbol == 'XRP/USD':
        position_size = calculate_position_size('XRP/USD', current_price, buy_price, portfolio_value)
    elif symbol == 'DOGE/USD':
        position_size = calculate_position_size('DOGE/USD', current_price, buy_price, portfolio_value)

     if final_signal == 'buy' and buy_price is None and vwap[-1] > some_vwap_threshold and obv[-1] > some_obv_threshold:
        safe_execute(place_order, 'buy', symbol, amount, current_price)
        buy_price = current_price
        logging.info(f"Buy order executed at {current_price}")

    elif (final_signal == 'sell' or advanced_risk_management(current_price, buy_price) == 'sell') and vwap[-1] < some_vwap_threshold and obv[-1] < some_obv_threshold:
        safe_execute(place_order, 'sell', symbol, amount, current_price)
        buy_price = None
        logging.info(f"Sell order executed at {current_price}")