'''Singly Linked List '''

class Node(object):
    
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList(object):
    
    def __init__(self):
        self.head=None
    
    def addAtBegin(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    
    def deleteAtBegin(self):
        temp = self.head
        self.head = temp.next
        return temp
    
    def addAtEnd(self,data):
        node = Node(data)
        if self.head is None:
            self.addAtBegin(data)
        else:
            curnode = self.head
            while(curnode.next is not None):
                curnode=curnode.next
            curnode.next=node
            
    def deleteAtEnd(self):
        if self.head is None:
            return None
        elif len(self) ==1:
            self.deleteAtBegin()
        else:
            curnode=self.head
            while(curnode.next.next is not None):
                curnode = curnode.next
            temp = curnode.next   
            curnode.next=None     
            return temp
    

    def elementAt(self,index):
        if index > len(self):
            raise IndexError
        curnode=self.head
        while(index >=0):
            curnode=curnode.next
            index = index-1
        return  curnode.data
    

    def addAtindex(self,index,data):
        if (index == 0):
            return self.addAtBegin(data)
        elif (index == len(self)):
            return self.addAtEnd(data)
        
        else:
            node = Node(data)
            curnode = self.head
            while(index >= 0):
                curnode=curnode.next
                index = index - 1
            node.next=curnode.next
            curnode.next=node
    
    def __len__(self):
        i = 0
        curnode = self.head
        if curnode is None: return i
        else:
            while(curnode.next is not None):
                curnode = curnode.next
                i= i+1
        return i+1
        
    def display(self):
        n = self.head
        while n is not None:
            print str(n.data) + " =>",
            n=n.next




a =  LinkedList();
a.addAtBegin(5);
a.addAtBegin(15);
a.addAtEnd(20);
a.addAtEnd(21);
a.deleteAtBegin();
a.deleteAtEnd();
a.addAtindex(2,10);
a.addAtEnd(15); 
a.display()         
            
    
        