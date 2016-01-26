class BinaryTree(object):
    
    def __init__(self,root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        
    
    def insertLeft(self,newNode):
        t = BinaryTree(newNode)
        if self.leftChild is None:
            self.leftChild = t
        else:
            t.leftChild = self.leftChild
            self.leftChild = t
        return t
    
    
    
    def insertRight(self,newNode):
        t = BinaryTree(newNode)
        if self.rightChild is None:
            self.rightChild = t
        else:
            t.rightChild = self.rightChild
            self.rightChild = t
        return t
    
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self,val):
        self.key = val
    
    def getRootVal(self):
        return self.key

        
t = BinaryTree('a')
l = t.insertLeft('b')
r = t.insertRight('c')
t.getRightChild().setRootVal('hello')
print t.getRootVal()
print t.getRightChild().getRootVal()
print t.getLeftChild().getRootVal()

    
    