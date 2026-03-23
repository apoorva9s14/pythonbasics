import time
from collections import deque
import threading

class Ratelimiter:
    def __init__(self, limit, window_seconds):
        self.limit = limit
        self.window = window_seconds
        self.logs=deque()
        self.lock = threading.Lock()

    def is_allowed(self,key):
        now=time.time()
        window_start_time = now.self.window
        with self.lock:
            if key not in self.logs:
                self.logs[key]=deque()
