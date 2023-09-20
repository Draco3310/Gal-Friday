
# Importing required libraries
import pandas as pd
import numpy as np
import logging

# Initialize logging
logging.basicConfig(level=logging.INFO)


class DataProcessingMaster:
    def __init__(self):
        """
        Initialize the DataProcessingMaster instance.
        """
        self.slaves = []  # List to store slave instances

    def add_slave(self, slave):
        """
        Add a DataProcessingSlave instance to the master's list.

        :param slave: An instance of DataProcessingSlave
        :type slave: DataProcessingSlave
        """
        self.slaves.append(slave)
        logging.info(f"Added a new DataProcessingSlave. Total Slaves: {len(self.slaves)}")

    def distribute_data(self, data):
        """
        Distribute raw data to all the DataProcessingSlave instances.

        :param data: Raw data to be processed
        :type data: pandas.DataFrame

        Computational Complexity: O(n * m), where n is the number of slaves and m is the size of the data.
        """
        for slave in self.slaves:
            slave.load_data(data.copy())
        logging.info(f"Distributed data to {len(self.slaves)} slaves.")

    def aggregate_data(self, time_window='1T'):
        """
        Aggregate processed data from all slaves and combine it.

        :param time_window: The time window for aggregation (default is '1T' or 1 minute).
                            This can be any valid pandas time frequency string.
        :type time_window: str

        Computational Complexity: O(n * m), where n is the number of slaves and m is the size of the aggregated data.
        """
        aggregated_data_list = [slave.data_aggregation(time_window=time_window) for slave in self.slaves]
        combined_data = pd.concat(aggregated_data_list)
        logging.info(f"Aggregated data from {len(self.slaves)} slaves.")

        return combined_data


# Sample usage of DataProcessingMaster
if __name__ == "__main__":
    # Initialize DataProcessingMaster
    master = DataProcessingMaster()

    # Initialize two DataProcessingSlave instances (for demonstration)
    slave1 = DataProcessingSlave()
    slave2 = DataProcessingSlave()

    # Add slaves to master
    master.add_slave(slave1)
    master.add_slave(slave2)

    # Sample raw data (for demonstration purposes)
    raw_data_dict = {
        'timestamp': [pd.Timestamp('2021-01-01 00:00:00'), pd.Timestamp('2021-01-01 00:01:00')],
        'price': [1.0, 2.0],
        'volume': [100, 200]
    }
    raw_data_df = pd.DataFrame(raw_data_dict)

    # Distribute raw data to slaves
    master.distribute_data(raw_data_df)

    # Aggregate data from slaves
    combined_data = master.aggregate_data(time_window='1T')
    print("Combined Aggregated Data:")
    print(combined_data)
    