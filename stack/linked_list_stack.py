class Node(object):

    def __init__(self,item):
        self.data = item
        self.next = None

class Stack(object):

    def __init__(self):
        self.head=None

    def push(self,item):
        node = Node(item)
        tmp = self.head
        node.next = tmp
        self.head = node

    def pop(self):
        tmp = self.head
        self.head = tmp.next
        return tmp.data

    def isEmpty(self):
        return (self.head is None)

    def __len__(self):
        l = 0
        cur = self.head
        while(cur is not None):
            cur = cur.next
            l+=1
        return l

    def __str__(self):
        cr = self.head
        l = '('
        while (cr!=None):
            l= l+str(cr.data)+','
            cr=cr.next
        l+=')'
        return l
if __name__ == '__main__':
    s = Stack()
    s.push(9)
    s.push(13)
    s.push(45)
    s.push(67)
    s.push(46)
    s.push(87)
    print s.pop()
    print s.pop()
    print s
