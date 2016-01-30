'''
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''

class Node(object):
    def __init__(self,data,parent=None):
        self.value = data
        self.left = None
        self.right = None
        self.parent = parent
    
    def getValue(self):
        return self.value
    
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def setLeftChild(self,node):
        self.left = node
    def setRightChild(self,node):
        self.right = node

def search(root,data):
    if not root:
        return False
    if root.getValue() == data: 
        return tree
    if root.getValue() < data : 
        return search(root.right,data)
    else : 
        return search(root.left,data)


def insert(root,data):

                
            
            
            

'''
start from left. Go left till left becomes null
'''            
def find_minimum(root):
    current = root
    while current.getLeftChild() is not None:
        current = current.getLeftChild()
    return current
    
    

''' Start from root. Go right till right becomes null    '''  
def find_maximum(root):
    current = root
    while current.getRightChild() is not None:
        current = current.getRightChild()
    return current

'''
In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree. Inorder Successor is NULL for the last node in Inoorder traversal.

In Binary Search Tree, Inorder Successor of an input node can also be defined as the node with the smallest key greater than the key of input node


1. If the right tree is not null then:
        Go to right subtree and return node with minimum key value in right subtree

2. If right tree is null  then successor is one of its parents:
        Traverse up using parent reference until a node is found which is left child of it's parent. The parent of such a node is successor
                                                          
                           o-->r                          o-->s
                          / \                            / 
                         o   o                          o
                        /   / \                          \
                       o   os  o                          o
                      / \                                  \
                     o   o                                  o-->r
                                     
'''
def find_successor(root):
    if root.getRightChild() is not None:
        return find_minimum(root.getRightChild())
    else:
        current = root
        parent = root.parent
        while (current is not None and current == parent.getRightChild()):
            current = parent
            parent = parent.parent
        return parent
        

        
def find_predecessor(root):
    if root.getLeftChild() is not None:
        return find_maximum(root.getLeftChild())
    else:
        current = root
        parent = current.parent
        while(current is not None and current == parent.getLeftChild()):
            current = parent
            parent = parent.parent
        return parent

        
        
#def find_height(root):
#    
 

T = Node(8) 
insert(T,2)
insert(T,16)
insert(T,5)
insert(T,4)        
insert(T,9)
insert(T,13)
insert(T,7)
insert(T,1)

print find_maximum(T).getValue()
print find_minimum(T).getValue()
#print find_successor()


    
