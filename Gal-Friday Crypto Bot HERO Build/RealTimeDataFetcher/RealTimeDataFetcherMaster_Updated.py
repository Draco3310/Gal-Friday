
import logging

class RealTimeDataFetcherMaster:
    def __init__(self, api_url='https://api.kraken.com/0/public/'):
        self.api_url = api_url
        self.slaves = []
        self.data_cache = {}
        logging.basicConfig(level=logging.INFO)

    def register_slave(self, slave):
        try:
            self.slaves.append(slave)
            logging.info(f"Registered slave. Total slaves: {len(self.slaves)}")
        except Exception as e:
            logging.error(f"Failed to register slave: {e}")

    def allocate_task(self, task):
        try:
            if not self.slaves:
                logging.error("No slaves available for task allocation.")
                return

            # For now, allocate all tasks to the first slave.
            # TODO: Implement more sophisticated task allocation logic
            slave = self.slaves[0]
            slave.perform_task(task)
            logging.info(f"Task {task} allocated to slave {slave}")
        except Exception as e:
            logging.error(f"Failed to allocate task {task}: {e}")

if __name__ == "__main__":
    master = RealTimeDataFetcherMaster()
    # Simulation: Register a slave and allocate a task
    master.register_slave("Slave_1")
    master.allocate_task("Fetch_BTC_Data")
