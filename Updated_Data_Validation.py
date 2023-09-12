import numpy as np
import pandas as pd

def enhanced_validate_data(df):
    # Outlier detection using Z-score
    z_scores = np.abs(df[['open', 'high', 'low', 'close']].apply(zscore))
    df = df[(z_scores < 3).all(axis=1)]

    # Data integrity check
    if not (df['high'] >= df['low']).all():
        return False, "Data integrity check failed"

    return True, "Data is valid"
