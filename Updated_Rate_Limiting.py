import time
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=150, period=600)
def rate_limited_api_call(api_function, *args, **kwargs):
    return api_function(*args, **kwargs)
