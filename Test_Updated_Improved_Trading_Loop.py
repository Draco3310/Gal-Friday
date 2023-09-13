buy_price = None

while True:
    time.sleep(1)
    
    ohlcv = safe_execute(kraken.fetch_ohlcv, symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

    if not validate_data(df):
        continue
    
    k, d = talib.STOCHRSI(df['close'])
    buy_signal, sell_signal = generate_signal(k, d, df['volume'])
    
    current_price = df['close'][-1]
    
    if buy_signal and buy_price is None:
        safe_execute(place_order, 'buy', symbol, amount, current_price)
        buy_price = current_price
        logging.info(f"Buy order executed at {current_price}")
    elif sell_signal or check_stop_loss_or_take_profit(current_price, buy_price) in ['stop_loss', 'take_profit']:
        safe_execute(place_order, 'sell', symbol, amount, current_price)
        buy_price = None
        logging.info(f"Sell order executed at {current_price}")