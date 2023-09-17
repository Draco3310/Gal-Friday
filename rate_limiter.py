# rate_limiter.py

import time

def rate_limit(fetch_frequencies):
    for symbol, frequency in fetch_frequencies.items():
        time.sleep(frequency)
