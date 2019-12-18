"""
CALL AFTER function
is a function which is
1. accessible by another function
2. is called after the first function completes execution
You dont call me
I will call you back
"""

import time


def sample_return_fn(sample_inp):
    time.sleep(10)
    return sample_inp
