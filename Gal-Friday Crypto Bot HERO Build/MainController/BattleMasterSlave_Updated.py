
import logging

class BattleMasterSlave:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)

    def select_strategy(self, predicted_signal):
        if not isinstance(predicted_signal, str):
            logging.error("Invalid input type for predicted_signal")
            return None
        
        if predicted_signal == 'BUY':
            strategy = 'Strategy1'
        elif predicted_signal == 'SELL':
            strategy = 'Strategy2'
        else:
            logging.error("Invalid predicted_signal value")
            return None

        logging.info(f"Selected strategy based on predicted signal: {strategy}")
        return strategy
