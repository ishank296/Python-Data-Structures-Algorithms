'''
python dequeue module
'''

from collections import deque

q= deque(['Eric','John','Michael'])
q.append('Terry')  #insert element from right side of queue
q.appendleft('Graham') #insert element from left side of queue 

print q
r1= q.popleft() #remove element from left side of queue
r2= q.pop()     #remove element from right side of queue

print r1
print r2
print q