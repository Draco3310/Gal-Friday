
import logging

# Configure logging
logging.basicConfig(filename='trading_bot.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def log_trade(action, symbol, price, reason):
    logging.info(f"Trade executed: {action} {symbol} at {price}. Reason: {reason}")

def log_error(error_type, error_message):
    logging.error(f"{error_type}: {error_message}")

def log_status(status_message):
    logging.info(f"Status: {status_message}")
