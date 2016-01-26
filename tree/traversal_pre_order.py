'''
pre-order traversal

rootNode
leftNode
rightNode
'''
from binary_tree import BinaryTree

def preorder(tree):
    print tree.getRootVal()
    if tree.getLeftChild():
        preorder(tree.getLeftChild())
    if tree.getRightChild():
        preorder(tree.getRightChild())

t = BinaryTree('1')
l1 = t.insertLeft('2')
l2 = t.insertLeft('4')
r1 = t.insertRight('3')
r1 = t.insertRight('5')

preorder(t)