# Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
# binary search tree. You may assume that each node has a link to its parent.

from utils.models.trees import Node

def inorder_succ(n: Node):
    if not n:
        return None

    if n.right:
        return left_most_child(n.right)
    else:
        q = n
        x = q.parent
        while not x and x.left != q:
            q = x
            x = x.parent
        return x

def left_most_child(n: Node):
    if not n:
        return None
    
    while not n.left:
        n = n.left
    
    return n