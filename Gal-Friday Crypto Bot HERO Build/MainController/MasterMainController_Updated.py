
import logging

class MasterMainController:
    def __init__(self):
        self.slave_modules = []
        logging.basicConfig(level=logging.INFO)

    def register_slave(self, slave_module):
        self.slave_modules.append(slave_module)

    def orchestrate(self):
        try:
            for slave in self.slave_modules:
                slave.execute_task()
            logging.info("Orchestration completed successfully.")
        except Exception as e:
            logging.error(f"Orchestration failed: {e}")
