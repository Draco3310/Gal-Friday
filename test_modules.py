import unittest
from parameterized import parameterized
from Updated_Improved_Trading_Loop import ensemble_trading_strategy
from Updated_Risk_Management import fetch_historical_data  # Import added here
import pandas as pd

class TestTradingLogic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Fetch historical OHLCV data for backtesting
        cls.historical_data = fetch_historical_data('BTC/USD', '1d')  # Fetch historical data here

    @classmethod
    def tearDownClass(cls):
        # Release resources
        del cls.historical_data

    def setUp(self):
        # Sample OHLCV data for individual tests
        self.sample_data = self.historical_data.tail(5).copy()

    @parameterized.expand([
        ("bull", [104, 105, 106, 107, 120]),
        ("bear", [104, 103, 102, 101, 90]),
        ("sideways", [104, 105, 104, 105, 104])
    ])
    def test_market_conditions(self, market_type, close_prices):
        self.sample_data['close'] = close_prices
        signal = ensemble_trading_strategy(self.sample_data)
        # Validate signal based on expected behavior in different market conditions

    @parameterized.expand([
        ("spike", [104, 105, 106, 107, 200]),
        ("drop", [104, 105, 106, 107, 50])
    ])
    def test_extreme_price_movements(self, movement_type, close_prices):
        self.sample_data['close'] = close_prices
        signal = ensemble_trading_strategy(self.sample_data)
        # Validate signal based on expected behavior during extreme price movements

    def test_consecutive_signals(self):
        close_prices = [104, 105, 106, 107, 120]
        self.sample_data['close'] = close_prices
        first_signal = ensemble_trading_strategy(self.sample_data)
        second_signal = ensemble_trading_strategy(self.sample_data)
        self.assertEqual(first_signal, second_signal)
        # Validate that the bot handles consecutive signals appropriately

if __name__ == "__main__":
    unittest.main()
