import time

def adaptive_rate_limited_request(func, *args, **kwargs):
    rate_limit = 1.0  # initial rate limit in seconds
    while True:
        response = func(*args, **kwargs)
        if 'X-RateLimit-Remaining' in response.headers:
            rate_limit = float(response.headers['X-RateLimit-Remaining'])
        if rate_limit > 0:
            break
        time.sleep(rate_limit)
    return response
