
import pandas as pd

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
