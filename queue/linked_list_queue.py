class Node(object):
    def __init__(self,item):
        self.data=item
        self.next=None

class Queue(object):

    def __init__(self):
        self.first = None

    def enqueue(self,item):
        node = Node(item)
        if self.first is None:
            self.first = node
        else:
            cr = self.first
            while (cr.next != None):
                cr = cr.next
            cr.next= node

    def dequeue(self):
        tmp = self.first
        self.first = tmp.next
        return tmp.data

    def isEmpty(self):
        return (self.first is None)


    def __len__(self):
        cr = self.first
        l = 0
        while (cr is not None):
            cr = cr.next
            l+=1

        return l

    def __str__(self):
        cr = self.first
        a = '('
        while (cr is not None):
            a+=str(cr.data)
            cr=cr.next
        a+=')'
        return a


if __name__ == '__main__':
    q = Queue()
    q.enqueue(0)
    print q.dequeue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print q.dequeue()
    print q.dequeue()
    q.enqueue(4)
    q.enqueue(5)
    print q.dequeue()
    q.enqueue(6)
    q.enqueue(7)
    print q.dequeue()
    print q.dequeue()
    q.enqueue(8)
    q.enqueue(9)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
