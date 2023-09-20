
# Importing required libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
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

    def data_normalization(self):
        """
        Normalize the cleaned data to have a mean of 0 and variance of 1.
        
        Computational Complexity: O(n), where n is the number of data points.
        """
        if self.raw_data is None:
            logging.error("No data loaded for normalization.")
            return None

        # Initialize the StandardScaler
        scaler = StandardScaler()

        # Normalize the data
        normalized_data = pd.DataFrame(scaler.fit_transform(self.raw_data), columns=self.raw_data.columns)

        logging.info("Data normalization completed.")
        return normalized_data


# Sample usage of DataProcessingSlave for data normalization
if __name__ == "__main__":
    # Sample cleaned data (for demonstration purposes)
    cleaned_data_dict = {
        'timestamp': [1, 4],
        'price': [100, 103],
        'volume': [10, 13]
    }
    cleaned_data_df = pd.DataFrame(cleaned_data_dict)

    # Initialize a DataProcessingSlave instance (if not already)
    slave = DataProcessingSlave()

    # Load cleaned data
    slave.load_data(cleaned_data_df)

    # Perform data normalization
    normalized_data = slave.data_normalization()
    print("Normalized Data:")
    print(normalized_data)
    