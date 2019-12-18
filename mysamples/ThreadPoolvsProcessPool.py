"""
ThreadPoolExecutor vs ProcessPoolExecutor example
Given a sample_input_range of items
What is the performance of ThreadPoolExecutor vs ProcessPoolExecutor

Input: sample_input_range = list of input items
ThreadPool max_workers :tmax_workers = 50
ProcessPool max_workers :pmax_workers = os.cpu_count() - 1  i.e, no.of cores - 1

Load Distribution:
ThreadPool : sample_input_range -> tmax_workers
ProcessPool :
sample_input_range =
floor(sample_input_range/pmax_workers) + remainder -> pmax_workers -> tmax_workers
(Just to Ensure even distribution of load to all the processes)

"""

import concurrent.futures
import time
import cProfile
import pstats
import os
import math
from profiling import decorator_profile

# TODO use decorator_profile in the logic
# TODO MANDATORY getting pid and threadid

sample_input_range = 500
tmax_workers = 50
pmax_workers = os.cpu_count() - 1


def mysamplejob (i):
    """I/O intense tasks"""
    time.sleep(7)
    i = i + 1  # Some random compute
    time.sleep(5)
    return i


def threadfn ():
    """sample fn to spawn threads"""
    tpool = concurrent.futures.ThreadPoolExecutor(max_workers=tmax_workers)
    # TODO - what is the upper limit of max_workers for a given set of data
    futures = []
    results = []

    for i in range(0, sample_input_range):
        futures.append(tpool.submit(mysamplejob, i))

    for task in concurrent.futures.as_completed(futures):
        results.append(task.result())
    # print("Results", results)


def processjob (process_input_range):
    """Sample fn to spawn threads inside a single process"""
    tpool = concurrent.futures.ThreadPoolExecutor(max_workers=tmax_workers)
    futures = []
    results = []

    for i in range(0, process_input_range):
        futures.append(tpool.submit(mysamplejob, i))
    for task in concurrent.futures.as_completed(futures):
        results.append(task.result())
    # print("Results",results)


def processfn ():
    """sample fn to spawn processes"""
    tpool = concurrent.futures.ProcessPoolExecutor(max_workers=pmax_workers)
    futures = []
    floor_range = math.floor(sample_input_range / pmax_workers)
    remainder_range = sample_input_range % pmax_workers

    for i in range(0, pmax_workers):
        futures.append(tpool.submit(processjob, floor_range))
    for i in range(0, remainder_range):
        futures.append(tpool.submit(processjob, remainder_range))

    for task in concurrent.futures.as_completed(futures):
        # print(task.result())
        pass

def process_new_fn ():
    """sample fn to spawn processes"""
    tpool = concurrent.futures.ProcessPoolExecutor(max_workers=pmax_workers)
    futures = []
    floor_range = math.floor(sample_input_range / pmax_workers)
    remainder_range = sample_input_range % pmax_workers
    for i in range(0, sample_input_range):
        futures.append(tpool.submit(mysamplejob, i))

    # for i in range(0, pmax_workers):
    #     futures.append(tpool.submit(processjob, floor_range))
    # for i in range(0, remainder_range):
    #     futures.append(tpool.submit(processjob, remainder_range))

    for task in concurrent.futures.as_completed(futures):
        # print(task.result())
        pass


if __name__ == "__main__":
    # decorator_profile(threadfn)()
    cProfile.run('processfn()', 'proessStats')
    cProfile.run('process_new_fn()', 'proessnewStats')
    cProfile.run('threadfn()', 'threadStats')
    p = pstats.Stats('proessStats')
    print(p.sort_stats('time').print_stats(10))
    p = pstats.Stats('proessnewStats')
    print(p.sort_stats('time').print_stats(10))
    p = pstats.Stats('threadStats')
    print(p.sort_stats('time').print_stats(10))
