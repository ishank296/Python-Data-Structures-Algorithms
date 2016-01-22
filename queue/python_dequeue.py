'''
python dequeue module
'''

from collections import deque

q= deque(['Eric','John','Michael'])
q.append('Terry')
q.append('Graham')

r1= q.popleft()

print r1
print q