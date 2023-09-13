import unittest
from Updated_Improved_Trading_Loop import ensemble_trading_strategy
import pandas as pd

class TestTradingLogic(unittest.TestCase):

    def setUp(self):
        # Sample OHLCV data for testing
        self.sample_data = pd.DataFrame({
            'timestamp': [1, 2, 3, 4, 5],
            'open': [100, 101, 102, 103, 104],
            'high': [105, 106, 107, 108, 109],
            'low': [95, 96, 97, 98, 99],
            'close': [104, 105, 106, 107, 108],
            'volume': [1000, 1000, 1000, 1000, 1000]
        })

    def test_ensemble_trading_strategy_buy_signal(self):
        # Modify sample data to simulate a buy signal
        self.sample_data['close'] = [104, 105, 106, 107, 120]
        signal = ensemble_trading_strategy(self.sample_data)
        self.assertEqual(signal, 'buy')

    def test_ensemble_trading_strategy_sell_signal(self):
        # Modify sample data to simulate a sell signal
        self.sample_data['close'] = [104, 105, 106, 107, 90]
        signal = ensemble_trading_strategy(self.sample_data)
        self.assertEqual(signal, 'sell')

    def test_ensemble_trading_strategy_no_signal(self):
        # Use sample data as-is to simulate no signal
        signal = ensemble_trading_strategy(self.sample_data)
        self.assertIsNone(signal)

if __name__ == '__main__':
    unittest.main()
