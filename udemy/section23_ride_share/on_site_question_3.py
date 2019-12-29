# Given a binary tree, check wheter it's a binary search tree or not

class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

def isBST(tree: Node, min_val=float('-infinity'), max_val=float('infinity')):
    if tree is None:
        return True
    
    if not min_val <= tree.val <= max_val:
        return False

    return isBST(tree.left, min_val, tree.val) and isBST(tree.right, tree.val, max_val)

def isBST2(tree, lastNode=[float('-infinity')]):

    if tree is None:
        return True
    
    if not isBST2(tree.left, lastNode):
        return False

    if tree.val < lastNode[0]:
        return False
    
    lastNode[0] = tree.val

    return isBST2(tree.right, lastNode)