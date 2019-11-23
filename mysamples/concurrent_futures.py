"""
Simple ThreadPoolExecutor example
"""

import concurrent.futures
import time
import cProfile
import pstats
from profiling import decorator_profile


def mysamplejob(i):
    '''I/O intense tasks'''
    time.sleep(10)
    x = 1
    time.sleep(30)
    return i


def threadfn():
    """sample fn to spawn threads"""
    tpool = concurrent.futures.ThreadPoolExecutor(max_workers=8000)
    #TODO - what is the upper limit of max_workers
    futures = []
    results = []

    for i in range(0, 8000):
        futures.append(tpool.submit(mysamplejob, i))

    for task in concurrent.futures.as_completed(futures):
        results.append(task.result())
    # print("Results", results)


def processjob():
    tpool = concurrent.futures.ThreadPoolExecutor(max_workers=2000)
    futures = []
    results = []

    for i in range(0, 2000):
        futures.append(tpool.submit(mysamplejob, i))
    for task in concurrent.futures.as_completed(futures):
        results.append(task.result())
    # print("Results",results)

def processfn():
    """sample fn to spawn processes"""
    tpool = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    futures = []

    for i in range(0, 4):
            futures.append(tpool.submit(processjob))

    for task in concurrent.futures.as_completed(futures):
        # print(task.result())
        pass


if __name__ == "__main__":
    # decorator_profile(threadfn)()
    cProfile.run('processfn()', 'proessStats')
    cProfile.run('threadfn()', 'threadStats')
    p = pstats.Stats('proessStats')
    print(p.sort_stats('time').print_stats(10))
    p = pstats.Stats('threadStats')
    print(p.sort_stats('time').print_stats(10))
