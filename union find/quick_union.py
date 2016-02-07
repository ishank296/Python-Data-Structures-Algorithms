'''
QUICK UNION
SIMILAR TO QUICK FIND:
Create root for each union and update nodes value to tree's root


find: check if p and q have same roots
union: to merge comphonents containing p and q set the id of p's root to the id of q's root
'''

class QuickUnion(object):

    def __init__(self,N):
        self._nodes=  [i for i in range(N)]
    
    def root(self,p):
        while(p!=self._nodes[p]):
            p = self._nodes[p]
        return p
        
    def union(self,p,q):
        i = self.root(p)
        j = self.root(q)
        self._nodes[i] = j
    
    
    def connected(self,p,q):
        return self.root(p) == self.root(q)
        
        
if __name__ =='__main__':
    qu = QuickUnion(10)
    qu.union(2,4)
    qu.union(8,0)
    qu.union(6,9)
    qu.union(6,5)
    print qu.connected(5,9)
    print qu.root(5)
    print qu._nodes
    