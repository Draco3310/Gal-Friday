from pybreaker import CircuitBreaker

breaker = CircuitBreaker(fail_max=3, reset_timeout=60)

@breaker
def safe_execute(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        # Switch to a backup API or data source
        return backup_func(*args, **kwargs)
