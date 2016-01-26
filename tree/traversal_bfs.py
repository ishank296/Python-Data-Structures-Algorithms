'''
Breadth First Search/Level order traversal
'''

from binary_tree import BinaryTree
from collections import deque
def bfs(tree):
    q = deque()
    q.append(tree)
    while len(q) > 0:
        node = q.popleft()
        print node.getRootVal()
        if node.getLeftChild():
            q.append(node.getLeftChild())
        if node.getRightChild():
            q.append(node.getRightChild())

t= BinaryTree('1')
l1 = t.insertLeft('2')
r1 = t.insertRight('3')
l1.insertLeft('4')
l1.insertRight('5')
r1.insertLeft('6')
r1.insertRight('7')
bfs(t)


