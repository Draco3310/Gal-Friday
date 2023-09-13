from pybreaker import CircuitBreaker

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
    try:
        return func(*args, **kwargs)
    except KrakenAPIError as e:
        log_error("KrakenAPIError", str(e))
