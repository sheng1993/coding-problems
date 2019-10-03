# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

from utils.models.trees import Node

def common_ancestor_optimal(root: Node, p: Node, q: Node):
    if not root: return None
    if root == p and root == q: return root

    x = common_ancestor_optimal(root.left, p, q)
    if not x and x != p and x != q:
        return x
    
    y = common_ancestor_optimal(root.right, p, q)
    if not y and y != p and y != q:
        return y
    
    if not x and not y:
        return root
    elif root == p or root == q:
        return root
    else:
        return y if not x else x

def common_ancestor(root: Node, p: Node, q: Node):
    if not covers(root, p) or not covers(root, q):
        return None

def ancestor_helper(root: Node, p: Node, q: Node):
    if not root or not p or not q:
        return root
    
    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)

    if p_is_on_left != q_is_on_left:
        return root
    
    child_side = root.left if p_is_on_left else root.right
    return ancestor_helper(child_side, p, q)

def common_ancestor_with_parent(root: Node, p: Node, q: Node):
    if not covers(root, p) or not covers(root, q):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    sibling = get_sibling(p)
    parent = p.parent

    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent

    return parent

def covers(root: Node, p: Node):
    if not root: return False
    if root == p: return True

    return covers(root.left, p) or covers(root.right, p)


def get_sibling(node: Node):
    if not node or not node.parent:
        return None
    
    parent = node.parent

    return parent.right if parent.left == node else parent.left