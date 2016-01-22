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

from queue import Queue

def worker():
    while True:
        item = q.get()
        if item is None:
            break
        do_work(item)
        q.task_done()

q = queue.Queue()
threads = []

# start worker threads 
for i in range(num_worker_threads):
    t = threadin.Thread(target = woker)
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
