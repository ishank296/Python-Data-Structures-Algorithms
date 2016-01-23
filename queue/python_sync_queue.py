'''
Synchronized python queue
queue.Queue : FIFO Queue
queue.LifoQueue : LIFO Queue
queue.PriorityQueue : PRIORITY Queue

methods
q.put(item)
q.get()
q.qsize()
q.empty()
q.full()
'''

from Queue import Queue
import threading
import time,random
num_worker_threads=2

#generator to simulate task source
def source():
    for i in xrange(10):
        yield i

#method for processing item
def do_work(item):
    print "task", item, "finished"
    #time.sleep(random.randint(10,100)/1000.0)
    


def worker():
    while True:
        # extract task from queue in FIFO manner
        item = q.get()
        if item is None:
            print "No item in queue"
            break
        # process task
        do_work(item)
        # mark task as done
        q.task_done()

q = Queue()  #thread-safe FIFO queue
threads = []

# start worker threads 
for i in range(num_worker_threads):
    t = threading.Thread(target = worker)
    t.start()
    threads.append(t)

for item in source():
    q.put(item)
    
# block until all tasks are done
q.join()

# stop workers
for i in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()
