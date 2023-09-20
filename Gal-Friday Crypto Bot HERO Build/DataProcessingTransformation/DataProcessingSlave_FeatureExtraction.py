
# Importing required libraries
import pandas as pd
import numpy as np
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)


class DataProcessingSlave:
    def __init__(self):
        """
        Initialize the DataProcessingSlave instance.
        """
        # Placeholder for storing raw data
        self.raw_data = None

    def load_data(self, data):
        """
        Load raw data into the Slave instance.
        
        :param data: Raw data to be processed.
        :type data: pandas.DataFrame
        """
        self.raw_data = data

    def feature_extraction(self):
        """
        Perform feature extraction on the normalized data to create new features that can be 
        used for better predictive analytics.
        
        Computational Complexity: O(n), where n is the number of data points.
        """
        if self.raw_data is None:
            logging.error("No data loaded for feature extraction.")
            return None

        # Sample feature extraction: Calculate moving average for 'price' over a window of 2
        self.raw_data['moving_avg_price'] = self.raw_data['price'].rolling(window=2).mean()

        # Sample feature extraction: Calculate price change as a new feature
        self.raw_data['price_change'] = self.raw_data['price'].diff()

        logging.info("Feature extraction completed.")
        return self.raw_data


# Sample usage of DataProcessingSlave for feature extraction
if __name__ == "__main__":
    # Sample normalized data (for demonstration purposes)
    normalized_data_dict = {
        'timestamp': [-1.0, 1.0],
        'price': [-1.0, 1.0],
        'volume': [-1.0, 1.0]
    }
    normalized_data_df = pd.DataFrame(normalized_data_dict)

    # Initialize a DataProcessingSlave instance (if not already)
    slave = DataProcessingSlave()

    # Load normalized data
    slave.load_data(normalized_data_df)

    # Perform feature extraction
    feature_extracted_data = slave.feature_extraction()
    print("Feature Extracted Data:")
    print(feature_extracted_data)
    