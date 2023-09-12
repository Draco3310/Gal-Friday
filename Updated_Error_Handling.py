from pybreaker import CircuitBreaker

# Custom exception classes
class APIError(Exception):
    pass

class DataValidationError(Exception):
    pass

breaker = CircuitBreaker(fail_max=3, reset_timeout=60)

@breaker
def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except APIError as e:
        log_error("APIError", str(e))
    except DataValidationError as e:
        log_error("DataValidationError", str(e))
    except Exception as e:
        log_error("UnknownError", str(e))
