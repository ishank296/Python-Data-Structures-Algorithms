'''
post-order traversal

leftNode
rightNode
rootNode
'''
from binary_tree import BinaryTree

def postorder(tree):
    if tree.getLeftChild():
        postorder(tree.getLeftChild())
    if tree.getRightChild():
        postorder(tree.getRightChild())
    print tree.getRootVal()

t = BinaryTree('1')
l1 = t.insertLeft('2')
l2 = t.insertLeft('4')
r1 = t.insertRight('3')
r1 = t.insertRight('5')

postorder(t)