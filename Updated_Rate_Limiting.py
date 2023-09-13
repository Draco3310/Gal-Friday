
import time
from collections import deque
from Error_Handling import safe_execute

# Initialize rate-limiting variables
request_queue = deque()
rate_limit = 1.0  # Initial rate limit in seconds

def rate_limited_request(func, *args, **kwargs):
    global rate_limit
    current_time = time.time()

    # Dynamic Rate Limiting
    while request_queue and current_time - request_queue[0] > 60:
        request_queue.popleft()

    if len(request_queue) >= rate_limit * 60:
        time_to_wait = 60 + request_queue[0] - current_time
        time.sleep(time_to_wait)

    # Execute the API call safely
    response = safe_execute(func, *args, **kwargs)

    # Update rate limit based on API response (placeholder, to be filled in later)
    # rate_limit = ...

    request_queue.append(time.time())
    return response
