import time
from pybreaker import CircuitBreaker
import sentry_sdk

sentry_sdk.init(
    dsn="https://5f11fa4041efbc2a2d40248970836357@o4505875776667648.ingest.sentry.io/4505875779158016",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)
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
