'''
Expression evaluation using tree
1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.

2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.

3. If the current token is a number, set the root value of the current node  to the number and return to the parent.

4. If the current token is a ')', go to the parent of the current node.
'''

from binary_tree import BinaryTree

def build_parse_tree(exp):
    explist = exp.split()
    pStack = list()  # parent stack
    etree = BinaryTree('')
    pStack.append(etree)
    current = etree
    
    for i in explist:
        if i == '(':
            newtree = current.insertLeft('')
            pStack.append(current)
            current = newtree
        elif i not in ['*','+','-','/',')']:
            current.setRootVal(i)
            current = pStack.pop()
        elif i in ['*','+','-','/']:
            current.setRootVal('i')
            newtree = current.insertRight('')
            pStack.append(current)
            current = newtree
        elif i == ')':
            current = pStack.pop()
        else:
            raise ValueError
    return etree
            


