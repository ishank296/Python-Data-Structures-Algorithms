class Stack:
    
    def __init__(self):
        self.elements=list()
        
    def push(self,item):
        self.elements.append(item)
    
    def pop(self):
        return self.elements.pop()
    
    def isEmpty(self):
        return (self.elements == [])
    
    def top(self):
        return self.elements[-1]
    
    
    def __len__(self):
        return len(self.elements)
        
    def __str__(self):
        return str(self.elements)

def sort_insert(stk,elem):
    if stk.isEmpty() or elem > stk.top():
        stk.push(elem)
    else:
        temp = stk.pop()
        sort_insert(stk,elem)
        stk.push(temp)

def sort_stack(stk):
    if stk.isEmpty():
        return
    elem = stk.pop()
    sort_stack(stk)
    sort_insert(stk,elem)
    
    
s=Stack()
s.push(-3)
s.push(14)
s.push(18)
s.push(-5)
s.push(30)
print s
sort_stack(s)
print s
    