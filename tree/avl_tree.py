'''
Balanced Search Trees:
height : log(n) where n is number of nodes in tree
height of a node in a tree : longest path from node down to a leaf : max(height(leftChild),height(rightChild))+1 

                    41
                   /  \
                  20   65
                 /  \  /
                11  29 50
                    /   
                   26  

AVL Tree : Required height of left child and right child of every node to differ by at most +1 or -1

AVL Trees are balanced : worst case is when right subtree has height 1 more than left for every node


Nh = minimum number of nodes in a tree of height h.

Nh =    N(h-2)      +     N(h-1)       +   1
    > 2N(h-1)
h   > 2logn



'''