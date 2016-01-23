'''
Queue Module
Thread Safe Priority Queue
'''


import Queue
#simple min priority queue
#min element will be at the top
q1 = Queue.PriorityQueue()
q1.put(10)
q1.put(5)
q1.put(1)

while not q1.empty():
    print q1.get()
    
#priority queue storing tuples
q2 = Queue.PriorityQueue()
q2.put((10,'ten'))
q2.put((1,'one'))
q2.put((4,'four'))
q2.put((11,'eleven'))

while not q2.empty():
    print q2.get()






# Priority Queue storing objects

class Skill(object):
    
    def __init__(self,priority,description):
        self.priority = priority
        self.description = description
        
    def __cmp__(self,other):
        return cmp(self.priority,other.priority)
    
q3 = Queue.PriorityQueue()
q3.put(Skill(5,'Proficient'))
q3.put(Skill(10,'Expert'))
q3.put(Skill(1,'Novice'))
 
while not q3.empty():
    next = q3.get()
    print "processing level: ", next.description
    