import unittest
from Updated_Data_Validation import enhanced_validate_data
import pandas as pd
from parameterized import parameterized

class TestDataValidation(unittest.TestCase):
    def test_no_missing_values(self):
        df = pd.DataFrame({'open': [1, 2], 'close': [2, 3]})
        self.assertIsNone(enhanced_validate_data(df))

class TestDataValidation(unittest.TestCase):
    @parameterized.expand([
        ("case1", [1, 2], [2, 3]),
        ("case2", [3, 4], [4, 5]),
    ])
    def test_no_missing_values(self, name, open_values, close_values):
        df = pd.DataFrame({'open': open_values, 'close': close_values})
        self.assertIsNone(enhanced_validate_data(df))

from unittest.mock import patch

class TestTradingLoop(unittest.TestCase):
    @patch('krakenex.fetch_ohlcv')
    def test_fetch_ohlcv(self, mock_fetch):
        mock_fetch.return_value = # Mocked data
        # Your test code

def validate_data(df):
    if df.empty or df.isnull().values.any():
        return False, "Dataframe is empty or contains null values"

    # Type Validation
    expected_types = {'timestamp': 'int64', 'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64'}
    for column, expected_type in expected_types.items():
        if df[column].dtype != expected_type:
            return False, f"Unexpected data type in column {column}. Expected {expected_type}, got {df[column].dtype}"

    # Value Range
    if (df['open'] < 0).any() or (df['high'] < 0).any() or (df['low'] < 0).any() or (df['close'] < 0).any():
        return False, "Negative values found in price columns"

    # Temporal Consistency
    if not df['timestamp'].is_monotonic_increasing:
        return False, "Timestamps are not in increasing order"

    return True, "Data is valid"
