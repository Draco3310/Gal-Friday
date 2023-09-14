import time
from Updated_Improved_Trading_Loop import main_loop
from Updated_Improved_Trading_Loop import start_trading_loop
from config_handler import get_config

def main():
    config = get_config()
    
    # Fetch API keys from environment variables
    KRAKEN_API_KEY = config.get('Credentials', 'KRAKEN_API_KEY')
    KRAKEN_API_SECRET = config.get('Credentials', 'KRAKEN_API_SECRET')
    
    # Initialize trading pairs and timeframes
    trading_pairs = ['BTC/USD', 'XRP/USD', 'DOGE/USD']
    timeframes = ['1m', '5m', '15m', '1h', '4h']
    
    while True:
        for pair in trading_pairs:
            for timeframe in timeframes:
                start_trading_loop(pair, timeframe, KRAKEN_API_KEY, KRAKEN_API_SECRET)
        time.sleep(60)  # Wait for 1 minute before the next iteration

if __name__ == "__main__":
    main()
