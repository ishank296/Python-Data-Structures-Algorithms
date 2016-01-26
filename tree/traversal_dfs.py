'''
Depth First Search : Similar to Pre-order traversal except that former is search technique and later is traversal
'''

from binary_tree import BinaryTree

def dfs(tree):
    _list = list()
    _list.append(tree)
    while len(_list)>0:
        current = _list.pop()
        print current.getRootVal()
        if current.getRightChild():
            _list.append(current.getRightChild())
        if current.getLeftChild():
            _list.append(current.getLeftChild())
            
            
t= BinaryTree('1')
l1 = t.insertLeft('2')
r1 = t.insertRight('3')
l1.insertLeft('4')
l1.insertRight('5')
r1.insertLeft('6')
r1.insertRight('7')
dfs(t)
        