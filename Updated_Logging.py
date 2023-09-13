import logging
import logging.handlers

logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[logging.handlers.TimedRotatingFileHandler("logs/trading_bot.log", when="midnight", backupCount=3)]
    logging.info(f"Buy order executed at {current_price}")
)

def log_trade(action, symbol, price, reason):
    logging.info(f"Trade executed: {action} {symbol} at {price}. Reason: {reason}")

def log_error(error_type, error_message):
    logging.error(f"{error_type}: {error_message}")

def log_status(status_message):
    logging.info(f"Status: {status_message}")
