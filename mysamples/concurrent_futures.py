'''
Simple ThreadPoolExecutor example
'''

import concurrent.futures
import time

def mysamplejob(i):
    '''I/O intense tasks'''
    time.sleep(10)
    return i

def mytestfn():
	'''sample fn to spawn threads'''
	tpool = concurrent.futures.ThreadPoolExecutor(max_workers=10)
	futures = []

	for i in range(0,10):
		futures.append(tpool.submit(mysamplejob,i))
	
	for task in concurrent.futures.as_completed(futures):
		print(task.result())