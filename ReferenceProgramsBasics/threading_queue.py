
'''
#Intro to threads, Hello Threads.
#Inheriting from the Thread class and defining the run method
#Creating object for that inherited class, and starting that thread object
#self.getName() is a method that will identify the name of the thread.

import threading
import datetime
 
class ThreadClass(threading.Thread):
  def run(self):
    now = datetime.datetime.now()
    print("%s says Hello World at time: %s" %(self.getName(), now))
 
for i in range(2):
  t = ThreadClass()
  t.start()
    
'''
'''
#Threading is complicated when threads share data or resources. There is synchronization provided by threading module - semaphores, condition variables, events, and locks.
#Queues make threaded programming considerably safer, as they effectively funnel all access to a resource to a single thread, and allow a cleaner and more readible design pattern.
#urllib-fetch the urls and write to a file
#Without using threading
from urllib.request import urlopen
import time
 
hosts = ["http://yahoo.com", "http://google.com"]
 
start = time.time()
#grabs urls of hosts and prints first 1024 bytes of page
for host in hosts:
  url = urlopen(host)
  print(url.read(1024))
 
print("Elapsed Time: %s" % (time.time() - start))

'''
#Same action as previous with threading support

#!/usr/bin/env python
import queue
import threading
from urllib.request import urlopen
import time
 
hosts = ["http://yahoo.com", "http://google.com"]
 
queue = queue.Queue()
#Create an object of Queue class

#Define a class inheriting from the Thread class,inherit the init and add queue parameter to it 
class ThreadUrl(threading.Thread):
  """Threaded Url Grab"""
  def __init__(self, queue):
    threading.Thread.__init__(self)
    self.queue = queue
 
  def run(self):
    while True:
      #grabs host from queue
      host = self.queue.get()
   
      #grabs urls of hosts and prints first 1024 bytes of page
      url = urlopen(host)
      print(url.read(1024))
   
      #signals to queue job is done
      self.queue.task_done()
 
start = time.time()
def main():
 
  #spawn a pool of threads, and pass them queue instance 
  for i in range(5):
    t = ThreadUrl(queue)
    t.setDaemon(True)
    t.start()     
    #populate queue with data   
    for host in hosts:
      queue.put(host)  
  #wait on the queue until everything has been processed     
  queue.join()
 
main()
print("Elapsed Time: %s" % (time.time() - start))
