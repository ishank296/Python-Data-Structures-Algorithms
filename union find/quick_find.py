'''
QUICK FIND : Tells whether two nodes of a graph are connected

UF ADT:
    UF(n): initialize n nodes (with list of integers 0 to n-1)
    union(p,q): connects nodes p and q (makes nodes entries same)
    find(p): component identifier for p(0 to n-1)
    connected(p,q): returns True if p and q are in same component i.e. connected
'''

# p and q are connected if and only if id[p] is equal to id[q]
class QuickFind(object):

    def __init__(self,n):
        self._nodes = [i for i in range(n)]
    
    
    def union(self,p,q):
        pid = self._nodes[p]
        qid = self._nodes[q]
        for i,j in enumerate(self._nodes):
            if self._nodes[i] == pid:
                self._nodes[i] = qid
    

    def connected(self,p,q):
        return self._nodes[p] == self._nodes[q]
        
if __name__ == '__main__': 
    qf = QuickFind(9)
    qf.union(2,3)
    qf.union(6,8)
    qf.union(0,5)
    qf.union(5,8)
    print qf.connected(0,8)
    print qf.connected(2,6)
    print qf._nodes

        
