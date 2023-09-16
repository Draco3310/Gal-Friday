import time
import requests

class DynamicRateLimiter:
    def __init__(self):
        self.rate_limit_remaining = None
        self.rate_limit_reset_time = None

    def rate_limited_api_call(self, api_function, *args, **kwargs):
        if self.rate_limit_remaining is not None and self.rate_limit_remaining <= 0:
            sleep_time = self.rate_limit_reset_time - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        response = api_function(*args, **kwargs)
        
        self.rate_limit_remaining = int(response.headers.get('RateLimit-Remaining', 0))
        self.rate_limit_reset_time = int(response.headers.get('RateLimit-Reset', 0))
        
        return response
