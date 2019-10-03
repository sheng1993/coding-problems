# Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
# algorithm to determine ifT2 is a subtree of Tl.
# A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
# That is, if you cut off the tree at node n, the two trees would be identical.

from utils.models.trees import Node

def contains_tree(t1: Node, t2: Node):
    if not t2:
        return True

    return sub_tree(t1, t2)

def sub_tree(r1: Node, r2: Node):
    if not r1:
        return False
    elif r1.val == r2.val and match_tree(r1, r2):
        return True
    return sub_tree(r1.left, r2) or sub_tree(r1.right, r2)

def match_tree(r1: Node, r2: Node):
    if not r1 and not r2:
        return True
    elif not r1 or not r2:
        return False
    elif r1.val != r2.val:
        return False
    else:
        return match_tree(r1.left, r2.left) and match_tree(r1.right, r2.right)