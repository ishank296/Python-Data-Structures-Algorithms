class SegmentTree(object):
    
    def __init__(self,input_arr):
        n = len(input_arr)
        self.size = 2*n-1
        self.tree = [0]*self.size
        self.build(0,0,n-1,input_arr)
        print self.tree
        
        
    def build(self,node,start,end,input_arr):
        print start,end
        if (start == end):
            self.tree[node] = input_arr[start]
        else:
            mid = (start+end)/2
            print mid
            #Recurse on the left child
            self.build(2*node+1,start,mid,input_arr)
            #Recurse on the right child
            self.build(2*node+2, mid+1, end,input_arr)
            #Internal node will have the sum of both of its children
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]