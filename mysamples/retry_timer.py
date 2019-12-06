"""
Given a function write a decorator which retries
for a certain period of time and breaks when the output is received
"""

from datetime import datetime
from datetime import timedelta
retry_time_period_secs = 10


def retry_time_decorator(fn):
    def inner_fn(*args, **kwargs):
        retry_end_time = datetime.now() + timedelta(seconds=retry_time_period_secs)
        while datetime.now() < retry_end_time:
            if fn(*args, **kwargs):
                print("Found the Value")
                break
            else:
                continue
        print("End of While Loop")
        return fn(*args, **kwargs)
    return inner_fn


@retry_time_decorator
def sample_fn_retry_time():
    """ to check for retry for a certain period of time"""
    return False


sample_fn_retry_time()
