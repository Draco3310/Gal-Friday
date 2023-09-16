# advanced_indicators.py

import pandas as pd
import talib
import numpy as np

def calculate_VWAP(df):
    """
    Calculate Volume Weighted Average Price (VWAP)
    
    Parameters:
    df (DataFrame): OHLCV data
    
    Returns:
    DataFrame: VWAP values
    """
    df['TP'] = (df['high'] + df['low'] + df['close']) / 3.0
    df['TradedValue']  = df['TP'] * df['volume']
    df['CumVolume'] = df['volume'].cumsum()
    df['CumTradedValue'] = df['TradedValue'].cumsum()
    return df['VWAP']

def calculate_OBV(df):
    """
    Calculate On Balance Volume (OBV)
    
    Parameters:
    df (DataFrame): OHLCV data
    
    Returns:
    DataFrame: OBV values
    """
    df['DailyRet'] = df['close'].pct_change()
    df['Direction'] = np.where(df['DailyRet'] >= 0, 1, -1)
    df['Direction'][0] = 0
    df['VolDirection'] = df['volume'] * df['Direction']
    df['OBV'] = df['VolDirection'].cumsum()
    return df['OBV']

def calculate_MACD(df, short_window=12, long_window=26, signal_window=9):
    """
    Calculate Moving Average Convergence Divergence (MACD)
    
    Parameters:
    df (DataFrame): OHLCV data
    short_window (int): Short term EMA window
    long_window (int): Long term EMA window
    signal_window (int): Signal line window
    
    Returns:
    DataFrame: MACD and Signal line values
    """
    short_ema = df['close'].ewm(span=short_window, adjust=False).mean()
    long_ema = df['close'].ewm(span=long_window, adjust=False).mean()
    MACD = short_ema - long_ema
    signal_line = MACD.ewm(span=signal_window, adjust=False).mean()
    return MACD, signal_line

def calculate_RSI(df, window=14):
    """
    Calculate Relative Strength Index (RSI)
    
    Parameters:
    df (DataFrame): OHLCV data
    window (int): Window for RSI calculation
    
    Returns:
    DataFrame: RSI values
    """
    delta = df['close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=window, min_periods=1).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window, min_periods=1).mean()
    RS = gain / loss
    RSI = 100 - (100 / (1 + RS))
    return RSI

def calculate_VAR(df_btc, df_xrp, df_doge):
    """
    Calculate Vector AutoRegression (VAR) model
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    df = pd.DataFrame({
        'BTC': df_btc['close'],
        'XRP': df_xrp['close'],
        'DOGE': df_doge['close']
    })
    model = VAR(df)
    model_fitted = model.fit(5)
    lag_order = model_fitted.k_ar
    forecast_input = df.values[-lag_order:]
    fc = model_fitted.forecast(y=forecast_input, steps=5)
    return fc



def calculate_OBV(df):
    df['DailyRet'] = df['close'].pct_change()
    df['Direction'] = np.where(df['DailyRet'] >= 0, 1, -1)
    df['Direction'][0] = 0
    df['VolDirection'] = df['volume'] * df['Direction']
    df['OBV'] = df['VolDirection'].cumsum()
    return df['OBV']


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


def calculate_VWAP(df):
    df['TP'] = (df['high'] + df['low'] + df['close']) / 3.0
    df['TradedValue']  = df['TP'] * df['volume']
    df['CumVolume'] = df['volume'].cumsum()
    df['CumTradedValue'] = df['TradedValue'].cumsum()
    df['VWAP'] = df['CumTradedValue'] / df['CumVolume']
    return df['VWAP']


def generate_signals(volume, short_window=5, long_window=20):
    signals = pd.DataFrame(index=volume.index)
    signals['price'] = volume
    signals['short_mavg'] = moving_average(volume, window_size=short_window)
    signals['long_mavg'] = moving_average(volume, window_size=long_window)
    signals['signal'] = 0.0
    signals['signal'][short_window:] = np.where(signals['short_mavg'][short_window:] > signals['long_mavg'][short_window:], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals


def moving_average(volume, window_size):
    return volume.rolling(window=window_size).mean()
