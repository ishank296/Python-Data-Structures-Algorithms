'''
inorder traversal

leftChild
root
RightChild
'''

from binary_tree import BinaryTree

def inorder(tree):
    if tree.getLeftChild(): inorder(tree.getLeftChild())
    print tree.getRootVal()
    if tree.getRightChild(): inorder(tree.getRightChild())
    
    
t = BinaryTree('1')
l1 = t.insertLeft('2')
l2 = t.insertLeft('4')
r1 = t.insertRight('3')
r1 = t.insertRight('5')

inorder(t)
    
