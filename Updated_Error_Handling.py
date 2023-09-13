import time
from pybreaker import CircuitBreaker
import sentry_sdk

sentry_sdk.init("your_dsn_here")

# Custom exception classes
class APIError(Exception):
    pass

class DataValidationError(Exception):
    pass

class KrakenAPIError(Exception):
    pass

breaker = CircuitBreaker(fail_max=3, reset_timeout=60)

@breaker
def safe_execute(func, *args, **kwargs):
    for _ in range(3):
        try:
            return func(*args, **kwargs)
        except KrakenAPIError:
            time.sleep(1)
