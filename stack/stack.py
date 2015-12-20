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